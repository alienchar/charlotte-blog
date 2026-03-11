---
title: 'Karpathy Open-Sourced an AI Researcher That Runs 100 Experiments While You Sleep'
date: 2026-03-07
summary: 'Karpathy just dropped autoresearch: an AI Agent that modifies code, trains models, and evaluates results on its own — 100 experiments in a single night.'
tags: ["AI Tools", "Karpathy", "Open Source", "Agent", "Automation"]
cover: '/images/cover_karpathy-ai-researcher.png'
---

Last Friday night, Karpathy posted a tweet.

It ended with one line and a GitHub link:
![](/images/Pasted_image_20260308124007.png)
![](/images/Pasted_image_20260308123411.png)

The tagline? "Half code, half sci-fi, and a pinch of insanity."

The tweet blew up. 1.1 million views, 10,000+ bookmarks.

He open-sourced a project called **autoresearch**.

The idea is dead simple — you write a prompt, and AI runs experiments for you. A hundred of them. Overnight.

## What Does This Thing Actually Do?

Quick background — you probably know who Karpathy is. Former Tesla AI Director, OpenAI founding member, basically the ceiling of deep learning education. When he ships something, all of Silicon Valley stops to look.

The core logic of autoresearch is surprisingly straightforward. Three files:

- **`prepare.py`**: Prepares data and trains the tokenizer. Run it once, then forget about it.
- **`train.py`**: The model training script. This is the *only* file the AI Agent touches. Architecture, optimizer, hyperparameters — everything's fair game.
- **`program.md`**: Your "research playbook" for the AI. You tell it how to think, what to explore, and which directions are worth pursuing.

Here's the workflow:

1. You write program.md (basically giving the AI its research brief)
2. The AI Agent reads it and modifies train.py on its own
3. It runs one training session — **capped at exactly 5 minutes**
4. Checks whether validation loss went down
5. Loss dropped? Keep the code, git commit. Didn't drop? Toss it, try again
6. Repeat. Keep repeating. A hundred times overnight.

You go to sleep. It runs experiments. You wake up, open `git log`, and see what it did last night.

## The 5-Minute Timer: Quietly Brilliant Design

The most elegant design in this entire project isn't some fancy AI architecture — it's that **fixed 5-minute time budget**.

When an AI Agent modifies code, anything can change. The model gets bigger, batch size shrinks, the optimizer swaps out, maybe the entire architecture gets rewritten from scratch.

If you time things by "run until done," a big model takes 20 minutes and a small one takes 2 — you can't compare them at all.

But 5 minutes is 5 minutes. No matter what you changed, **whoever gets a lower loss in the same amount of time wins**.

This turns the open-ended problem of "AI research" into a game with a clear scoring system. Like a timed exam — everyone gets the same 150 minutes, highest score wins. When the clock runs out, pencils down. No extensions.

Lior Alexander explained it like this:

> *Each dot is a full training run. The Agent loops autonomously on a git branch — finds a better setup, commits the code; doesn't find one, discards it. 12 experiments per hour, 100 overnight.*

Twelve experiments per hour.

How many can you do manually in a day? Two or three, tops?

That's the gap between humans and Agents — **it's not an intelligence gap, it's a time gap**. AI doesn't eat, doesn't sleep, doesn't scroll its phone, doesn't agonize over "is this direction even worth trying." It just tries. Relentlessly, mechanically, brute-force tries.

## You're Not Writing Code Anymore — You're Writing a Playbook

There's a subtle identity shift happening here.

What did traditional AI research look like? Researchers write their own code, tune their own parameters, run their own experiments, analyze their own results. Finish one experiment, change two lines of code, run it again. Day after day.

autoresearch flips this workflow upside down:

**You don't touch Python files anymore. You write Markdown.**

`program.md` is your "research command center." In it, you define:
- What the current research direction is
- Which dimensions should be explored first
- What kinds of changes are encouraged
- What kinds of changes should be avoided

Yeah — you've gone from being "the person who runs experiments" to "the person who designs experiment strategy."

Karpathy himself said:

> *You can imagine comparing different prompts, different Agents' research progress.*

In other words, the future competition isn't about "who writes better code" but **"who writes better prompts."** Whoever can direct AI more effectively will iterate faster.

It reminds me of something — *the best lab of the future won't be the one with the most compute, but the one with the best Agent instructions.*

## Can Regular People Use This?

Honestly, there's a barrier to entry.

Running autoresearch requires an NVIDIA GPU (Karpathy uses an H100). Your laptop probably won't cut it.

But that doesn't mean it's irrelevant to us.

**Option 1: Rent a GPU and try it.**

Lambda, Vast.ai, RunPod — an H100 costs around $10-15/hour. Spend $40 running it overnight, and the next morning you can see what experiments the AI ran, what code it changed. That experience alone is worth a Xiaohongshu post.

**Option 2: Understand the idea and apply it to your own work.**

autoresearch's core philosophy isn't limited to LLM training:

- **Fixed time budget + automatic evaluation + iterative loops** — this methodology works for any task with a clear metric
- Writing prompts matters more than writing code — this has been consensus in the Vibe Coding era for a while
- Agents do the repetitive labor, humans make strategic decisions — this is what I've been saying all along: "humans think, AI executes"

## Quick Start (For Those Who Want to Try)

If you actually have a GPU, four steps and you're done:

```bash
# Install the uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Prepare data (run once)
uv run prepare.py

# Manual training run to verify everything works
uv run train.py
```

Once the environment checks out, open your Claude or Codex, point it to the project directory, and say:

> "Hi have a look at program.md and let's kick off a new experiment!"

Then turn off the lights and go to sleep.

Next morning, `git log` to see what it did.

## Why Does This Matter?

Real talk — at first glance, this project seems irrelevant to most of us. We're not doing research ourselves.

And the tech itself isn't exactly groundbreaking — 5-minute training + auto-evaluation in a loop isn't that complex.

But because Karpathy personally turned this into a **minimalist, universally understandable demo** — 630 lines of code, 3 files, runnable in a weekend.

He put a "sci-fi prologue" at the beginning of the README:

> *Once, frontier AI research was conducted by meat-brains in between eating, sleeping, and entertainment, occasionally synchronizing via sonic-wave interconnect rituals known as "group meetings." That era has long since passed.*

It's tongue-in-cheek, but not entirely.

Two years ago, I was still pulling all-nighters tuning hyperparameters. Now I have OpenClaw running daily reports, doing topic analysis, and managing my knowledge base.

autoresearch just pushes this one step further: **AI isn't just helping you execute — it's starting to do research for you.**

Karpathy calls it "the post-AGI feeling." I think he's only half right.

This isn't AGI. It's just the beginning of a new division of labor between humans and AI.

---

📎 **Project**: [github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)
📎 **Karpathy's tweet**: [x.com/karpathy/status/2030371219518931079](https://x.com/karpathy/status/2030371219518931079)

---

Tools amplify advantages you already have. And your greatest advantage is knowing which questions are worth asking.

Thanks for reading.
