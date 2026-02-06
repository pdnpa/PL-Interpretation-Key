---
code: g3
title: Unconsolidated bare ground
parent: g
ukhab: s3
status: draft
description: >
  Ground types that are not fixed and can move around, such as loose sand, shingle or mud. Vegetation cover is sparse, as it is difficult for plants to root in unstable ground.
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
    - [g3a Sand](sand.md)
    - [g3b Mud](mud.md)

---

## In Protected Landscapes

Occurs widely, especially near coasts, rivers, estuaries, and dynamic shorelines; includes sand/mud/shingle surfaces depending on location.

### Management and drivers

The structure and extent are influenced by:

* Sediment supply and transport by wind/water
* Tidal and river flow dynamics
* Storm events and extreme rainfall/flooding
* Coastal and river engineering/defences altering movement
* Dredging and sediment management
* Recreational trampling and vehicle access


## Useful Links

* [UKHab – Habitat Definitions v1.0 (PDF)](https://ecountability.co.uk/wp-content/uploads/2018/05/UK-Habitat-Classification-Habitat-Definitions-V1.0-May-2018-1.pdf)
* [UK BAP – Priority Habitat Descriptions (revised 2011) (PDF)](https://data.jncc.gov.uk/data/2728792c-c8c6-4b8c-9ccd-a908cb0f1432/UKBAP-PriorityHabitatDescriptions-Rev-2011.pdf)
