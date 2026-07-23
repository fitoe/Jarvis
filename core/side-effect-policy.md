# Side-Effect Policy

Record externally visible or hard-to-repeat operations before execution:

- publish, deploy, release, or push;
- create external resources;
- send messages;
- charge money or change inventory;
- migrate or delete data;
- modify production state.

Each record names action, exact target, stable idempotency key, status, and
evidence. Before acting:

```json
{
  "id": "S1",
  "action": "create_repository",
  "target": "owner/repository",
  "idempotency_key": "github:owner/repository",
  "status": "confirmed",
  "evidence": "https://github.com/owner/repository"
}
```

1. Check the ledger for the idempotency key.
2. Query current external state when possible.
3. Confirm authority and scope.
4. Execute once.
5. Record confirmed result or failure evidence.

Never repeat an operation solely because the session, agent, or plan restarted.
If external state and the ledger disagree, stop and reconcile rather than guess.
