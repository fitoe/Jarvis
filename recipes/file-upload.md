# File Upload

## Use when

Users or integrations submit files for storage, processing, or later access.

## Avoid when

A small trusted configuration file can remain part of an existing form boundary.

## Default solution

- Validate type, size, and ownership on the server boundary.
- Use direct-to-storage upload only when the platform already supports safe signed
  access; otherwise use the existing request path.
- Represent pending, progress when meaningful, success, retryable failure, and
  cancellation when supported.
- Store metadata separately from opaque file content.
- Clean partial or orphaned objects when the workflow can create them.

## Common failures

Trusting browser MIME type, public object exposure, orphaned uploads, duplicate
submissions, and memory-heavy server buffering.

## Verify

Upload an allowed file, reject one material invalid case, and verify stored object
access follows ownership rules.

## Escalate when

Sensitive files, malware scanning, public sharing, large uploads, retention, or
production storage credentials enter scope.
