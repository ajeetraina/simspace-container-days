#!/usr/bin/env python3
"""Deck generator: rebuilds deck.md with a consistent dark + monospace system.

Each slide is either HTML (rebuilt, in SLIDES) or falls back to its talk-NN.webp
image. Rebuild slides batch by batch by adding entries to SLIDES.
"""
import os

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SANS = "ui-sans-serif,system-ui,sans-serif"
BLUE, WHITE, BODY, MUTED, RULE = "#7da2ff", "#ffffff", "#aeb8c9", "#7f8ba3", "#26324a"

FOOTER = (f'<div style="position:absolute;left:6.5%;bottom:6.5%;font:700 11px/1 {SANS};'
          f'letter-spacing:.32em;color:#566071;">DOCKER&nbsp;&nbsp;/&nbsp;&nbsp;N&nbsp;E&nbsp;X&nbsp;T</div>')

def bg(inner):
    return (f'<div style="position:absolute;inset:0;background:#0a1019;'
            f'background-image:radial-gradient(rgba(125,162,255,0.06) 1.3px, transparent 1.3px);'
            f'background-size:26px 26px;overflow:hidden;font-family:{SANS};">{inner}{FOOTER}</div>')

def header(eyebrow, title, size=56):
    return (f'<div style="position:absolute;left:6.5%;right:6%;top:8.5%;">'
            f'<div style="font:700 16px/1 {MONO};letter-spacing:.22em;color:{BLUE};">{eyebrow}</div>'
            f'<div style="margin-top:14px;font:800 {size}px/1.04 {MONO};color:{WHITE};">{title}</div></div>')

def divider(num, name, sub):
    up = name.upper()
    return bg(
        f'<div style="position:absolute;right:6%;top:9%;font:700 15px/1 {MONO};letter-spacing:.22em;color:{BLUE};">PILLAR {num}</div>'
        f'<div style="position:absolute;left:6.5%;right:6%;top:50%;transform:translateY(-50%);">'
        f'<div style="font:700 16px/1 {MONO};letter-spacing:.22em;color:{BLUE};">&sect; {num} / {up}</div>'
        f'<div style="margin-top:14px;font:800 82px/1.0 {MONO};color:{WHITE};">{name}</div>'
        f'<div style="margin-top:18px;font:400 24px/1.4 {SANS};color:{BODY};max-width:74%;">{sub}</div></div>')

def big_title(eyebrow, title, sub, size=74, link=None, link_label=None):
    linkhtml = ""
    if link:
        linkhtml = (f'<div style="margin-top:30px;font:700 14px/1 {MONO};letter-spacing:.18em;color:{MUTED};">{link_label}</div>'
                    f'<div style="margin-top:8px;font:700 26px/1.2 {MONO};color:{BLUE};text-decoration:underline;text-underline-offset:5px;">{link}</div>')
    return bg(
        f'<div style="position:absolute;left:6.5%;right:6%;top:50%;transform:translateY(-50%);">'
        f'<div style="font:700 16px/1 {MONO};letter-spacing:.22em;color:{BLUE};">{eyebrow}</div>'
        f'<div style="margin-top:14px;font:800 {size}px/1.03 {MONO};color:{WHITE};">{title}</div>'
        f'<div style="margin-top:20px;font:400 24px/1.45 {SANS};color:{BODY};max-width:74%;">{sub}</div>{linkhtml}</div>')

def step_cells(items):
    n = len(items); cells = ""
    for i, s in enumerate(items, 1):
        cells += (f'<div><div style="font:700 15px/1 {MONO};color:{BLUE};">0{i}</div>'
                  f'<div style="margin-top:10px;border-top:2px solid {RULE};"></div>'
                  f'<div style="margin-top:14px;font:400 19px/1.45 {SANS};color:{BODY};">{s}</div></div>')
    return f'<div style="display:grid;grid-template-columns:{"1fr " * n};gap:0 28px;">{cells}</div>'

def steps(eyebrow, title, items, foot=None):
    foothtml = (f'<div style="position:absolute;left:6.5%;right:6%;bottom:16%;font:italic 400 23px/1.4 {SANS};color:{BLUE};">{foot}</div>'
                if foot else "")
    return bg(header(eyebrow, title) +
              f'<div style="position:absolute;left:6.5%;right:6%;top:36%;">{step_cells(items)}</div>' + foothtml)

def cards(eyebrow, title, items, cols=None):
    cols = cols or len(items)
    cells = ""
    for it in items:
        tag = (f'<div style="margin-top:14px;font:600 14px/1.3 {SANS};letter-spacing:.03em;color:{MUTED};">{it["tag"]}</div>'
               if it.get("tag") else "")
        cells += (f'<div style="border-top:2px solid {RULE};padding-top:16px;">'
                  f'<div style="font:700 15px/1 {MONO};letter-spacing:.16em;color:{BLUE};">{it["k"]}</div>'
                  f'<div style="margin-top:10px;font:800 30px/1.1 {MONO};color:{WHITE};">{it["h"]}</div>'
                  f'<div style="margin-top:12px;min-height:84px;font:400 18px/1.5 {SANS};color:{BODY};">{it["b"]}</div>{tag}</div>')
    return bg(header(eyebrow, title) +
        f'<div style="position:absolute;left:6.5%;right:6%;top:32%;bottom:12%;display:grid;'
        f'grid-template-columns:{"1fr " * cols};gap:0 26px;align-content:start;">{cells}</div>')

def numbered(eyebrow, title, items):
    cells = ""
    for it in items:
        cells += (f'<div style="border-top:2px solid {RULE};padding-top:16px;">'
                  f'<div style="font:700 15px/1 {MONO};letter-spacing:.16em;color:{BLUE};">{it["k"]}</div>'
                  f'<div style="margin-top:10px;font:700 26px/1.2 {MONO};color:{WHITE};">{it["h"]}</div>'
                  f'<div style="margin-top:12px;font:400 19px/1.5 {SANS};color:{BODY};">{it["b"]}</div></div>')
    return bg(header(eyebrow, title) +
        f'<div style="position:absolute;left:6.5%;right:6%;top:34%;bottom:13%;display:grid;'
        f'grid-template-columns:{"1fr " * len(items)};gap:0 28px;align-content:start;">{cells}</div>')

def lab_intro(title, items, badge="LAB"):
    return bg(
        f'<div style="position:absolute;left:6.5%;right:6%;top:50%;transform:translateY(-50%);">'
        f'<div style="display:inline-block;background:{BLUE};color:#0a1019;font:700 14px/1 {MONO};'
        f'letter-spacing:.12em;padding:8px 16px;border-radius:999px;">&bull; {badge}</div>'
        f'<div style="margin-top:20px;font:800 68px/1.05 {MONO};color:{WHITE};">{title}</div>'
        f'<div style="margin-top:30px;">{step_cells(items)}</div></div>')

# ---------------------------------------------------------------- batch 1
SLIDES = {}
SLIDES[4]  = big_title("LAB 1 &middot; SETUP", "Access the Workshop",
                       'containerdays.dockerworkshop.com &mdash; runs in your browser, nothing to install.', size=64)
SLIDES[19] = big_title("A FALSE START", "Why not containers?",
                       "Containers isolate applications well. Agents need more access than applications do.")
SLIDES[22] = big_title("THE FIX", "Hello, Sandboxes",
                       "Give the agent everything it needs, inside a boundary it can't cross.")
SLIDES[24] = cards("CONTAIN &middot; CONTROL &middot; CHOICE &middot; CAPACITY", "A sandbox gives you four things", [
    {"k":"01","h":"Contain","b":"Isolate the agent in a microVM with a guarded network."},
    {"k":"02","h":"Control","b":"Set what the agent can reach. Organizations add governance and audit."},
    {"k":"03","h":"Choice","b":"Bring your own agent, tools, and endpoints with kits."},
    {"k":"04","h":"Capacity","b":"Reproduce the same sandbox for every developer and every run."},
])
SLIDES[25] = divider("01", "Contain", "The boundary that keeps the agent &mdash; and your secrets &mdash; inside the sandbox.")
SLIDES[32] = divider("02", "Control", "Decide what the agent can reach and touch &mdash; you set where the boundary sits.")
SLIDES[36] = divider("03", "Choice", "A locked box still has to be useful &mdash; bring your own agent, tools, and MCP endpoints.")
SLIDES[42] = divider("04", "Capacity", "Reproduce the same sandbox for every developer and every run.")
SLIDES[31] = lab_intro("Testing the boundaries", [
    "Try the same escape &mdash; the socket belongs to the sandbox",
    "Look for host keys and other projects",
    "Call a model API without ever seeing the key",
])
SLIDES[48] = cards("WRAP-UP", "Recap", [
    {"k":"01","h":"A trusted boundary","b":"A microVM, a network proxy, and credentials the agent never holds.","tag":"CONTAIN &middot; CONTROL"},
    {"k":"02","h":"Your choice inside it","b":"Agent and mixin kits for your harness, tools, and endpoints.","tag":"CHOICE"},
    {"k":"03","h":"Shared with the team","b":"One environment file in the repo. Update once, everyone follows.","tag":"CAPACITY"},
], cols=3)

# ---------------------------------------------------------------- batch 2
SLIDES[20] = steps("WHY NOT CONTAINERS", "Escaping a container", [
    "A coding agent runs in a container",
    "The Docker socket is mounted so it can build and test",
    "The agent uses the socket to reach the host",
])
SLIDES[27] = steps("CONTAIN", "Credentials are added outside the sandbox", [
    "<b style='color:#fff'>Agent calls an API</b><br>The request has no key attached.",
    "<b style='color:#fff'>Policy check</b><br>Is this destination allowed? If not, the request stops here.",
    "<b style='color:#fff'>Key injected</b><br>The proxy adds the credential stored on the host.",
    "<b style='color:#fff'>API responds</b><br>The agent gets the result, never the key.",
], foot="The raw key never enters the sandbox.")
SLIDES[35] = lab_intro("Adjusting policy", [
    "The agent hits a blocked endpoint",
    "Find it in the policy log",
    "Allow it and keep working",
])
SLIDES[40] = lab_intro("Running kits from Docker Hub", [
    "Start a sandbox with one agent kit",
    "Swap the harness, keep the project",
    "Add mixins for GitHub, signing, and the dev env",
])
SLIDES[47] = lab_intro("Sharing a sandbox with the team", [
    "Clone a repo that has an environment file",
    "Start a sandbox &mdash; kits and policy are already set",
    "Change one line and start again",
], badge="LIVE DEMO")
SLIDES[45] = steps("CAPACITY", "Commit it once and the whole team shares one setup", [
    "<b style='color:#fff'>Change the file</b><br>Update a kit, add a kit, or swap the harness.",
    "<b style='color:#fff'>Open a pull request</b><br>The change is reviewed like code.",
    "<b style='color:#fff'>Merge</b><br>The repo holds the new definition.",
    "<b style='color:#fff'>Everyone pulls</b><br>The next sandbox each person starts matches.",
], foot="Update once. Every sandbox follows.")
SLIDES[41] = big_title("CHOICE", "You can build your own kits",
    "Kits follow an open specification. Package your own agent or tooling the same way the Hub kits are built.",
    link="github.com/docker/sandbox-kit-spec", link_label="SANDBOX KIT SPECIFICATION")
SLIDES[46] = cards("CAPACITY", "Cloud Sandboxes run the same setup remotely", [
    {"k":"LOCAL","h":"On your machine","b":"The sandbox runs on your laptop, limited by its CPU and memory."},
    {"k":"CLOUD","h":"On Docker's infrastructure","b":"The same environment file, running remotely. Start more sandboxes than one laptop can hold.","tag":"EARLY ACCESS &middot; not yet available for org use"},
], cols=2)

# ---------------------------------------------------------------- emit
IMG = ('<img src="assets/talk-{n:02d}.webp" alt="{alt}" width="1600" height="900" loading="lazy" '
       'decoding="async" style="position:absolute;inset:0;width:100%;height:100%;max-width:none;max-height:none;object-fit:fill" />')
ALT = {4:"Access the Workshop",19:"Why not containers?",22:"Hello, Sandboxes",
       24:"A sandbox gives you four things",25:"Contain",31:"Testing the boundaries",
       32:"Control",36:"Choice",42:"Capacity",48:"Recap"}

HERE = os.path.dirname(os.path.abspath(__file__))
DECK = os.path.join(HERE, "..", "deck.md")

def main():
    parts = []
    for n in range(1, 49):
        body = SLIDES.get(n) or IMG.format(n=n, alt=f"Slide {n}")
        parts.append("<!-- chrome: false -->\n\n" + body + "\n")
    with open(DECK, "w") as f:
        f.write("\n---\n\n".join(parts))
    print(f"wrote deck.md: {len(SLIDES)} HTML slides, {48-len(SLIDES)} image slides")

if __name__ == "__main__":
    # render a few HTML slides to /tmp for visual QA when asked
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "render":
        head = '<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0}#s{position:relative;width:1600px;height:900px;overflow:hidden}</style></head><body><div id="s">'
        for n in [int(x) for x in sys.argv[2:]]:
            open(f"/tmp/qa_{n}.html","w").write(head + SLIDES[n] + "</div></body></html>")
            print(f"/tmp/qa_{n}.html")
    else:
        main()
