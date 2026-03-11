---
title: 'I Connected OpenClaw to Obsidian, and My Content Factory Started Running Itself'
date: 2026-03-08
summary: "It's not a note-taking app — it's the operating system for content production. Here's how I built it, step by step."
tags: ["Obsidian", "AI Tools", "Content Creation", "Workflow", "Creator Economy"]
cover: '/images/oc_cover.png'
---
![](/images/oc_cover.png)

I recently read an article about someone who turned Obsidian into a factory — 468 git commits, 85 AI Skills, 7 platforms synced for distribution, one person producing the output of a ten-person team.

I was nodding furiously.

Not because of the numbers, but because one sentence perfectly captured what I've been doing for the past week: building a content factory that's entirely mine, has a unique personal style, and won't disappear if any one tool goes away.

**Apps are fleeting. Files are forever.**

That's from Steph Ango, Obsidian's CEO. The idea: over a long enough timeline, *the files you create matter far more than the tools you used to create them.*

I'd never thought about it from that angle before. But it summed up everything I've been doing in a single line.

---

## My Starting Point Was… Rough

I come from a marketing background. Can't write code. But I managed to build a fairly complex **Obsidian + Claude Code + OpenClaw** workstation.

Before agents blew up, I'd tried every tool out there — Notion, Feishu, Evernote, and every Markdown editor under the sun. Each migration was a mini-disaster: broken formatting, dead links, two weeks of reorganizing everything I'd accumulated.

Eventually I asked myself a serious question: if this software shuts down tomorrow, or hikes its prices, or gets acquired and changes direction — will my content still be there?

The answer was depressing.

But a .md file — plain text, Markdown format — opens on any device, doesn't depend on any company's servers to survive, and won't vanish because some product manager decided to "optimize the experience."

That's something that truly belongs to me.

---

## Building Workflows Hand-in-Hand With AI

![](/images/oc_illus1.png)

My current system was a team effort — built piece by piece together with my lobster OpenClaw, Claude Code, and Gemini. Lots of meetings (with AI). Lots of iteration.

I wanted a ton of features, all highly personalized. And with no technical background, there's no way to design everything perfectly upfront. It all came together through actually producing content — hitting walls and improving as I went.

### Core Architecture at a Glance

**The lobster as a powerful execution engine:**
- Text content: fetching source material, analyzing content, first-draft writing, creating illustrations, designing covers, pushing to platforms
- Video content: subtitle extraction, scriptwriting, prompt generation, voiceover synthesis, subtitle matching, video editing
- Personal assistant: daily briefings, work logs, second brain

**Obsidian as the storage hub:**
- All drafts, documents, and logs live here — all local .md files
- One-click article formatting and platform draft imports
- System-managed file organization, cleanup, and categorization

**Claude Code as the project manager:**
- System management: building, managing, and iterating programs, workflows, and skills
- Bug fixes: repairing every code issue that comes up

**GitHub as the bridge:**
- Version control, history tracking, recoverability

*These four layers together form my content factory.*

**What does a complete content production run look like?**

For example: I send a URL to the lobster and say "rewrite this as a WeChat Official Account article."

It automatically:
1. Grabs the topic
2. Searches the web for supplementary information
3. Calls my Writing Skill and drafts in my personal style
4. Generates article illustrations
5. Pushes the draft

Another example: I tell the lobster about a YouTube creator and ask it to analyze them. Instantly:
![](/images/Pasted_image_20260306195140.png)

Or: I send a video to the lobster and say "make a video on the same topic."

It automatically:
1. Extracts the content
2. Supplements with additional research
3. Writes the script
4. Generates subtitles, voiceover, and video clips
5. Edits the final cut

![](/images/Pasted_image_20260306195413.png)
---

## A Content Factory That Evolves

Skills can learn.

I have a mechanism: every time I manually polish an article, the lobster reads the latest version, compares it with the original, extracts the style patterns from my edits, and updates the "Charlotte Writing Skill."

With every article, the Skill becomes a little more like me.
![](/images/Pasted_image_20260306194611.png)

I have another mechanism: things I've learned, plans I'm making, sudden flashes of inspiration, current project status... everything mentioned in AI conversations, everything successfully executed with the lobster, everything fixed by Claude Code — it all gets extracted and organized.

*My experience is captured. My lessons are learned.*

*This flywheel is the most valuable part of the entire system. Because it grows with me, and like me, it's one of a kind.*



<div class="callout">
<strong>💡 💡 Key Insight</strong>

Most people use AI like this: every time, they give it a pile of context and hope "maybe this time it'll understand me."

A better approach: turn your style, preferences, and principles into a living document that AI reads every time and improves every time. That document is your most valuable asset.
</div>


---

## About "Your Files Belong to You"

![](/images/oc_illus2.png)

One reversed line of script logic, and 1,174 files were wiped clean in an instant.

But because of Git, one command restored everything.

I haven't experienced that exact disaster myself, but I understand the logic:

Your knowledge assets should live somewhere you have complete control.

Notion is a great product — I still use it. But I don't store my core article drafts, writing style documents, or Skill system in Notion. Not because Notion isn't good — but because that's their server, not my hard drive.

What if they change their pricing? What if they get acquired and everything changes?

.md files are different. They're just files. Open them with any editor, no company API required, no "export" needed, no waiting. They're always there, quietly, belonging to you.

This isn't paranoia — it's good design.

Everything should be .md. Everything should be CLI. That's my biggest takeaway from the past month.

---

![](/images/oc_illus3.png)

## Problems I Haven't Solved Yet

A few real issues that still exist — I don't want to pretend everything's perfect.

**Illustration style is sometimes inconsistent.** Generated images sometimes have a cohesive look, sometimes they're all over the place. I'm constraining prompts through detailed Skill documentation, but there's still a luck factor.

**Can't one-click publish image posts to X.** X's editor won't accept pasted images — you have to upload them manually. Text can be copied directly, but images still require manual intervention.

**Obsidian syncing requires manual triggers.** I use the Git plugin for syncing, but I have to manually commit+push after writing. Haven't automated that yet.

**Full video automation is expensive.** Most of the time, I still have the lobster generate prompts while I manually operate the web tools, since Seedance 2.0's API isn't exactly cheap...

These are all on the to-fix list. But they also prove a point: building a workflow isn't a one-time event — it's continuous iteration.

You don't need to wait until the system is "finished" before you start using it. Build as you go. That's the real rhythm.

---

## If You Want to Build Your Own, Where to Start

I can't give you a "just follow these steps" checklist — everyone's situation is too different.

But a few starting points are universal:

**Step 1: Choose local-first tools.** Obsidian or any tool built around local .md files works. The only criterion: your files live on your own hard drive, not on someone else's server.

**Step 2: Build your own Skills.** Don't just rely on downloaded community skills. Only when you start writing your own do you clarify your thinking and figure out what you actually want. Iterate based on results. It's also a great way to train your structured thinking.

**Step 3: Pick a trigger phrase and automate your first process.** Don't try to automate everything at once. Find one thing you repeat daily, and try to automate just that.

**Step 4: Develop a "files as records" habit.** Every update, write it down. Every discovery, log it. These records are the raw material for your system's evolution.

*Notebooks wait for you to write. Operating systems push you forward.*

Design your content workflow to match what you want it to become.


<div class="callout">
<strong>💡 🎯 A Litmus Test</strong>

Ask yourself: if this tool shut down today, could I continue working tomorrow?

If the answer is "no — everything I have is in there" — then be careful.
</div>


---

Files outlive tools.

Content outlives platforms.

Your .md files outlive...

Thanks for reading.
