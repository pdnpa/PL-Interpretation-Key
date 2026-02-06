---
code: g3a
title: Sand
parent: g3
ukhab: s3
status: draft
description: >
  Fine grains of rocks and minerals. Typically found coastally or by water systems.
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
    - [h1 Sand dunes](../coastland/sand-dunes.md)

---

## In Protected Landscapes

Typically found coastally (beaches, dunes) and also beside rivers and some lakes/reservoir margins. Therefore present mainly in coastal protected landscapes, but can also occur inland along sandy river systems or where geology and sediment supply create sandy substrates.

### Management and drivers

The structure and extent are influenced by:

* Sediment supply and transport (wind, tides, river inputs)
* Coastal defences and development altering movement and deposition
* Dredging and sediment management
* Storm events and changing sea conditions (climate-driven)
* Recreational pressure (trampling, vehicles) redistributing sediment
* Stabilisation/planting in dune systems (where applicable)
* Sea-level rise and shifting currents affecting accumulation/erosion

## Useful Links

* [JNCC – Coastal Sand Dunes (UK BAP) (PDF)](https://data.jncc.gov.uk/data/4b9e595b-c337-48c7-9880-b1611d02acbb/UKBAP-BAPHabitats-09-CoastSandDunes.pdf)
* [UKHab – Habitat Definitions v1.0 (PDF)](https://ecountability.co.uk/wp-content/uploads/2018/05/UK-Habitat-Classification-Habitat-Definitions-V1.0-May-2018-1.pdf)
