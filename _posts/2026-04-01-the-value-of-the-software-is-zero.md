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

Tonight I decided that I was done with QuickBooks. By the end of the night, I'd confirmed something I'd been thinking about for weeks.

## The last straw

I needed to send my P&L and balance sheet to my accountant to prepare my 2025 tax filings. I had a discrepancy I couldn't resolve, so I tried Intuit's new AI assistant, which was offered at exactly the moment that I needed help.

The assistant was in beta, so I expected some fit and finish issues. Over the next hour, it lost track of our conversation at least three times, asking me basic contextual questions that I had already answered; and then it told me that my free trial had run out and asked me if I wanted to pay to continue the conversation. This was the first indication that the new AI assistant was not a new feature of my QuickBooks subscription but a metered trial of a new product, offered inside of the product that I pay to use. The placement of the offer was perfect. The roughness of the product was typical of AI products that are early in their development. Choosing to ask customers to pay for a product that wasn't yet capable of fulfilling its basic purpose was a business decision.

But the AI assistant was just the last straw. I find the Quickbooks user experience in general to be overly complex for the things that I need to do most often: send invoices, post transactions, and run basic reports. This generally poor UX is made worse by persistent advertisements for other Intuit products and services that I don't need and aren't relevant to my business. I have to dismiss two of these ads every time I go to manage my bank transactions in order to regain the full use of my screen. I searched for a global setting to turn off the ads and found one mentioned in a user forum; but Quickbooks seems to ignore it and keeps on showing me the same ads for the same products, no matter how many times I dismiss them. None of this is accidental.

These product design decisions are very consistent with each other, and they're consistent with what the organization is being measured on. I don't think anyone at Intuit intended to design a less usable product. I think that the organization inside of which they're working rewards short-term revenue capture, and over time, that's what the product reflects. That's the part I take issue with: not the product, but the culture that produced it. The FTC reached a related conclusion in January 2024, when it ruled Intuit had engaged in deceptive advertising and barred the company from advertising services as "free" without clear disclosure.

## What I'd been designing

I've been frustrated with QuickBooks for a long time: the poor UX, the persistent cross-sells, the price increases, the misalignment between what I need (accurate books, minimal friction) and what the company optimizes for (revenue extraction).

So I'd been researching an alternative. Beancount is open-source, plain-text, double-entry accounting that you can version-control. It's human-readable, it belongs to you, and it implements five hundred years of accounting principles in a format that doesn't depend on a vendor.

I'd designed the product before writing a line of code, working through the problem, the solution, and who it was for. The shape that emerged was different from QuickBooks: not an accounting package, but an autonomous bookkeeper agent that uses one. Beancount served as the ledger, Plaid handled bank feeds, and Agent Skills gave the AI the abilities a bookkeeper actually exercises: reconciling transactions, categorizing them, and producing reports.

I knew that I could build it and had a strong idea of how I might do so. I hadn't planned to start building it yet, but that's what happened tonight.

## Forty-eight minutes

Here's what happened. The timestamps are real.

20:48. Exported my data from QuickBooks. Uploaded it to my OpenClaw agent. Asked it to create a double-entry accounting system based on beancount, starting with the first feature: import and reconcile a QuickBooks data export zip file.

20:59. First P&L and balance sheet generated. Eleven minutes from "I'm done with QuickBooks" to financial statements.

21:18–21:36. Corrections, trial balance reconciliation, final clean reports. Forty-eight minutes total, start to finish.

Let me be precise about what happened. I exported my QuickBooks data and gave my agent its first bookkeeping capability: an Agent Skill that reads the export, runs it through Beancount, and produces clean statements. It's not production-ready for general use, but it met my needs tonight: data import, trial balance reconciliation, clean financial statements. More importantly, my agent then helped me solve the accounting problem that started all of this. I could see exactly where the discrepancy was, and I could give my accountant what he needed to file my taxes.

Working with my agent to solve my accounting problem was enough to see something clearly.

## The insights

The value of the software is almost zero. Bookkeeping is a 500-year-old solved problem. Double-entry accounting hasn't changed since Luca Pacioli published his treatise in 1494. The requirements couldn't be more clear; and an AI agent with a skilled user and the right requirements can replicate the necessary functionality in a matter of days.

The cost and risk of switching software is also approaching zero. If one person and their AI agent can migrate a small company's financial data and produce clean statements in forty-eight minutes, even if that's just the first step, the speed itself reveals that system implementation risk is no longer the moat that it used to be.

There are only a handful of major features between what I built tonight and something on which I could run my solo consulting business: bank feed integration, recurring transaction handling, simple invoicing, accountant-ready reports. Each is a solved problem. A similar feature set would cover many small businesses, as well as many small non-profits. I'm not claiming to be on the verge of replacing QuickBooks for a restaurant, a small consulting company, or an early stage tech startup yet. But the path is clear, even if the timeline is uncertain.

The value in business software will come from the accumulated context that an agent can build through interaction with skilled users over time and their willingness to be accountable for end user outcomes, whether they are employees of the company that makes the software or end-users of an open-source product. My agent will increasingly understand my business, remembering where things are, knowing my patterns: which clients are new, which expenses recur, how I categorize transactions, what my accountant needs and when. It will proactively recognize anomalies and continuously improve how we work together.

## What I don't know yet

I built this because I could. I'm a CTO and have been running my own businesses for almost 15 years. I'm familiar enough with my accounting needs. My current work includes helping clients develop autonomous AI agents; so I had already designed the architecture for this kind of application. The bar for building something like this is dropping rapidly, but it hasn't dropped to a point where the average small-business owner can vibe-code an accounting system.

The import feature that I built tonight isn't ready for anyone else to use. It handles the chart of accounts, transaction history, and edge cases that it encountered in importing and reconciling my specific QuickBooks data. It needs to learn from importing a lot of other companies' books before it's ready for general use.

I only built one feature, not a whole small business accounting product. Even for my own very basic needs, I still have to implement automated bank transaction feeds and categorization, and invoicing and accounts receivable management before I can stop paying Intuit for Quickbooks.

I don't know if a full-featured agentic bookkeeper will be more cost-effective than a human bookkeeper using a traditional SaaS accounting package. Whether I save money or not depends on many factors including which LLMs I use, how much they cost, how effectively the system manages context windows, and the cost of traditional bookkeeping services and software in general. An agent that reconciles my books every month might cost more in LLM costs than a human bookkeeper using QuickBooks or one of its competitors.

What I do know is that my annual Quickbooks subscription renews in October and I intend to cancel it before then; so stay tuned!

## What it means

If even an incomplete implementation of one feature demonstrates that the functionality isn't the hard part, what happens when bank feeds work, when reconciliation is automated, and when accountant-ready reports get generated with a single prompt? Intuit has been selling a solution to an extremely well-understood problem that's been protected by a moat that is rapidly dissolving.

Morningstar downgraded Intuit's economic moat from Wide to Narrow in 2025, citing AI disruption risk; and the stock dropped roughly 36 percent over the same period on AI-related fears. Venture capital is taking shots at the same opening: Digits raised $100M to build what it calls an "autonomous general ledger" aimed directly at QuickBooks and reported 11x revenue growth in 2024.

Intuit is responding, launching four of its own AI agents for Quickbooks in 2025, with more on the way. I'm confident that Intuit and all of their competitors' agents (including my own) will soon have similar capabilities. But in Intuit's case, those agents are being developed by the same organization that thought that it was a good idea to persistently abuse my limited time, attention, and screen real estate to push products and services that aren't relevant to my business. Whatever their agents offer, they will do in service of what the organization is measured on.

Intuit made a choice. After an hour with a beta product that wasn't ready, they could have allowed me to keep working with it for free until I figured out my accounting problem, used the interaction to improve their product, and then asked if I'd be willing to pay for it. Instead, they asked for payment to continue a clearly unproductive conversation. That's a small choice in isolation, but it indicates how the organization is incentivized to behave.

An alternative is a system that's actually designed to serve customer needs first: an agent that knows your business and gets better the longer you work together, financial data and business context that's stored in an open format that you can easily manage and export, and if you prefer, an agent that runs on infrastructure that you control.

Yes, enabling portable agent memory and context allows customers to easily switch vendors. This is a requirement that customers should demand and CIOs should write into procurement: plain-text exportable memory, full business context, no proprietary formats. If we don't insist on it, natural business incentives will lead vendors to implement various forms of context lock-in, forcing customers to choose between migrating to a better solution and giving up potentially years of business context that may not be documented anywhere else.

This is what the kindness flywheel looks like in practice: organizations that embody radical customer empathy as a business strategy, from individual contributors to management, executive leadership, and investors, delivering products and services that grow shareholder value because they rely on trust that can only be earned by consistently meeting customer needs.

Will Intuit's AI agents serve the user, or be optimized for their quarterly results, like the rest of the product? Will they let customers export their agents' full memory and accumulated business context in plain text? Does the agent layer end up owned by whoever owns the bank account? Ramp, Brex, and Mercury are already doing accounting-adjacent work from the spend side, without calling themselves accounting software.

I don't have answers to any of those. If you've watched a company work on one of them, I'd love to read about it.

---

*Sources: Luca Pacioli, Summa de arithmetica (1494). Morningstar 2025 (Intuit economic moat downgrade). CPA Practice Advisor and Intuit Investor Relations, July 2025 (Intuit AI agents launch). Yahoo Finance, 2025 (Intuit stock performance). Digits funding and growth figures via GlobeNewswire and company materials, 2024–2025. [FTC final order, January 2024](https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-issues-opinion-finding-turbotax-maker-intuit-inc-engaged-deceptive-practices) (Intuit deceptive advertising ruling). Timestamps and migration details from my own session, the night of March 31, 2026.*
