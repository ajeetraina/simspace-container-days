# Try the Escape

The classic container breakout: reach the Docker socket, launch a privileged
container, and you own the host. Let's try it - from inside the sandbox.

## Reach for the Docker daemon

```bash
sbx exec demo docker ps
```

There *is* a Docker daemon here - but it's the **sandbox's own**, empty and
throwaway. A privileged container launched against it writes into the sandbox and
dies with it. The host socket is not mounted, so the host daemon is unreachable.

## Read the record

```bash
sbx policy log
```

Every connection the agent tried is logged with the rule that decided it - the
LLM endpoint was `allowed`, the cloud metadata endpoint (`169.254.169.254`) was
`blocked` by default.

```text no-run-button
  on the host              in the sandbox
  rm -rf ~          →      /host is read-only
  read ~/.aws       →      not mounted
  docker.sock       →      sandbox's own daemon
```

> [!NOTE]
> **Contain** done. The agent kept every capability it needs - and lost every
> path to the host. Next pillar: **Control** - deciding what it may reach.

You've completed Contain.
