---
code: r2
title: Rivers and streams
parent: r
ukhab: r2
status: draft
description: >
  Rivers and streams from bank top to bank top (see UKHabs, specifications?). Often appears very dark aerially.
subclasses: []
associated_habitats:
  - "Canal"
  - "Fast-flowing river and stream"
  - "Sluggish river and stream"
  - "Chalk river and stream"

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
    - [r1 Inland open water](open-water.md)

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