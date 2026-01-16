# scripts/wms.py
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Tuple, Optional

import pandas as pd
import requests
from shapely.geometry import Point

WMS_URL = "https://www.getmapping.com/GmWMS/31583b86-e918-444f-adb6-0aeedfaecb8d/APGB.wmsx"

# Layers
LAYER_RGB_125 = "APGB_Latest_UK_125mm"
LAYER_CIR500 = "APGB_CIR500mm"

# Index layers for metadata
INDEX_RGB_125 = "APGB_Latest_UK_125mmIndex"
INDEX_CIR500 = "APGB_CIR500mmIndex"

_RE_KM = re.compile(r"Km Reference:\s*([A-Z]{2}\d{4})")
_RE_DT = re.compile(r"Date Flown:\s*([0-3]?\d/[01]?\d/\d{4})")
_RE_YR = re.compile(r"Flown Year:\s*(\d{4})")

_SESSION = requests.Session()

# copied from exmaple wms ;)! 

@dataclass(frozen=True)
class WmsMeta:
    kmreference: Optional[str]
    date_flown: pd.Timestamp | pd.NaT
    flown_year: Optional[int]
    raw: str


def bbox_buffered(bounds: Tuple[float, float, float, float], buffer_m: float) -> Tuple[float, float, float, float]:
    minx, miny, maxx, maxy = bounds
    return (minx - buffer_m, miny - buffer_m, maxx + buffer_m, maxy + buffer_m)

def getmap_bytes(layer: str, bbox: Tuple[float, float, float, float], *, width: int = 1400, fmt: str = "image/png") -> bytes:
    minx, miny, maxx, maxy = bbox
    dx, dy = (maxx - minx), (maxy - miny)
    height = max(1, int(round(width * (dy / dx)))) if dx > 0 else width

    params = {
        "SERVICE": "WMS",
        "VERSION": "1.3.0",
        "REQUEST": "GetMap",
        "LAYERS": layer,
        "CRS": "EPSG:27700",
        "BBOX": f"{minx},{miny},{maxx},{maxy}",
        "WIDTH": str(width),
        "HEIGHT": str(height),
        "FORMAT": fmt,
        "STYLES": "",
        "TRANSPARENT": "TRUE",
    }
    r = _SESSION.get(WMS_URL, params=params, timeout=60)
    r.raise_for_status()
    return r.content


def getfeatureinfo_text(index_layer: str, bbox: Tuple[float, float, float, float]) -> str:
    minx, miny, maxx, maxy = bbox
    width = height = 101
    i = j = 50

    params = {
        "SERVICE": "WMS",
        "VERSION": "1.3.0",
        "REQUEST": "GetFeatureInfo",
        "LAYERS": index_layer,
        "QUERY_LAYERS": index_layer,
        "CRS": "EPSG:27700",
        "BBOX": f"{minx},{miny},{maxx},{maxy}",
        "WIDTH": str(width),
        "HEIGHT": str(height),
        "I": str(i),
        "J": str(j),
        "INFO_FORMAT": "text/plain",
        "FEATURE_COUNT": "5",
        "FORMAT": "image/png",
        "STYLES": "",
    }
    r = _SESSION.get(WMS_URL, params=params, timeout=60)
    r.raise_for_status()
    return r.text


def parse_featureinfo(txt: str) -> WmsMeta:
    km = _RE_KM.search(txt)
    dt = _RE_DT.search(txt)
    yr = _RE_YR.search(txt)

    km_val = km.group(1) if km else None
    dt_val = pd.to_datetime(dt.group(1), dayfirst=True, errors="coerce") if dt else pd.NaT
    yr_val = int(yr.group(1)) if yr else (int(dt_val.year) if pd.notna(dt_val) else None)

    return WmsMeta(kmreference=km_val, date_flown=dt_val, flown_year=yr_val, raw=txt)


def meta_at_point(index_layer: str, pt: Point, *, buf_m: float = 200.0) -> WmsMeta:
    bbox = (pt.x - buf_m, pt.y - buf_m, pt.x + buf_m, pt.y + buf_m)
    return parse_featureinfo(getfeatureinfo_text(index_layer, bbox))
