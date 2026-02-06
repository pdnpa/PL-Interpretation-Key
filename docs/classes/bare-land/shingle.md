---
code: g3c
title: Shingle
parent: g3
ukhab: s3
status: draft
description: >
  Coarse fragments of rock, such as pebbles, rounded by the erosion of water. Typically found coastally or by water systems.
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
    - [h3 Vegetated shingle](../coastland/vegetated-shingle.md)

---

## In Protected Landscapes

Typically found along the coastline or near dynamic water systems, therefore only present in protected landscapes with coastal/estuarine sections (or large river gravel bars in rarer cases). Often occurs as mobile beaches/banks where vegetation struggles to establish.

### Management and drivers

The structure and extent are influenced by:

* Storms, wave energy, and longshore drift
* Coastal engineering/defences altering sediment movement
* Dredging and sediment management
* Shingle removal or reprofiling for coastal management
* Human access (trampling, vehicle tracks) redistributing material
* Sea-level rise and changing storm regimes (climate-driven)
* Sediment supply from cliffs and offshore sources

## Useful Links

* [JNCC – Coastal Vegetated Shingle (UK BAP) (PDF)](https://data.jncc.gov.uk/data/4b9e595b-c337-48c7-9880-b1611d02acbb/UKBAP-BAPHabitats-10-CoastVegShingle.pdf)
* [UK BAP – Priority Habitat Descriptions (revised 2011) (PDF)](https://data.jncc.gov.uk/data/2728792c-c8c6-4b8c-9ccd-a908cb0f1432/UKBAP-PriorityHabitatDescriptions-Rev-2011.pdf)
