---

title: 'Raised $1 Billion — Yann LeCun Is Betting That LLMs Are a Dead End'
date: '2026-03-11'
summary: 'Turing Award winner Yann LeCun left Meta to found AMI Labs, raised $1 billion, and declared LLMs a dead end. His bet: "World Models" will redefine AI.'
tags: ["AI", "Yann LeCun", "LLM", "World Models", "Startup"]
cover: '/images/cover_lecun-llm-doomed_en.png'
description: 'Turing Award winner Yann LeCun left Meta to found AMI Labs, raised $1 billion, and declared LLMs a dead end. His bet: "World Models" will redefine AI.。'
keywords: ["AI", "Yann LeCun", "LLM", "World Models", "Startup"]
readingTime: 42
faq:
  - q: 'What is the main point of this article about A Turing Award Winner Just Walked Out?'
    a: 'This article provides an in-depth analysis of A Turing Award Winner Just Walked Out, with practical insights and personal experience from an AI content creator.'
images: ["/images/cover_lecun-llm-doomed_en.png"]
---

## A Turing Award Winner Just Walked Out

In November 2025, Yann LeCun officially left Meta.

Twelve years at Meta. Chief AI Scientist. Turing Award winner. Someone like that leaving is news by itself. But what really sent shockwaves through the AI world wasn't that he left — it was what he said on the way out:

> You certainly don't tell a researcher like me what to do.

![](/images/Pasted_image_20260311135711.png)

The backstory: Meta brought in a younger executive, Alexandr Wang, to manage his department. A Turing Award winner, "managed" by a younger guy.

Yeah. You'd be annoyed too.

To be fair, Wang is no slouch himself. Born in '97, dropped out of MIT, co-founded **Scale AI** in 2016 — a company providing AI data labeling and data infrastructure services (what a prescient bet that turned out to be!). By 2021, the company was valued at over **$7 billion**, making Wang one of the youngest self-made billionaires.

Zuckerberg announced in June 2025 that he was acquiring 49% of Scale AI for approximately **$14.3 billion**.
![](/images/Pasted_image_20260311134451.png)

But there's been plenty of gossip about Wang and Meta too. Rumors say he and Zuck don't get along, and that he's basically semi-retired at this point. Zuck even posted photos recently to quash the rumors.
![](/images/Pasted_image_20260311134341.png)

Anyway, that's all background and drama. But LeCun's departure wasn't just about bruised ego. The real rift runs much deeper — you can see it from his public statements and papers: he and Zuckerberg have a fundamental disagreement about the direction of AI.

Zuckerberg wants to go all-in on large language models. LeCun thinks that's a dead end.

## "Auto-Regressive LLMs Are Doomed"

On September 10, 2025, at an NYU Center for Data Science symposium, LeCun put up a slide. The opening line was a five-word verdict:

**"Auto-Regressive LLMs Are Doomed."**

(The actual title was even more... aggressive.)
![](/images/Pasted_image_20260311134911.png)

This wasn't the first time he'd said something like this. I still remember the shock I felt the first time I heard him make this kind of claim.

Many of us — myself included — don't come from a programming or tech background. We just happen to be interested in and passionate about AI. So LLMs — large language models — felt like we'd finally found the yellow brick road. With LLMs and their chat interfaces, we started collaborating with GPT, Doubao, Gemini, and so on.

That's how we got *prompt engineering*, tips on *"how to write good prompts,"* and *structured outputs*.

But what if it was wrong from the start? Can human language actually express the full breadth of what we think and know? Is language overrated? Could communicating with AI through language be a dead end from the very beginning?

Musk has always thought so, which is why he's aggressively pushing Neuralink's brain-computer interface — thoughts outputting directly, bypassing language altogether.

LeCun lays out his logic very clearly:

**First, LLMs don't understand the world.**

LeCun's argument is blunt: the essence of LLMs is "predicting the next token." They learn patterns of language at a statistical level, but they don't understand the physical world, causality, or common sense behind that language.

His famous example: a four-year-old child has processed more sensory data — through vision, touch, and hearing — since birth than all LLM training data combined. Yet that four-year-old already has basic physical world cognition — they know things fall down, they know pushing a ball makes it roll.

And GPT-4? It can't reliably tell you what happens when you flip a cup of water upside down on a table.

**Second, the mathematical trap of token generation.**

LeCun identifies a core mathematical problem: autoregressive models generate one token at a time, and each step carries a probability of error. As the output sequence grows longer, the probability of generating a completely correct answer drops exponentially.

In plain terms — the more it says, the more likely it is to talk nonsense.

This isn't a problem of the model being too small. It's a structural mathematical flaw of the architecture itself.

**Third, LLMs can't plan or reason.**

What does real intelligence require? The ability to predict the consequences of your own actions, to perform multi-step reasoning, to formulate long-term plans.

LeCun says: LLMs fail at all three. What they do is System 1-style fast reaction — like human instinct. But what makes humans truly powerful is System 2 — deliberate, conscious reasoning. LLMs have no System 2.

(Side note: the dual-system concept comes from Daniel Kahneman's classic *Thinking, Fast and Slow* — absolutely one of the most essential books you can read.)

LeCun's closing salvo at the talk:

> IF YOU ARE INTERESTED IN HUMAN-LEVEL AI, DON'T WORK ON LLMs.

All caps. No hedging.

## One Man Against the Entire Industry

Let me put this in perspective.

In 2025, virtually every major AI company — OpenAI, Google DeepMind, Anthropic, xAI — is all-in on large language models. Hundreds of billions of dollars in capital chasing bigger models, more compute, longer context windows. The industry consensus: Scaling Law has no ceiling; as long as models are big enough and data is plentiful enough, AGI is just ahead.

Then LeCun stands up and says: **You're all wrong.**

This isn't some random person ranting online. This is a Turing Award winner — the AI equivalent of a Nobel laureate — publicly declaring war on the entire industry's roadmap.

![illustration-2](/images/illustration-2_lecun.png)

And he's not just talking. He's been in ongoing public debates with two other godfather-level figures in AI — Geoffrey Hinton and Yoshua Bengio — for years.

**LeCun vs. Hinton: Will AI Destroy Humanity?**

After leaving Google, Hinton became the poster child for AI safety. He believes superintelligent AI could go rogue, could be weaponized, and that humanity must take the threat seriously.

LeCun thinks that's "preposterous" (his actual word). He believes that as long as you embed the right objective functions and guardrails in AI systems, they're safe and controllable. Doomsday rhetoric isn't just unfounded — it hands ammunition to those who want to ban open-source AI.

Interestingly, despite being at loggerheads on risk assessment, they agree on one point: AI needs built-in directives for "obeying humans" and "empathy." Hinton calls it "maternal instinct." LeCun calls it "objective-driven AI."

Different paths, same destination — but plenty of fireworks along the way.

**LeCun vs. OpenAI: Open-Source vs. Closed-Source**

LeCun is the fiercest advocate for open-source AI. He publicly attacks OpenAI's pivot from open to closed, saying "doing research in secret isn't research."

He said: "The research community has mostly stopped paying attention to OpenAI. Because they don't publish papers. They don't share their results."

That's a brutal thing to say. And he's not just talk — during his time at Meta, he spearheaded the open-source release of the Llama model series, putting his money where his mouth is on "AI should belong to everyone."

## AMI Labs: $1 Billion for "World Models"

After leaving Meta, LeCun didn't retire. The industry had been watching his next move closely.

In January 2026, he officially founded Advanced Machine Intelligence Labs — AMI for short. On March 10 — literally **yesterday** — AMI announced a **$1.03 billion** seed round.

$1.03 billion. Seed round.

This is the largest seed round in European startup history. Company valuation: $3.5 billion.

The investor list reads like *the Avengers of AI*: Jeff Bezos' personal fund Bezos Expeditions, NVIDIA, Toyota, Samsung, Temasek, plus Eric Schmidt and Mark Cuban.

> AMI takes its name from the French word "ami," meaning "friend." Headquartered in Paris, with offices in New York, Montreal, and Singapore. CEO is Alexandre LeBrun; LeCun serves as Executive Chairman.

So what's AMI building?

**World Models.**

Not predicting the next word, but understanding the physical world. Not learning from text, but from video, images, and sensor data. Not generating language, but building abstract representations of reality. (Sound familiar? It's basically what Fei-Fei Li has been saying too...)

LeCun has proposed a technical framework for this: **JEPA (Joint Embedding Predictive Architecture)**.

![illustration-3](/images/illustration-3_lecun.png)

## JEPA: Don't Predict Pixels — Predict "Abstractions"

JEPA's core approach is fundamentally different from LLMs.

LLM logic: given a sequence of text, predict the next word.
JEPA logic: given a video clip, predict what happens next — but not by predicting specific pixel changes. Instead, predict changes in *abstract representations*.

This distinction is crucial.

The human brain doesn't understand the world by memorizing every frame. When you see a ball rolling off a table edge, you don't need to precisely predict where every pixel of the ball will be in the next second. You just need to know: the ball will fall.

That's "abstract representation" — ignoring unimportant details, grasping underlying patterns.

Under LeCun's leadership, Meta already open-sourced several JEPA models: I-JEPA (for images), V-JEPA (for video), V-JEPA 2 (improved version). These models don't generate images or text — they learn *how to understand scenes*.

AMI will build on this foundation to construct a truly "general intelligence system." LeCun's timeline: three to five years.

## Prophet or Gambler?

Honestly, I have complicated feelings about LeCun's views.

On one hand, a lot of what he says is logically sound. LLMs do hallucinate, they don't understand the physical world, they can't truly reason. The more you use ChatGPT, the more you feel the gap between its "cleverness" and genuine "understanding" — it doesn't actually comprehend what you're saying, it just gives you a statistically plausible-sounding answer.

On the other hand, this man is unbelievably bold.

Some of the smartest people on the planet — Ilya Sutskever, Sam Altman, Dario Amodei — are all betting on the LLM path. Trillions of dollars in capital support this trajectory. And LeCun stands up alone and says: you're all wrong, and I have a better plan.

This is either historic foresight or the most expensive case of academic stubbornness ever.

I use LLMs every day. Writing this very article, my AI assistant PiPiXia (that's what I named my OpenClaw — it's a lobster) is right here helping me research and organize material. It's built on LLMs, and it genuinely works well.

But I also do feel the limitations LeCun describes —

It can't fully remember what I discussed with it last week (unless I manually write it into a memory file). It doesn't understand the spatial relationship between the coffee cup on my desk and the keyboard next to it. It can't help me plan a truly complex action requiring five-step-ahead prediction.

It's like an incredibly well-read person with zero life experience — knows everything, but hasn't truly experienced any of it.

While I'm at it, I have to mention the project that's been dominating GitHub trending these past few days: MiroFish. A Chinese college senior named BaiFu (real name Guo Hangjiang) vibe-coded a "**next-generation swarm intelligence prediction engine**" in just 10 days. Shanda's Chen Tianqiao already invested **30 million RMB** for commercialization.
![](/images/Pasted_image_20260311141124.png)

My biggest takeaway is "we're both vibe coding but look at this guy," but this kind of prediction engine seems to be hinting at something deeper.

## Final Thoughts

Yann LeCun is 75 years old.

Most Turing Award winners his age are either serving as honorary professors or sitting on advisory boards, occasionally giving keynotes and collecting speaking fees.

He chose to leave Meta, start a company, raise a billion dollars, and bet against the entire industry.

That alone is pretty cool.

Because it means he's not just complaining — he genuinely believes LLMs are a dead end. Believes it enough to stake his reputation, his time, and everything on proving it.

He might be right — World Models might truly be the correct path to AGI.
He might be wrong — LLMs keep evolving, and World Models become a footnote in academic papers.

But regardless, a 75-year-old willing to tear everything down and start over? That deserves respect.

---

The future of AI won't have just one path. And those who dare to walk against everyone else are often the ones who end up changing the world.

Thanks for reading.
