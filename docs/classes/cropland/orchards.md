---
code: b3
title: Orchards
parent: b
ukhab: c1
status: draft
description: >
  Collections of fruit and/or nut producing trees, currently managed for food production, with an intensely managed ground cover.
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
    - [c4 Traditional orchard](../woodland/traditional-orchard.md)
    - [b2 Permanent crops](permanent.md)

---

## In Protected Landscapes

*where and which PL's this is likely found*

### Management and drivers

*Dense scrub may be maintained by:*
- Reduced grazing pressure
- Woodland succession
- We have no money!!!!!
- Conservation management for species diversity

## Useful Links

*useufl links to open data to help with interpretation e.g. FC Woodland Data or OS or CEH*