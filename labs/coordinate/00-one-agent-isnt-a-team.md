# One Agent Isn't a Team

Across the earlier Cs you secured one sandbox - an isolated microVM (Contain), a
network policy (Control), the right MCP tools (Choice) - and Capacity made it
reproducible for everyone. So you can hand any teammate the same safe box.

But a safe box with one agent in it is still one pair of hands. Run it the solo
way and watch what's missing:

```bash
sbx run claude
```

It boots and waits for you to type a task. That works - but notice who *isn't*
there:

```text no-run-button
  one session
      │
      ▼
  does whatever you type
      ✗ nobody decides WHAT to work on
      ✗ nobody reviews the result
      ✗ nobody owns the product decision
```

A **software factory** is the fifth C: **Coordinate**. Instead of one session, you
run a small team inside the same secured sandbox, each role a session of its own:

- a **coordinator** that pulls work from a backlog and assigns it,
- a **developer** that edits and commits,
- a **reviewer** that checks the result against the task and your coding policy.

And when the work hits a decision that isn't in the task - a real product call -
the team **stops and asks you**, instead of guessing.

> [!NOTE]
> The team runs *inside* the sandbox you already secured. Every role inherits the
> same microVM, the same network policy, and the same DHI pin. Coordinate adds
> the roles; it doesn't loosen the boundary.

Next: boot the team and assign a task from the backlog.
