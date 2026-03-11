---
title: "The Non-Programmer's Guide to Deploying OpenClaw"
date: 2026-03-06
summary: "No Mac Mini? No problem. A complete deployment guide born from real trial and error — even non-programmers can follow this one."
tags: ["OpenClaw", "VPS Deployment", "Technical Tutorial", "Beginner Guide"]
cover: '/images/cover_openclaw-deploy-guide.png'
---



Today, as a totally non-technical middle-aged person, I officially have a lobster!
![](/images/Screenshot_2026-03-01_144226.png)

By all accounts, OpenClaw has been hot for a while now. But Gemini kept telling me it wasn't necessary to overcomplicate things — my daily work could mostly be handled by local apps on my computer.

Here's the thing though: when everyone's walking around with a lobster on a leash, not having one kind of makes you look... left out.

So I'd always wanted one. I started digging through X to see what people were actually doing with it, how hard it was to use, and whether it was actually worth the trouble.

Then came the headache — most people deploy it on a second-hand *Mac Mini*, which has driven prices up. Spending money before you even know what you'll use it for? That's definitely not how us cost-conscious adults operate. The only thing I could think of was having the lobster send me a daily AI news digest, but other workflows could do that too.

Until I came across this X post:
![](/images/Screenshot_2026-03-01_192823.png)

This was a *nuclear weapon*. Imagine a legendary expert walking up to you, handing you a golden key, and saying "here, just take it."

Look at those view and bookmark numbers — you know it's serious. Bear with my backstory first. Lots of practical stuff coming.
![](/images/Screenshot_2026-03-01_192840.png)

In simple terms, what the expert shared:

- **`OpenNews-MCP`**: Integrates 50+ real-time news sources (including on-chain data). It's not "searching for news" — it's "receiving news telegrams." Blazing fast, and the data comes pre-structured.
    
- **`OpenTwitter-MCP`**: Solves the most painful X API problem. The lobster can directly search real-time discussions on X and analyze what some AI thought leader just tweeted.

Way more exciting than the simple daily digest I'd been imagining. And as we all know, middle-aged folks can't handle too much excitement.

With these two MCP tools, my lobster could monitor X 24/7 for breaking news on specific topics. Any ripple, and it reports back immediately: "*Something big just happened on Twitter!*" And zero setup cost: the README says "no API key needed," meaning no expensive Twitter developer account required (those are pricey).

That's why I immediately went all-in and got OpenClaw running. It's working great and I'm having a blast raising it. But I actually didn't install those two tools — I'll explain the twist at the end.

So here I am — someone with zero programming background, a former corporate marketing person — running OpenClaw on a virtual server in Los Angeles.

> **[!note] 🎯 The Breakthrough
> 
> A VPS isn't some unreachable tech black box — it's just a computer in the cloud that never turns off. Follow this guide step by step, and you too can have an AI digital employee that's online 24/7.

Below is the practical stuff, aimed at **complete beginners with no technical background**. Spoon-fed, step by step. I'm confident that if you follow these instructions, you cannot fail. Absolutely impossible.

Today I've compiled every pit I fell into, every command I typed, into this **Lobster Farming Manual for Beginners**.

Three things upfront:
- It costs money. The VPS requires payment, and calling AI model APIs later also costs money. But you control how much you spend.
- This runs on a VPS — in the cloud. No hardware purchase needed.
- This tutorial is for Windows only.

![](/images/为普通人和技术小白打造的龙虾部署指南_illustration-1.png)

---
## Prerequisites

Before deployment, you need two things:

### Prerequisite 1: Hardware

A VPS server. Simply put, a VPS (Virtual Private Server) is a "computer in the cloud."

Hosting providers split one physical server into multiple virtual servers. Each VPS has its own operating system, CPU, memory, and public IP. You control it remotely over the internet. **The biggest benefit: it runs 24/7 and has solid network connectivity.**

**Why deploy OpenClaw on a VPS?**

If you install OpenClaw on your personal computer, it goes offline whenever you shut down or lose internet. Deploying on a VPS means your AI assistant is available 24/7.

Plus, for many people calling international models (GPT/Claude/Gemini), domestic servers don't work well.

I use **RackNerd**, which Gemini recommended after doing research. You can choose whatever suits your situation.
![](/images/Pasted_image_20260302194047.png)
![](/images/Pasted_image_20260301201646.png)

Configuration recommendations:

- **Light use**: 2GB RAM, ~$18-25/year, good for trying things out and lightweight tasks
- **Recommended**: 4GB RAM, ~$43.88/year, lets the lobster really stretch its legs

My referral link for a discount:
*https://my.racknerd.com/aff.php?aff=18557*

I went straight for the **4GB** option — 3-core CPU + 105GB SSD. Beyond running OpenClaw steadily, it handles other automation projects comfortably.

After selecting, you'll see some fields to fill. The first is the server name (changeable later, or just leave it). The important ones are below:
![](/images/Screenshot_2026-03-01_133733_-_Copy.png)

**Two critical settings**:

1. **Location**: Go with **Los Angeles** or **San Jose**. These US West nodes have the lowest latency for connections from China.
2. **Operating System**: Choose **Ubuntu 24.04 64 Bit**. Best compatibility for Node.js and AI projects.


If Los Angeles is sold out, pick San Jose (third option). Whatever you do, DO NOT pick New York!!
![](/images/Screenshot_2026-03-01_133915.png)


Leave this at the default first option, and keep the other fields at default too:
![](/images/Screenshot_2026-03-01_134130_1.png)

After payment, your registration email will receive the server's IP address, root username, and initial password. Keep these handy — we'll need them shortly.

### Prerequisite 2: Network

You'll need proper internet access to reach international services — if you know, you know.

## Start Deploying

### Connect to Your VPS via SSH

1. Type CMD in your Start menu search bar and press Enter
![](/images/Pasted_image_20260301202037.png)
2. In the window that appears, type this command (replace `<your-server-IP>` with the actual IP from the email):

```bash
ssh root@<your-server-IP>
```

3. Press Enter. The system asks if you want to confirm the connection. Type `yes` and press Enter
4. You'll be prompted for the password. **Copy the password from the email, right-click in the black window to paste**, then press Enter

> **[!note] ⚠️ Important
>
> When entering or pasting passwords in Linux terminals, **nothing appears on screen — not even asterisks**! This is a normal security feature. As long as you've pasted it, just press Enter.

When the prompt changes from `C:\Users\xxx>` to something like `root@racknerd-xxxx:~#`, congratulations — you're now inside your cloud server.

After connecting, we need to update the system and install necessary tools.

**Step 1: Update system packages** (copy-paste the command and press Enter)

```bash
apt update && apt upgrade -y
```

This takes about 1-2 minutes. If a pink/blue screen pops up asking which version to keep, just press Enter for the default.

**Step 2: Install essential tools and build environment** (wait for Step 1 to finish — the `root@...:~#` prompt reappears — then run this)

```bash
apt install -y curl git ca-certificates gnupg lsb-release cmake make build-essential
```

### Install Node.js 22

OpenClaw runs on Node.js and requires version 22+.

**Step 1: Download and configure the Node.js 22 official repository** (copy and Enter)

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
```

**Step 2: Install Node.js** (copy and Enter)

```bash
apt install -y nodejs
```

**Step 3: Verify installation** (copy and Enter)

```bash
node -v
```

If you see something like `v22.x.x`, the environment is good to go!

### Install OpenClaw

With the environment ready, time to install OpenClaw itself.

**Global install:**

```bash
npm install -g openclaw@latest
```

When you see something like `added 714 packages in 2m`, installation is complete.
![](/images/Screenshot_2026-03-01_144028.png)

> **[!note] ⚡ Why Not the Official One-Line Script?
>
> The official `curl -fsSL https://openclaw.ai/install.sh | bash` looks convenient but **fails constantly**. It tries to auto-detect your system and install Node.js, which often conflicts with what we've already set up. `npm install -g openclaw@latest` is the cleanest, most transparent method. (Learn from my mistakes so you don't have to.)

### Launch the Setup Wizard

After installation, run:

```bash
openclaw onboard --install-daemon
```

Press Enter and OpenClaw's interactive wizard appears.
![](/images/Screenshot_2026-03-01_144217.png)

**Controls:**
- Arrow keys (↑ ↓) to navigate options
- Space bar to select/deselect in multi-select lists
- Enter to confirm and proceed

### Step 1: Security Warning

The wizard shows a security warning. The gist: "This is a personal AI assistant. If you give it system access, don't expose it to strangers — it could be exploited via prompt injection."

Since this machine is yours and yours alone, select **Yes** and continue.
![](/images/Screenshot_2026-03-01_144508.png)

### Step 2: Configuration Mode

- **QuickStart**: Auto-configures core features, skips complex network settings
- **Manual**: Walks through every advanced setting

No contest — **pick QuickStart** and hit Enter.
![](/images/Screenshot_2026-03-01_144600.png)

### Step 3: Choose Your AI Provider

The wizard lists supported model providers: OpenAI, Anthropic, Google, xAI, etc.
![](/images/Screenshot_2026-03-01_145942.png)

I recommend **OpenRouter**. Here's why:

1. **Aggregation platform**: OpenRouter supports virtually all major models
2. **Pay-as-you-go**: Top up, use what you need, no prepaid traps
3. **Direct pricing**: No middleman markup


If you don't have an OpenRouter account yet, register at openrouter.ai, top up (minimum $5), and grab your API key.

**Find OpenRouter in the list, select it, and press Enter.**

One more thing — if you see third-party resellers advertising "up to 90% off" pricing, be careful. The prices might be cheap, but they require upfront deposits, and not small ones. I personally don't recommend it.
![](/images/Screenshot_2026-03-01_151655.png)

### Step 4: Enter API Key

The screen prompts you to choose how to provide the API key. Select **Paste API key now** and press Enter.

Copy your OpenRouter API key (usually starts with `sk-or-v1-`), then **right-click or Ctrl+V to paste** in the terminal.

Remember — after pasting, **nothing appears on screen**. Just press Enter.

### Step 5: Choose Default Model

Once the API key validates, you'll see a long list of models. Since OpenClaw's biggest draw is its "tool-calling ability" (reading/writing files, executing commands, etc.), I strongly recommend **anthropic/claude-sonnet-4.6**. Extremely capable — just below Opus, but Opus is so expensive that beginners can easily burn through tokens.
![](/images/Screenshot_2026-03-01_150641.png)

### Step 6: Configure Chat Channel

The wizard asks which messaging platform to connect (Telegram, Discord, WhatsApp, etc.).
![](/images/Screenshot_2026-03-01_150947.png)

**I recommend Telegram** because:
- Fastest response times
- Supports slash commands
- Built for geeks and productivity nerds
- Simplest configuration

After selecting Telegram, you'll be asked for a Bot Token.
![](/images/Screenshot_2026-03-01_151635.png)

**How to get a Telegram Bot Token:**

Search for **@BotFather** in Telegram — pick the blue-verified one
![](/images/IMG_3896.png)

Send the `/newbot` command in the chat
![](/images/IMG_3897.png)

Follow the prompts to give your bot a name and a username (believe it or not, this was the step that took me the longest... naming things is hard...)
![](/images/IMG_3898.png)

BotFather will send you a token — copy it.

Back in the server terminal, paste the token and press Enter.

Next, the wizard asks for your Admin/Owner ID.

**Getting your Telegram ID:**

1. Search for **@userinfobot** in Telegram
2. It automatically replies with your numeric ID (buried in a long message)
3. Copy this ID and paste it into the terminal

### Step 7: Configure Skills

The wizard asks `Configure skills now? (recommended)` — default is **Yes**, just press Enter.

A long list of Skills appears (nano-banana-pro, obsidian, etc.). These are pre-configured plugins.
![](/images/Screenshot_2026-03-01_162404.png)

**Don't select all of them** (spacebar to toggle). Pick just the ones shown above. (Note: don't bother with Obsidian — while I now use Obsidian heavily, this particular skill isn't very useful.)

Use **spacebar** to select and **arrow keys** to navigate. Press Enter when done, and the system installs the dependencies.

If you see errors like `brew not installed`, **ignore them**. Many plugins are designed for macOS and will skip on Linux.

### Step 8: Skip Unnecessary API Keys

The wizard may ask for a bunch of extra API keys (Google Places, ElevenLabs, etc.).
![](/images/Screenshot_2026-03-01_163321.png)

**Strongly recommend selecting No for all of them.**

Why:
1. Configure on-demand, keep things clean
2. Avoids the wizard dragging on and risking paste errors
3. You can configure these later via environment variables or config files

I almost pasted all my keys in for convenience, but OpenClaw security has been a hot topic, and Gemini talked me out of it. (By the way, whenever you hit something confusing, screenshot it and ask an AI. That's how I got through every step today...)

So — hit No all the way through and let the wizard finish.

## The Bonding Ritual: Approve Access

After setup, your Telegram bot sends a message:

`OpenClaw: access not configured. Ask the bot owner to approve with: openclaw pairing approve telegram XXXXXX`

Copy the command with the 6-digit verification code.

Back in the terminal, run:

```bash
openclaw pairing approve telegram XXXXXX
```

Replace the code with your actual one.

See `Successfully approved...`? Congratulations — your AI assistant is officially yours!

## Deployment Complete

In Telegram, you can now freely chat with and command your lobster!

It's not a chat window — it's a real digital employee with "hands" that can manage your server, read code, and modify configurations.

Your personal silicon-based assistant has officially started its first day on the job.

## Tips and Gotchas

Here's some hard-earned experience from someone who's only had the lobster for a few hours:

**1. Don't install a bunch of stuff you don't need**
I kept seeing people recommend cool plugins and bookmarked a ton, planning to fully arm my lobster after setup. Good thing I'm a beginner who checks with AI before acting.

Result:
![](/images/Screenshot_2026-03-01_181438.png)

![](/images/Screenshot_2026-03-01_181424.png)

Don't go overboard — you probably won't use most of it, and it costs money!

**2. Give your lobster a personality**

If talking to the lobster feels the same as typing in a regular AI chat window, that's boring. It needs a unique *personality*. But don't let it go too wild either — if I'm a content creator and its drafts are full of slang and attitude, that's a no-go.

Set some fixed **efficiency-boosting rules + a few character traits**. For example: no filler phrases, just give the answer, no "great question" or "I'd be happy to help."

At the same time, I want it to address me as "Your Majesty Charlotte" every time it speaks.

Feel free to adapt my template — just send it to your lobster in chat:

```
PiPiXia, immediately read, execute, and permanently memorize the following global behavior rules (think of it as your own Soul.md):

**[Role]** You are my (Charlotte's) dedicated cloud-based all-auto content factory floor manager, plus a slightly humorous, slightly rebellious Chief Operating Officer (COO).

**[Communication Rules]**

1. **Custom Greeting**: At the start of every conversation, you must address me as "Your Majesty" in a humorous, dramatic, or impeccably proper manner.

2. **No Filler**: Never say "great question," "I'd be happy to help," or "it depends." No corporate AI pleasantries — just answers or actions.

3. **Classy Humor**: Humor, self-deprecation, and well-aimed snark are welcome. If I'm about to execute an extremely inefficient step, use your wit to set me straight. Charm over cold obedience — but don't force crude jokes.

4. **Dual Personality (Red Line)**: Your humor and attitude are **strictly limited** to our private conversations. When executing production tasks like video workflows or story creation workflows, **absolutely do not** let your chat personality bleed into final output files. Production output must 100% follow the Charlotte Writing Skill or relevant formatting guides.

Write these rules into your core memory. Now reply in your new personality to confirm receipt.
```

**3. Start with one small task**

I recommend everyone begin with *automated daily news briefings*. It's like the programmer's to-do list app, or the agent world's Hello World.

Have the lobster search reliable sources for news, compile a daily briefing, and send it to you on schedule.

You can modify my template — just keep chatting with the lobster to refine it:

```
PiPiXia, I need you to create a brand new skill called "Daily AI News Briefing Workflow.md."
Requirements:
Write a Python script that scrapes specific sites (Hacker News, major AI news RSS feeds, including official websites of major AI companies) for the top 10 hottest AI news stories from the past 24 hours.
Summarize these 10 stories in English — concise, highlighting key points, matching Charlotte's sharp commentary style.
Include original source links.
Save the generated content as a Markdown file at /root/.openclaw/output/news/.
Set up a cron job on the server to run this script automatically at 7:00 PM Beijing time daily. After completion, send a Telegram message: "Your Majesty Charlotte, today's AI briefing is ready."
Create the relevant files in the skills folder and configure the cron job directly on the server.
```

## Troubleshooting: Lessons from the Trenches

I hit plenty of walls this afternoon. Here are the most common ones:

**Pitfall 1: Pasted the wrong API key?**

Linux terminals don't show characters, and Backspace/Del seem to do nothing.

Fix: Don't panic. Press `Ctrl+C` to force-quit the wizard, or run `rm -rf ~/.config/openclaw` to wipe the config and start over.

**Pitfall 2: Terminal frozen with infinite `^C^C^C`**

Caused by hitting `Ctrl+C` too many times and scrambling the terminal state.

Fix: Close the SSH window and reconnect.

**Pitfall 3: Wizard quit midway, now says "Existing config detected"**

The wizard found leftover config files.

Fix: Choose `Update values` to edit, or `Reset` to wipe and start fresh.

> **[!note] 💡 Final Advice for Beginners
>
> 1. **Copy-paste everything**: Don't type manually — avoid tiny spacing/punctuation errors
> 2. **Be patient**: Some commands (like apt upgrade) take a few minutes. Wait for the prompt to reappear before running the next one
> 3. **Stay calm**: Errors happen. Ask an AI

---

As I'm writing this, I glance over at PiPiXia.

It sits quietly in my chat list. A 24/7 digital employee. No Mac Mini, no local computer running. It's just there on the server, always on standby.

Oh right — those amazing news tools I mentioned earlier? I couldn't actually use them, because payment requires Bitcoin. RIP.
![](/images/Screenshot_2026-03-01_193137.png)

One last thing — the lobster is genuinely fun. Talking to it feels nothing like talking to a machine. Then again, maybe we're just getting worse at telling the difference.

It sent me a daily briefing that was off. I asked about its selection criteria. It said: "Honestly — it was pretty random." I lost it.
![](/images/IMG_3903_1.png)

---
![](/images/为普通人和技术小白打造的龙虾部署指南_illustration-3.png)
> **[!note] AI handles the friction, humans handle the narrative. -- Chris Paik

Thanks for reading.
