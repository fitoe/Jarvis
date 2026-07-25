# Lead List Development Guide

Status: ready
Product plan: ../../product-plan.md
Page overview: ./overview.md
Related shared documents: none for this fixture
Last reviewed against upstream documents and current code: 2026-07-25

## Current development goal

Implement the read-only Lead List page so an authorized user can load leads, use
owner and status filters, recover from request failure, and open the matching
Lead Detail page.

Search, pagination, sorting controls, bulk actions, export, lead reassignment,
status mutation, and Lead Detail content are not part of this work.

## Product and journey context needed for this work

Lead List is the working queue between Dashboard and Lead Detail. Sales
representatives may see their own and unassigned leads. Sales managers may see
any team member's leads. Users require `leads:read`.

Supported statuses are `new`, `contacted`, `qualified`, and `disqualified`.
Filters must live in URL query parameters so returning from Lead Detail restores
the prior queue. List loading is read-only and must never mutate a lead.

These rules come from the Product Plan and Lead List Overview. This guide repeats
them because the implementation worker should not need those documents.

## Complete expected behavior

1. Opening `/leads` reads optional `owner` and `status` query parameters.
2. Invalid or unauthorized owner values fall back to All allowed owners without
   sending the invalid value to the API.
3. Invalid status values fall back to All statuses.
4. The page requests leads immediately using the normalized filters.
5. Changing either filter updates the URL and sends one new request using both
   current filter values.
6. The latest successful response replaces table rows. Responses from superseded
   requests must not overwrite newer filter results.
7. Selecting a row navigates to `/leads/<lead-id>` while the current list URL
   remains in browser history.
8. Clear filters removes both query parameters and reloads the unfiltered queue.

## States and failure behavior

The page must implement loading, empty, error, and retry behavior as well as the
normal result state:

- Initial loading: filters remain usable; table area shows skeleton rows.
- Filter loading: keep previous rows visible but mark the table busy.
- Normal: show lead name, company, owner, status, and localized last activity.
- Empty: show `No leads match these filters.` When a filter is active, show Clear
  filters; otherwise do not suggest clearing.
- Error: preserve current filters, show `Leads could not be loaded.` and Retry.
- Retry: repeat the same normalized request; disable Retry while it is running.
- Superseded request: ignore its success or failure result.

## Data and API details

Consume:

```text
GET /api/leads?owner=<owner-id>&status=<status>
```

Omit query parameters whose filter is All. Expected successful response:

```json
{
  "items": [
    {
      "id": "lead_123",
      "name": "Ada Chen",
      "company": "Northwind",
      "owner": { "id": "user_7", "name": "Mina Park" },
      "status": "contacted",
      "last_activity_at": "2026-07-24T08:30:00Z"
    }
  ]
}
```

Treat non-2xx responses and malformed payloads as the same user-visible load
failure. Do not invent pagination fields or mutation operations.

## Permissions and side-effect limits

- Reuse the existing route permission guard for `leads:read`.
- Reuse the existing current-user role and allowed-owner selector.
- Do not implement a new authorization rule inside the page.
- Do not request hidden owners, mutate leads, write production data, or add
  assignment, export, deletion, or status actions.
- If existing permission code conflicts about owner visibility, return
  `needs-context`; do not choose the more permissive interpretation.

## Visual and interaction requirements

Use the established internal-tool page shell and shared controls. Place page title
above one compact row containing Owner and Status filters. Use shared DataTable,
StatusBadge, TableSkeleton, EmptyState, and ErrorBanner components. Below 768px,
wrap filters and allow horizontal table scrolling.

Do not generate a new visual system. Do not add controls present only in generic
table examples.

## Existing code and patterns to reuse

- `web/src/pages/orders/OrderListPage.tsx`: URL-backed filters and stale-request
  protection.
- `web/src/features/leads/api.ts`: lead list request client and response types.
- `web/src/features/leads/permissions.ts`: allowed-owner calculation.
- `web/src/components/DataTable.tsx`: table, busy state, and row activation.
- `web/src/components/feedback/`: skeleton, empty, and error components.
- `web/src/router/routes.tsx`: route guard and Lead Detail route helper.

## Suggested change area

- `web/src/pages/leads/LeadListPage.tsx`
- focused Lead List tests under `web/src/pages/leads/__tests__/`
- `web/src/features/leads/api.ts` only if the existing read method lacks required
  optional filter parameters

## Do not change

- shared permission meaning or route-guard behavior
- Lead Detail implementation
- lead mutation APIs
- global DataTable or request-client contracts for other consumers
- application-wide visual tokens

## Implementation guidance

Start with focused page tests for normalized URL filters, request parameters,
states, retry, stale-response protection, and navigation. Reuse the Order List
pattern and existing lead methods. Keep filter normalization near the page unless
another current consumer already owns it. Do not add a generic query framework.

## Acceptance criteria

- AC-1: `/leads` loads all leads visible to the current user.
- AC-2: valid owner and status filters update the URL and API request together.
- AC-3: invalid filter values do not reach the API.
- AC-4: loading, normal, empty, error, and retry states match this guide.
- AC-5: superseded responses cannot replace newer filter results.
- AC-6: selecting `lead_123` opens `/leads/lead_123`.
- AC-7: the page performs no lead mutation and does not broaden permissions.

## Verification

- AC-1 to AC-3: focused page tests inspect initial and changed request URLs.
- AC-4: render focused loading, empty, error, disabled Retry, and recovered states.
- AC-5: resolve two requests out of order and assert only the latest rows render.
- AC-6: activate a row and assert the router reaches matching Lead Detail.
- AC-7: inspect the diff and request mocks; no mutation endpoint or permission
  change may appear.
- Run the repository's focused Lead List test command, then relevant type or
  syntax check. Report exact commands and results in the handback.

## When to stop and request more context

Return `needs-context` when:

- Product Plan, Page Overview, this guide, and repository permission behavior
  disagree;
- the API response shape differs materially from the described consumed fields;
- stale-request protection requires changing a shared request-client contract;
- Lead Detail routing does not have a stable identifier contract;
- acceptance cannot be verified at the page boundary.

Name the missing rule or contract, blocked behavior, safe work completed, and
smallest additional decision needed. Do not guess shared behavior.
