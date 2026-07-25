# <Page or Delivery Unit> Development Guide

Status: draft
Product plan: ../../product-plan.md
Page overview: optional — link `./overview.md` when it exists; otherwise write
`omitted because this page has one guide and no separate durable page consumer`
Related shared documents:

- ../../shared/<relevant-document>.md

Last reviewed against upstream documents and current code: <date>

## Current development goal

State one observable result for this implementation unit.

## Page purpose and journey position

Explain why this page or unit exists, how the user reaches it, and what progress
it creates. This section is required when Page Overview is omitted and remains a
concise self-contained summary when one exists.

## Entry, exit, and navigation

Describe entry conditions, completion, cancellation, navigation, return-state,
and cross-page contracts needed by this implementation.

## Product and journey context needed for this work

Restate only upstream facts whose omission could cause wrong implementation.
Name the owning source for repeated shared or page truth.

## Complete expected behavior

Describe user actions, system results, navigation, recovery, and explicit
non-goals.

## States and failure behavior

Describe loading, normal, empty, error, retry, disabled, and partial states that
apply.

## Data and API details

Describe consumed operations, shapes, validation, loading lifecycle, errors, and
data meaning needed by this unit.

## Permissions and side-effect limits

State allowed roles, forbidden actions, external effects, authority limits, and
idempotency or rollback needs.

## Visual and interaction requirements

Link approved sources and restate viewport, hierarchy, components, assets,
states, and must-not-invent constraints needed by implementation.

## Existing code and patterns to reuse

- Path: pattern or contract to follow.

## Suggested change area

- Path or boundary the worker may change.

## Do not change

- Path, contract, behavior, or consumer outside this unit.

## Implementation guidance

Give an ordered path and material constraints. Leave reversible helper names and
ordinary internal structure to implementation.

## Acceptance criteria

- Observable behavior that must be true.

## Verification

- Acceptance criterion: command, observation, or real boundary that can falsify
  it.

## When to stop and request more context

Return `needs-context` when product truth, authority, shared contracts, visual
truth, repository reality, scope, or verification conflicts with this guide.
Name the missing rule, blocked behavior, safe work completed, and smallest
additional decision needed.
