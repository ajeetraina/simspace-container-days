# An Agent Built This

Before we box anything, see the problem. You hand an AI coding agent **one**
instruction and it containerises a whole service - with no mention of base
images, versions, or security. It works on the first try. That is exactly what
makes it dangerous.

## The app, with no Dockerfile

The project is a Node.js catalog service - a backend API fronted by a React UI,
talking to PostgreSQL, Kafka, LocalStack (S3) and WireMock. It ships with **no
Dockerfile and no compose file**:

```text
product-catalog-demo-showcase/
  src/            Express API (Node.js)
  frontend/       React SPA (Vite)
  db/schema.sql   PostgreSQL schema + seed data
  package.json    deps: express, pg, kafkajs, @aws-sdk/client-s3, axios ...
  (no Dockerfile, no compose.yaml)
```

Now hand it, untouched and with no guidance, to the agent.

## Ask the agent to containerise it

The agent reads the project, picks a base image on its own, writes a Dockerfile,
resolves the dependency tree, and builds:

```bash
claude -p "Containerise this Node.js app (frontend, backend, LocalStack, Kafka, WireMock) for production. Add a Dockerfile and build the image as catalog-service:baseline."
```

It succeeded. No errors, no warnings, no questions. **This works** - and that is
the trap: nothing about the image *behaving correctly* tells you what it is built
from.

## Freeze here. Three questions.

**What base image did it pick, and who decided that?**
Nobody in your organisation chose `node:20`. The agent pattern-matched against
whatever was most common in its training data.

**How many packages did that resolve?**
431. You reviewed none of them. Neither did the agent - resolving a dependency and
evaluating it are different activities, and it only did the first.

**Can you prove where any of it came from?**
No. Not the base image, not the packages, not the build itself.

## Measure the baseline

This image is the ungoverned baseline every later lab is measured against. Get the
vulnerability overview:

```bash
docker scout quickview catalog-service:baseline
```

Run the default policy evaluation - watch it fail:

```bash
docker scout policy catalog-service:baseline
```

Note the size:

```bash
docker images catalog-service:baseline
```

Write these down - they are the "before":

| | Critical | High | Medium | Low | Size |
|---|---|---|---|---|---|
| `catalog-service:baseline` | 0 | 8 | 41 | 93 | 1.1GB |

Zero critical, but **8 high and over a hundred known vulnerabilities**, 1.1GB, and
it runs as **root** - and the default policy fails. The agent was fast. It was also
completely unaccountable.

## Nothing is boxed yet

```bash
sbx ls
```

No sandboxes - so that agent ran straight on your **host**, as **you**, with your
filesystem, your secrets, and your Docker daemon in reach. A bad base image is one
problem; an agent with that much reach is another.

> [!NOTE]
> This is **Contain**, the first of the four Cs. Hardening the image - swapping in
> a trusted base - is the **Control** lab later. First we put a wall around the
> agent itself, so "its own" stops meaning "all of yours".

Next: box the agent.
