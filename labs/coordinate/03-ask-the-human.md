# Ask the Human

The team is blocked on one thing - and it's not a thing an agent should settle.
See the question:

```bash
team ask
```

```text no-run-button
reviewer → you:
  incidents with no service assigned. Options:
    (a) show them under an "Unassigned" service
    (b) hide them when a service filter is active
```

This is the whole reason a factory beats a runaway agent. The team did everything
mechanical - read the task, wrote the code, ran the tests, checked the policy -
and then **drew the line exactly where human judgement starts.** Make the call:

```bash
team answer "a"
```

Watch the hand-off run back down the team: the developer applies your decision,
the reviewer re-checks and approves, and the coordinator closes the task and
writes the result back to the backlog. Confirm it's done:

```bash
team status
```

```text no-run-button
WAD-104  done  ✓ reviewed and closed in the backlog.
```

That's the factory, end to end:

```text no-run-button
  backlog → coordinator → developer → reviewer → YOU (decide) → done
                                         └── loops back if it's a bug ──┘
```

> [!NOTE]
> Notice what *didn't* happen. The team never invented a product answer, never
> touched a secret, never reached a registry the policy denies. Autonomy ran right
> up to the boundary you set - and the one judgement call stayed yours.

## The five Cs, together

You've now seen the whole arc:

| C | What it gives the factory |
|---|---|
| **Contain** | an isolated microVM the team can't escape |
| **Control** | a network policy that scopes what it can reach |
| **Choice** | the MCP tools and DHI pin it's allowed to use |
| **Capacity** | the same secured sandbox, reproduced for everyone |
| **Coordinate** | a team of roles that works the backlog and asks you when it matters |

A single agent is a demo. A *team of agents inside a boundary you defined* - doing
the work, stopping for the decisions - is a software factory you'd actually trust.

Take the `team` block and this flow to a real repo: point the backlog at your
tracker over the MCP gateway, and let the roles run in the sandbox you secured in
the earlier Cs.
