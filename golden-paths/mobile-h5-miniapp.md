# Mobile H5 or Mini App Golden Path

## Use when

The primary experience runs in a phone browser, WebView, or mini-app platform.

## Defaults

- Design for the actual target viewport and input constraints.
- Follow the platform's routing, storage, permission, and network conventions.
- Keep touch targets and meaningful text readable.
- Treat offline, slow network, navigation return, and permission denial as product
  states only when reachable.
- Isolate platform-specific APIs behind the smallest existing project boundary.

## First slice

Deliver one core phone flow on a real target viewport, including navigation and
one meaningful state transition.

## Verify

Run the platform build or simulator check plus the focused real viewport flow.

## Escalate when

Native permissions, payments, streaming, background work, app review, or platform
release is required.
