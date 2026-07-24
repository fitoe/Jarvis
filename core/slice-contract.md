# Slice Contract

Use one compact packet when design, solution, and build reasoning must share
context. Keep it temporary unless recovery or another consumer needs it.

## Input

- goal and current observable result;
- current Product Truth and Visual Truth relevant to the slice;
- in-scope and out-of-scope behavior;
- typed product, functional, visual, quality, or release claims when the
  distinction affects completion;
- relevant files and local patterns;
- material assumptions and decisions;
- authority limits and known external effects;
- iteration, dependency, spend, and fidelity budget;
- visual source, viewport, project style references, must-preserve details, and
  must-not-invent boundaries when fidelity matters;
- verification and replanning triggers.

## Output

- result: completed, partial, or blocked;
- changed behavior and files;
- decisions added or invalidated;
- fresh, stale, and missing evidence;
- side effects confirmed or still planned;
- remaining material risk;
- next action.

The packet is a context boundary, not a mandatory project artifact. Routine work
can remain in conversation and code. Never use it to copy full logs or product
history between capabilities. When a slice delegates bounded work, derive each
worker's smaller [Delegated Task Packet](../templates/delegated-task.json) from
this context instead of forwarding the entire packet.
