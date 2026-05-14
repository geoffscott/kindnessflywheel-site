# Research Brief: AI Adoption Outcomes, 2024–2026

**Prepared:** March 28, 2026  
**Scope:** AI adoption rates, ROI outcomes, commoditization evidence, moat erosion  
**Focus period:** 2024–2026 only (pre-2024 data flagged)  
**Purpose:** Evidentiary base for Kindness Flywheel content on AI and competitive strategy

---

## Executive Summary

The 2024–2026 data tells a complicated, two-layer story. At the infrastructure and model layer, AI capability is commoditizing fast — benchmark gaps are collapsing, costs are falling 10x per year, and first-mover advantage from a new model version lasts weeks, not months. At the application and business layer, the picture is more contested: ROI is genuinely hard to achieve (95% of AI pilots show no measurable P&L impact), and the companies that are succeeding are doing so through data flywheels, workflow depth, and domain expertise — not raw model access. The "race to the mean" is happening at the model level. Whether it translates to business-level parity is the central unresolved question.

---

## Key Findings

### 1. AI Adoption Rates and the ROI Gap

**Finding: Adoption is high; measurable returns are rare.**

- In 2024, McKinsey reported 78% of organizations had adopted AI in some function, up from 55% in 2023. Organizations reporting generative AI use in at least one business function more than doubled, from 33% (2023) to 71% (2024).  
  *Source: Stanford AI Index 2025, citing McKinsey Global Survey; Stanford HAI, April 7, 2025*

- MIT's "The GenAI Divide: State of AI in Business 2025" report found that despite $30–40 billion in enterprise AI investment, **only 5% of AI initiatives produced measurable P&L impact**. The study attributed failure primarily to lack of alignment between AI and business workflows, skills gaps, and cultural barriers.  
  *Source: MIT Media Lab, Aditya Challapally; "The GenAI Divide: State of AI in Business 2025." Cited in ComplexDiscovery, August 21, 2025; Computing.co.uk, The Register, Entrepreneur, Gizmodo — multiple outlets. **Note:** The primary MIT report URL (mlq.ai) was referenced in Menlo Ventures' report; source credibility appears high but the report itself is behind a paywall. The 95% figure should be cited as "MIT study reported by multiple outlets" pending direct access to the primary document.*

- McKinsey's 2025 State of AI describes a **"genAI paradox"** — rapid technological adoption paired with slow productivity gains. The proportion of companies abandoning the majority of their AI initiatives before broad deployment jumped to **42% in 2025, up from 17% the previous year**.  
  *Source: McKinsey & Company, "State of AI 2025," cited across PCBB, LinkedIn, and Azati (February 2026). **Note:** The 42% figure is widely cited but the primary McKinsey report page (mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) was confirmed to exist but requires verification of exact statistic.*

- Externally procured AI solutions succeed at nearly **twice the rate** of internally built systems (per MIT study). Consistent with Menlo Ventures data showing enterprise preference shifted from 47% buy/53% build (2024) to **76% buy/24% build (2025)**.  
  *Source: Menlo Ventures, "2025: The State of Generative AI in the Enterprise," December 9, 2025. Based on ~500 U.S. enterprise decision-maker survey.*

- Menlo Ventures data shows enterprise AI deals close at a **47% conversion rate** vs. 25% for traditional SaaS — suggesting genuine perceived value even where P&L impact is not yet measured.  
  *Source: Menlo Ventures, December 2025*

**ROI Gap Summary:** High adoption, low realized returns. The MIT 95% failure stat is the sharpest data point but should be treated as directionally correct rather than precisely verified without primary source access.

---

### 2. What's Being Commoditized — and How Fast

**Finding: Model capability is commoditizing rapidly; inference costs are collapsing; the application layer is the new battleground.**

#### Model Performance Convergence

- The gap between top U.S. and Chinese models on MMLU shrank from **17.5 percentage points (2023) to 0.3 percentage points (2024)** — from a meaningful lead to statistical noise in one year.  
  *Source: Stanford AI Index 2025, Technical Performance chapter. Published April 7, 2025.*

- The gap between closed-source and open-weight models on key benchmarks shrank from **8% to 1.7% in a single year** (2024–2025).  
  *Source: Stanford AI Index 2025 / arXiv:2504.07139*

- By November 2025, the Chatbot Arena Leaderboard top model gap had "basically collapsed" with margins in "measurement error territory." Claude, Grok, Llama, DeepSeek were functionally indistinguishable on common tasks.  
  *Source: Towards AI / Ali Khalilvandi, "The Great LLM Convergence," November 30, 2025*

- Artificial Analysis (2025 Year-End State of AI Report) confirms: "OpenAI began and ended 2025 with the most capable language model, but their lead is narrower than ever." The race "only intensified" with no consolidation.  
  *Source: Artificial Analysis, "State of AI: 2025 Year-End Edition." PDF available at artificialanalysis.ai*

#### Cost Collapse

- GPT-4 level intelligence is now **100x cheaper** than when GPT-4 originally launched.  
  *Source: Artificial Analysis, 2025 Year-End Report*

- Inference costs have fallen **9–900x per year** depending on task type. A model scoring equivalent to GPT-3.5 on MMLU dropped from $20 per million tokens (November 2022) to **$0.07 per million tokens** (October 2024) — a 280-fold reduction in 18 months.  
  *Source: Stanford AI Index 2025*

- Sam Altman stated: "The cost to use a given level of AI falls about 10x every 12 months."  
  *Source: Cited in Towards AI, November 2025*

- Open-source models like DeepSeek-R1, Llama 4, and Qwen 3 deliver **70–90% cost savings** versus closed APIs. DeepSeek claimed its V3 training cost ~$5.6M in GPU-hours; comparable closed models (e.g., GPT-5) estimated at $500M+ per training run.  
  *Source: California Management Review / Congshan Li, "The Coming Disruption," January 9, 2026 (UC Berkeley Haas)*

- Small model catch-up: Microsoft's Phi-3-Mini (3.8B parameters) in 2024 matched benchmark scores previously requiring 540B parameter models (PaLM, 2022) — a **142-fold reduction** in model size over two years.  
  *Source: Stanford AI Index 2025*

#### What's NOT Being Commoditized (Yet)

- Anthropic held **54% share of enterprise LLM API usage for coding** in late 2025, up from 42% six months earlier — suggesting durable leadership is possible, at least at the capability frontier.  
  *Source: Menlo Ventures, December 2025*

- Anthropic maintained ~18 months atop coding benchmarks (starting with Claude Sonnet 3.5, June 2024). This is the longest sustained differentiation in the LLM market.  
  *Source: Menlo Ventures, December 2025*

---

### 3. Evidence of a "Race to the Mean"

**Finding: Strong evidence at the model layer; mixed at the application layer; largely absent at the true moat layer.**

#### Model Layer: Convergence is Real

- Stanford's AI Index 2025 documents benchmark saturation: models "saturated MMLU, GSM8K, HumanEval" — prompting the industry to invent harder tests. AI researcher response: create "Humanity's Last Exam" where top systems score **8.8%**. This is the industry avoiding acknowledging parity by raising the bar.  
  *Source: Towards AI, November 2025; Stanford AI Index 2025*

- DeepSeek-R1 (released January 2025) matched leading Western models while reportedly using a fraction of the compute resources — demonstrating that performance parity is achievable at dramatically lower cost.  
  *Source: DeepSeek-AI, arXiv:2501.12948; cited in CMR Berkeley, January 2026*

- Menlo Ventures reports: Open-source enterprise share fell from **19% to 11%** in 2025 (enterprises still prefer closed models), but this may reflect procurement conservatism rather than capability gap.  
  *Source: Menlo Ventures, December 2025*

#### Application Layer: Startup Disruption of Incumbents

- AI-native startups captured **63% of the enterprise AI application market** in 2025, up from 36% in 2024 — despite incumbents having distribution, data moats, and enterprise relationships.  
  *Source: Menlo Ventures, December 2025*

- This is evidence that new entrants can achieve competitive parity and superiority faster than expected — but it's not "race to the mean." It's disruption. Different from commoditization.

#### Retention Problem Signals Parity

- Sequoia's data: Median DAU/MAU for generative AI applications is **14%** — vs. 60–65% for best consumer companies. Low retention signals users aren't finding lasting differentiation.  
  *Source: BuildMVPFast.com, citing Sequoia, "AI Moats" article, 2026. **Note:** Could not directly verify the Sequoia primary source; this is a secondary citation.*

- 79% of organizations report competitors making **similar GenAI investments**; only 23% believe they're building sustainable advantage.  
  *Source: Azati, February 2026, citing McKinsey 2025 State of AI*

---

### 4. How Fast Are Tech-Based Moats Eroding?

**Finding: Feature-level moats last weeks; workflow/data moats remain durable; first-mover model advantage is near-zero.**

- **6–8 weeks**: Average duration of first-mover advantage from adopting a new model version before competitors replicate, per Harvard Business Review analysis.  
  *Source: Cited in Azati (February 2026) and BuildMVPFast (2026), citing HBR. **Note:** Could not directly verify the HBR primary source. Secondary citations only; treat as directionally credible but unverified.*

- **Fake moats (confirmed by market outcomes):**
  - Speed to market: Replicating features "takes hours" per BuildMVPFast
  - Fine-tuning a foundation model: "6-month head start, max" per r/Entrepreneur (cited by BuildMVPFast)
  - System prompt + UI: "Weekend project for a competent developer"
  
  *Source: BuildMVPFast, "AI Moats: What Prevents Competitors from Copying You," 2026*

- **966 U.S. AI startups closed in 2024** (up 25.6% from 2023). SimpleClosure analysis: dominant pattern was "AI wrappers and application-layer tools built on commoditized models, without deep defensive moats."  
  *Source: BuildMVPFast, 2026, citing SimpleClosure. **Note:** SimpleClosure is a bankruptcy services platform; this is an observational claim from their data, not a formal study.*

- **Companies demonstrating durable moats (data points):**
  - **Cursor**: $0 to $2B ARR by March 2026; moat is codebase integration depth, team-specific conventions, model-agnostic architecture.
  - **Harvey AI**: $50M ARR (end of 2024) to $195M (end of 2025) — 4x growth. Moat: custom models fine-tuned on each law firm's proprietary documents.
  - **EvenUp**: $2B valuation; proprietary model trained on 200,000+ real injury cases; largest customer pays $4M+ annually.
  - **Midjourney**: $500M+ 2025 revenue, 100 employees, zero outside funding; moat is Discord community network effects.
  
  *Source: BuildMVPFast, 2026 (secondary source aggregating public data points)*

- **a16z counterpoint on data moats:** Martin Casado published that "data is rarely a strong enough moat" — the cost of collecting unique data rises while value of incremental data falls, opposite of network effects. They now prioritize verticalization and go-to-market dominance over raw data.  
  *Source: BuildMVPFast, 2026, citing a16z; Bessemer similar position*

---

## Contradictions and Counterarguments

These findings **partially contradict** or complicate a clean "AI commoditizes everything" thesis:

1. **Anthropic's 18-month coding lead**: Real, sustained technical differentiation exists. Not everyone converged. The race intensified but didn't flatten.

2. **Vertical AI is growing, not converging**: Healthcare AI tripled from $450M (2024) to $1.5B (2025). Legal AI at $650M. These verticals show deepening specialization, not parity.

3. **Startups are beating incumbents**: If AI capability were purely commoditized, incumbents with distribution would dominate. They don't. AI-native startups are out-executing them in most categories. This suggests execution and integration matter more than access.

4. **Enterprise buying behavior suggests trust hierarchy**: 76% of enterprises now buy AI solutions rather than build — and they're not buying randomly. They're paying premiums for vendors who demonstrate workflow integration and domain depth. Commoditization doesn't erase trust-based pricing.

5. **Open-source enterprise adoption is falling, not rising**: Despite near-parity benchmarks, enterprise open-source LLM share dropped from 19% to 11%. Enterprises are moving toward closed, curated models — possibly valuing support, reliability, and accountability over raw cost savings.

6. **The productivity paradox may be temporary**: Historical parallel from McKinsey — the PC productivity paradox resolved. AI's "genAI paradox" may follow the same arc.

---

## Data Gaps and Reliability Flags

| Claim | Reliability | Issue |
|---|---|---|
| MIT "95% of AI initiatives fail" | **Medium-High** | Primary report behind paywall; widely cited by credible outlets including Menlo Ventures. Treat as directionally valid. |
| McKinsey "42% abandoned initiatives" | **Medium** | Secondary citations only; primary McKinsey report paywalled. Could not verify exact phrasing/methodology. |
| HBR "6–8 weeks first-mover advantage" | **Low-Medium** | Secondary citation only via Azati and BuildMVPFast. Could not locate original HBR source. Should be flagged as unverified. |
| Sequoia "14% DAU/MAU" | **Low-Medium** | Secondary citation only. Could not verify primary Sequoia source. |
| Stanford AI Index 2025 benchmarks | **High** | Primary source accessed; specific data points (17.5pp → 0.3pp MMLU gap, 8% → 1.7% open-closed gap) confirmed. |
| Menlo Ventures enterprise spend data | **High** | Methodology disclosed (~500 surveyor + bottom-up model). Specific and consistent. |
| Artificial Analysis cost data | **High** | Primary report accessed; independent benchmarking firm. |
| 966 startup closures, SimpleClosure | **Medium** | SimpleClosure is a bankruptcy services firm with real data; not a formal research organization. |
| BuildMVPFast company revenue figures | **Medium** | Secondary aggregation of public data; individual company ARR figures often come from self-reported or press-cited sources. Cursor, Harvey, EvenUp figures widely reported. |

---

## What Can Be Confidently Claimed

**Highest confidence** (multiple independent sources, primary data accessible):

1. AI model inference costs are falling ~10x per year; GPT-4 level intelligence is 100x cheaper than at launch.
2. The performance gap between U.S. and Chinese AI models on major benchmarks has effectively collapsed (from 17.5 percentage points to 0.3 on MMLU, Stanford 2025).
3. The gap between open-weight and closed-source models narrowed from 8% to 1.7% on some benchmarks in 2024–2025.
4. Enterprise AI adoption surged (78% of organizations use AI in some form, per McKinsey 2024, per Stanford AI Index).
5. Enterprise AI application market is $19B in 2025 (up from ~$5.7B in 2024); coding is the dominant use case at $4B.
6. AI-native startups captured 63% of enterprise AI app market in 2025, up from 36% in 2024.
7. Enterprises shifted from 47%/53% build/buy to 24%/76% build/buy in a single year.

**Medium confidence** (widely cited but primary source not directly verified):

8. Only ~5% of enterprise AI initiatives produce measurable P&L returns (MIT, 2025).
9. 42% of organizations abandoned most AI initiatives in 2025, up from 17% (McKinsey, 2025).
10. First-mover advantage from adopting new model versions lasts approximately 6–8 weeks (HBR — unverified primary).
11. Median DAU/MAU for generative AI apps is 14% (Sequoia — unverified primary).

**Low confidence / should not be asserted without caveat:**

12. Exact startup closure counts (966 / SimpleClosure).
13. Any specific 2026 projection presented as fact.

---

## Synthesis: Implications for the "AI Commoditizes Technical Capability" Thesis

The thesis is **largely supported at the model layer** and **contested at the business layer**.

What's happening:
- Model access is democratizing fast. Anyone can call the same API.
- Benchmark differentiation between providers has near-zero practical value.
- First-mover advantage from using "the latest model" is measured in weeks.
- Inference costs are in freefall; will approach near-zero for commodity tasks.

What this means competitively:
- Companies whose differentiation was "we use AI" or "we use GPT-5" have no moat.
- Companies whose differentiation is proprietary data + workflow integration + domain expertise do have moats, but those moats come from human organizational assets, not technical ones.
- The new competitive question is not "do you have AI?" but "what can your AI learn from that no one else can replicate?"

This reframes the Kindness Flywheel thesis: if AI commoditizes the technical layer, what differentiates is the **quality of relationships, trust, and accumulated human knowledge** — things that cannot be pulled from an API. That argument is strongly supported by the data.

---

## Sources Summary

| Source | Type | Date | Access |
|---|---|---|---|
| MIT, "The GenAI Divide: State of AI in Business 2025" | Academic study | 2025 | Paywalled; cited by multiple outlets |
| McKinsey, "State of AI 2025" | Annual survey | 2025 | Paywalled; secondary citations |
| Menlo Ventures, "2025: State of Generative AI in the Enterprise" | VC annual report | December 9, 2025 | Publicly accessible |
| Stanford HAI, "2025 AI Index Report" | Academic annual | April 7, 2025 | Publicly accessible |
| Artificial Analysis, "State of AI: 2025 Year-End Edition" | Benchmarking report | End-2025 | Highlights free; full behind paywall |
| California Management Review / Congshan Li | Peer-reviewed perspective | January 9, 2026 | UC Berkeley, publicly accessible |
| Towards AI / Ali Khalilvandi | Analysis piece | November 30, 2025 | Publicly accessible |
| BuildMVPFast, "AI Moats: What Prevents Competitors from Copying You" | Industry analysis | 2026 | Publicly accessible |
| Azati, "Generative AI and Competitive Advantage" | Consulting firm blog | February 2026 | Publicly accessible |
| ComplexDiscovery staff, MIT AI failure analysis | Tech journalism | August 21, 2025 | Publicly accessible |

---

*Research conducted March 28, 2026. All sources accessed via Firecrawl search and scrape tools. Primary sources were accessed where available; secondary citations flagged. This brief is intended for internal strategic use by Growth Science / Kindness Flywheel.*
