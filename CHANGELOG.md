# Changelog

## 0.3.0 - 2026-07-24

- Add a conditional GPT Image 2 visual-source policy for new UI surfaces.
- Preserve one approved visual baseline across later project screens and prompts.
- Use `Product Design:image-to-code` as the preferred translation and QA provider
  while Jarvis retains product and delivery ownership.
- Add same-viewport comparison, product-truth boundaries, and visual-source fields
  to the Slice Packet.
- Add behavior evaluations for generation, reuse, source priority, and hallucinated
  functionality.

## 0.2.0 - 2026-07-24

- Replace four public skill entry points with one `jarvis` skill.
- Move product, solution, and build guidance into internal capability modules.
- Add Slice Contract and Slice Packet context boundary.
- Add product validation and delivery budget policies.
- Add evidence freshness and side-effect idempotency policies.
- Replace YAML state template with validated JSON state and reconciliation CLI.
- Consolidate behavior evaluations and add positive/negative trigger fixtures.
- Treat skill size as a review signal instead of a validation failure.

## 0.1.0 - 2026-07-24

- Establish initial four-skill feedback-control foundation.
- Add Golden Paths, Feature Recipes, packaging, structural validation, and CI.
