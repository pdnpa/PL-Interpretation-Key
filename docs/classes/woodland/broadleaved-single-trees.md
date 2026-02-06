---
code: c1a
title: Single trees (broadleaved)
parent: c1
ukhab: w1
status: draft
description: >
  Isolated, broadleaved trees outside woodland. Only includes individual trees; as soon as there are more than one it must be classed as c1.
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
    - [s2 Hedgerows](../woodland/hedgerows.md)

---

## In Protected Landscapes

Occurs throughout protected landscapes as parkland trees, field trees, street/settlement trees, and isolated boundary trees.

### Management and drivers

The structure and extent are influenced by:

* Veteran tree management and safety works
* Loss/replacement rates and planting initiatives
* Grazing pressure and browsing on saplings
* Field boundary change (hedge removal/creation)
* Disease and pests (e.g., ash dieback effects where relevant)
* Storm damage, drought stress, and soil compaction
* Agricultural operations (ploughing close to roots, spray drift)
* Development and infrastructure pressures near settlements/roads

## Useful Links

* [JNCC – Wood-pasture and parkland (UK BAP, revised 2011) (PDF)](https://data.jncc.gov.uk/data/0a8c2440-20c8-4a0c-85e7-7a8e7f4b9d4b/UKBAP-BAPHabitats-65-WoodPastureParkland-2011.pdf)
* [UKHab – Habitat Definitions v1.0 (PDF)](https://ecountability.co.uk/wp-content/uploads/2018/05/UK-Habitat-Classification-Habitat-Definitions-V1.0-May-2018-1.pdf)
