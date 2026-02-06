---
code: g1
title: Bare ground
parent: g
ukhab: g1
status: draft
description: >
  Areas of exposed, unvegetated land.
subclasses: []
associated_habitats:
  - "To be confirmed with Landscapes"

---

# {{ title }} ({{ code }})

**UKHab:** {{ ukhab }}  
**Parent:** {{ parent }}  
**Status:** {{ status }}

*insert horizontal habitat image w: pix h: pix*

## Definition

{{ description }}

## Identification criteria

*This class should be mapped when:*
- XXX vegetation <5 m tall covers >XX% of the polygon
- Vegetation has clearly defined edges
- Dominated by XXX rather than tree canopy

## Aerial Definition

*examples of aerial photography annotations etc....*

---

## Associated habitat concepts

!!! info "Associated habitat concepts (not to be annotated separately)"
    The habitat types listed below are commonly associated with **{{ title }} ({{ code }})** in ecological and conservation literature.  

    These represent **interpretive or descriptive groupings**, not separate interpretation classes, and should **not** be mapped independently from imagery.

    {% for hab in associated_habitats %}
    - **{{ hab }}**
    {% endfor %}

    Associations are **contextual characteristcis** and will be derived post-mapping.

---

## Overlap with other classes

!!! warning "Potential confusion with related classes"
    - [a3 Open mosaic](../artificial-land/open-mosaic.md)

---

## In Protected Landscapes

Occurs across all protected landscapes as temporary/disturbed surfaces (tracks, construction, eroding paths, livestock poached ground, recently managed sites).

### Management and drivers

The structure and extent are influenced by:

* Disturbance intensity (recreation, livestock, vehicles)
* Path/track creation and maintenance practices
* Erosion and sediment movement by wind/water
* Construction, restoration works, and extraction activities
* Seasonal vegetation cover changes (drying, dieback)
* Management to stabilise or re-vegetate exposed areas
* Extreme weather events increasing bare patches

## Useful Links

* [UKHab – Habitat Definitions v1.0 (PDF)](https://ecountability.co.uk/wp-content/uploads/2018/05/UK-Habitat-Classification-Habitat-Definitions-V1.0-May-2018-1.pdf)
* [UKHab – Field Key (May 2018) (PDF)](https://ecountability.co.uk/wp-content/uploads/2018/05/UK-Habitat-Classification-Field-Key_May2018.pdf)
