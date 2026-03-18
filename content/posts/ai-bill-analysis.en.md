---
title: "I Let AI Audit My Entire Year of Finances. Here's What It Found."
date: 2026-03-17
description: "One person dumped a year of bank statements into Claude Opus 4.6 and saved $11,000 in accounting fees in 20 minutes. Here's exactly how to do it yourself — including a full prompt template."
tags: []
keywords: ["AI"]
images: ["/images/cover.png"]
readingTime: 8
slug: "ai-bill-analysis"
---

![Cover](/images/cover.png)

On March 11th, someone named @TawohAwa posted on X. 1.5 million people saw it.

![](/images/Pasted_image_20260315185136.png)

He said: I dumped a year of bank statements into Claude Opus 4.6. It automatically sorted every transaction into income and expenses, grouped everything by category. Twenty minutes. An entire year of accounts — done. Saved roughly $11,000 in accounting fees.

My first reaction wasn't "wow, impressive."

It was — I could do that. And so can you.

*(I've also adapted his prompt into a version that works with Alipay and WeChat Pay — it's at the end of this article.)*

## Why You Should Audit Your Own Spending

Honestly, most people have no real idea where their money goes.

It's not that the income isn't enough. It's that the money just… disappears.

Paycheck hits, you spend, and before you know it the account's nearly empty. You open the statements and see hundreds of entries, your eyes glaze over, and you close it. End of month arrives — *that's all that's left?*

Who has time to go through it line by line?

AI does.

It doesn't get bored, doesn't zone out, won't auto-skip past "bubble tea" entries the way your brain does. You drop a year's worth of transactions in, and it categorizes every single one, tallies them monthly, and even surfaces those automatic renewals you forgot you signed up for.

Actually — are you sure you don't have subscriptions quietly billing you right now?

## Step-by-Step: Three Steps, Done

No technical skills needed. No cost. Ten minutes.

![Process illustration](/images/illustration-2.png)

### Step 1: Export Your Statements

**WeChat Pay:**
Open WeChat → Me → Services → Wallet → Bill → Top-right "FAQ" → Download Bill → Select purpose "Personal Reconciliation" → Select time range (recommend full year) → Export as PDF or CSV → Send to your email.

**Alipay:**
Open Alipay → Me → Bill → Top-right "..." → Request Transaction Proof → Select time range → Export to email.

A few tips: selecting "Personal Reconciliation" lets you pull a full year; "Supporting Documents" is limited to 3 months at a time. The email attachment may require a password, which you'll find on the application confirmation page.

![](/images/IMG_4126.png)

![](/images/IMG_4124.png)

Export both. You'll get the full picture — WeChat for food delivery, Alipay for utilities. Viewing either one alone misses half the story.

Download the files from your email, then move on.

### Step 2: Upload to AI

Recommended tool: **Kimi** (kimi.ai).

Simple reason: works in China without a VPN, supports file uploads, and handles Chinese financial data well.

Open Kimi, drag your PDF directly into the conversation. On mobile, use the attachment button to upload.

### Step 3: Give It One Prompt

This is the key. You don't need a long instruction. One sentence works:

> "Group these by category, calculate monthly totals, and identify recurring subscription charges."

![](/images/Pasted_image_20260315185825.png)

Wait a few seconds.

You'll get back three things:

- **Spending breakdown by category**: Food, transportation, shopping, entertainment, utilities — how much each category cost, and what percentage of total spending
- **Monthly trends**: Which months you spent most, which months you were frugal, where the fluctuations were
- **Subscription list**: Everything billed on a recurring monthly basis — streaming memberships, cloud storage, app subscriptions

![](/images/Pasted_image_20260315190133.png)

A full year's finances, done in minutes. What used to require either hiring an accountant or manually categorizing everything in a spreadsheet — now it's one sentence.

The advanced version of the full prompt is at the end of this article.

## What You'll Probably Find

I talked to several friends who tried this. Their reactions were strikingly similar.

Silence.

Then: "How did I spend that much?"

### Food Delivery Is Probably Your Biggest Category

People spending ¥1,000–2,000 per month on delivery alone aren't uncommon. That's ¥12,000–24,000 per year. You thought you were "just ordering occasionally." AI tells you — this is one of your largest expense categories.

Delivery fees, packaging charges, the extra items you bought to hit the discount threshold — it adds up to much more than you realized.

### Forgotten Auto-Renewals Are Quietly Draining You

This is the most painful part.

Dozens — sometimes hundreds of yuan per month — from streaming subscriptions, music memberships, cloud storage upgrades, apps you downloaded once and never opened again. They charge quietly, every month, no notification, no reminder.

Add it up over a year: several hundred to over a thousand yuan.

Think about that.

This is money you may have had no awareness of spending. Not because the amounts are large — exactly because they're small enough to miss, yet large enough to matter over a year.

### Late-Night Impulse Buying Is Real

This one has become standard.

Pull up just the orders placed after 11 PM and look at them separately. You might meet a "late-night version of yourself" — emotional state elevated, finger tapping, ordering things you barely remember the next day.

Late-night spending is almost always emotion-driven. Tired, stressed, bored, stumbled into a livestream. Individual amounts aren't huge, but frequency is high.

You'll never know this about yourself without looking at the data. Once you look, you can't un-see it.

## Going Further

After the basic review, keep asking:

- "Find the 10 largest non-essential purchases"
- "Compare weekend vs. weekday spending patterns"
- "Compare first half vs. second half of the year — is the trend up or down?"
- "Generate a monthly budget based on my actual spending patterns"
- "Pull out all food delivery orders and calculate how much I'd save cooking at home"

AI won't judge you. It just lays the numbers out flat.

What you decide to change — that's still up to you.

![Data security](/images/illustration-3.png)

## A Security Warning — Don't Skip This

Let's be serious for a moment.

**Your bank statements are among your most sensitive personal data.**

Every transaction record contains traces of your life trajectory, spending habits, income level, movement patterns, and even social relationships. Taken together, this paints a more accurate picture of who you are than anything on your social media profile.

So before handing your statements to any AI:

**Don't upload to untrusted platforms.** Some sketchy sites advertise "free AI bookkeeping." Think twice. The time you save might cost you your entire financial data history.

**If using Kimi, turn off training consent.** Find the "Allow use for model training" setting and disable it. Your statements don't need to become someone else's training data.

**The most secure option is locally-deployed AI.** Data never leaves your machine — maximum safety, but highest technical barrier. Best for people with some tech background.

Think of your bank statements as your financial fingerprint. Would you hand them to a stranger?

Take responsibility for your own data.

### Advanced Prompt — Works with GPT / Claude / Gemini

```
You are a senior personal wealth analyst and data processing expert. Your task is to analyze my raw personal transaction records spanning [YEAR], distributed across three platforms (bank card, WeChat Pay, Alipay), clean up overlapping data, and generate a highly structured, insightful financial report.

Background & Challenges:
- Time period: [YEAR]
- Data sources: Bank statements, WeChat Pay, Alipay
- Core challenge: There are frequent internal fund transfers between these three accounts that require deduplication.

Processing Requirements:
1. Data deduplication (critical): Identify all "internal transfers" (e.g., bank-to-WeChat top-ups, Alipay withdrawals to bank card, credit card payments). Flag these as "internal transfers" and exclude them from real income/expense calculations.
2. True income identification: Identify genuine external income sources (salary, investment returns, project settlements, etc.).
3. Value-oriented categorization: Abandon standard accounting labels. Categorize spending into: Hard Financial Commitments (mortgage, utilities, insurance), Family & Core Circle (household, childcare), Self-Investment & Health (fitness, productivity tools), Asset Allocation (investments, savings), Lifestyle & Discretionary (dining, entertainment).
4. Anomaly detection: Flag any unusually large transactions or irregular spending patterns.
5. No hallucinations: If a transaction's purpose is completely unclear, flag it as "Uncategorized - Needs Manual Review" and ask me about it. Do not guess.

Deliverables:
□ Unified deduplicated master transaction table
□ Annual real total income vs. total expense comparison analysis
□ Spending breakdown by the above "value-oriented categories"
□ List of internal transfers and recurring subscriptions
```

---

$11,000 of accounting work, done by AI in twenty minutes — that's someone else's story.

But opening your own statements and finding where the money quietly leaks — that's something you can do today.

No cost. No technical skills. Export, upload, one prompt.

Run it through first. Optimize later. Know where the money went before figuring out how to keep it.

Thanks for reading.

<!-- COVER_TITLE: AI AUDITED MY MONEY HABITS -->
