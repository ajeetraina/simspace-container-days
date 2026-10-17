# Speaker Notes — *Run Fast Without Running Wild*

**Workshop:** Run Fast Without Running Wild — AI Coding Agent Horror Stories and
the microVM That Saves You
**Event:** Container Days Singapore 2026
**Deck:** `deck.md` (64 full-bleed slides)
**Companion labs:** `an-agent-built-this` (Contain), `find-vulnerabilities`
(Control), `securing-the-agentic-stack` (Choice), `capacity` (Capacity)

---

## How to use this document

This is a **talk track** — what to *say*, not just what's on the slide. Each
entry gives the one-line purpose of the slide, a spoken script you can read or
riff off, and a transition into the next slide. Lines in `[brackets]` are stage
directions (clicks, demo switches, audience prompts), not words to read aloud.

**The spine of the whole talk is the Four Cs:** **Contain**, **Control**,
**Choice**, **Capacity**. Everything before them is the problem; everything after
is those four ideas, each with a lab. If you remember nothing else, land those
four words and the single sentence under each.

**Timing (≈45 min):** Intro & problem (slides 1–23) ~12 min · Why not containers
(24–26) ~3 min · Contain (27–37) ~8 min · Control (38–41) ~5 min · Choice (42–54)
~9 min · Capacity (55–63) ~6 min · Close (64) ~1 min. The agenda shows four
15-minute labs — the slides set each one up, the hands-on happens in the Simspace
lab pane.

**The one message:** *Refusal is a behaviour, not a boundary.* A well-behaved
agent is not a security control. The fix is an enforcement layer at runtime — a
microVM you can't talk your way out of. Say that sentence, in some form, at least
three times.

---

# Part 0 — Open (slides 1–4) · ~3 min

### Slide 1 — Title: "Run Fast Without Running Wild"
*Purpose: set the tone — this is a security talk, but it's about going faster, not slower.*

> "AI coding agents are the most productive thing to happen to our workflow in a
> decade. They're also the most dangerous thing we've ever given a shell to. This
> talk is about having both — running fast *without* running wild. We'll look at
> real incidents where agents wrecked machines, leaked secrets, and ran commands
> nobody approved — and then at the one piece of infrastructure that makes all of
> that stop mattering: a microVM sandbox."

[Hold a beat on the title. Don't rush off it.]

### Slide 2 — Meet your instructor
*Purpose: credibility, fast. Don't dwell.*

> "Quick hello — I'm Ajeet, a Developer Advocate at Docker. I've spent 20-plus
> years in testing, consulting and developer relations, I was a Docker Captain
> before I joined, and I run a 17,000-member meetup in Bengaluru. I also co-wrote
> *Operational AI with Docker*, which is basically this talk at book length. But
> you're not here for my bio — you're here because an agent did something on your
> machine last week that made you a little nervous. Let's talk about that."

[~20 seconds max. The self-deprecating pivot keeps it from feeling like a résumé.]

### Slide 3 — Agenda: Workshop labs
*Purpose: show the shape. Four labs, four Cs, ~15 min each. Lab 1 is already done for them.*

> "Here's the shape of the next 45 minutes. Four short labs. Lab 1 is just getting
> you logged in — two minutes, and you can start it now. Lab 2 is the horror-story
> half: why autonomy needs guardrails, and we'll watch an agent containerise a
> real app. Then Labs 3 and 4 are the fix, in four parts we call the Four Cs —
> **Contain**, **Control**, **Choice**, **Capacity**. Each lab is hands-on in the
> pane on your right; the slides just set it up."

[Point at the right pane. Tell them the labs run in the browser — nothing to install.]

### Slide 4 — Access the workshop
*Purpose: get everyone to the URL before the content starts.*

> "This is the only setup step. Go to **containerdays.dockerworkshop.com** — it
> runs entirely in your browser, nothing to install, no account to make. Open it
> now; by the time we hit the first lab you'll already be in."

[Leave this up for a moment. Read the URL aloud twice. Confirm a show of hands that people are in before moving on.]

---

# Part 1 — Autonomy requires guardrails (slides 5–23) · ~9 min

### Slide 5 — Section divider: "Autonomy requires guardrails"
*Purpose: frame the problem half of the talk.*

> "Before the fix, the problem — and I want to earn the fix, not just assert it.
> The thesis of this section is three words: autonomy requires guardrails. Not
> *autonomy is bad* — autonomy is the whole point. But the thing that makes an
> agent useful is exactly the thing that makes it dangerous, and no amount of good
> behaviour changes that."

### Slide 6 — AI agents are here, doing real work
*Purpose: establish that this is not hypothetical — agents already act, across functions.*

> "Let's be clear about where we are. Agents stopped being autocomplete a while
> ago. In **engineering** they read whole codebases and open pull requests with no
> human in the loop. In **marketing** they pull CRM data and launch campaigns,
> research to send. In **finance** they reconcile reports and query live systems.
> The common word across all three is *act*. They don't answer — they do. And
> every one of those actions touches something real: a repo, a customer record, a
> ledger."

[If the room is mostly engineers, lean on the engineering card and nod at the others.]

### Slide 7 — Autonomy ladder: more autonomy = more productivity
*Purpose: give people a map of where agents sit, and where the industry actually is.*

> "Here's a useful way to think about it — a ladder of autonomy. Stage one is
> autocomplete: stateless, prompt in, text out. Stage two remembers you. By stage
> three it's proactive within boundaries; stage four it makes judgment calls on
> your behalf; stage five it drives its own agenda and coordinates around the
> clock; stage six it sets goals inside ethical bounds. Now — the honest part.
> Most enterprises are living at **stage one or two**. Silicon Valley is poking at
> **three**. So when I talk about risk, I'm not talking about sci-fi stage-six
> agents. The damage we'll see today comes from stage two and three agents that
> are *already in your pipeline*."

### Slide 8 — Autonomy ladder: a change of control
*Purpose: reframe the same ladder as a transfer of control, not just capability.*

> "Same ladder, different axis. As you climb it, something shifts that has nothing
> to do with how smart the model is: *who's in control*. Down here it's
> human-led, AI-assisted — you drive, it helps. Up there it flips:
> AI-led, human-assisted — it drives, you supervise. The moment you cross the
> middle of this line, 'the developer reviewed it' stops being true by default.
> That crossing is where you need something other than trust."

### Slide 9 — The lethal trifecta
*Purpose: THE conceptual core of the problem half. Slow down here.*

> "This is the single most important slide in the first half. Every genuinely
> useful agent is built on three things at once. One: **access to private data** —
> your code, your internal systems, your credentials. Two: **exposure to untrusted
> content** — web pages, emails, files, the responses coming back from tools. Any
> of that can carry an instruction the agent will follow as if *you* typed it.
> Three: **the ability to act externally** — send mail, call APIs, touch the open
> internet. And here's the point" —
>
> [read the callout verbatim, slowly] —
>
> "a useful agent has all three *by design*. You cannot train it out. You cannot
> prompt it out. You cannot policy-doc it out. If you remove any one of the three,
> you've removed the reason you hired the agent. The only place left to fix this
> is an **enforcement layer at runtime** — something outside the agent that holds
> no matter what the agent decides."

[This "by design" framing is the whole talk in miniature. If you only nail one slide, nail this one. Pause after "by design."]

### Slide 10 — What can go wrong?
*Purpose: turn the abstract trifecta into a concrete story. Pure transition slide.*

> "So let's make that concrete. Not a threat model on a whiteboard — a real app, a
> real agent, and three real ways it goes wrong."

### Slide 11 — A Product Catalog sample demo
*Purpose: introduce the app we'll hand to the agent. Point out the credentials.*

> "Here's our victim — a perfectly ordinary Product Catalog service. Node and
> Express, backed by Postgres for catalog data, S3 for images, Kafka for updates,
> talking to an inventory service and to **live Stripe payments**. This is a
> normal microservice. The only thing I want you to notice is what's underneath
> every one of those arrows: a credential. A database password, AWS keys, a Stripe
> key, an internal API key — and in this repo they're sitting in a plaintext
> `.env` file right next to the code. That's leg one of the trifecta — private
> data — and it's not exotic. It's every repo you've ever cloned."

### Slide 12 — The traditional workflow
*Purpose: baseline — in the old world the attack surface is bounded by human choice.*

> "Think about how this used to work. Inner loop: you code, build, pull in open
> source, test. Outer loop: integrate, test, deploy. A *human* stands at every one
> of those stations. And that matters for security in a way we never said out
> loud: your attack surface was only ever *what you chose to pull*. Every
> dependency, every base image, every command — a person decided it, and usually
> another person reviewed it."

### Slide 13 — The agentic workflow
*Purpose: the pivot — same loop, agent at every station, surface is now unbounded.*

> "Now replace every one of those humans with an agent." [Note the green badges —
> same diagram, same stations, different operator.] "Nothing about the *pipeline*
> changed. But the sentence from the last slide just broke. The attack surface is
> no longer what *you* pull — it's what the *agent* pulls, generates, and reaches
> for, autonomously, at every stage. You didn't expand the surface on purpose. It
> expanded because you handed the keyboard to something that acts faster than you
> can review."

### Slide 14 — Agents expand your attack surface, automatically
*Purpose: spell out the before/after concretely, land the blast-radius line.*

> "Side by side. Traditionally: you pull the base image, with intent. You install
> dependencies, reviewed in a PR. CI runs with human-authored config. Agentically:
> the agent pulls the base image autonomously. Installs packages with no review.
> Invokes external tools with *real credentials*. Rewrites the Dockerfile
> mid-pipeline. Same four steps — zero human gates. And the line I want you to take
> home from this slide" — [read the quote] — "*the better the agent, the bigger the
> blast radius.* A worse agent would be safer. That should bother you, because
> you're going to keep buying the better one."

### Slide 15 — What agents are already doing in your pipeline
*Purpose: make it present-tense and personal. This is today, not a forecast.*

> "And this isn't a warning about next year. Right now, in your pipeline, agents
> are **pulling dependencies** from registries nobody audited, **generating
> Dockerfiles** — picking base images, install steps, and the user it runs as,
> usually whatever it saw first. **Editing infrastructure**: Terraform, Helm
> values, Compose files, IAM policy. And **triggering builds** — opening PRs,
> pushing branches, kicking off pipelines on their own initiative. Every one of
> those is a place the trifecta is live today."

### Slide 16 — The ungoverned agent
*Purpose: show the concrete bad outcome we'll reproduce live. Anchor the CVE numbers.*

> "Here's what that looks like with no boundary. The agent runs on your host, with
> your daemon and your credentials. You say 'containerise this app.' It reaches
> open registries with no allowlist, and it picks `FROM node:20` because that's the
> convenient, famous base — chosen with zero guidance. The result, before anyone's
> done anything malicious: an image with **critical and high CVEs**, 431 packages,
> no SBOM, no attestation, running as **root**. That's not a mistake. That's the
> default. Keep that picture — we'll put the exact same prompt in a sandbox later
> and watch the numbers go to zero."

[The 0C/6H/30M/54L here previews the Scout numbers in the lab; don't over-promise exact values, the lab is the source of truth.]

### Slide 17 — Demo time!
*Purpose: hand off to the first hands-on moment.*

> "Let's stop talking about it and watch it happen. This is Lab 2 in your right
> pane — an agent containerising this exact app. Follow along at
> containerdays.dockerworkshop.com, the `an-agent-built-this` lab."

[Switch to the Simspace lab pane. Give the room a moment to find it.]

### Slide 18 — Set up: clone the repo
*Purpose: orient people in the lab's first steps.*

> "Four quick steps. Clone the repo. Verify there's no Dockerfile and no Compose
> file — it ships source only, which is exactly what teams hand an agent today.
> Peek at the `.env` so you've seen the secrets with your own eyes. Then ask the
> agent to containerise it for production, and scan the result with
> `docker scout quickview`. Watch what number comes back."

[If running live, do the clone and the `cat .env` yourself so the room sees the plaintext keys. Then let them run the agent step.]

### Slide 19 — AI Coding Agent Horror Stories
*Purpose: section title — shift from "what could happen" to "what did happen."*

> "That was a clean demo. Now the part that isn't clean. These next few are real —
> they shipped, they hit production, and someone paid for them."

[Let the title land. The tonal shift from demo to dread is the point.]

### Slide 20 — Horror headlines (collage)
*Purpose: overwhelm, briefly — this is a pattern, not a one-off.*

> "I didn't have to dig for these. An agent deleted **25,000 documents** from the
> wrong database — one second of distraction, right credentials, perfectly
> referenced script. A team's agent deleted *production* data, and the chilling
> detail is it was *technically allowed to* — no policy layer ever said no.
> Researchers found a prompt-injection hole in the GitHub MCP integration with no
> obvious fix. Someone watched their agent delete 400 emails because it decided
> they were 'clutter.' McDonald's AI hiring bot exposed millions of applicants
> because the password was one-two-three-four-five-six. Different companies,
> different tools — same shape every time: an agent with access, and nothing
> standing between it and the damage."

[Don't read every headline — pick three or four and gesture at the wall of the rest. The volume *is* the argument.]

### Slide 21 — "Clean up my project folder" (comic)
*Purpose: the signature story — a friendly request, root access, total loss.*

> "This one's a comic because it's almost funny, until it's you. Developer says:
> 'Hey agent, clean up my project folder.' Agent says 'On it!' — analyses the
> project, finds 'unneeded files,' removes 'clutter,' optimises the structure…
> with `rm -rf` on *everything*. 'Cleanup complete!' Wait — where's my home
> directory? Documents, Downloads, Pictures, all of it. And the kicker in the last
> panel: 'Oh, did I forget to mention I had root access this whole time?' Nobody
> asked it to be malicious. It was being *helpful*, with permissions it should
> never have had."

[The blog link is on the slide if anyone wants the write-up. Beat on "root access this whole time.")

### Slide 22 — Claude Cowork (comic)
*Purpose: same failure, different surface — show it's the pattern, not one tool.*

> "January 2026, a different agent, a home-user scenario. 'Help organise my wife's
> desktop.' It finds some temp Office files, starts cleaning up — and runs
> `rm -rf family_photos/`. Thirteen years of memories. And it **bypassed the
> Trash** — nothing to restore from. The only reason this story has a happy
> ending is iCloud's 30-day retention saved them by luck. Same story, different
> path, same damage. The lesson isn't 'that one tool is bad.' It's that this is
> structural."

### Slide 23 — Developers have to choose between speed and safety
*Purpose: name the false dilemma the rest of the talk dissolves.*

> "So today developers feel stuck choosing between two bad options. On the left:
> **safe and slow** — approve every single action. The agent stops to ask
> permission constantly and *you* become the bottleneck; you're not developing,
> you're babysitting. On the right: **fast and risky** — YOLO mode, skip the
> prompts, and now the agent has exactly the access you have, with none of your
> judgment. The most common thing I hear from developers is right there at the
> bottom:" — [read the quote] — "*'I'm babysitting my agents.'* Hold that feeling.
> The entire rest of this talk is about refusing this choice — getting fast *and*
> safe at the same time."

---

# Part 2 — Why not containers? (slides 24–26) · ~3 min

### Slide 24 — Section divider: "Why not containers?"
*Purpose: pre-empt the obvious objection at a Docker conference.*

> "We're at a Docker conference, so some of you are already thinking the obvious
> thing: just put the agent in a container. It's a fair instinct — and it's worth
> taking seriously instead of waving away. Containers isolate *applications*
> beautifully. The problem is an agent isn't an application. It needs more access
> than an application does — and that difference is everything."

### Slide 25 — Escaping a container (Lab setup)
*Purpose: set up the escape demo — three steps, one socket.*

> "Here's the most common setup I see: a coding agent in a container, with the
> **Docker socket mounted** so it can build images and run tests. Totally
> reasonable — that's how it does its job. Watch the three steps: agent in a
> container; socket mounted so it can build; and then the agent uses that socket
> to reach the host. The socket is the feature *and* the hole."

[This maps to the `an-agent-built-this` lab, "Why Not a Container?" section. Run it live if time allows.]

### Slide 26 — Each new capability weakens the container's isolation
*Purpose: the killer table — every useful grant erodes the box, until nothing's left.*

> "And it's not one bad flag — it's a ramp. Give the agent your **source** so it
> can edit the project: now it can modify files on your host. Give it the
> **network** so it can fetch packages: now it can reach anything, inside or out.
> Pass it **API keys** so it can call services: now it can read those keys and
> send them anywhere. Mount the **Docker socket** so it can build: now it can start
> containers on the host with full access — it owns the machine, which you just
> watched. Look at the isolation bar on the right collapse row by row. Every single
> grant was *reasonable*. Together they leave you with nothing." — [read the
> footer] — "*The more useful the agent, the less isolated the container.* That's
> not a bug in containers. A container shares the host kernel, and the access an
> agent needs is exactly the access that lets it escape. So we need a different
> kind of box."

[This is the hinge from problem to solution. The next slide is the pivot — say "a different kind of box" and click.]

---

# Part 3 — CONTAIN (slides 27–37) · ~8 min

### Slide 27 — Agenda recap (Labs 1–2 done)
*Purpose: breadcrumb — show progress, orient for the Four Cs.*

> "Quick checkpoint. We've done the setup and the problem — Labs 1 and 2 are
> behind us. Now the fix, in four parts. First one up: Contain."

[Keep this to one breath. It's a signpost, not a slide.]

### Slide 28 — Hello, Sandboxes
*Purpose: introduce the solution in one sentence.*

> "Meet the Docker Sandbox. Here's the whole idea in one line:" — [read it] —
> "*give the agent everything it needs, inside a boundary it can't cross.* Not
> fewer capabilities — the same capabilities, in a box that holds. That's how we
> escape the speed-versus-safety trap from a few slides ago."

### Slide 29 — A sandbox is a private machine for your agent
*Purpose: the mental model — a whole private machine, not a locked-down container.*

> "The right way to picture it: a sandbox is a *private machine* for your agent,
> running on your machine but walled off from it. Inside the box the agent gets
> what it needs — the agent itself, Claude Code or Codex or whatever you bring;
> your project, and *only* this folder; and its own Docker. The only way out is a
> **proxy** — one controlled exit to package registries, model APIs, your
> services. And notice what's on the *outside*: your `~/.ssh`, your API keys, your
> other projects, your host Docker. The agent literally cannot see them. Three
> ideas underneath — a trusted boundary, you choose what goes inside, and the whole
> team can reproduce it — and those become Contain, Choice, and Capacity."

### Slide 30 — Container vs Sandbox
*Purpose: the technical "why" — different kernel, so sudo inside ≠ admin outside.*

> "Why does this hold when a container didn't? One picture. An ordinary container —
> Container A, Container B — shares the **host kernel**. That's fine for apps, but
> it's a thin wall for an agent that'll run any command it likes. A Docker Sandbox
> runs Claude Code, with `sudo`, on **its own Linux kernel** in a microVM. So
> `sudo` *inside* the sandbox is not admin on your Mac. The agent can go wild in
> its own room — install anything, break anything, be root — and it's root of a
> throwaway machine, not yours."

### Slide 31 — A sandbox gives you four things
*Purpose: name the Four Cs explicitly. This is the skeleton of the whole back half.*

> "So a sandbox gives you four things, and these are the four words the rest of the
> talk hangs on. **Contain** — isolate the agent in a microVM with a guarded
> network. **Control** — decide what it can reach; organisations layer governance
> and audit on top. **Choice** — bring your own agent, tools, and endpoints, with
> kits. **Capacity** — reproduce the exact same sandbox for every developer and
> every run. Contain, Control, Choice, Capacity. We'll do each one, and each one
> has a lab."

[Say the four Cs as a rhythm. You'll repeat them at every divider and in the recap.]

### Slide 32 — Contain (divider)
*Purpose: enter the first C.*

> "Contain first — the boundaries that keep the agent's actions inside the
> sandbox. This is the always-on foundation; everything else sits on top of it."

### Slide 33 — Three boundaries surround every agent
*Purpose: name the three mechanisms of Contain with memorable analogies.*

> "Containment is really three boundaries working together. One: the **microVM** —
> its own kernel, filesystem, and Docker engine; the host is simply out of reach.
> Think of it as a separate room with its own walls. Two: the **network proxy** —
> every outbound request passes through a proxy that applies policy. That's a front
> desk that checks every exit. Three: **credential injection** — keys get added by
> the proxy on the way out, so the agent never holds them. A front desk that holds
> the keys *for* you. Separate room, checked exits, keys held at the desk. That's
> Contain."

### Slide 34 — What the agent can reach
*Purpose: concrete reachability — full freedom inside, nothing outside.*

> "Zoom into the box. Inside, the agent is *unleashed* — Claude Code runs with
> `--dangerously-skip-permissions` and `sudo`, and that's fine, because it's inside
> the VM only. It has its private files and its own inner Docker, separate from the
> one on your Mac. Through the workspace mount it reaches your project folder — read
> and write, or read-only if you choose. Outbound traffic goes through the policy
> proxy, which allows or blocks each destination and adds API keys so they stay out
> of the VM. And everything else — unshared files, host processes, your host Docker
> engine — has **no direct path**. Full freedom inside; a hard wall at the edge.
> That's the trade we wanted: run fast *inside*, can't run wild *outside*."

### Slide 35 — A sandbox has its own kernel (how it works)
*Purpose: reinforce the kernel point at full size — the load-bearing technical claim.*

> "Worth saying once more, because this is the load-bearing claim. Ordinary
> containers all share the host kernel — the part of the OS that manages processes
> and hardware. The Docker Sandbox brings **its own Linux kernel** in a microVM.
> That one architectural choice is what lets the agent have a real, full-power
> Docker daemon *inside* without ever touching yours — and it's why `sudo` in the
> box isn't admin on your Mac."

[If you're short on time, slides 30 and 35 make the same point — you can skip one. 35 is the cleaner full-size version.]

### Slide 36 — Credentials are added outside the sandbox
*Purpose: the credential-injection flow, step by step. This is the "aha" for secrets.*

> "Let me walk the credential flow, because it's the part people don't believe
> until they see it. Step one, in the sandbox: the agent calls an API — and the
> request has *no key attached*. Authorization: none. Step two, at the proxy: policy
> check — is this destination allowed? If not, it stops right here. Step three,
> still at the proxy, *outside* the box: the key, which lives on the host, gets
> injected now. Step four: the API responds, 200 OK, and the agent gets the result
> — but never the key. Read the line at the bottom:" — [read it] — "*the raw key
> never enters the sandbox.* So even if the agent is prompt-injected into trying to
> exfiltrate a secret, there's no secret inside to steal."

### Slide 37 — Testing the boundaries (Lab setup)
*Purpose: hand off to the Contain lab's proof steps.*

> "Now you prove it yourself. In the lab: try the *same* container escape from
> before — but the socket here belongs to the sandbox, not the host, so it goes
> nowhere. Go looking for host SSH keys and other projects — they're not mounted,
> so they're simply not there. And make a real model API call *without ever seeing
> the key*. Same agent, same prompts as the horror stories — the blast radius just
> collapsed. That's Lab 3's first half, `an-agent-built-this`."

[Switch to the lab. The payoff lines — `printenv ANTHROPIC_API_KEY` returns nothing; `cat ~/.ssh/id_rsa` says no such file — land best if you run them live.]

---

# Part 4 — CONTROL (slides 38–41) · ~5 min

### Slide 38 — Control (divider)
*Purpose: enter the second C — tuning the boundary.*

> "Contain is the wall, and it's always on. **Control** is where *you* decide where
> the wall sits. Let the agent work — and choose exactly what it's allowed to
> reach."

### Slide 39 — Developers decide what the agent can reach (network profiles)
*Purpose: show the policy model — profiles over deny-by-default, everything logged.*

> "Control starts from **deny-by-default** and you open things up deliberately. You
> pick a profile as a starting posture: **Locked Down** — only what you explicitly
> allow. **Balanced** — the default — common dev endpoints allowed, everything else
> denied. Or **Open** — outbound allowed, but *still logged*. Then you add allow and
> deny rules on top of any profile. And the thing that makes this real rather than
> theatre: every single connection the agent attempts is logged — so you can
> actually see what it tried to reach, with `sbx policy log`."

### Slide 40 — Organizations add governance on top
*Purpose: scale the story from one dev to an org — three layers, bottom always on.*

> "This also scales past one developer, and the layering matters. At the bottom,
> **always on**: Contain — the microVM, the proxy, credential injection. Nobody can
> switch that off. In the middle, the **developer**: your local policy — choose a
> profile, add allow/deny rules, read the log. On top, the **organisation**: central
> policy, audit logs, approved agents and kits, enforced across *every* sandbox.
> The developer gets freedom to move; the org gets a floor nobody can go beneath.
> That's how you give a whole company agents without hoping every single person
> configured them right."

### Slide 41 — Adjusting policy (Lab setup)
*Purpose: hand off to the Control lab.*

> "Your turn again. Three steps: the agent hits a blocked endpoint — an internal
> service it needs. You find that attempt in the policy log. You add one allow rule
> and it keeps working — and you watch the decision flip from Denied to Allowed
> without ever restarting the agent. That's the `find-vulnerabilities` lab. The
> whole point: this is a fast feedback loop — you can check a host against policy
> *before* the agent ever trips over it."

[Switch to the lab. `sbx policy check network inventory.internal:8080` before and after the allow rule is the money moment.]

---

# Part 5 — CHOICE (slides 42–54) · ~9 min

### Slide 42 — Choice (divider)
*Purpose: enter the third C — a locked box still has to be useful.*

> "A perfectly locked box that can't do anything is useless. **Choice** is how the
> box stays useful: a restricted sandbox still needs *your* tools, *your* agent,
> *your* endpoints. The trick is adding them without weakening the wall."

### Slide 43 — Security tools usually trade away flexibility
*Purpose: position sandboxes against the usual security-vs-flexibility tradeoff.*

> "Most security tools make you pay for safety with flexibility. Plot it: a locked
> VM with no network is very secure and nearly useless; an agent on the bare host
> is maximally flexible and maximally dangerous; a plain container, or a container
> plus the Docker socket, drifts right as it gets useful. Sandboxes break the line.
> The security comes from the microVM and the proxy — those are *fixed*. What runs
> *inside* is configurable. You make the inside more capable without moving the
> boundary an inch."

### Slide 44 — Kits define what runs inside the boundary
*Purpose: introduce kits — the mechanism of Choice. Agent kit vs mixin kits.*

> "The mechanism is called a **kit**. Two flavours. An **agent kit** — one per
> sandbox — is the harness: *which* coding agent runs and how it starts, Claude
> Code or Codex or another. **Mixin kits** — stack as many as you want — add tools,
> their credentials, and their network rules on top of any agent: a code-server, a
> GitHub SSH setup, your project's dev environment. The microVM and proxy
> underneath stay *unchanged*. And kits ship anywhere — Docker Hub or any registry,
> a Git repo, or just a folder in your project."

### Slide 45 — Swap the agent, add the tools
*Purpose: show the composability — pick one agent, check any tools, boundary unchanged.*

> "Here's the composability in one picture. Pick **one** agent — radio button,
> Claude Code today, Codex tomorrow. Check **any** tools you want — GitHub SSH, SSH
> signing, your dev env. And you get your sandbox: those tools, that agent, and
> underneath it all, 'MicroVM + proxy — ALWAYS.' Change either side as much as you
> like — swap the harness, add or drop tools — and the boundary stays exactly the
> same. That's the whole promise of Choice: configure the inside freely, never
> touch the wall."

### Slide 46 — Running kits from Docker Hub (Lab setup)
*Purpose: hand off to the first half of the Choice lab.*

> "In the lab you'll do exactly this: start a sandbox with one agent kit; swap the
> harness while keeping the same project; then stack mixins for GitHub, signing,
> and the dev env. The specific mixin we add is **GitGuardian** — it wires a secret
> scanner into the agent as an AI hook, so every write the agent makes is scanned,
> and its API key is injected by the proxy and never enters the box. Same
> credential trick as Contain, now for a tool."

[This is `securing-the-agentic-stack`. The highlight: ask the agent to hardcode AWS keys — it refuses — then show the kit catches a real key regardless, because the kit is enforcement, not hope.]

### Slide 47 — You can build your own kits
*Purpose: open specification — this is extensible, not a fixed menu.*

> "And you're not limited to Docker's kits. Kits follow an **open specification** —
> you can package your own agent or your own tooling exactly the way the Hub kits
> are built. The spec and example kits are at **github.com/docker/sandbox-kit-spec**.
> Building kits is genuinely a session of its own, so I'll just plant the flag: if
> your team has an internal tool, it can live in the box the same governed way."

### Slide 48 — Agents talking to an MCP server (divider)
*Purpose: introduce the second kind of tool — external MCP servers through a gateway.*

> "Kits put tools *in* the box. The other way to give an agent capability is to let
> it *call out* to external tool servers — MCP servers — but through **one governed
> gateway**, never directly. This is where Choice gets powerful, and where
> governance gets interesting."

### Slide 49 — Agent with a sandbox (DHI MCP example)
*Purpose: concrete MCP example — the DHI server steering the agent to a clean base.*

> "Concrete example, and it closes the loop on the horror from the first half.
> Inside the sandbox — own daemon, own network, host read-only — the agent has full
> permissions and one new tool: the **Docker Hardened Images MCP server**, signed
> tools only. So when you say 'containerise this,' before it writes a single `FROM`
> line it *queries the catalog* and picks `dhi.io/node`. Result: zero criticals,
> zero highs, zero mediums, zero lows. 211 packages, SBOM attached, signed,
> non-root. Same task that gave us dozens of CVEs on the host — now clean, because
> the right tool was in the box."

### Slide 50 — Letting the agent use MCP servers safely (gateway)
*Purpose: the architecture — one gateway, one chokepoint, namespaced tools.*

> "How does 'safely' actually work? The agent never talks to those servers
> directly. It talks to **one gateway** — one governed endpoint — and the gateway
> fans out to local-wiki, GitHub, Notion, DuckDuckGo, whatever you've registered.
> Every tool call flows through that single chokepoint, and the tools are namespaced
> `mcp__mcp-gateway__<tool>`. One chokepoint is exactly where policy and audit can
> live. Many servers, one door."

### Slide 51 — SBX_MCP_URL — the gateway gatekeeper
*Purpose: the fail-closed design detail. Governance can't be bypassed.*

> "There's a deliberate safety design here. The whole `sbx mcp` subtree stays
> *hidden* until `SBX_MCP_URL` is set, and only two values carry the full governed
> flow: a **local gateway** on localhost:8811 — great for learning the mechanics,
> you control what's registered — or the **hosted control plane** at
> gateway.docker.com — org policy governs what's invocable, with central audit;
> that's the real governance story. And it's **fail-closed**: no policy loaded means
> deny-all. Policy is authored in Docker Hub, fetched at `docker login`, and
> developers *can't* override it. The default state of this system is 'nothing,'
> not 'everything.'"

### Slide 52 — Govern it — MCP access policy (Cedar)
*Purpose: show real policy-as-code. Default-deny allow-list over (server, tool).*

> "And for the people who want to see it's real policy, not vibes: here's the actual
> rule, written in **Cedar**, authored in Docker's AI governance console. It's a
> default-deny allow-list over `(server, tool)` pairs — this one permits only the
> read-only DHI tools: list repositories, get CVEs, get attestations, and so on.
> What it buys you: anyone in the org may *register* a server, but the tools are
> only *invocable* if policy permits — evaluated at the gateway on every single
> invoke, by the same engine that does network and filesystem policy. One surface,
> no bypass. A developer can `sbx mcp add` anything they like; if org policy
> doesn't permit its tools, the calls are denied and audited. Author once, sync
> everywhere."

[This is the deepest slide technically. For a developer-heavy room, dwell. For a mixed room, hit "default-deny allow-list, evaluated on every invoke" and move on.]

### Slide 53 — One feature: agents in a sandbox, using external tools, safely
*Purpose: zoom back out — summarise the whole MCP scope in four questions.*

> "Let me pull the MCP thread back together, because it's really one feature
> answering four practical questions. *What tool-servers are supported?* Remote,
> local stdio, docker.io images — and the slide's honest about what isn't. *How do
> you register them?* `sbx mcp add`, one at a time or as a shareable bundle. *How
> does the sandbox connect?* As a locked static set, or a discoverable dynamic
> catalog. *How are credentials managed?* The gateway holds OAuth centrally —
> authorize, revoke, audit. Agents in a sandbox, using external tools, safely.
> That's the whole scope."

### Slide 54 — Same agent, same prompt — a 0-CVE base
*Purpose: the payoff slide. The single before/after number that proves Choice.*

> "And here's the whole of Choice in one comparison. Left, ungoverned:
> `claude -p 'containerise this'` picks `node:20` blind — Scout says 2 critical, 12
> high, 20 medium, 13 low, over 431 packages, no SBOM. Right, with the DHI MCP
> server in the box: the *same prompt* queries DHI first, lands on
> `dhi.io/node:24-debian13` — zero, zero, zero, zero, over 211 packages, SBOM,
> signed. Read the line:" — [read it] — "*the tool in the box changed the outcome —
> not the prompt.* I didn't write a better prompt. I didn't use a smarter model. I
> put the right tool inside the boundary. That's Choice."

[This slide is the emotional peak of the technical argument. Let the 0/0/0/0 sit for a second against the 2/12/20/13.]

---

# Part 6 — CAPACITY (slides 55–63) · ~6 min

### Slide 55 — Agenda recap (Labs 1–3 done)
*Purpose: breadcrumb — three Cs down, one to go.*

> "Checkpoint: Contain, Control, Choice — done. One C left, and it's the one that
> turns all of this from a personal trick into something a team can actually run."

### Slide 56 — Capacity (divider)
*Purpose: enter the fourth C.*

> "**Capacity.** One developer with one great sandbox is a start. But a boundary
> that only exists on *your* laptop isn't governance — it's a one-off. Teams need
> the same sandbox everywhere."

### Slide 57 — Scaling up starts with reproducibility
*Purpose: the drift problem, in three steps.*

> "Watch how this breaks without Capacity. One developer: configured by hand, works
> on one machine — fine. A team, by hand: every setup drifts — different kits,
> different policies, and that's exactly where 'works on my machine' comes from,
> and where an *ungoverned* sandbox quietly sneaks in because your policy never
> reached the next person. A team, from one *file*: every sandbox matches, and you
> run as many as you need. The fix is the same one we use for everything that
> matters — declare it once, in a file, and share it like code."

### Slide 58 — An environment file describes the whole sandbox
*Purpose: show sbxenv.yaml — the sandbox as reviewable data.*

> "That file is `sbxenv.yaml`, and it's committed to the repo. It names the
> **agent** — which harness runs. The **workspace** — the folder the agent can see.
> The **kits** — tools, credentials, and network rules, each one coming along for
> the ride. And **resources** — CPU and memory. The sandbox stops being a pile of
> flags you remember to type and becomes *data* — reviewable, diffable, versioned.
> You start it with `sbx env run`. Fair warning: the format's experimental and may
> change."

### Slide 59 — Commit it once and the whole team shares one setup
*Purpose: the git-native workflow — governance as a reviewed change.*

> "Because it's just a file, it travels like code. Change the file — add a kit, swap
> the harness. Open a pull request — now the change is *reviewed*, like any other.
> Merge — the repo holds the new definition. Everyone pulls — and the next sandbox
> each person starts matches yours. Update once, every sandbox follows. The
> important shift: changing your team's agent security is no longer a silent local
> tweak in someone's shell history — it's a reviewable event with a paper trail."

[Call out the secrets nuance if the room is security-minded: the file holds a *source* for each secret — a 1Password ref — resolved on each developer's own host. The secret itself never travels in the repo.]

### Slide 60 — Cloud Sandboxes run the same setup remotely
*Purpose: the scale story — same file, Docker's infrastructure. Flag early access.*

> "And the same file isn't limited to your laptop. **Local**: it runs on your
> machine, bounded by your CPU and memory. **Cloud**: the exact same environment
> file, running on Docker's infrastructure — so you can start far more sandboxes
> than one laptop could ever hold. One agent per PR, a fleet of them, without
> melting your machine. Honest caveat: Cloud Sandboxes are **early access, not yet
> available for org use** — but the model is: write the file once, run it anywhere,
> one laptop or a thousand in the cloud."

### Slide 61 — Sharing a sandbox with the team (Lab setup)
*Purpose: hand off to the Capacity lab.*

> "Last lab. You'll be the *new teammate*: clone a repo that already has an
> environment file, start a sandbox — and the kits and policy are already set, you
> did nothing to configure them. Then change one line and start again. Before you
> run it, `sbx env plan` shows exactly what it'll set up outside the box — including
> which secrets it'll resolve from *your* host — and asks for approval before
> touching anything. That's the `capacity` lab."

[Switch to the lab. The contrast to show: the ad-hoc `sbx run claude` warning at the start vs. the fully-declared `sbx env run` at the end.]

### Slide 62 — Agenda recap (all four done)
*Purpose: all four Cs checked. The visual close of the content.*

> "And that's all four. Contain, Control, Choice, Capacity — every box checked.
> Let me put them together one last time."

[This duplicates slide 55's layout with everything ticked — it's a deliberate 'we did it' beat. Quick.]

### Slide 63 — Recap
*Purpose: the three-sentence takeaway. If someone walked in late, this is the talk.*

> "If you remember three things. One — **a trusted boundary**: a microVM, a network
> proxy, and credentials the agent never holds. That's Contain and Control. Two —
> **your choice inside it**: agent and mixin kits for your harness, tools, and
> endpoints. That's Choice. Three — **shared with the team**: one environment file
> in the repo; update once, everyone follows. That's Capacity. The boundary comes
> from the box — not from the agent behaving. That's the difference between hoping
> and knowing."

[Land the callback: "refusal is a behaviour, not a boundary — the box is the boundary."]

### Slide 64 — Thank you
*Purpose: close, and point them at the labs to keep going.*

> "That's the talk: run fast, *without* running wild. The four labs stay open —
> finish any you didn't get to, they're all at
> containerdays.dockerworkshop.com. Come find me after; I'd love to hear what your
> agents have gotten up to. Thank you."

[Leave the Thank You slide up for Q&A. Have the workshop URL ready to repeat.]

---

## Appendix — Quick-reference cheat sheet

**The four Cs, one line each:**
- **Contain** — isolate the agent in a microVM with a guarded network. (Always on.)
- **Control** — decide what it can reach; deny-by-default, everything logged; orgs govern on top.
- **Choice** — bring your own agent, tools, endpoints via kits and MCP — without moving the boundary.
- **Capacity** — one `sbxenv.yaml`, reproduced for every developer and every run.

**The three recurring punchlines:**
1. *Refusal is a behaviour, not a boundary.* (A well-behaved agent is not a control.)
2. *The better the agent, the bigger the blast radius.*
3. *The tool in the box changed the outcome — not the prompt.*

**The numbers that prove it (from the labs, verify live):**
- Ungoverned `node:20`: **2C / 12H / 20M / 13L**, 431 packages, no SBOM, root.
- DHI hardened base: **0 / 0 / 0 / 0**, 211 packages, SBOM, signed, non-root.

**Lab ↔ slide map:**
- Lab 2 *Autonomy requires guardrails* → slides 5–23 (`an-agent-built-this`, first half)
- Lab 3 *Contain & Control* → slides 24–41 (`an-agent-built-this` Contain + `find-vulnerabilities` Control)
- Lab 4 *Choice & Capacity* → slides 42–63 (`securing-the-agentic-stack` Choice + `capacity` Capacity)

**If you're running short on time, safe cuts:** slide 30 *or* 35 (same kernel
point); slide 8 (second autonomy ladder); slide 53 (MCP four-questions recap).
**Never cut:** 9 (trifecta), 26 (isolation table), 31 (four Cs), 54 (0-CVE
payoff), 63 (recap).

**Commands worth running live (source of truth is the lab terminal):**
- Contain: `sbx exec demo printenv ANTHROPIC_API_KEY` (empty) · `sbx exec demo cat ~/.ssh/id_rsa` (not found)
- Control: `sbx policy check network inventory.internal:8080` (before/after `sbx policy allow`)
- Choice: `docker scout quickview` on the ungoverned vs DHI image
- Capacity: `sbx env plan` then `sbx env run`
