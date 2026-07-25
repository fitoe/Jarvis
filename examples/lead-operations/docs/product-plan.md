# Lead Operations Product Plan

Status: approved for evaluation

## Product goal

Help a small sales team see its active leads, narrow the queue to relevant work,
and open one lead for follow-up without losing context.

## Users and core jobs

- Sales representative: find owned leads and open the next record to contact.
- Sales manager: inspect team leads by owner and status.

## Core journeys

1. Open Dashboard and see current lead workload.
2. Open Lead List and narrow leads by owner or status.
3. Open Lead Detail to review history and continue follow-up.

## Page inventory

- Dashboard: summary and entry to the working lead queue.
- Lead List: searchable working queue with owner and status filters.
- Lead Detail: full lead record, activity history, and follow-up actions.

## Page relationships

Dashboard opens Lead List without mandatory filters. Selecting a Lead List row
opens Lead Detail for that lead. Returning from Lead Detail should preserve list
filters through URL query parameters.

## Shared business rules

- Supported lead statuses: `new`, `contacted`, `qualified`, `disqualified`.
- A lead has one current owner or is unassigned.
- Lead List and Lead Detail use the same lead identifier and status labels.

## Shared data and API constraints

- Lead identifiers are opaque strings.
- Dates arrive as ISO 8601 strings and display in the user's local timezone.
- List requests are read-only and must not mutate lead state.

## Permissions and authority

- Users need `leads:read` to open Lead List or Lead Detail.
- Sales representatives may view their own and unassigned leads.
- Sales managers may view leads for any team member.
- This evaluation does not authorize lead mutation, reassignment, export, or
  deletion.

## Visual direction

Use the established internal-tool shell, shared filter controls, DataTable,
status badge, spacing tokens, and error banner. No new visual system or Image 2
generation is needed for this established page family.

## Delivery priority

1. Lead List loading, filters, recovery, and Lead Detail navigation.
2. Lead Detail read-only information.
3. Dashboard summary.

## Product-level acceptance

- An authorized user can move from the working queue to one lead record.
- Permission and status meaning remain consistent across Lead List and Detail.
- Failed list loading has a visible recovery path.

## Assumptions and unresolved decisions

- Search, bulk actions, reassignment, export, pagination, and lead mutation are
  outside the first evaluation slice.
