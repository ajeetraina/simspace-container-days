# Setup

Two minutes of configuration, then you never touch it again.

## 1. Log in

Log in to Docker Hub - the agent pulls its base image and you'll pull the `sbx` sandbox
runtime later:

```bash terminal-id=main
docker login
```

## 2. Preflight

Confirm Git is available - it should print a version:

```bash terminal-id=main
git --version
```

Everything else the agent needs ships with the Docker Engine you just logged in to.

## 3. Clone the project

Pull down the app you're about to hand to an agent - a Node.js catalog service (frontend,
backend, Postgres, Kafka, LocalStack, WireMock) that ships with **no Dockerfile yet**:

```bash terminal-id=main
git clone https://github.com/ajeetraina/product-catalog-demo-showcase
```

That project is now in your workspace. In the next section you hand it - untouched, no
Dockerfile and no guidance - to an agent and watch it containerise the whole thing, right
here on your host.

You're ready. Continue to **An Agent Built This**.
