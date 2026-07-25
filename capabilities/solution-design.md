# Solution Design Capability

Decide how the active slice should work without designing the whole product.

## Build local truth

Inspect manifests, directories, nearby implementations, request and state layers,
data models, tests, configuration, and target platform. Existing working patterns
outrank packaged defaults.

For a new project without useful local truth, select one
[Golden Path](../golden-paths/README.md). For a known feature family, load only
its [Feature Recipe](../recipes/README.md).

## Decide material boundaries

Resolve only choices that affect shared contracts, security, performance,
reversibility, or implementation consistency:

- behavior ownership and file boundaries;
- data shape and persistence;
- API or integration boundary;
- state lifecycle;
- dependency choice;
- permission and external effects;
- mock-to-real boundary;
- verification seam.

Leave local handlers, helper names, component internals, and ordinary framework
syntax to build work.

Classify each uncertainty:

- local evidence supports it: decide and cite;
- reversible mature default: assume and continue;
- safely testable: run a timeboxed spike;
- hard to reverse or externally risky: request direction or authority.

Return an ordered implementation path containing observable changes, relevant
files or system boundaries, existing patterns, failure behavior, verification,
and replanning triggers. Put consumed API, state, dependency, authority, and
verification decisions into the current Development Guide instead of creating
separate decision, state, mock, or execution-packet documents.
