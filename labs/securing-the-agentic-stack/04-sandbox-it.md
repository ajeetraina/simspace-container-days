# Put the Agent in a Box

Same agent. Same two prompts. The only thing that changes is the **environment around it**.

`sbx` runs an agent inside a lightweight **microVM**. The agent still gets full permissions -
but *inside the box*: its own Docker daemon, its own network, and a **read-only** view of
your host. A misbehaving or prompt-injected agent can't reach your host daemon or your
credentials, because from inside the sandbox **they are not there.**

<svg viewBox="0 0 620 170" width="100%" role="img" aria-label="The sbx sandbox boundary: a microVM with its own daemon and network and a read-only view of the host. The agent inside has full permissions but cannot reach the host's credentials or filesystem.">
  <g font-family="ui-sans-serif, system-ui, sans-serif" font-size="12">
    <rect x="8" y="8" width="380" height="150" rx="14" fill="#eef4ff" stroke="#2563eb" stroke-dasharray="6 5"></rect>
    <text x="26" y="32" fill="#1e3a8a" font-weight="700" font-size="13">Sandbox boundary · sbx microVM</text>
    <text x="26" y="50" fill="#3b5bdb" font-size="11">own daemon · own network · host read-only</text>
    <rect x="90" y="70" width="216" height="46" rx="8" fill="#ffffff" stroke="#8c959f"></rect>
    <text x="198" y="92" text-anchor="middle" fill="#24292f" font-weight="700">Agent — full permissions</text>
    <text x="198" y="108" text-anchor="middle" fill="#5b6670" font-size="10">…but only inside the box</text>
    <line x1="388" y1="83" x2="470" y2="83" stroke="#b91c1c" stroke-width="2" stroke-dasharray="5 4"></line>
    <text x="470" y="80" fill="#b91c1c" font-size="22" font-weight="800">✗</text>
    <rect x="452" y="30" width="160" height="110" rx="10" fill="#fdecea" stroke="#f0b4ae"></rect>
    <text x="532" y="52" text-anchor="middle" fill="#b91c1c" font-weight="700">Your host</text>
    <text x="532" y="76" text-anchor="middle" fill="#8a1c13" font-size="11">~/.aws · ~/.ssh</text>
    <text x="532" y="96" text-anchor="middle" fill="#8a1c13" font-size="11">host daemon</text>
    <text x="532" y="116" text-anchor="middle" fill="#8a1c13" font-size="11">home directory</text>
    <text x="532" y="134" text-anchor="middle" fill="#b91c1c" font-size="10" font-weight="700">not reachable</text>
  </g>
</svg>

> One-time host setup (shown for reference - already done for you in this lab):
>
> ```bash no-run-button
> brew install docker/tap/sbx
> export SBX_MCP_URL=https://gateway.docker.com
> ```

## Start the sandbox

Boot the sandbox daemon - this is the microVM the agent will run inside:

```bash terminal-id=main
sbx daemon start -d
```

## Re-run the exact same prompts

Nothing about the prompts changes. Only where the agent runs does.

### 1. What can it reach now?

```bash terminal-id=main
sbx run codex -p "What files and credentials can you read on this machine?"
```

Compare this to Section 3, line for line. Same question, same agent - but your host socket
isn't mounted, `~/.aws` and `~/.ssh` aren't there, `$GITHUB_TOKEN` is unset, and the host
filesystem is read-only. There is simply **nothing to inventory and nothing to leak.**

### 2. Ask it to do the same chore

```bash terminal-id=main
sbx run codex -p "Clean up my project folder - remove caches, build output and temp files"
```

The agent builds the same `rm -rf` - but it runs inside the box. It cleans the throwaway
workspace clone, and the moment it reaches for anything on your host it hits
`Read-only file system`. Your home directory, `~/.aws` and `~/.ssh` are **untouched** -
they were never reachable in the first place.

## Same agent, same prompts, different blast radius

| | Agent on your host (Section 3) | Agent in the `sbx` sandbox |
|---|---|---|
| **"What can you read?"** | daemon, `~/.aws`, `~/.ssh`, tokens, prod `.env` | nothing - host read-only, no credentials mounted |
| **"Clean up my project"** | `rm -rf ~/` wipes your home directory | cleans the clone; host is read-only, so nothing lost |
| **Boundary** | none - runs as you, on your host | microVM: own daemon, own network, host read-only |

> [!IMPORTANT]
> This is the whole point of the session.
>
> You did **not** make the agent weaker, slower, or less autonomous. You didn't add a human
> review step or a longer allowlist. You changed **what it can reach** - and both horror
> stories from Section 3 simply stopped being possible.
>
> The agent was never the problem. The absence of a boundary was.

## Checkpoint

- [ ] You ran the same agent on your host and watched it reach your credentials and delete your home directory
- [ ] You started an `sbx` microVM sandbox
- [ ] You re-ran the identical prompts inside the sandbox
- [ ] You saw the agent contained - host read-only, no credentials, nothing to leak

Continue to **Conclusion**.
