# Generative Engine Optimization (GEO): Research & Strategy Guide
### For The Kindness Flywheel / Growth Science Publication
**Research compiled:** March 2026  
**Sources:** Princeton academic research, Search Engine Land, The Digital Bloom (680M+ citation analysis), Lureon, Geneo, plus primary platform documentation  
**Status:** Living document — this field moves fast, re-verify quarterly

---

## Table of Contents
1. [What Is GEO? How It Differs from SEO](#1-what-is-geo)
2. [How LLMs Select Sources to Cite](#2-how-llms-select-sources)
3. [Platform-by-Platform Citation Analysis](#3-platform-by-platform)
4. [GitHub, GitHub Pages, and AI Crawlability](#4-github-and-ai-crawlability)
5. [Technical Implementations for GEO](#5-technical-implementations)
6. [Content Architecture & Formatting](#6-content-architecture)
7. [Author Credibility & Editorial Governance](#7-author-credibility)
8. [Creative Commons Licensing & AI Training](#8-creative-commons)
9. [AI-Generated Content: Citation Credibility](#9-ai-generated-content)
10. [What Doesn't Work: Common Misconceptions](#10-what-doesnt-work)
11. [Implementation Roadmap](#11-implementation-roadmap)
12. [Key Uncertainties & Rapidly-Changing Areas](#12-key-uncertainties)

---

## 1. What Is GEO?

**Generative Engine Optimization (GEO)** is the practice of optimizing content so it gets cited, quoted, or referenced in AI-generated answers from LLMs like ChatGPT, Perplexity, Google AI Overviews, Claude, and Microsoft Copilot.

### GEO vs. Traditional SEO

| Dimension | Traditional SEO | GEO |
|-----------|----------------|-----|
| Goal | Rank on search results pages (SERPs) | Get cited/extracted by AI response systems |
| Key signals | Backlinks, keyword density, technical crawlability | Brand authority, content depth, entity clarity, semantic density |
| Content unit | Page-level ranking | Paragraph/chunk-level extractability |
| Backlinks | Strongest signal | **Weak to neutral correlation** (proven) |
| Freshness | Important | Critical (65% of AI citations target content from past year) |
| Structured data | Helpful for rich snippets | Higher importance for entity graph |
| Outcome | Blue link click-through | Direct answer, brand mention, or citation with link |

**Academic foundation:** The Princeton University paper "GEO: Generative Engine Optimization" (KDD 2024, arxiv.org/abs/2311.09735) is the seminal work. It analyzed 10,000 queries across 9 sources and established that GEO optimization can boost AI visibility by **30–40%**, with specific tactics showing up to 115% improvement.

### Also known as:
- **AEO** (Answer Engine Optimization) — often used interchangeably
- **AI Overviews Optimization**
- **LLM Seeding** — a related concept focused on getting into training data
- **AI Citation Optimization**

---

## 2. How LLMs Select Sources to Cite

### Two Distinct Pathways

**Pathway 1: Parametric Knowledge (Training Data)**
- What the model "memorized" during pre-training
- Static, fixed at training cutoff
- ~60% of ChatGPT queries answered purely from parametric knowledge (no live search)
- Entities mentioned frequently across authoritative sources in training have stronger neural representations
- Wikipedia represents ~22% of major LLM training data — this is a massive structural advantage for Wikipedia-presence

**Pathway 2: Retrieved Knowledge (RAG)**
- Real-time Retrieval Augmented Generation — the model searches, retrieves, then generates
- Pipeline: Query → embedding → hybrid retrieval (semantic + BM25 keyword matching) → reranking → generation
- NVIDIA benchmarks: page-level chunking achieves 0.648 accuracy; paragraphs of 200–500 words work best
- Hybrid retrieval delivers 48% improvement over single-method approaches

### What Predicts AI Citations? (Proven Data)

From analysis of 7,000+ citations across 1,600 URLs:

| Signal | Correlation / Impact | Verification |
|--------|---------------------|--------------|
| **Brand search volume** | 0.334 correlation — #1 predictor | ✅ Proven (Seer Interactive) |
| **Content word count** | Higher for Perplexity/AI Overviews | ✅ Proven |
| Adding statistics | +22% visibility improvement | ✅ Princeton study |
| Adding quotations | +37% improvement (Perplexity) | ✅ Princeton study |
| Citing sources within content | +115.1% for rank #5 sites | ✅ Princeton study |
| Fluency optimization | +15–30% boost | ✅ Princeton study |
| Domain Rating (DA) | Light preference for ChatGPT | Partial |
| Flesch Readability Score | Matters for ChatGPT | ✅ Documented |
| **Backlink quantity** | **Weak/neutral** | ✅ Contradicts SEO orthodoxy |
| Keyword stuffing | **Negative impact** | ✅ Princeton (worse than no optimization) |

### Citation Recency Data
- **65%** of AI bot hits target content published within the past year
- **79%** from content updated within 2 years
- **Only 6%** from content older than 6 years
- Multi-modal content (images, videos) did **not** meaningfully move the needle

---

## 3. Platform-by-Platform Citation Analysis

### ChatGPT
- **Without web browsing:** Relies entirely on parametric (training) knowledge
- **With web browsing:** Queries Bing, selects 3–10 sources
- 87% of SearchGPT citations match Bing's top 10 organic results
- Only 56% correlation with Google results
- Wikipedia dominates at **47.9%** of citations
- 3.2x more likely to mention a brand than cite it with a URL link
- Training data priority hierarchy:
  1. Wikipedia, licensed publishers (Condé Nast, Vox Media), GPTBot-accessible sites
  2. Reddit (3+ upvotes), industry publications
  3. YouTube transcripts, podcasts

**Implication for KF:** Being on Wikipedia (if notability criteria met) is highest leverage for ChatGPT parametric visibility. Short of that, building cross-platform brand presence matters most.

### Perplexity
- Every query triggers real-time search against 200+ billion URLs indexed
- **Reddit leads at 46.7%** of top citations
- YouTube: 13.9%
- Gartner: 7.0%
- Typical response: 5–10 inline citations
- Content recency is critical here

**Implication for KF:** Being mentioned authentically on Reddit (relevant subreddits) and industry publications matters significantly for Perplexity.

### Google AI Overviews
- **93.67%** of citations link to at least one top-10 organic result — strongest correlation with traditional SEO
- Only **4.5%** of AI Overview URLs directly match a Page 1 organic URL (draws from deeper pages on authoritative domains)
- Average: 10.2 links from 4 unique domains per response
- 50%+ of searches now show AI Overviews (up from 18% in March 2025)
- Reddit represents 21% of citations

### Claude
- Uses Brave Search backend for web retrieval
- Constitutional AI framework creates preference for helpful, harmless, honest content
- Provides citations with URL, title, and cited_text snippets

### Microsoft Copilot
- Bing grounding for consumer queries
- IndexNow protocol is critical for fast indexing (instant notification to Bing)

### Cross-Platform Reality
- **Only 11% of domains are cited by BOTH ChatGPT and Perplexity**
- Must optimize for multiple platforms independently
- No single strategy guarantees cross-platform coverage

---

## 4. GitHub, GitHub Pages, and AI Crawlability

### Do AI Crawlers Index GitHub Repos and GitHub Pages?

**What's confirmed:**
- GitHub repositories (especially READMEs, markdown files) are indexed by Bing and Google, and therefore appear in ChatGPT (via Bing) and Google AI Overviews
- GitHub Pages sites (`.github.io` or custom domains) are treated as standard websites by all AI crawlers
- GPTBot traffic grew **305%** from May 2024 to 2025 — GitHub is a major target
- Each AI platform has its own crawler user agent:
  - OpenAI: `GPTBot` (training), `OAI-SearchBot` (live search)
  - Google: `Googlebot`, `Google-Extended` (Gemini training)
  - Anthropic: `ClaudeBot`
  - Perplexity: `PerplexityBot`
  - Apple: `Applebot-Extended`

**GitHub domain authority:**
- GitHub.com has very high domain authority — content on `github.com/[user]/[repo]` benefits from that DA
- GitHub Pages on `github.io` has somewhat lower authority than the main domain
- Custom domain GitHub Pages (e.g., `kindnessflywheel.com`) is treated independently and builds its own authority
- **Recommendation:** Use a custom domain for the primary publication rather than `*.github.io` for long-term authority building

### GitHub-Specific robots.txt Considerations
- By default, GitHub repos have no robots.txt blocking AI crawlers
- GitHub Pages sites should add an explicit `robots.txt` that **allows** major AI crawlers
- Blocking training bots (`GPTBot`, `ClaudeBot`) but allowing search bots (`OAI-SearchBot`, `PerplexityBot`) is an increasingly common strategy

### Does Open Source Licensing (CC-BY 4.0) Help?

**What's established:**
- CC licenses only grant permission for rights covered by copyright — they don't mandate inclusion in training data
- CC-BY 4.0 does not legally require attribution in AI training contexts (contested, but current legal reading in most jurisdictions supports fair use for training)
- **However**, content with permissive licenses is *more likely* to be included in curated training datasets that explicitly source licensed content
- The lack of a restrictive license removes friction for AI systems and their data partners

**LLM training data and licensing:**
- Some AI training datasets (e.g., The Pile, Common Crawl) prioritize openly licensed content
- OpenAI has licensed content specifically from publishers — CC-BY content on high-DA domains has a better chance of being included
- Creative Commons itself supports broad use of openly licensed content for AI training "in the public interest"

**Practical implications:**
- CC-BY 4.0 is not a GEO guarantee but it removes barriers
- It signals willingness to share knowledge — culturally aligned with how AI systems prefer content
- The CC license should be machine-readable (RDFa or JSON-LD) on the page, not just stated in text

### Does a Public GitHub Repo's Visible PR/Commit History Help?

*Speculative/emerging:* There is no documented evidence that AI systems parse GitHub PR history for E-E-A-T signals. However:
- Visible contributor history adds human credibility signals for visitors who vet sources
- GitHub's API is parsed by some AI-adjacent tools and data aggregators
- Named contributors with linked profiles (verified GitHub + LinkedIn) improve human-perceived authority, which translates to domain-level citations

---

## 5. Technical Implementations for GEO

### 5.1 robots.txt — AI Crawler Strategy

For maximum citation visibility, allow search-focused bots; optionally block training-only bots:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Googlebot
Allow: /

User-agent: GPTBot
# Decision: Allow for maximum training data coverage
Allow: /

# If you prefer: block training but allow live search
# User-agent: GPTBot
# Disallow: /

User-agent: Google-Extended
Allow: /
```

**Note:** 312 of the top 10K domains block GPTBot entirely; 546 have explicit AI bot rules. Blocking training bots has minimal effect on current AI citations (which rely on live search), but reduces contribution to future model training.

### 5.2 Sitemap.xml

- Standard XML sitemap with `<lastmod>` dates for all content pages
- **Submit to IndexNow** (instant Bing/Copilot indexing) — this is high leverage for Copilot/ChatGPT visibility
- Google Search Console submission remains important for AI Overviews
- Include sitemap reference in robots.txt

### 5.3 Schema.org / JSON-LD Structured Data

**Proven impact:** A Search Engine Land experiment showed:
- Well-implemented schema: Position 3 + AI Overview appearance
- Poorly implemented: Position 8, no AI Overview
- No schema: **Not indexed at all**

Also: **47% higher AI citation rates** for comparison tables using proper HTML (`<thead>`, descriptive columns)

#### Tier 1 — Essential Schema Types

**Organization** (site-level, all pages):
```json
{
  "@context": "https://schema.org",
  "@id": "https://kindnessflywheel.com/#org",
  "@type": "Organization",
  "name": "The Kindness Flywheel",
  "url": "https://kindnessflywheel.com",
  "sameAs": [
    "https://github.com/kindness-flywheel",
    "https://www.linkedin.com/company/kindness-flywheel"
  ]
}
```

**Article / BlogPosting** (each content page):
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title Here",
  "datePublished": "2025-01-15",
  "dateModified": "2025-03-01",
  "author": {"@id": "https://kindnessflywheel.com/#author-geoff"},
  "publisher": {"@id": "https://kindnessflywheel.com/#org"},
  "mainEntityOfPage": "https://kindnessflywheel.com/articles/article-slug"
}
```

**Person** (author profiles, persistent IDs):
```json
{
  "@context": "https://schema.org",
  "@id": "https://kindnessflywheel.com/#author-geoff",
  "@type": "Person",
  "name": "Geoff Scott",
  "jobTitle": "Executive Coach and CTO",
  "knowsAbout": ["Leadership", "Organizational Psychology", "Growth Science"],
  "sameAs": [
    "https://www.linkedin.com/in/geoffscott",
    "https://github.com/geoffscott"
  ]
}
```

#### Tier 2 — High Value

- **FAQPage** — directly feeds AI question-answer extraction; use only where page visibly has multi-Q&A
- **HowTo** — step extraction for procedural content
- **Review/AggregateRating** — trust signals

#### Entity Disambiguation (Critical)

- **Wikidata** is #1 source for Google's Knowledge Graph (500 billion facts, 5 billion entities)
- Adding `sameAs` links to Wikidata entries increases entity recognition dramatically
- Being present on 4+ external platforms = **2.8x more likely to appear in ChatGPT responses**

### 5.4 llms.txt — Emerging Convention

**What it is:** A markdown file at `yourdomain.com/llms.txt` (proposed by Jeremy Howard, September 2024) that provides AI-friendly content context — similar to robots.txt/sitemap but for LLM consumption.

**Format:** Plain markdown. Can be:
- A list of key URLs with summaries
- Full flattened text of the entire site (`llms-full.txt`)
- Multiple files per content section

**Adoption status (March 2026):** Growing but not at critical mass. Anthropic, Hugging Face, Perplexity, Zapier, and many developer tools have implemented it. Not all LLMs consume it, but those that do benefit from the clarity.

**Documented by Anthropic:** `https://docs.anthropic.com/llms-full.txt`

**Practical recommendation:** Implement a `llms.txt` at the site root. The full-flattened version (`llms-full.txt`) provides the most value — it makes the entire site parseable as a single document. For a Jekyll/GitHub Pages site, this can be generated at build time.

**Limitations:**
- No guarantee LLMs will honor it (voluntary)
- Potential security concern: exposes full site content easily to competitors
- Still being standardized — format may evolve

### 5.5 CITATION.cff — Machine-Readable Citation Format

For a publication on GitHub, a `CITATION.cff` file provides structured citation metadata:

```yaml
cff-version: 1.2.0
title: "The Kindness Flywheel"
message: "If you cite content from this publication, please use this reference."
type: article
authors:
  - family-names: Scott
    given-names: Geoff
    affiliation: "Growth Science"
    orcid: "https://orcid.org/0000-XXXX-XXXX-XXXX"
repository-code: "https://github.com/kindness-flywheel/kindness-flywheel"
url: "https://kindnessflywheel.com"
license: CC-BY-4.0
date-released: "2024-01-01"
```

**Impact:** GitHub natively reads `CITATION.cff` and displays a "Cite this repository" button. Academic tools (Zotero, etc.) parse it automatically. This is particularly valuable if the publication gains academic traction.

### 5.6 YAML Frontmatter for Machine Readability

For Jekyll/GitHub Pages, rich frontmatter increases machine-parseable metadata:

```yaml
---
title: "The Science of Kindness in Organizations"
description: "Evidence-based exploration of how kindness drives organizational performance and individual wellbeing."
date: 2025-03-15
updated: 2025-03-28
author:
  name: "Geoff Scott"
  url: "https://kindnessflywheel.com/authors/geoff-scott"
  linkedin: "https://linkedin.com/in/geoffscott"
categories: ["organizational-psychology", "leadership", "wellbeing"]
tags: ["kindness", "EQ", "organizational-culture", "research"]
schema_type: "Article"
license: "CC-BY-4.0"
canonical_url: "https://kindnessflywheel.com/articles/science-of-kindness"
---
```

### 5.7 RSS/Atom Feeds

- Some AI aggregators and research tools do consume RSS feeds for content discovery
- Perplexity's crawler indexes content discovered via feeds
- Full-text RSS (not truncated summaries) is preferable for AI consumption
- **Recommendation:** Publish full-content RSS feed for the publication

### 5.8 IndexNow Protocol

- Open protocol for instant Bing/Copilot indexing notification
- Adopted by Amazon, Shopify, GoDaddy, Internet Archive
- Adds a simple API call when new content is published
- High leverage for Copilot and ChatGPT (which uses Bing) visibility
- Easy to add to a GitHub Pages build process (curl call in CI/CD)

---

## 6. Content Architecture & Formatting

### Structure for Maximum Extractability

The Princeton GEO research and industry analysis converge on these patterns:

1. **Lead with the direct answer** in the first paragraph — "The answer is X because Y"
2. **Optimal paragraph length:** 40–60 words for AI chunking and extraction
3. **Clear heading hierarchy** — H2/H3 that mirror likely search queries
4. **Self-contained sections** — each section independently comprehensible when extracted
5. **Verifiable data points** with sources cited inline (+22% visibility)
6. **Expert quotations** attributed to named, credentialed sources (+37% on Perplexity)
7. **Comparison tables** with proper `<thead>` and descriptive columns (+47% citation rate)

### High-Citation Content Formats (from 30M+ citations analysis)

| Format | % of AI Citations |
|--------|-----------------|
| **Comparative listicles** | **32.5% — highest** |
| Opinion blogs | 9.91% |
| Product/service descriptions | 4.73% |
| FAQ/Q&A | High (especially Perplexity, Gemini) |
| How-to guides | Strong performer |

### NLP-Friendly Formatting Checklist
- [ ] Use declarative, direct sentences ("Kindness improves performance by X%")
- [ ] FAQs for common questions in the domain (triggers FAQPage schema and AI Q&A extraction)
- [ ] Numbered lists for processes and how-tos
- [ ] Bullet points for features, benefits, factors
- [ ] Short summary "Key Takeaways" or "TL;DR" block at top
- [ ] Clear definitions when introducing specialized concepts

---

## 7. Author Credibility & Editorial Governance

### E-E-A-T Translated to GEO

Google's E-E-A-T framework (Experience, Expertise, Authoritativeness, Trustworthiness) maps to GEO as follows:

**What's documented with evidence:**
- Content with **proper author attribution** gets **40% more AI citations** than unattributed content (serps.io, citing multiple studies)
- Named authors with verifiable identities (LinkedIn, institutional affiliation) increase citation likelihood
- Every content page targeting AI citation benefits from:
  - Full author name and professional title
  - Relevant credentials and experience markers
  - Consistent identity across platforms
  - `sameAs` schema linking to authoritative profiles

### Named vs. Anonymous Authors
- **Named authors with verifiable identities = significant advantage**
- AI systems favor content with attributable human experts
- Author pages with bios, credentials, external profile links help entity recognition
- Multi-author content signals community vetting — generally positive

### Editorial Standards & Transparent Process
- *Emerging/theoretical:* Transparent editorial process (visible via GitHub PR history) has not been proven to directly affect AI citation rates
- However, it contributes to human-perceived credibility, which affects:
  - Inbound citations from other credible sources (which do affect AI visibility)
  - Press/media coverage (which affects parametric training data)
  - Academic or practitioner reference (high-value citations)
- **Version control / dated revisions** visible in git history signals content freshness and care

### Multi-Author Community Curation
- *Emerging:* Multiple named, credentialed contributors likely improves perceived authority
- Mirrors Wikipedia's model (highest-cited source in training data), which benefits from crowd-sourced expertise
- Contributor diversity (different institutional affiliations, industries) signals breadth of validation

### Wikidata Entity Presence
- The highest-leverage E-E-A-T move for GEO is **creating/verifying Wikidata entries** for the publication and key authors (if they meet notability criteria)
- Google's Knowledge Graph draws from Wikidata (500B facts, 5B entities)
- A Wikidata Q-number + `sameAs` in schema creates a strong entity node

---

## 8. Creative Commons Licensing & AI Training

### Legal Reality (2024–2026)
- CC licenses grant copyright permissions but don't govern all AI uses
- LLM training in many jurisdictions is treated as "fair use" or "text data mining" exemption (especially EU DSM Directive)
- **CC-BY 4.0 does not legally stop AI systems from training on your content** — nor does any CC license
- **NC (NonCommercial) licenses** have even weaker enforcement in training contexts
- The 2025 LSE/Impact of Social Sciences research confirms: "Creative commons licenses and copyright may not stop academic work being used to train AI"

### Practical Impact of CC-BY 4.0 on GEO
- **Positive signals:**
  - Some curated AI training datasets explicitly filter for permissively licensed content
  - CC license removes friction for AI data partners and academics who want to cite openly
  - Signals openness and trust — consistent with high-citation content ethos
  - Machine-readable license markup (via JSON-LD or RDFa) helps automated systems recognize reuse permissions
- **No negative impact:** There is no evidence that CC-licensed content is penalized by AI systems

### Recommendation
- Keep CC-BY 4.0
- Make it machine-readable in schema:
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "license": "https://creativecommons.org/licenses/by/4.0/"
}
```
- Add visible human-readable license badge on each page

---

## 9. AI-Generated Content: Citation Credibility

### What Google Has Said (Official Policy)
- Google does **not** penalize content for being AI-generated per se
- Google penalizes **low-quality, spammy, or unhelpful content** regardless of how it was created
- The 2024–2025 Helpful Content Updates are AI-*aware* — Google's classifier looks for "robotic" writing patterns, lack of original insight, and thin content signals

### What the Research Shows (2025)
- **Perception research** (multiple studies): Disclosure of AI use in content creation reduces reader trust — with *detailed* AI disclosure showing larger trust drops than *brief* disclosure
- Reuters Institute (2025): Consumers are skeptical of AI-generated news; "AI-assisted" framing is better-received than "AI-written"
- Academic writing field: Distinguishes "AI-assisted" (human edits/validates AI output) vs. "AI-generated" (AI with no human review) — only the latter draws significant criticism

### How Other AI Systems Treat AI-Generated Content
- *No confirmed evidence* that LLMs explicitly detect and penalize AI-generated content when deciding to cite
- The actual citation signals are about quality, authority, and structure — a well-structured, authoritative, human-validated AI-assisted piece would likely outperform a shallow human-written piece
- Perplexity's real-time retrieval prioritizes freshness and relevance — less concern about generation method
- *Emerging concern:* As AI-generated content floods the web, curated human-validated sources may receive a credibility premium — this is speculative but directionally likely

### Recommendations for AI-Assisted Publication
1. **Frame it as "AI-assisted" not "AI-generated"** — positions humans as editorial decision-makers
2. **Name the human author** who reviewed, edited, and takes responsibility for each piece
3. **Add original insights, data, or perspectives** that AI couldn't generate alone (first-person experience, original research, curated interviews)
4. **Implement editorial standards** visibly: review process documented, author bios present, corrections policy stated
5. **Avoid disclosure overload:** Brief disclosure ("This article was drafted with AI assistance and reviewed by [author]") is better than detailed AI methodology descriptions — which paradoxically reduce trust
6. **Focus on depth and accuracy** — AI tools can produce comprehensive, well-structured content; the human role is validation, original perspective, and quality assurance

---

## 10. What Doesn't Work: Common Misconceptions

| Strategy | Traditional SEO Impact | AI Visibility Impact |
|----------|----------------------|---------------------|
| Backlink quantity | High (core signal) | **Weak/neutral** ✅ Proven |
| Keyword stuffing | Negative | **Worse in AI** ✅ Princeton |
| Images/videos | Engagement boost | No measurable citation impact |
| #1 ranking focus | Primary goal | Only 4.5% correlation |
| Short thin content | Variable | **Actively penalized** |
| Meta keywords tag | Ignored by Google | No GEO value |
| Press releases alone | Some DA value | Weak without quality content backup |
| Social media shares alone | Weak signal | Not a direct GEO signal |

---

## 11. Implementation Roadmap

### Phase 1: Foundation (Weeks 1–4)

**Technical:**
- [ ] Audit `robots.txt` — explicitly allow `OAI-SearchBot`, `PerplexityBot`, `ClaudeBot`, `GPTBot`
- [ ] Generate and submit XML sitemap (with `<lastmod>` dates) to Google Search Console
- [ ] Implement IndexNow API call in CI/CD pipeline for Bing/Copilot instant indexing
- [ ] Add JSON-LD Organization schema with `sameAs` links to all pages
- [ ] Add JSON-LD Article/Person schema with persistent `@id`s to all content pages
- [ ] Create `CITATION.cff` in GitHub repo root
- [ ] Implement machine-readable CC-BY 4.0 license in schema
- [ ] Create author profile pages with full bio, credentials, external profile links

**Entity Building:**
- [ ] Create Wikidata entry for the publication (if meets notability criteria)
- [ ] Verify/create LinkedIn page for "The Kindness Flywheel"
- [ ] Ensure consistent brand name across all platforms

**Monitoring:**
- [ ] Set up AI citation tracking (Otterly.AI freemium tier, or manual weekly Perplexity queries)
- [ ] Configure GA4 to capture `perplexity.ai` and `chat.openai.com` referrals as AI traffic segments

### Phase 2: Content Optimization (Weeks 5–12)

- [ ] Add `llms.txt` (URL-and-summary format minimum; `llms-full.txt` if feasible)
- [ ] Audit existing articles: restructure to lead with direct answers in opening paragraph
- [ ] Ensure all paragraphs 40–60 words where possible
- [ ] Add statistics and citations to key articles (+22% visibility)
- [ ] Add expert quotations (attributed) to key articles (+37% on Perplexity)
- [ ] Create or expand FAQ sections on highest-traffic pages
- [ ] Implement FAQPage schema where multi-Q&A content exists
- [ ] Create 2–3 comparative listicle articles on core topics (32.5% of AI citations)
- [ ] Add full RSS feed with complete article text

### Phase 3: Entity & Authority Building (Ongoing)

- [ ] Build authentic Reddit presence in relevant communities (leadership, organizational psychology, wellbeing)
- [ ] Pursue guest posts / mentions on frequently-cited domains (Forbes, Harvard Business Review, industry publications)
- [ ] Develop YouTube content (transcripts improve AI discoverability)
- [ ] Build cross-references: each article cites other articles and external authoritative sources
- [ ] Quarterly content refresh cycle — update statistics, add new research, reflect recent dates
- [ ] Monitor citation drift monthly (~40–60% volatility is normal)

---

## 12. Key Uncertainties & Rapidly-Changing Areas

> **⚠️ This field moves fast. Re-verify these quarterly.**

### Rapidly Changing
1. **llms.txt adoption** — Not yet at critical mass; watching for major LLM official endorsement
2. **AI crawler bot list** — New bots appear frequently (Apple Intelligence, Meta AI, etc.)
3. **Google AI Overviews share** — Jumped from 6.49% to 13.14% of searches in one year (2024→2025); 50%+ showing in some verticals now
4. **LLM citation drift** — ~55–60% of citations change month-to-month; optimization is ongoing not one-time
5. **AI content detection** — The arms race between AI generation and detection is ongoing; quality signals may become more important as low-quality AI content floods the web

### Contested / Unconfirmed
1. **Whether blocking GPTBot (training) affects live ChatGPT citations** — Separating OAI-SearchBot (live) from GPTBot (training) means you can block training while still allowing live search access. Whether this strategy is beneficial long-term is unclear.
2. **Whether transparent editorial process (GitHub PRs) translates to GEO signals** — No documented evidence; likely indirect
3. **Whether CC license machine-readable markup directly improves citation probability** — Logical but unproven
4. **Multi-author vs. single-author advantage** — Trust signals in E-E-A-T suggest multi-author is positive; no controlled GEO study has confirmed this
5. **Wikipedia entries for the publication** — Highest-leverage move for ChatGPT parametric knowledge, but requires meeting Wikipedia notability guidelines (which requires significant prior media/academic coverage)

### Areas Where Evidence Is Clearest
- Backlinks are **not** the primary GEO signal (proven)
- Brand search volume **is** the strongest predictor (0.334 correlation, proven)
- Statistics and quotations in content directly improve citation rates (Princeton, KDD 2024, proven)
- Content recency matters significantly (65% from past year, proven)
- Schema markup affects AI Overview eligibility (documented experiment)
- Named authors with credentials improve citation likelihood (40% differential, documented)

---

## Appendix A: AI Crawler Reference Table

| Crawler | Owner | Purpose | robots.txt Token |
|---------|-------|---------|------------------|
| GPTBot | OpenAI | Model training | `GPTBot` |
| OAI-SearchBot | OpenAI | Real-time search (ChatGPT) | `OAI-SearchBot` |
| Google-Extended | Google | Gemini/Bard training | `Google-Extended` |
| ClaudeBot | Anthropic | Model training | `ClaudeBot` |
| PerplexityBot | Perplexity | Real-time search | `PerplexityBot` |
| Applebot-Extended | Apple | Apple Intelligence | `Applebot-Extended` |
| Googlebot | Google | Standard search indexing | `Googlebot` |

---

## Appendix B: Key Resources & Citations

### Academic Research
- [GEO: Generative Engine Optimization — Princeton/KDD 2024](https://arxiv.org/abs/2311.09735)
- Transparency and AI disclosure trust research — ScienceDirect (2025)
- Reuters Institute: Generative AI and News Report 2025

### Industry Data
- The Digital Bloom: 2025 AI Visibility Report (680M+ citations analyzed)
- Seer Interactive: STUDY: What Drives Brand Mentions in AI Answers
- Search Engine Land: llms.txt proposed standard (March 2025, Rob Garner)
- Geneo: Schema for AI Citations implementation guide (2026)
- Lureon: Top GEO Ranking Factors (2025)

### Platform Documentation
- Google: AI features and your website — developers.google.com
- Google: Top ways to ensure content performs well in Google's AI Search (May 2025)
- Anthropic: llms-full.txt live example — docs.anthropic.com/llms-full.txt
- IndexNow: indexnow.org

### Leading Voices in GEO (2024–2026)
- **Kevin Indig** — Growth Memo newsletter; ChatGPT/Google content strategy research
- **Vlad Kuryatnik** — The Digital Bloom; large-scale citation data analysis
- **Rob Garner** — Search Engine Land contributor; llms.txt research
- **Princeton research group** — Academic foundation of GEO (Aggarwal et al., KDD 2024)
- **Seer Interactive** — Brand mention / LLM visibility data research

---

*Document compiled by research subagent, March 28, 2026. Sources are primarily 2024–2026. Re-verify critical claims before major publication decisions.*
