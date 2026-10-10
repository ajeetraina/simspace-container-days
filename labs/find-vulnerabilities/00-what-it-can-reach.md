# What the Agent Can Reach

Containment is always on; **Control** is what you tune. The agent is already
boxed - every outbound request leaves through a proxy that allows or blocks it
against your policy. First, see the posture you start with.

## The profiles you can pick

```bash
sbx policy profile ls
```

Three governance profiles: **locked-down** (only what you allow), **balanced**
(common dev endpoints, everything else denied - the default), and **open**
(outbound allowed, still logged).

## The active policy

```bash
sbx policy ls
```

Under `balanced`, the agent can reach `api.anthropic.com` and `registry.npmjs.org`,
but anything else is denied and logged.

> [!NOTE]
> You don't have to choose "all or nothing". You start from a sensible default
> and adjust - per host, per sandbox.

Next: check an endpoint before you run.
