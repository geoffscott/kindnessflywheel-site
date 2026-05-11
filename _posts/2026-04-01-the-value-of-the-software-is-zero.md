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

Tonight I decided I was done with QuickBooks. By the end of the night, I'd confirmed something I'd been working through for weeks.

## The last straw

I needed to send my P&L and balance sheet to my accountant to prepare my 2025 tax filings. I had a discrepancy I couldn't resolve, so I tried Intuit's new AI assistant, which was in beta.

I spent over an hour with it. It couldn't hold context. By the third time it asked me a question I'd already answered, I knew this wasn't going to work. I don't fault Intuit for shipping their AI system this early. They're a large company, and I'd have expected the bar for release to be higher than what I saw. Maybe they wanted to be more experimental, which I would applaud. I don't know. The issue isn't that they released it early.

The issue is that Intuit released it early and expected me to start paying for it after I'd been using it for an hour. That's where the implicit deal of a beta breaks. If you ship early and ask people to figure it out alongside you, those people are helping you refine the product for commercial readiness. Charging them to keep going once they've done that work flips the relationship. They aren't co-piloting an early release anymore; they're customers of an unfinished product.

But the AI assistant was just the last straw. The product itself works against me. Ads for services I don't need keep returning no matter how many times I dismiss them, despite my paying for the product. Session after session, my attention gets hijacked the same way. None of this is accidental.

Someone designed this. The persistent ads, the usage cap on a beta, the upsell when a session fails: those are individual decisions, but they're consistent with each other, and they're consistent with what the organization is being measured on. I don't think anyone at Intuit set out to make a worse product. I think the system they're working inside rewards short-term revenue capture, and over time, that's what the product reflects. That's the part I take issue with: not the product, but the culture that produced it.

## What I'd been designing

I've been frustrated with QuickBooks for a long time, and not just with the product. With the posture: the persistent upsells, the creeping price increases, the misalignment between what I need (accurate books, minimal friction) and what the company optimizes for (revenue extraction).

So I'd been researching an alternative. Beancount is open-source, plain-text, double-entry accounting that you can version-control. It's human-readable, it belongs to you, and it implements five hundred years of accounting principles in a format that doesn't depend on a vendor.

I'd designed the product before writing a line of code, working through the problem, the solution, and who it was for. The shape that emerged was different from QuickBooks: not an accounting package, but an autonomous bookkeeper agent that uses one. Beancount served as the ledger, Plaid handled bank feeds, and Agent Skills gave the AI the abilities a bookkeeper actually exercises: reconciling transactions, categorizing them, and producing reports.

I knew I could build it.

But tonight, I started, without planning to.

## Forty-eight minutes

Here's what happened. The timestamps are real.

**20:48.** Exported my data from QuickBooks. Uploaded it to my agent. Asked it to create a double-entry accounting system based on beancount, starting with the first feature: import a QuickBooks data export zip file.

**20:59.** First P&L and balance sheet generated. Eleven minutes from "I'm done with QuickBooks" to financial statements.

**21:18–21:36.** Corrections, trial balance reconciliation, final clean reports. Forty-eight minutes total, start to finish.

Let me be precise about what happened. I exported my QuickBooks data and gave my OpenClaw agent its first bookkeeping capability: an Agent Skill that reads the export, runs it through Beancount, and produces clean statements. It's not production-ready for general use, but it met my needs tonight: data import, trial balance reconciliation, clean financial statements. More importantly, it solved the problem that started all of this. I could see exactly where the discrepancy was, and I could give my accountant what he needed to file my taxes. QuickBooks also does bank feeds, recurring invoices, payroll integrations, tax calculations, and a dozen other things I didn't touch tonight.

But that one feature was enough to see something clearly.

## The insight

**The value of the software is zero. I mean that literally, not approximately.** Bookkeeping is a 500-year-old solved problem. Double-entry accounting hasn't changed since Luca Pacioli published his treatise in 1494. The math is the math. Any competent system can do it. And now, any AI agent with the right instructions can replicate the functionality in minutes.

If one person and their AI agent can migrate a company's financial data and produce clean statements in forty-eight minutes, even if that's just the first step, the speed itself reveals where the value lives. It's not in the ledger math. It never was. The ledger underneath is a commodity. It has been for centuries. Which one I use barely matters.

There are only a handful of major features between what I built tonight and something I could run my consulting business on: bank feed integration, recurring transaction handling, simple invoicing, tax-ready exports. Each is a solved problem. The same feature set would cover most small businesses, not just mine. I'm not claiming to be on the verge of replacing QuickBooks for a hundred-person company. The narrower claim still stands: the trajectory is clear, even if the timeline is uncertain.

But the insight isn't about the features remaining. It's about what I noticed when the first one fell so easily. The hard part was never the functionality. The hard part is the accumulated context. The agent has to understand *your* business, remember where things are, know your patterns: which expenses recur, how you categorize things, what your accountant needs and when. That context builds through interaction, through the agent and the human working together over time.

**The value lives in that relationship: in the accumulated context, in the way the agent and I have learned to work together. Not in the software underneath it.**

## What I don't know yet

I want to be honest about the limits of what I proved tonight, because I think the honest version makes a stronger argument than the overclaimed one.

**I built this because I could.** I'm a CTO. I run an AI agent platform. I had the architecture already mapped out. Most people can't do this yet. The gap between "only a technical founder can do this" and "anyone can do this" is closing, but it hasn't closed.

**I migrated one feature, not the whole product.** QuickBooks has network effects that aren't trivial to replace: accountant integrations, tax filing workflows, payroll connections. The bookkeeping math is the easy part; the ecosystem around it is the hard part. I have significant development ahead before I can fully stop paying Intuit.

**I don't know if this is cheaper.** The post might read like I'm saving money. Maybe. But it depends on which LLMs I use and how much they cost per interaction. An agent that reconciles your books daily might cost more in API calls than a QuickBooks subscription. I genuinely don't know yet. I'll find out and report back.

**The skills I built tonight aren't ready for anyone else.** They handle my edge cases, my chart of accounts, my specific QuickBooks export format. I plan to open source them: MIT-licensed, free forever for core functionality. But "planning to open source" and "production-ready for other people" are very different things. Significant development separates the two.

**The trajectory is clear but the timeline is uncertain.** I can see the path to running my consulting business on this. I can't tell you when I'll finish walking it.

## Why the honest version is the stronger one

Here's what I keep coming back to.

If even an incomplete migration of one feature (data export, import, and reporting) proves that the functionality isn't the hard part, what happens when the rest gets built? What happens when bank feeds work, when reconciliation is automated, when tax-ready exports are a single command?

**The functionality was never the moat.** QuickBooks has been selling a 500-year-old solved problem wrapped in lock-in. And the lock-in is dissolving.

This is the same pattern we're seeing across every knowledge-work tool. In [the inaugural post on this site](/2026/03/28/the-race-to-the-mean), I wrote about convergence: how AI is compressing the execution layer of every knowledge profession. The gap between the best AI models and the rest shrank from 17.5 percentage points to 0.3 in a single year. Feature-level replication now takes hours to days. This isn't just happening to accounting software. It's happening everywhere.

Even the market sees it. Morningstar downgraded Intuit's economic moat from Wide to Narrow in 2025, citing AI disruption risk, and the stock dropped roughly 36 percent over the same period on AI-related fears. Venture capital is taking shots at the same opening: Digits has raised around $100M to build what it calls an "autonomous general ledger" aimed directly at QuickBooks, and reported 11x revenue growth in 2024. The argument I'm making is one that institutional analysts and venture capital have already started pricing in.

When capability converges to zero cost, what's left?

## What it means

Intuit had a choice tonight. After an hour with a beta product that wasn't ready, they could have said: *We're sorry that didn't work. Here's a credit. Let us make this right.* That would have cost them almost nothing and might have kept me for another year.

Instead, they sent me an upgrade prompt. That's a small thing in isolation, but it tells you what the system is optimized for. When a paying customer hits a wall, the default response isn't to make it right. It's to make a sale. That isn't a bug; it's how the organization is structured to behave.

And AI doesn't change this. Intuit is shipping AI agents of its own. Four went live inside QuickBooks Online on July 1, 2025, with more on the way. The capability is real. But those agents are running inside the same organization that put a usage cap on a beta and sent me an upgrade prompt when its product failed me. Whatever the agents can do, they will do in service of what the organization is measured on.

The alternative is a system that's actually on your side: an agent that knows your business, that gets better the longer you work together, that doesn't have a financial incentive to keep you confused or locked in. Books in plain text, data in a format you own, an agent running on infrastructure you control.

One detail matters more than it looks. An AI agent that won't let you fully export its memory has its own form of lock-in: the context you've built becomes the thing you can't take with you. Portable memory is what makes "on your side" real. Without it, you've traded the ledger lock-in for a context lock-in, and the new one is harder to see.

**This is what I think the kindness flywheel looks like in practice.** Not kindness as softness, but kindness operationalized: systems built to serve the people who use them rather than to extract from them.

In a world where functionality is free, care is what's left to compete on. Software capability is already commoditizing; the question is what we build in its place. I think what we build instead is relationships between people and the systems that serve them, with accumulated context and a structural incentive for the tool to get it right rather than to optimize for a quarterly result.

But I don't know yet what that looks like at the scale of an organization. When the agent is mine and runs on my infrastructure, the picture is clean. At larger scale, the questions get concrete.

Will Intuit's AI agents serve the user, or be optimized for the same upsell as the rest of the product? Will they let customers export the agent's full memory in plain text? Does the agent layer end up owned by whoever owns the bank account? Ramp, Brex, and Mercury are already doing accounting-adjacent work from the spend side, without calling themselves accounting software. What about the accountant channel? Roughly 600,000 US firms maintain QuickBooks ProAdvisor relationships, and they're the trust layer between small businesses and the tax-filing machinery. Their endorsement may matter more than the ledger underneath.

I don't have answers to any of those. If you've watched a company work on one of them, I'd love to read about it.

---

*Sources: Luca Pacioli, Summa de arithmetica (1494). Convergence figures via [The Race to the Mean](/2026/03/28/the-race-to-the-mean), citing the Stanford AI Index 2025. Morningstar 2025 (Intuit economic moat downgrade). CPA Practice Advisor and Intuit Investor Relations, July 2025 (Intuit AI agents launch). Yahoo Finance, 2025 (Intuit stock performance). Digits funding and growth figures via GlobeNewswire and company materials, 2024–2025. Intuit QuickBooks ProAdvisor program (accountant-channel scale). Timestamps and migration details from my own session, the night of March 31, 2026.*
