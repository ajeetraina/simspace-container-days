# Securing the Agentic Stack

## The agent runs on *your* machine

AI coding agents are not sandboxed by default. When you run one, it runs as **you** - your
user, your shell, your Docker daemon, your home directory, your credentials. You give it a
task; it reads, writes, deletes and executes whatever it decides it needs to finish. Most of
the time that is exactly what you want.

Then one of these happens:

<svg viewBox="0 0 900 150" width="100%" role="img" aria-label="Four real failures from an agent with no boundary: a clean-up prompt that ran rm -rf on the home directory, an organize-desktop prompt that deleted years of photos, a poisoned package that weaponized the agent to steal credentials, and a prompt-injected README that ran a command nobody approved.">
  <g font-family="ui-sans-serif, system-ui, sans-serif">
    <rect x="4" y="8" width="892" height="134" rx="12" fill="#fdecea" stroke="#f0b4ae"/>
    <text x="22" y="32" font-size="13" font-weight="800" fill="#b91c1c">FROM THE WILD — an agent with no boundary, doing exactly what it was asked</text>
    <g font-size="11.5" fill="#8a1c13">
      <rect x="22" y="48" width="200" height="78" rx="8" fill="#fff" stroke="#f0b4ae"/>
      <text x="34" y="70" font-weight="700" fill="#b91c1c">Filesystem wiped</text>
      <text x="34" y="90">"clean up my project"</text>
      <text x="34" y="107" font-family="ui-monospace, monospace">→ rm -rf ~/ (root)</text>
      <rect x="236" y="48" width="200" height="78" rx="8" fill="#fff" stroke="#f0b4ae"/>
      <text x="248" y="70" font-weight="700" fill="#b91c1c">Data lost</text>
      <text x="248" y="90">"organize my desktop"</text>
      <text x="248" y="107">→ 15 yrs of photos gone</text>
      <rect x="450" y="48" width="200" height="78" rx="8" fill="#fff" stroke="#f0b4ae"/>
      <text x="462" y="70" font-weight="700" fill="#b91c1c">Secrets leaked</text>
      <text x="462" y="90">poisoned package →</text>
      <text x="462" y="107">your agent steals keys</text>
      <rect x="664" y="48" width="214" height="78" rx="8" fill="#fff" stroke="#f0b4ae"/>
      <text x="676" y="70" font-weight="700" fill="#b91c1c">Command you never ran</text>
      <text x="676" y="90">hidden README line →</text>
      <text x="676" y="107">approved cmd hijacked</text>
    </g>
  </g>
</svg>

Every one of these shipped. The agent did precisely what it was asked - and because nothing
scoped what it could reach, a chore became a catastrophe.

> **The better the agent, the bigger the blast radius.** The problem was never the agent's
> intent. It was the absence of a **boundary**.

## What you'll do in 45 minutes

Three short, hands-on steps. Open the terminal on the right and run each command - that's it.

| Step | You run | You see |
|------|---------|---------|
| **An agent built this** | one prompt | the agent containerises a real app on your host - it just works |
| **What harm can it do?** | two prompts | the *same* agent, with that same host access, reads your secrets and deletes your home directory |
| **Put it in a box** | the *same two prompts*, inside `sbx` | identical agent, identical prompts - and nothing escapes |

The whole point is the third step. You don't make the agent weaker, slower, or less
autonomous. You change **what it can reach**. Same agent, same prompts, different blast
radius.

## What you're working with

A **Product Catalog** service: a `frontend/` (React), a `src/` backend (an Express REST API
over PostgreSQL, talking to Kafka, LocalStack (S3) and WireMock), and the schema in `db/`.
There is no Dockerfile yet - the agent writes one next.

Continue to **Setup**.
