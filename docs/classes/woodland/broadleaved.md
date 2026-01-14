---
code: c1
title: Broadleaved woodland
parent: c
ukhab: w1
status: draft
description: >
  Areas dominated by trees >5m tall. There must be a tree canopy cover of at least ???%, with ≥???% consisting of deciduous, broadleaved species. Includes ancient and recent woodland, with trees that have grown from seed or planted seedlings. Tends to have shades of green and appear full in the summer, with a more brown and sparse appearance in the winter when the leaves have been lost.
subclasses: [c1a, c1b]
associated_habitats:
  - "To be confirmed with Landscapes"

---

# {{ title }} ({{ code }})

**UKHab:** {{ ukhab }}  
**Parent:** {{ parent }}  
**Status:** {{ status }}

---

<figure class="interp-figure">
  <img src="../../../assets/images/c/c1.png" alt="{{ title }} ({{ code }})">
  <figcaption>
    Broadleaved high forest with mixed species. 
    <br><small>Image: CC-BY, Woodland Trust</small>
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
    - [s1 Scrub](../scrubland/scrub.md)

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