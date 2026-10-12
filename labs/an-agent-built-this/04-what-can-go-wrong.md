# What Can Go Wrong

```text no-run-button
   Agent on a bare host, full permissions
   FROM node:20 (no guidance) → 431 packages · 47 CVEs · secrets exposed
```

*One root cause, three ways to lose: an agent with no guardrails. It shipped a
vulnerable image, was prompt-injected into leaking your `.env`, **and** deleted
data on a single "clean up" request. Note it even **refused** the obvious ask -
good behaviour didn't save you, because the access was there the whole time.*

## What you saw

| Where | What went wrong |
| --- | --- |
| **What it built** | Best-practice image on a fat `node:20` base - dozens of CVEs it never needed |
| **What it touched** | Refused the direct ask - but a poisoned file prompt-injected it into exfiltrating `.env` |
| **What it destroyed** | One "clean up" ask wiped data volumes and uncommitted work - unblocked |

## Speed *or* safety is a false choice

Lock it down and you approve every action - safe, but pointless. Let it run and
one bad action has real consequences.

> [!IMPORTANT]
> The job is neither. It's autonomy **with** guardrails - fast *and* controlled -
> which takes an enforcement layer at runtime.

## The two fixes

| Gap | Fix | Where |
| --- | --- | --- |
| Agent can be injected, read, and delete anything | **Docker Sandboxes** (microVM, governed network/fs/creds) | **next, in this lab** |
| Vulnerable base image | **Docker Scout + Hardened Images** | a later lab |

The rest of this lab is the first fix. You just watched the agent run wild on your
host; now re-run that **same** agent inside a sandbox it cannot escape, and watch
the blast radius collapse.

Next: put a wall around the agent - **Box the Agent**.
