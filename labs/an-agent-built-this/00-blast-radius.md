# The Blast Radius

An AI coding agent is useful *because* it acts on its own - it plans, runs
commands, edits files, and calls APIs, hundreds of times, without stopping to
ask. The problem is **where** it does that: on your host, it runs as **you**,
with your filesystem, your secrets, your Docker daemon, and your whole network
in reach.

## Start from nothing boxed

```bash
sbx ls
```

No sandboxes yet - so an agent would run straight on the host. One prompt-injected
instruction or one bad command, and the blast radius is your entire machine.

> [!NOTE]
> This is **Contain**, the first of the four Cs. It doesn't make the agent less
> capable - it puts a wall around what "its own" means.

Next: put the agent in a box.
