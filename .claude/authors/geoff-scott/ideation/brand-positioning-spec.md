Brand Positioning
Growth Science LLC is Geoff’s executive coaching and business advisory practice.
The Kindness Flywheel is a publication and content brand under Growth Science. It’s the public voice of the practice — the place where Geoff’s thinking about leadership, AI strategy, and human-centered technology is shared. It serves as the top-of-funnel for coaching clients, the credibility engine for speaking and writing, and the connective tissue for a peer community.
Thesis: In a world where AI commoditizes technical competence, the only durable competitive advantage is genuine human care. Organizations that systematically cultivate trust, accountability, and service will outperform those chasing pure automation.

The Problem the Skill Solves
Geoff enjoys thinking, journaling, and having conversations about these topics. He does not enjoy the production work of turning raw thinking into polished, publishable content and managing the publishing process. That production toil is the bottleneck — not ideas, not time for reflection, but the last mile from insight to published piece.
The content associate skill sits at the boundary between thinking and publishing. It:
	1.	Draws on the agent’s shared memory (conversations, journal entries, notes)
	2.	Identifies publishable insights and suggests topics
	3.	Drafts content in Geoff’s voice
	4.	Presents drafts for approval or light editing
	5.	Learns from feedback via the shared kaizen skill
Geoff’s role: think, reflect, approve, and provide feedback. The skill’s role: surface, draft, refine, and (eventually) publish.

Architecture
The content associate is a skill, not a standalone agent. It lives within Geoff’s personal chief of staff agent alongside other skills that manage different aspects of his work and life. The agent provides unified memory and identity; each skill provides a specific capability.
The key architectural benefit: memory is shared at the agent level. Journal entries, to-do context, conversation history, and coaching notes are all visible to every skill. The content associate doesn’t need its own separate memory of Geoff’s voice and themes — it inherits that from the agent. A journal entry about a coaching insight can surface as a content topic without any cross-skill coordination.

~/.openclaw/agents/chief-of-staff/
├── AGENTS.md              # "You are Geoff's personal chief of staff..."
├── SOUL.md                # Geoff's voice, values, judgment style
├── memories.md            # Accumulated context across all skills
├── skills/
│   ├── journal/SKILL.md
│   ├── todo/SKILL.md
│   ├── content-associate/SKILL.md      # The Kindness Flywheel content skill
│   ├── bookkeeper/SKILL.md             # CFO Kit bookkeeping skill (installed from ClawHub)
│   └── ...
└── ...

~/.openclaw/skills/                      # shared skills
├── kaizen/SKILL.md                      # continuous improvement, used by any agent
└── ...


Note that the bookkeeper skill is a CFO Kit skill installed from ClawHub — a domain-specific capability developed and maintained by the CFO Kit project. The content associate skill is a personal skill developed for Geoff’s specific workflow. Both sit equally within the chief of staff agent’s skill library. The agent decides when to invoke each based on context: a journal entry about cash flow might trigger the bookkeeper skill, while a journal entry about leadership philosophy might trigger the content associate skill.
This pattern — a personal agent composed of both custom and marketplace skills — is the general model for how individuals and organizations will assemble their AI tooling.

Target Audience (for The Kindness Flywheel publication)
	∙	CTOs and tech leaders navigating AI transformation
	∙	Founders and executives rethinking competitive strategy as traditional moats erode
	∙	Leaders at the intersection of contemplative practice and business

Publishing Cadence
Starting cadence: 2-4 LinkedIn posts per month. Modest and sustainable given Geoff’s availability. Quality over volume. Increase only when the skill is reliably producing drafts that need minimal editing.
Platform: LinkedIn first. Evaluate adding a Substack or blog for longer-form pieces after 3-6 months based on audience response and skill maturity.
Future state: Skill-assisted production could enable higher frequency and multi-format output without increasing Geoff’s time commitment beyond 1-2 hours/week of review and feedback.

Content Associate Skill — Specification
Skill Identity
	∙	Skill name: content-associate
	∙	Location: ~/.openclaw/agents/chief-of-staff/skills/content-associate/SKILL.md
	∙	Publication brand: The Kindness Flywheel (under Growth Science LLC)
Core Capabilities
	1.	Topic Discovery
	∙	Scan the agent’s shared memory for insights with publishing potential
	∙	Draw from conversation transcripts, journal entries, coaching notes, and work artifacts
	∙	Present a weekly shortlist of 2-3 suggested topics with brief rationale
	∙	Learn which suggestions get approved vs. rejected (via kaizen skill)
	1.	Drafting
	∙	Produce LinkedIn post drafts (300-600 words) from selected topics
	∙	Voice: practitioner tone, not pundit; reflective but grounded in real work; connects strategy to philosophy without being preachy
	∙	Include a suggested hook/opening line optimized for LinkedIn engagement
	∙	Provide 1-2 draft variants when the angle could go multiple directions
	1.	Voice Calibration
	∙	Rely on the agent’s SOUL.md for baseline voice and values
	∙	Maintain skill-level notes on publishing-specific patterns (what works on LinkedIn, preferred post structures, topics that resonate)
	∙	Track patterns in what Geoff edits, rejects, or approves without changes
	∙	Feed observations to kaizen skill for systematic improvement
	1.	Publishing Preparation
	∙	Format final approved content for LinkedIn (plain text, appropriate line breaks, hashtags if warranted)
	∙	Suggest posting timing based on audience engagement patterns
	∙	Future: direct posting integration via LinkedIn API or scheduling tool
Interaction with Other Skills
	∙	Journal skill: Primary source of raw material. Journal entries are the richest input for content topics. The content associate reads journal output from shared memory but never writes to the journal.
	∙	To-do skill: May flag publishing tasks (e.g., “Review draft on AI moats”) as to-do items. May also check to-do context for client-sensitive work that should not be referenced in published content.
	∙	Bookkeeper skill: Example of a co-resident domain skill. No direct interaction, but illustrates how the chief of staff agent composes personal and professional capabilities. A journal entry about financial strategy could theoretically surface insights relevant to both skills.
	∙	Kaizen skill (shared): The content associate feeds performance data to kaizen — draft approval rates, edit distance, topic acceptance patterns. Kaizen periodically reviews this data and suggests improvements to the content associate’s approach.
Privacy & Boundaries
	∙	Journal content is raw and personal. The skill must distinguish between insights that are publishable and material that is private.
	∙	Client work must be anonymized — no company names, individual names, or identifiable details without explicit approval.
	∙	The skill should flag any draft that might cross a privacy boundary for explicit review.
	∙	Geoff has final approval on everything. Nothing publishes without his explicit sign-off.

Phased Rollout
Phase 1: Prime the Skill (Weeks 1-3)
	∙	Build the chief of staff agent in OpenCLAW (if not already running)
	∙	Create the content-associate skill
	∙	Seed agent memory with initial content:
	∙	Summary of key Claude conversations (moat analysis, kindness flywheel thesis, content strategy development)
	∙	Selected journal entries
	∙	Voice examples and guidelines
	∙	Define privacy boundaries in the skill’s SKILL.md
	∙	Skill begins generating topic suggestions and first drafts
Phase 2: Train Through Feedback (Weeks 4-8)
	∙	Skill produces 2-3 draft suggestions per week
	∙	Geoff reviews, edits, approves, or rejects with feedback
	∙	Kaizen skill accumulates voice and quality learnings
	∙	Publish first posts — expect heavy editing at this stage
	∙	Target: 2-4 published LinkedIn posts during this phase
Phase 3: Steady State (Weeks 9+)
	∙	Skill drafts require lighter editing
	∙	Consistent cadence of 2-4 LinkedIn posts per month
	∙	Begin evaluating longer-form content potential
	∙	Track audience engagement to inform topic selection
Phase 4: Expand (Month 4+)
	∙	Evaluate adding Substack or blog for monthly long-form essays
	∙	Consider multi-format repurposing (same insight as LinkedIn post + essay + talk notes)
	∙	Assess community-building opportunities
	∙	Revisit frequency based on skill maturity and audience growth

Success Metrics
Skill quality (ongoing):
	∙	Decreasing edit distance between skill drafts and published versions
	∙	Increasing approval rate on first drafts
	∙	Geoff’s subjective sense that drafts “sound like me”
Content performance (12-18 months):
	∙	Growing LinkedIn engagement (comments, shares, connection requests from target audience)
	∙	Inbound coaching inquiries attributable to content
	∙	Invitations to speak or contribute to publications
	∙	A body of work sufficient to support a book proposal or speaking series
Process health:
	∙	Geoff’s time stays at or below 1-2 hours/week
	∙	The workflow feels sustainable and energizing, not like another obligation
	∙	The skill is demonstrably improving over time (tracked by kaizen)

Open Questions
	∙	What tool or process handles the actual LinkedIn publishing? (Manual initially, API integration later?)
	∙	How do we handle the journal privacy boundary in practice? (Tagging system? Separate publishable journal? Skill-level filtering rules?)
	∙	Should the skill also monitor LinkedIn engagement and surface insights about what’s resonating?
	∙	What’s the relationship between building this skill and the SRE assistant agent work at OneEleven? Shared learnings about OpenCLAW development?
	∙	Is the chief of staff agent already running, or does this project bootstrap it?