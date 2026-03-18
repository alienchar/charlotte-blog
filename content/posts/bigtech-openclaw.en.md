---
title: "Tencent, ByteDance, and Alibaba All Launched AI Agents in the Same Week. Here's Why."
date: 2026-03-17
description: "In one week, China's three tech giants all released their own OpenClaw-style AI agents. QClaw, ArkClaw, CoPaw, WorkBuddy — they're not competing over a chatbot. They're fighting for the AI gateway. Charlotte breaks down each company's play, and why she still uses the original OpenClaw."
summary: "In one week, China's three tech giants all released their own OpenClaw-style AI agents. QClaw, ArkClaw, CoPaw, WorkBuddy — they're not competing over a chatbot. They're fighting for the AI gateway. Charlotte breaks down each company's play, and why she still uses the original OpenClaw."
tags: ["OpenClaw", "AI Agent", "Tencent", "ByteDance", "Alibaba", "AI gateway"]
keywords: ["OpenClaw", "AI Agent", "Tencent", "ByteDance", "Alibaba", "AI gateway"]
cover: "/images/cover_bigtech-openclaw.png"
images: ["/images/cover_bigtech-openclaw.png"]
readingTime: 14
slug: "bigtech-openclaw"
---

![Cover](/images/cover.png)

At the start of March, OpenClaw was still a niche toy for the tech crowd.

One week later, *Tencent, ByteDance, and Alibaba had all entered the space.*

My first reaction when I saw the news wasn't excitement. It was — *saw this coming, just not this fast.* What surprised me was the simultaneity: three companies launching their own OpenClaw products within essentially the same week, with timing so precise it looked like they were watching each other's release calendars.

This past week, friends have asked me some version of the same question at least ten times: "What's the difference between Tencent's version and the one you use?" "Is ByteDance's better?" "Alibaba did one too? Which should I pick?"

Today I'm not going to talk about how to install or configure any of them. I want to address a bigger question: **Why did all three giants move at the same time — and what are they actually after?**

---

## What Happened in One Week

Let me lay out the timeline.

Early March: OpenClaw's GitHub heat kept climbing, WeChat Index broke 70 million, and daily search growth hit 206% day-over-day. OpenClaw went from "geek toy" to national topic. People everywhere were talking about it. Moments full of screenshots — "I have an AI agent now!"

Then the giants couldn't sit still anymore.

March 9th: Tencent's QClaw beta was reported by technode.com.
Same week: ByteDance's ArkClaw quietly launched on the Volcengine platform.
Alibaba's CoPaw was revealed to be in development at the Tongyi lab.
Plus Tencent's WorkBuddy launched in early March (reported by Wall Street Horizon).
And the semi-public secret — WeChat's internal AI Agent project, reportedly planned for mid-year grey testing.

Within one week, at least five OpenClaw-adjacent products surfaced.

This isn't coincidence. This isn't trend-chasing. This is a *race to claim the AI gateway*, erupting in concentrated form during the first week of March.

![Five AI agent products launched in one week](/images/illustration-1.png)

---

## Tencent's Three-Pronged Assault

Of the three giants, Tencent is the most heavily committed. They're not dipping a toe in — *they put three dishes on the table at once.*

**Dish one: QClaw.**

From the Tencent PC Manager team. Beta launched March 9th.

QClaw's core pitch is **one-click installation**. Download a package, double-click, done. No terminal, no environment variables, no need to know what Node.js is, no API key to apply for. If you can install WeChat, you can install QClaw.

But the sharper move is that it's *integrated with WeChat and QQ*.

You can send instructions to your AI agent through WeChat on your phone, and it'll handle things on your desktop. Out running errands, send a message: "Clean up the reports on my desktop and send them to the work group." And it goes.

That's clever. The original OpenClaw's barrier is that you have to face a black terminal window with white text. For most people, that's as intimidating as logging into your router admin panel. QClaw removes that layer completely — the agent becomes a WeChat contact. You chat with it; it does the work.

For everyday users, this is probably *the lowest-barrier OpenClaw experience* available.

**Dish two: WorkBuddy.**

Desktop AI agent. Claims under-1-minute deployment. And — this is the key — **compatible with the OpenClaw Skill ecosystem**.

What does that mean? *All the Skills built by the original OpenClaw community* — daily report writing, news aggregation, data analysis, competitor monitoring — WorkBuddy can install and run all of them. Tencent isn't building an ecosystem from scratch; they're plugging directly into an open-source community with 80,000+ GitHub stars and thousands of contributing developers. (I'm trying not to editorialize here, but even OpenClaw's creator has publicly called out Tencent on X. China doesn't need more "no innovation" criticism — maybe show some restraint…)

That's a leverage play. How long would it take to build a Skill ecosystem from zero? A year? Two? By being OpenClaw-compatible, you have hundreds of usable Skills on day one.

WorkBuddy targets more advanced users. If QClaw is "raise an agent inside WeChat," WorkBuddy is "*a full AI assistant sitting on your desktop.*" It can see your screen, operate your applications, manage your files. More heavyweight than QClaw, but more capable.

**Dish three: WeChat AI Agent.**

This is *the semi-public secret*. Everyone in the industry is talking about it, but Tencent has officially confirmed nothing. Reportedly a highly classified internal WeChat project, planned for mid-year grey testing, with a core focus on integrating the WeChat Mini Program ecosystem.

Think about what that means. WeChat has 1.3 billion users. Mini Programs. Payments. Social graph. Official Accounts. Video Accounts. If WeChat had a built-in AI Agent, users wouldn't need to download anything new. It lives inside the green icon they open every day.

Order food delivery — calls the Meituan Mini Program. Track a package — calls the Cainiao Mini Program. Book movie tickets — calls the Maoyan Mini Program. Reply to messages — reads your chat context. Summarize group chats — analyzes 500 messages and hands you a paragraph.

This isn't science fiction. These are capabilities WeChat already has. Add an AI scheduling layer on top.

Ma Huateng said in an internal talk earlier this year: "AI is the only area worth investing heavily in right now."

Looking at the product rollout, he means it. Three simultaneous tracks — from casual users (QClaw) to power users (WorkBuddy) to everyone (WeChat AI Agent), with full coverage at each layer.

![Tencent: three tracks — social, desktop, super-app](/images/illustration-2.png)

---

## ByteDance: Skip the Install, Just Open a Browser

ByteDance's approach is completely different.

**ArkClaw**, from Volcengine. Cloud-hosted SaaS version of OpenClaw.

Translation: *you don't install anything on your machine.* Open a browser tab, log in, and the agent is already running in the cloud. **Out-of-the-box.** ByteDance handles the servers, models, and runtime environment — you just tell it what you need.

This transforms the agent from "a pet you raise yourself" into "a service the platform provides."

Obvious benefit: zero barrier. You don't need a high-powered machine, don't need any technical knowledge, don't need to spend an afternoon on configuration. Create an account, open a browser, start using it.

The trade-off: *your data is on ByteDance's servers, you're using models ByteDance has preconfigured, and Skills go through platform review.* Considerably less freedom than the original.

But ByteDance's real ace card isn't ArkClaw. It's **Doubao**.

Doubao's daily active users have passed 100 million. *145 million.* That number just sits there. It means 145 million people in China talk to an AI every single day. ByteDance doesn't need to educate the market about what an AI Agent is. They just need to add a "help me do things" button inside Doubao and upgrade chat into action.

Doubao's strength is *mobile and voice interaction*. You tell your phone, "Check tomorrow's weather in Beijing, then format it as a schedule reminder and add it to my calendar." It goes. No typing, no computer, no app-switching.

ByteDance's 2026 keyword, according to CEO Liang Rubo, is "climbing higher." From the product picture, they're climbing fast. Doubao's daily actives are a ready-made traffic pool. ArkClaw is the technical foundation. Combined: mobile-first AI Agent, voice-driven, built on a 100-million+ user base.

That combination has serious potential.

---

## Alibaba: Own the Office

Alibaba's entry point is the most concrete: work.

**CoPaw**, from the Tongyi lab. Covers document editing, desktop file organization, auto email archiving, meeting notes generation, and other office scenarios.

CoPaw doesn't chase "do everything." It chases "*do office work to an extreme.*"

Write your weekly report — automatically generate a draft from your week's activity log. Organize your desktop — file everything by project automatically. Manage email — flag important messages, archive ads, remind you what needs replies. Meeting notes — drop in the recording, get a structured summary with action items and owners in five minutes.

It's less flashy than "raise an agent inside WeChat." But honestly, these are the things most working people need most urgently. How much time do you spend writing weekly reports, organizing files, answering emails? An hour? Two? If CoPaw cuts that in half, its value is already very concrete.

Alibaba's other big move is brand unification. "Qianwen" (千问) now covers everything from base model to applications. Tongyi Qianwen, Qianwen large model, Qianwen Agent — one name across the whole stack.

That's brand strategy. When you think "AI for work," Alibaba wants "Qianwen" to be the first word that surfaces. The way you think of Baidu for search, WeChat for social, Taobao for e-commerce.

Brand mindshare, once held, costs ten times as much to displace. That's what Alibaba is competing for.

---

## What the Giants Are Actually Fighting Over

By now you've probably noticed — what Tencent, ByteDance, and Alibaba built looks similar on the surface, but their approaches are completely different.

- Tencent is pursuing the **social gateway**. WeChat and QQ are the carrier; the agent is a function embedded in social interaction.
- ByteDance is pursuing the **traffic gateway**. Doubao is the carrier; the agent is the upgrade from conversation to action.
- Alibaba is pursuing the **work gateway**. Qianwen is the brand; the agent is the tool blanketing the professional context.

**The three giants aren't competing over an AI agent. They're competing for the AI gateway.**

This logic isn't new. We saw it play out over the past decade. WeChat captured the social gateway. Alipay captured the payment gateway. TikTok/Douyin captured the short video gateway. Meituan captured the local services gateway. *Whoever controls the gateway controls user habits.* Whoever controls user habits controls all subsequent monetization — advertising, memberships, e-commerce, finance.

The same race is now happening in the AI Agent space. The gateway just happens to be called "OpenClaw" this time.

> Agents aren't the product. They're the gateway. Whoever shapes AI Agent usage habits shapes the next decade of digital life.

![Three giants fight for the AI gateway](/images/illustration-3.png)

This also explains why all three moved simultaneously. Not because the technology is mature — honestly, every product at launch still has rough edges. But because if you wait for the technology to mature, someone else already owns the gateway.

There's an old saying in the internet industry: *users first, business model second.*

Every company is in user acquisition mode right now. One-click install, cloud SaaS, WeChat messaging, voice interaction — whatever gets users using it. Once usage forms habits, monetization is a matter of time.

---

## What This Means for Regular People

Good news: getting an OpenClaw-style agent set up has never been easier.

Three months ago, installing OpenClaw required terminal commands, environment variables, API keys, and surviving a gauntlet of problems. I personally spent an entire afternoon. Now? QClaw is one click. ArkClaw is open-browser-and-go. WorkBuddy claims under a minute. The barrier has dropped from "need some tech knowledge" to "if you can use WeChat, you're fine."

That's genuinely good for people. AI agents are no longer exclusively for programmers.

But the bad news: **you now have analysis paralysis.**

QClaw, WorkBuddy, ArkClaw, CoPaw, the original OpenClaw, plus countless community forks and custom builds… which one do you actually use?

Every one claims to be the best. Every one is free or cheap. Every one has overlapping but not identical features. And every company has different approaches to your data.

The question I've been asked most this week: "Charlotte, which one do you use? Which one should I pick?"

Honestly, there's no universal answer. But there's a decision framework:

**If you want convenience, hate configuration, and can accept your data living on a platform server** → the big tech versions are for you. QClaw for heavy WeChat users, ArkClaw for people who don't want to install anything, CoPaw for those focused on office productivity.

**If you want full control, are willing to learn, and care about data privacy** → the original OpenClaw is for you. Higher barrier, but you own everything.

---

## One More Thing Worth Saying

Big tech building agents raises efficiency and lowers barriers — but some things also quietly change.

The original OpenClaw is open source, running on your machine, with data on your hard drive. What model you use, what Skills you install, what permissions you grant — all of that is your call.

But QClaw is connected to WeChat — do your conversations with the agent pass through Tencent's servers? ArkClaw runs in the cloud — do the documents you process with it live on ByteDance's infrastructure? CoPaw manages your email and files — can Alibaba see your work content?

I'm not saying they're definitely looking. Big companies have compliance teams, privacy policies, legal constraints. But **when your AI assistant runs on someone else's servers, you've surrendered a degree of control.** That's a structural reality, not a matter of trust.

The meaning of open source was never just "free." It's "my data is mine to control, my tools are mine to command."

When big tech packages an agent as a one-click service, they're simultaneously turning "your agent" into "an agent on their platform." You gain convenience; you give up autonomy. Whether that trade is worth it — every person's answer will be different.

---

## Why I'm Still on the Original OpenClaw

I've been asked enough times that I'll just answer it directly here.

I use the original OpenClaw. Running on my own server. Models of my own choosing (primary: Claude Opus — expensive, genuinely excellent). Skills configured together with my agent partner Pipixia. The last thing I say before bed is to my agent; the first thing I receive in the morning is from it.

Why not a big tech version? Four reasons.

**First: data isolation.** My writing materials, topic library, audience profiles, income data, business plans — none of this belongs on any platform's servers. The original OpenClaw runs on my machine. Data doesn't leave. That peace of mind is something QClaw and ArkClaw can't give me.

**Second: full control.** I choose the models. I can switch them anytime. I can run three models simultaneously for cross-validation. Claude for writing today, Gemini for research tomorrow, DeepSeek for cost efficiency the day after — I use what I want, unbounded by any platform. Big tech products limit you to their own or partner models; the selection is much narrower.

**Third: ecosystem compatibility.** I can install any community Skill freely. Skills I write can be shared with others. This is a genuine open-source ecosystem, not a walled garden someone fenced off. The video Skill, topic Skill, and distribution Skill I built for my agent all run smoothly within the OpenClaw framework.

**Fourth — honestly — the tinkering itself is education.** I went from someone with zero technical background to someone who can write Skills, configure automation pipelines, and run a content production workflow through my agent. Everything I've learned through the past three months of wrangling is more than I picked up during years of working in marketing. Those capabilities — that understanding — aren't something you get from a one-click QClaw install.

Are the big tech products good? Yes. Convenient? Very. I'm not the "only what I use is best" type. If you don't want to deal with complexity, QClaw or ArkClaw are genuinely solid choices.

But if you're like me — wanting to actually understand how the thing works, wanting to turn AI into your own core capability rather than a service someone else provides — it's worth spending the time to run the original.

![Independent vs. platform-dependent](/images/illustration-4.png)

Convenience has a price. The tinkering time you save by going big-tech is traded away for understanding of the tool, control over your data, and genuine judgment about AI.

---

The big tech companies are racing for the gateway. And a gateway is something you can either walk through on someone else's road, or hold the key to yourself. The difference: the road belongs to them. The key belongs to you.

Thanks for reading.

<!-- COVER_TITLE: BIG TECH WANTS YOUR AI GATEWAY -->
