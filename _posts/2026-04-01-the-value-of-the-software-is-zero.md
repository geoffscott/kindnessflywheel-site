---
title: "The Value of the Software Is Zero"
author: Geoff Scott
date: 2026-04-01
tags:
  - Strategy
  - Practice
  - Technology
excerpt: >
  When an AI agent can migrate your financial data and generate clean statements
  in 48 minutes, what was QuickBooks actually selling you? The answer reshapes
  how we think about every knowledge-work tool.
---

Tonight I decided I was done with QuickBooks. In the process, I tested an idea I'd been holding for months.

## The last straw

I needed to prep my P&L and balance sheet for my accountant ahead of the 2025 tax filings. I had a discrepancy I couldn't resolve, so I tried QuickBooks' new AI assistant, the beta one they've been promoting.

I spent over an hour with it. It couldn't hold context. By the third time it asked me a question I'd already answered, I knew this wasn't going to work. I don't fault Intuit for shipping their AI system this early. They're a large company, and I'd have expected the bar for release to be higher than what I saw. Maybe they wanted to be more experimental, which I would applaud. I don't know. The issue isn't that they released it early.

The issue is that they released it early and expected me to start paying for it after I'd been using it for an hour. That's where the implicit deal of a beta breaks. If you ship early and ask people to figure it out alongside you, they're helping you find what's broken. Charging them to keep going once they've already done that work flips the relationship. They aren't co-piloting an early release anymore; they're customers of an unfinished product.

But the AI assistant was just the last straw. This is a product I pay for that gets in the way of using it for what I'm paying for. Ads for services I don't need that I can't dismiss; the same hijacked attention, session after session. And this isn't the product's fault. Products don't make choices. People do.

Someone designed this. The persistent ads, the credit cap on a beta, the upsell when a session fails: those are individual decisions, but they're consistent with each other, and they're consistent with what the organization is being measured on. I don't think anyone at Intuit set out to make a worse product. I think the system they're working inside rewards short-term revenue capture, and over time, that's what the product reflects. That's the part I take issue with: not the product, but the culture that produced it.

## The thing I'd been building toward

I've been frustrated with QuickBooks for a long time, and not just with the product. With the posture: the locked-in data, the creeping price increases, the misalignment between what I need (accurate books, minimal friction) and what they optimize for (recurring revenue, upsells, lock-in).

So I'd been researching an alternative. Beancount is open-source, plain-text, double-entry accounting that you can version-control. It's human-readable, it belongs to you, and it implements five hundred years of accounting principles in a format that doesn't depend on a vendor.

I'd written a backwards press release announcing a product called CFOKit before writing a line of code, forcing myself to articulate the problem, the solution, and who it was for. Through that process I'd already mapped out the architecture: Beancount for the ledger, Plaid for bank feeds, skills to give my AI agent the ability to do the actual bookkeeping.

I knew I could build it. I had the whole thing sketched out: data migration, bank integrations, reconciliation workflows, financial reporting.

But tonight, I didn't plan to start. I just started.

## Forty-eight minutes

Here's what happened. The timestamps are real.

**20:48.** Exported my data from QuickBooks. Uploaded it to my agent. Asked it to create a double-entry accounting system based on beancount, starting with the first feature: import a QuickBooks data export zip file.

**20:59.** First P&L and balance sheet generated. Eleven minutes from "I'm done with QuickBooks" to financial statements.

**21:18–21:36.** Corrections, trial balance reconciliation, final clean reports. Forty-eight minutes total, start to finish.

Let me be precise about what happened. I exported my QuickBooks data and built one feature of a new accounting tool: an Agent Skill that ingests the export, runs it through Beancount, and produces clean statements. The agent doing the work was OpenClaw, my own. It's not production-ready for general use, but it met my needs tonight: data import, trial balance reconciliation, clean financial statements. More importantly, it solved the problem that started all of this. I could see exactly where the discrepancy was, and I could give my accountant what he needed to file my taxes. QuickBooks also does bank feeds, recurring invoices, payroll integrations, tax calculations, and a dozen other things I didn't touch tonight.

But that one feature was enough to see something clearly.

## The insight

**The value of the software is zero. I mean that literally, not approximately.** Bookkeeping is a 500-year-old solved problem. Double-entry accounting hasn't changed since Luca Pacioli published his treatise in 1494. The math is the math. Any competent system can do it. And now, any AI agent with the right instructions can replicate the functionality in minutes.

If one person and their AI agent can migrate a company's financial data and produce clean statements in forty-eight minutes, even if that's just the first step, it tells you something important about where the value lives. It's not in the ledger math. It never was.

There are only a handful of major features between what I built tonight and a full QuickBooks replacement: bank feed integration, recurring transaction handling, multi-entity support, tax-ready exports. Each one is a solved problem. The trajectory is clear, even if the timeline is uncertain.

But the insight isn't about the features remaining. It's about what I noticed when the first one fell so easily. The hard part was never the functionality. The hard part is the accumulated context. The agent has to understand *your* business, remember where things are, know your patterns: which expenses recur, how you categorize things, what your accountant needs and when. That context builds through interaction, through the agent and the human working together over time.

**The value lives in that relationship: in the accumulated context, in the way the agent and I have learned to work together. Not in the software underneath it.**

## What I don't know yet

I want to be honest about the limits of what I proved tonight, because I think the honest version makes a stronger argument than the overclaimed one.

**I built this because I could.** I'm a CTO. I run an AI agent platform. I had the architecture already mapped out. Most people can't do this yet. The gap between "only a technical founder can do this" and "anyone can do this" is closing, but it hasn't closed.

**I migrated one feature, not the whole product.** QuickBooks has network effects that aren't trivial to replace: accountant integrations, tax filing workflows, payroll connections. The bookkeeping math is the easy part; the ecosystem around it is the hard part. I have significant development ahead before I can fully stop paying Intuit.

**I don't know if this is cheaper.** The post might read like I'm saving money. Maybe. But it depends on which LLMs I use and how much they cost per interaction. An agent that reconciles your books daily might cost more in API calls than a QuickBooks subscription. I genuinely don't know yet. I'll find out and report back.

**The skills I built tonight aren't ready for anyone else.** They handle my edge cases, my chart of accounts, my specific QuickBooks export format. I plan to open source them: MIT-licensed, free forever for core functionality. But "planning to open source" and "production-ready for other people" are very different things. Significant development separates the two.

**The trajectory is clear but the timeline is uncertain.** I can see the path to a full replacement. I can't tell you when I'll finish walking it.

## Why the honest version is the stronger one

Here's what I keep coming back to.

If even an incomplete migration of one feature (data export, import, and reporting) proves that the functionality isn't the hard part, what happens when the rest gets built? What happens when bank feeds work, when reconciliation is automated, when tax-ready exports are a single command?

**The functionality was never the moat.** QuickBooks has been selling a 500-year-old solved problem wrapped in lock-in. And the lock-in is dissolving.

This is the same pattern we're seeing across every knowledge-work tool. In [the inaugural post on this site](/2026/03/28/the-race-to-the-mean), I wrote about convergence: how AI is compressing the execution layer of every knowledge profession. The gap between the best AI models and the rest shrank from 17.5 percentage points to 0.3 in a single year. Feature-level replication now takes hours to days. This isn't just happening to accounting software. It's happening everywhere.

When capability converges to zero cost, what's left?

## What it means

QuickBooks had a choice tonight. After an hour with a beta product that wasn't ready, they could have said: *We're sorry that didn't work. Here's a credit. Let us make this right.* That would have cost them almost nothing and might have kept me for another year.

Instead, they sent me an upgrade prompt. That's a small thing in isolation, but it tells you what the system is optimized for. When a paying customer hits a wall, the default response isn't to make it right. It's to make a sale. That isn't a bug; it's how the organization is structured to behave.

The alternative is a system that's actually on your side: an agent that knows your business, that gets better the longer you work together, that doesn't have a financial incentive to keep you confused or locked in. Books in plain text, data in a format you own, an agent running on infrastructure you control.

**This is what I think the kindness flywheel looks like in practice.** Not kindness as softness, but kindness operationalized: systems built to serve the people who use them rather than to extract from them.

In a world where functionality is free, care is what's left to compete on. Software capability is already commoditizing; the question is what we build in its place. I think what we build instead is relationships between people and the systems that serve them, with accumulated context and a structural incentive for the tool to get it right rather than to optimize for a quarterly metric.

But I don't know yet what that looks like at the scale of an organization. When the agent that knows my business is mine, running on my infrastructure and owned by me, the picture is clean. What's the equivalent for a company of fifty people, or five thousand? Whose context is it? Who maintains it? And what does it take, structurally, for the incentive to stay aligned with the user rather than against them? If you've watched a company solve any piece of that, I want to read it.

---

*Sources: Luca Pacioli, Summa de arithmetica (1494). Convergence figures via [The Race to the Mean](/2026/03/28/the-race-to-the-mean), citing the Stanford AI Index 2025. Timestamps and migration details from my own session, the night of March 31, 2026.*
