# "Works on My Machine" Is the Enemy

```text no-run-button
  you            a teammate
  ┌──────────┐   ┌──────────┐
  │ node:20  │   │ node:22  │   different base
  │ +notion  │   │ (none)   │   different tools
  │ open net │   │ locked   │   different policy
  └──────────┘   └──────────┘
        ╲             ╱
      same prompt, different sandbox → different result
```

*You secured a sandbox in the earlier Cs. But a boundary that only exists on your
laptop isn't governance - it's a one-off. Capacity is the fourth C: the same
sandbox, reproduced for everyone.*

## Try it

```bash
sbx run claude
```

It boots - but look at the warning. The image, agent, tools, and network policy
all come from **your local defaults**. A teammate running the very same command
can get a different base, different MCP tools, and a different network policy.

That drift is where "works on my machine" comes from - and, worse, where an
**ungoverned** sandbox sneaks in: the policy you carefully set never reaches the
next person.

> [!NOTE]
> The fix is the same one we use for everything else that matters: **define it
> once, in a file, and share it like code.**

Next: capture the sandbox as a template.
