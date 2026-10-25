# Assign From the Backlog

The team is just a few lines added to the `sbxenv.yaml` you already share. Read
it:

```bash
cat sbxenv.yaml
```

```text no-run-button
team:
  coordinator: { agent: claude, model: opus }
  developer:   { agent: claude, model: sonnet }
  reviewer:    { agent: claude, model: sonnet }
  backlog: ./backlog   # where the coordinator reads tasks and writes results
```

Three roles, each a session in the same box. The provider and model are chosen
**per role** - here a stronger model coordinates and reviews, a faster one does
the edits, but a reviewer could just as easily be a *different* assistant
entirely. Boot the team:

```bash
sbx env run
```

Same secured sandbox as Capacity - now with three roles instead of one. See who's
there:

```bash
team status
```

Everyone's idle, because nobody has told them what to do. That's the backlog's
job. Look at the work:

```bash
backlog ls
```

```bash
backlog show CAT-12
```

The coordinator reads from this backlog so *you* aren't the one dispatching every
step. Hand it the task:

```bash
team assign CAT-12
```

The coordinator picks up CAT-12 and hands it to the developer - then stays out of
the diff. Its job is **what** and **who**, not the edit itself. Check again:

```bash
team status
```

> [!NOTE]
> The backlog is a plain folder of task files here. In a real factory it's your
> tracker (Jira, GitHub issues, or any backlog tool) reached through the **MCP gateway** from
> Choice - so the team gets *scoped* access to it, not your whole host.

Next: let the developer finish and the reviewer check the work.
