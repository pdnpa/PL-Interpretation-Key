---
code: d
title: Heathland
parent: d
ukhab: h1
status: draft
description: >
  Land dominated by low (dwarf) shrub species, generally forming part of a succession from grassland to woodland but maintained through burning, cutting and grazing, e.g. moorlands. Includes grass moor as visually distinct from acid grassland and important as a transition between degraded (molinia dominated) landscapes and transition to blanket bog. Excludes seasonally and/or permanently wet areas, e.g. peat bogs.
subclasses: [d1, d1a, d1b, d2, d2a, d2b, d3, d4]
---

# {{ title }} ({{ code }})

**UKHab:** {{ ukhab }}  
**Parent:** {{ parent }}  
**Status:** {{ status }}

*insert horizontal habitat image w: pix h: pix*

## Definition

{{ description }}

## Identification criteria

Heath & Moorland covers open landscapes dominated by dwarf shrubs and/or grasses in upland and lowland settings, typically forming large semi-natural mosaics rather than neat field parcels. In aerial imagery it often appears as textured, irregular vegetation patterns with management signatures (burn/cut age mosaics) and strong context cues from enclosure, elevation, and adjacent peatland/grassland habitats.




## D — Heath & Moorland flow diagram (12.5 cm aerial interpretation)

> Use this flow for open “rough vegetation” land. If the area is clearly an enclosed improved field (smooth, uniform, cut/grazed), route to Grassland (E) first.

```mermaid
flowchart TD
  A[Start: Open rough vegetation patch] --> B{Clearly below the enclosure line?\n(regular fields/hedges/walls nearby)}
  B -->|Yes| C{Dwarf shrubs form the dominant cover?\n(textured heather-like surface, patchy dwarf shrub blocks)}
  B -->|No / Mostly unenclosed moor| D{Dwarf shrubs cover ≥ ~25% of the patch?\n(heather-type signal is obvious across the unit)}

  %% Lowland branch
  C -->|Yes| D3[d3 Lowland heath]
  C -->|No| E1[Not D-class:\nconsider E (grassland), C (scrub/bracken), or F (wetland)]

  %% Upland branch: heath vs grass moor
  D -->|Yes| D1[d1 Upland heath]
  D -->|No| G{Grass/sedge dominates?\n(broad smooth-to-tussocky grass texture, few shrubs)}

  %% Grass moor branch
  G -->|No| H[Not D-class:\nconsider C scrub/bracken or F peatland/wetland]
  G -->|Yes| I{Wetness/degradation cues prominent?\n(dark flush lines, saturated patches,\npeat disturbance nearby, sedge-dominated zones)}
  I -->|Yes| D2A[d2a Grass/Sedge moor (Degraded)]
  I -->|No| J{Strong tussock / acid-grass texture in unenclosed uplands?\n(mottled straw/green, persistent tussock pattern)}
  J -->|Yes| D2B[d2b Acid grass / tussocks / unenclosed grass moor]
  J -->|No| D2[d2 Upland grass moor]
```

