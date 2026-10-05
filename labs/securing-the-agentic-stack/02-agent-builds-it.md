# An Agent Built This

You're going to give an AI agent **one instruction** and watch it containerise the whole
service - with no mention of base images, versions, or security. It runs right here, on this
machine, with full access to the Docker daemon and your filesystem.

Here's the stack it has to reason about - a backend API fronted by a UI, talking to
PostgreSQL, Kafka, LocalStack (S3) and WireMock:

<svg viewBox="0 0 620 300" width="100%" role="img" aria-label="Architecture: the catalog-service image contains Frontend and Backend API; Backend API talks to PostgreSQL, Kafka, LocalStack S3 and WireMock.">
  <g font-family="ui-sans-serif, system-ui, sans-serif" font-size="13">
    <rect x="8" y="8" width="604" height="150" rx="10" fill="#fdf7e3" stroke="#caa93a"></rect>
    <text x="20" y="30" font-size="12" fill="#6b5b12" font-weight="700">image · catalog-service:baseline  (node:20 · ~1.1GB · 431 pkgs)</text>
    <rect x="250" y="46" width="120" height="32" rx="6" fill="#ffffff" stroke="#8c959f"></rect>
    <text x="310" y="66" text-anchor="middle" fill="#24292f">Frontend</text>
    <rect x="240" y="110" width="140" height="32" rx="6" fill="#ffffff" stroke="#8c959f"></rect>
    <text x="310" y="130" text-anchor="middle" fill="#24292f">Backend API</text>
    <line x1="310" y1="78" x2="310" y2="108" stroke="#6b7280" stroke-width="1.5"></line>
    <polygon points="306,102 310,110 314,102" fill="#6b7280"></polygon>
    <rect x="8" y="248" width="130" height="34" rx="6" fill="#ffffff" stroke="#8c959f"></rect>
    <text x="73" y="269" text-anchor="middle" fill="#24292f">PostgreSQL</text>
    <rect x="158" y="248" width="110" height="34" rx="6" fill="#ffffff" stroke="#8c959f"></rect>
    <text x="213" y="269" text-anchor="middle" fill="#24292f">Kafka</text>
    <rect x="288" y="248" width="150" height="34" rx="6" fill="#ffffff" stroke="#8c959f"></rect>
    <text x="363" y="269" text-anchor="middle" fill="#24292f">LocalStack (S3)</text>
    <rect x="458" y="248" width="150" height="34" rx="6" fill="#ffffff" stroke="#8c959f"></rect>
    <text x="533" y="269" text-anchor="middle" fill="#24292f">WireMock</text>
    <g stroke="#6b7280" stroke-width="1.5" fill="none">
      <path d="M310,142 L310,200 L73,200 L73,248"></path>
      <path d="M310,200 L213,200 L213,248"></path>
      <path d="M310,200 L363,200 L363,248"></path>
      <path d="M310,200 L533,200 L533,248"></path>
    </g>
    <g fill="#6b7280">
      <polygon points="69,242 73,250 77,242"></polygon>
      <polygon points="209,242 213,250 217,242"></polygon>
      <polygon points="359,242 363,250 367,242"></polygon>
      <polygon points="529,242 533,250 537,242"></polygon>
    </g>
  </g>
</svg>

## Ask the agent to containerise it

Run this. The agent reads the project, picks a base image on its own, writes a Dockerfile,
resolves the dependency tree, and builds:

```bash terminal-id=main
claude -p "Containerise this Node.js app (frontend, backend, LocalStack, Kafka, WireMock) for production. Add a Dockerfile and build the image as catalog-service:baseline."
```

It succeeded. No errors, no warnings, no questions. See the files it added:

```bash terminal-id=main
tree
```

Read the Dockerfile it wrote:

```bash terminal-id=main
cat Dockerfile
```

## See it actually run

A Dockerfile you can read is one thing; a service answering requests is another. Bring the
whole stack up the way the agent wired it:

```bash terminal-id=main
docker compose up -d
```

Then hit the API it exposes:

```bash terminal-id=main
curl http://localhost:3000/api/products
```

Two products come back - the catalog is live. **This works.** No crash, no warning, nothing
that would make you stop and look.

## Now look at *where* it ran

That's the part to sit with. The agent didn't run in some isolated build service. It ran
**on this machine, as you**:

- your **Docker daemon** - it can build, run, and push any image
- your **filesystem** - every file your user can read or delete, it can too
- your **credentials** - `~/.aws`, `~/.ssh`, tokens in your environment, all in reach

It did exactly what you asked and nothing went wrong. But nothing *scoped* it either. The
same open access that let it containerise an app would let it do a great deal more.

So let's ask it to.

Continue to **What Harm Can It Do?**
