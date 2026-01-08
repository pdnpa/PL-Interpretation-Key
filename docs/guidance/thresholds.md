# Threshold rules

This page defines the thresholds used to distinguish between visually similar habitat and land cover classes.

Thresholds are designed to support **consistent decision-making** during digitisation and the creation of robust AI training data.

---

## Why thresholds matter

Small differences in interpretation can introduce systematic bias into training datasets.

Explicit thresholds:
- reduce operator subjectivity
- improve class separability
- support model generalisation

---

## Cover thresholds

Unless otherwise specified:

- Percentage cover refers to **planimetric (map) area**
- Canopy cover is estimated visually from aerial imagery

Example thresholds include:
- >50% cover
- >75% dominance
- visually continuous canopy

---

## Woodland vs scrub

- Woodland:
  - trees typically >5 m in height
  - visually continuous canopy
- Scrub:
  - woody vegetation <5 m
  - broken or diffuse canopy

Where uncertain, default to **scrub** unless woodland criteria are clearly met.

---

## Heathland vs grassland

- Heathland:
  - dwarf shrub dominance (Calluna, Erica spp.)
- Grassland:
  - grass/herb dominance

Mixed areas should be classified by **dominant visible cover**, not species presence alone.

---

## Blanket bog variants

- Blanket bog is identified by:
  - landscape position
  - texture and colour
  - drainage patterns
- Variants (dry vs wet, grass/sedge dominated) are distinguished by:
  - surface moisture indicators
  - vegetation texture
  - presence/absence of visible standing water

---

## Bracken thresholds

- Bracken should be mapped where:
  - it forms visually coherent stands
  - cover exceeds **[X]%** within the polygon

Seasonal colour change should be anticipated and not misclassified.

---

## Edge cases and judgement calls

Where thresholds cannot be confidently applied:
- document the decision
- apply rules consistently across the project area
