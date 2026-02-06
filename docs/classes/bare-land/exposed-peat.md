---
code: g5
title: Exposed Peat
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
    - [f3 Raised bog](../wetland/raised-bog.md)

---

## In Protected Landscapes

Occurs mainly in upland protected landscapes where peatlands have been damaged, especially on heavily used/eroding moors and peat plateaus.

### Management and drivers

The structure and extent are influenced by:

* Erosion drivers (wind, water, freeze-thaw)
* Drainage/gripping* overgrazing and trampling
* Fire/burning history and wildfire* restoration (re-wetting, geotextiles, re-vegetation, gully blocking)
* Recreation pressure (paths, bikes, walkers)
* Climate change increasing drought/erosive rainfall events

## Useful Links

* [JNCC – Blanket Bog (UK BAP) (PDF)](https://data.jncc.gov.uk/data/aadfff3d-9a67-467a-ac65-45285e123607/UKBAP-BAPHabitats-03-BlanketBog.pdf)
* [UK BAP – Priority Habitat Descriptions (revised 2011) (PDF)](https://data.jncc.gov.uk/data/2728792c-c8c6-4b8c-9ccd-a908cb0f1432/UKBAP-PriorityHabitatDescriptions-Rev-2011.pdf)
