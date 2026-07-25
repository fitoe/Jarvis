# Lead List Overview

Status: approved
Product plan: ../../product-plan.md
Related shared documents: none for this fixture

## Page purpose

Provide the team's working lead queue and let users narrow it to relevant owner
and status combinations before opening one lead.

## Place in the user journey

Lead List sits between Dashboard and Lead Detail. It is the first page where a
user chooses the specific lead to work on.

## Entry and exit

- Entry: Dashboard lead summary or direct `/leads` navigation.
- Exit: selecting a row opens `/leads/<lead-id>`.
- Browser back should restore the list because filters live in URL query
  parameters.

## Users and permissions

Users need `leads:read`. Representatives see their own and unassigned leads;
managers may select any team member. Unauthorized users do not receive list data.

## Content and data

Each row shows lead name, company, current owner, status, and last activity time.
Owner and status values use shared product meaning.

## User actions

- Choose one owner or All allowed owners.
- Choose one status or All statuses.
- Retry a failed request.
- Open Lead Detail by selecting a row.

## Loading, normal, empty, error, and disabled states

- Loading: keep filters visible and show table skeleton rows.
- Normal: show returned leads in last-activity-descending order.
- Empty: explain that no leads match current filters and offer Clear filters when
  at least one filter is active.
- Error: show a non-destructive error banner and Retry action.
- Disabled: disable Retry while a retry request is running.

## Responsive and platform behavior

Desktop-first internal tool. At widths below 768px, filters wrap above the table;
all required columns may scroll horizontally rather than disappear.

## Visual structure

Use the established page shell, title row, compact filter row, DataTable, status
badge, skeleton, empty state, and error banner. Lead Detail navigation remains the
primary row interaction.

## Shared rules and dependencies

Depends on read permission, lead status labels, owner visibility rules, Lead List
API, router, and shared table and feedback components.

## In scope and out of scope

- In: initial load, owner filter, status filter, all required states, retry, and
  Lead Detail navigation.
- Out: search, sorting controls, pagination, bulk actions, export, assignment,
  status mutation, and Lead Detail content.

## Page-level acceptance

- Authorized users can load and filter the queue.
- Loading, empty, error, and retry states are usable.
- Selecting a row opens the matching Lead Detail route.
- No action mutates lead data.

## Remaining uncertainty

None for the current evaluation slice.
