---
code: c2
title: Coniferous woodland
parent: c
ukhab: w2
status: draft
description: >
  Areas dominated by trees >5m tall. There must be a tree canopy cover of at least ???%, with ≥???% consisting of coniferous species. The majority of coniferous woodlands in the UK are from planted seedlings. Easily recognisable in aerial imagery, as plantations consist of uniformly aged, coloured and spaced trees, often with defined borders.
subclasses: [c2a, c2b]
associated_habitats:
  - "To be confirmed with Landscapes"

---

# {{ title }} ({{ code }})

**UKHab:** {{ ukhab }}  
**Parent:** {{ parent }}  
**Status:** {{ status }}

---

<figure class="interp-figure">
  <img src="../../../assets/images/woodland/c2.jpg" alt="{{ title }} ({{ code }})">
  <figcaption>
    Edge of a Coniferous woodland area in active management for forestry. 
    <br><small>Image: CC-BY, Robin Webster</small>
  </figcaption>
</figure>

---

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
    - [c5 Clear felled / newly planted](felled.md)

---

## In Protected Landscapes

Occurs across many protected landscapes, particularly uplands and areas with commercial forestry blocks.

### Management and drivers

The structure and extent are influenced by:

* Harvesting cycles (clearfell vs continuous cover)
* Replanting/restocking rules and species selection
* Ground preparation (mounding, drainage) affecting hydrology
* Deer browsing and tree protection requirements
* Windthrow risk and storm events
* Pest/disease outbreaks and biosecurity measures
* Landscape design constraints and visual impact guidance
* Market economics for timber and policy incentives

## Useful Links

* [UK Forestry Standard (UKFS) – GOV.UK collection](https://www.gov.uk/government/collections/the-uk-forestry-standard)
* [UKHab – Habitat Definitions v1.0 (PDF)](https://ecountability.co.uk/wp-content/uploads/2018/05/UK-Habitat-Classification-Habitat-Definitions-V1.0-May-2018-1.pdf)
