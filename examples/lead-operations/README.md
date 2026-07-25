# Lead Operations Golden Example

This fixture shows the optional three-document form for one bounded page:

```text
docs/product-plan.md
  -> docs/pages/lead-list/overview.md
  -> docs/pages/lead-list/development.md
```

Dashboard and Lead Detail remain coarse in the Product Plan. Lead List is the
active page, so it receives a Development Guide. Lead List keeps Page Overview
because its durable filters, states, permissions, navigation contract, product
review, and future implementation slices have more than one consumer. A simple
single-guide page would omit Overview and compile this context directly into its
Development Guide.

The guide deliberately repeats consumed product, permission, API, state, and
visual rules so a fresh implementation model can understand the task without the
upstream documents.

The named application paths are illustrative repository context for a future
agent-vs-baseline fixture. This example proves document shape and context intent,
not small-model implementation quality. Run the read-only and implementation
comparisons before claiming behavioral improvement.
