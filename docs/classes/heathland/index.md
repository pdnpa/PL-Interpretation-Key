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

*   [Google photo sphere Errwood Reservoir](https://goo.gl/maps/vzTW5dfStQxpd9M36) D2 looking North mainly upland acid grassland but many other classes are present

<iframe style="border: 0;" src="https://www.google.com/maps/embed?pb=!4v1683133542221!6m8!1m7!1sCAoSLEFGMVFpcE14WExkRnhlUEx4WURqNi1DRHBKSVVsNHFrcFpJZ1RTc2ZUaVRW!2m2!1d53.274597!2d-1.955734!3f37.34!4f-44.4!5f0.8397475938514558" width="960" height="600" allowfullscreen="allowfullscreen" loading="lazy"></iframe>

*   [Google photo sphere Bamford Edge](https://goo.gl/maps/LLR5qYkbKaQk7Gdf9) Looking East a heather dominated moorland with evidence of moorland management of cutting heather

<iframe style="border: 0;" src="https://www.google.com/maps/embed?pb=!4v1683133491148!6m8!1m7!1sCAoSLEFGMVFpcE83U0N1ZHpEQnEzOVN6azNfcE42MVpseFlQSjc1S3VHZ2dvb0dM!2m2!1d53.36087490000001!2d-1.6909095!3f120.38!4f-30.340000000000003!5f0.7820865974627469" width="960" height="600" allowfullscreen="allowfullscreen" loading="lazy"></iframe>

*   [Google photo sphere Curbur Edge](https://goo.gl/maps/RKd5RAvsj6gZLb3J7) Looking East on Moorlands howing areas of heather of varying clump and within patch plot sizes intersected with upland acid grassland. Looking West on the slope below the cliff edge Bracken died back to orange/bwon intersected with Heather.

<iframe style="border: 0;" src="https://www.google.com/maps/embed?pb=!4v1683133881879!6m8!1m7!1sCAoSLEFGMVFpcE9RaGxLUUxIanM5R2diWS1majdwSFJneENuQnZJRWdWb1JpaEE5!2m2!1d53.27468320000001!2d-1.611619!3f84.46472599505043!4f-24.99925964006843!5f0.7820865974627469" width="960" height="600" allowfullscreen="allowfullscreen" loading="lazy"></iframe>


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


