---

title: "1 Million Tokens: Claude Can Now Remember an Entire Book"
date: 2026-03-15
description: "On March 13, Anthropic officially announced: the 1 million token context window for Claude Opus 4.6 and Sonnet 4.6 is now generally available. Not beta, not a waitlist, not a partial rollout — GA, for everyone."
tags: ["Claude", "AI", "Long Context", "Anthropic"]
keywords: ["Claude", "AI", "Long Context", "Anthropic"]
images: ['/images/cover_claude_en.png']
readingTime: 7
slug: 'claude'
---One million tokens.

I checked this number several times, went to Claude's official announcement to verify, and only then opened my laptop to write this.

On March 13, Anthropic officially announced: the 1 million token context window for Claude Opus 4.6 and Sonnet 4.6 is now generally available. Not beta, not a waitlist, not a "gradual rollout for select users" — it's GA, available to everyone.

Let me start with what this number actually means.

## How Big Is 1 Million Tokens, Really

![illustration-1](/images/illustration-1.png)

1 million tokens ≈ 750,000 English words ≈ 500,000 Chinese characters.

Still not clicking? Let me put it this way:

The entire Harry Potter series — all seven books — adds up to roughly 1.08 million English words. One million tokens can fit about 70% of that.

Or think of it as 15 to 20 average novels, loaded all at once, and Claude can keep track of everything.

Or an entire medium-sized codebase. Tens of thousands of lines. Or a company's full year of financial reports.

Claude's previous context window was 200K tokens, which was already considered large by industry standards. This update is a straight 5x increase.

Yeah. That's a pretty serious upgrade.

Since my AI assistant PiPiXia runs on Claude through OpenClaw, I was curious whether the lobster got the upgrade too. One look at the conversation window — yep, already showing 1M. Which means I no longer need to frantically start new sessions worrying about hitting the context limit. Nice.
![](/images/Pasted_image_20260315192951.png)

## Pricing Stays the Same — This Is the Real Story

![illustration-2](/images/illustration-2.png)

A bigger context window usually means a bigger bill. But Anthropic took an unusual approach this time:

**Pricing stays the same. No long-context premium.**

Opus is still $5/$25 per MTok. Sonnet is still $3/$15 per MTok.

Running one million tokens in a single call costs the same per token as running 100K tokens ten times.

Honestly, this surprised me. Long context clearly demands more compute. Keeping prices flat means either Anthropic achieved real technical optimizations to control costs, or this is strategic pricing — lock users in first, figure out the rest later.

Either way, for us users, this is straightforwardly good news.

There's another upgrade that's easy to miss: the media limit per request jumped from 100 images/PDF pages to 600. That's a 6x increase. You can now throw an entire multi-hundred-page contract, a full technical manual, or a year's worth of financial statements at Claude in one go. Previously, whenever I had lots of files, I'd go straight to Gemini. Now there's a real alternative.

## How Does It Stack Up Against the Competition

Let's be fair — 1 million tokens is impressive, but it's not the industry's largest. Here's a side-by-side:

- Gemini 2.5 Pro: 2 million tokens
- Claude Opus/Sonnet 4.6: 1 million tokens
- GPT-4o: 128K tokens
- DeepSeek V3: 128K tokens

Gemini does lead on raw window size. But context windows aren't just about "how much can you fit in" — it's about "can the model actually use what's in there."

Opus 4.6 scored 78.3% on the MRCR v2 benchmark — the highest among current frontier models. MRCR specifically measures a model's ability to find information and reason across ultra-long contexts.

In other words: it doesn't just remember — it understands.

## My Actual Experience

![illustration-3](/images/illustration-3.png)

I'm a Claude Max subscriber and a Gemini Pro subscriber. My AI assistant, PiPiXia — my AI assistant (a lobster named PiPiXia) — runs on Opus and Sonnet 4.6.

The 1 million token upgrade has had a real, tangible impact on my daily workflow.

**Long-form translation** — I used to have to feed articles in segments because Claude would "forget" earlier content once it exceeded the context window. The tone would suddenly shift halfway through. Now I drop the entire piece in at once, and the consistency is dramatically better.

**Code review** — When I have PiPiXia review a codebase, I used to go file by file because it couldn't grasp the overall architecture. Now I can load tens of thousands of lines together, and it finally sees the full picture. This difference is transformational.

**Content pipeline** — I produce content for YouTube and distribute across multiple platforms. The volume of material is significant. Previously I had to keep re-feeding Claude background information. Now a single conversation can hold all my materials and discussion history, and the efficiency gain is obvious.

Here's a rough analogy: the old Claude was like an intern with average memory — every time you assigned a task, you had to re-explain all the context from scratch. The new Claude is like an assistant who's been working with you for six months and remembers everything.

## What This Means for Regular Users

You might be thinking: I don't write code or review contracts, so what does 1 million tokens have to do with me?

A lot, actually.

A few direct scenarios:

**Reading.** You can drop an entire book into Claude and ask it anything. "Does the case study in Chapter 3 contradict the conclusion in Chapter 7?" "Find every argument in this book about X." Couldn't do that before — it wouldn't fit. Now it does.

**Research and notes.** Exam prep, thesis writing, project research — load all your reference materials at once and let Claude map out the structure, find cross-references, and generate outlines.

**Work conversations.** Dump months of meeting notes, emails, and documents in, then ask Claude "What were the key decision shifts in Q1?" It can give you a coherent answer instead of only seeing the last few messages.

The bottom line: 1 million tokens isn't a flex for tech enthusiasts. It solves a fundamentally simple problem: **letting AI actually understand what you're talking about, instead of starting from zero every conversation.**

## The Numbers Don't Lie — Industry Reaction

The engagement data on this announcement tells its own story.

Anthropic's official tweet: 5.2 million views. On Hacker News, it shot straight to a 1,110-point top post. Coverage across Reddit, Cursor forums, LinkedIn, Windows Report, and more.
![](/images/Pasted_image_20260315193508.png)

That level of attention tells you 1 million tokens isn't just a spec bump — it's a moment where the whole industry felt like things just changed.

## Enterprise Use Cases Worth Watching

![illustration-4](/images/illustration-4.png)

Anthropic's announcement highlighted feedback from several enterprise customers. A few notable ones:

- Physical Superintelligence uses the 1M context for physics research, loading massive experimental datasets in a single pass
- GC AI processes legal contracts — documents that routinely run hundreds of pages and previously couldn't be analyzed holistically
- Cognition (the team behind Devin) uses it for code review at the entire-codebase level
- Hex uses it for data analysis, loading massive datasets alongside query histories

These use cases share one thing: high information volume, strong context dependencies, and a previous need to process in segments. One million tokens makes "see it all at once" possible.

**One million tokens. No price increase.** 600 media items per request. The highest long-context score among frontier models.

This update doesn't come with a flashy feature name or a slick demo video. But it addresses one of AI's most fundamental challenges — memory.

An AI that can remember an entire book and one that can only remember the last few pages are fundamentally different things.

---

A tool's value isn't in how big its specs are — it's in what you can actually accomplish with it.

Thanks for reading.

<!-- COVER_TITLE: One Million Tokens / Claude Remembers / Everything Now -->
