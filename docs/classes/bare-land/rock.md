---
code: g2
title: Bare rock
parent: g
ukhab: s1
status: draft
description: >
  Areas of exposed, unvegetated rock, such as scree, cliffs and limestone pavements. Only planimetric area is mapped, so large but near vertical cliffs may cover a small area when mapped, or even be missed.
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
    - [g6 Scree](scree.md)

---

## In Protected Landscapes

Widespread but more common in uplands and coastal cliffs; also appears as outcrops, crags, and rock exposures in valleys.

### Management and drivers

The structure and extent are influenced by:

* Geology and natural exposure (outcrops, cliffs)
* Weathering and freeze-thaw processes
* Rockfalls and slope instability
* Vegetation colonisation (lichen, moss, scrub) over time
* Grazing pressure limiting soil build-up and plant cover
* Recreational climbing/walking impacts on fragile ledges
* Coastal erosion processes (where relevant)

## Useful Links

* [UKHab – Habitat Definitions v1.0 (PDF)](https://ecountability.co.uk/wp-content/uploads/2018/05/UK-Habitat-Classification-Habitat-Definitions-V1.0-May-2018-1.pdf)
* [UK BAP – Priority Habitat Descriptions (revised 2011) (PDF)](https://data.jncc.gov.uk/data/2728792c-c8c6-4b8c-9ccd-a908cb0f1432/UKBAP-PriorityHabitatDescriptions-Rev-2011.pdf)
