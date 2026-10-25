# Develop, Then Review

The developer has the task. It edits the board, runs the tests, and commits -
inside the sandbox, against the mounted project. See the commit it made:

```bash
git log
```

```text no-run-button
a1b2c3d (developer) WAD-104: add Service column + filter to the board
9f3c1a2 Add sbxenv.yaml - shared team sandbox
```

In a one-agent setup, that commit is where you'd stop and hope it's right. In a
team, it's where the **reviewer** starts. Run the review:

```bash
team review
```

Read what the reviewer actually checks. It isn't just "does it run" - it checks
the change against the **acceptance criteria in the task** *and* the **coding
policy** you installed back in the earlier Cs:

```text no-run-button
  ✓ Service column renders           (acceptance)
  ✓ filter narrows to one service    (acceptance)
  ✓ existing tests pass              (acceptance)
  ✓ no secrets, no new registry      (policy - the boundary from Choice holds)
```

So far so good. But the reviewer finds something the *task never decided*:

```text no-run-button
  ⚠ product question, not a bug:
    what should the board show for incidents with NO service set?
```

This is the important move. The reviewer **does not guess**. A bug it would send
back to the developer; a *product decision* it refuses to invent - it pauses and
escalates. Confirm the team is now waiting:

```bash
team status
```

> [!NOTE]
> Giving the reviewer its own session - ideally a different model from the
> developer - is what catches this. A single agent reviewing its own work tends to
> rationalise its choices. Separate roles create an honest second opinion.

Next: answer the one question that's actually yours to answer.
