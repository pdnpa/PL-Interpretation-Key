# scripts/plots.py
from __future__ import annotations

import io
from typing import Tuple, Optional

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import box


def _imshow(ax, img_bytes: bytes, bbox: Tuple[float, float, float, float]) -> None:
    img = plt.imread(io.BytesIO(img_bytes))
    extent = (bbox[0], bbox[2], bbox[1], bbox[3])
    ax.imshow(img, extent=extent)
    ax.set_axis_off()


def plot_plate_1x3(
    *,
    bbox: Tuple[float, float, float, float],
    rgb125_bytes: bytes,
    cir500_bytes: bytes,
    rgb_anno_bytes: bytes,
    sample_geom,
    annotations: Optional[gpd.GeoDataFrame] = None,
    label_col: str = "Main_Class",
    draw_labels: bool = False,
    title1: str = "",
    title2: str = "",
    title3: str = "",
    figsize=(14, 5),
):
    fig, axes = plt.subplots(1, 3, figsize=figsize, constrained_layout=True)

    # panel 1
    _imshow(axes[0], rgb125_bytes, bbox)
    gpd.GeoSeries([sample_geom], crs=27700).boundary.plot(ax=axes[0], linewidth=1.5)
    axes[0].set_title(title1)

    # panel 2
    _imshow(axes[1], cir500_bytes, bbox)
    gpd.GeoSeries([sample_geom], crs=27700).boundary.plot(ax=axes[1], linewidth=1.5)
    axes[1].set_title(title2)

    # panel 3
    _imshow(axes[2], rgb_anno_bytes, bbox)
    gpd.GeoSeries([sample_geom], crs=27700).boundary.plot(ax=axes[2], linewidth=1.5)

    if annotations is not None and not annotations.empty:
        ctx = box(*bbox)
        ann_sub = annotations[annotations.intersects(ctx)]
        if not ann_sub.empty:
            ann_sub.boundary.plot(ax=axes[2], linewidth=1.2)
            if draw_labels and (label_col in ann_sub.columns):
                for _, r in ann_sub.iterrows():
                    p = r.geometry.representative_point()
                    axes[2].text(p.x, p.y, str(r[label_col]), fontsize=9)

    axes[2].set_title(title3)

    return fig
