---
description: Premium B2B Semantic SEO Workflow with WIN Flavor Brand Integration & Quality Audit
---

# WIN Flavor Branded SEO Workflow

This is the **Premium Content Pipeline** for WIN Flavor (The R&D Solutionist).
It enforces strict adherence to **Semantic SEO**, **Competitor Benchmarking**, and the **WIN Flavor Brand Persona** ("Scientific & Solution-Oriented").

**Command:** `/WIN-Flavor-seo [keyword]`

**Global Quality Rules:**
1. **Content Freshness**: MUST use `search_web` to verify the latest regulations, decrees, and industry updates before writing. Always reference the most current legal documents (e.g., latest Nghị định, Thông tư, VBHN). Never rely on outdated information.
2. **No Emoji**: Articles must NOT contain any emoji characters (⭐, ⚠️, 🔥, etc.). Use text labels like **(MỚI)**, **Lưu ý**, **Quan trọng** instead.
3. **No Em Dash**: Never use em dash (—) in articles. Always use short dash (-) instead.
4. **Key Takeaways**: Every article MUST include a `[key_takeaways]...[/key_takeaways]` shortcode block after the intro paragraph (before the first image). Contains 5-7 bullet points summarizing the most important facts. MUST have a blank line before `[/key_takeaways]`.
5. **No Brand Prefix in Expert Remarks**: Blockquote expert remarks must NOT be prefixed with brand name (e.g., "Chuyên gia WIN Flavor:", "GOHA Note:"). The blockquote stands alone as objective expert insight.
6. **Keyword Density**: The **primary keyword** MUST appear **5-10 times** in the article body (excluding metadata table), scaled by content length. All **secondary keywords** and **semantic/LSI keywords** from `research.md` MUST also appear at least once naturally in the article. Verify keyword presence during the Audit phase.
7. **Heading Structure Cap**: Every article MUST have **maximum 5 H2 headings**. Use multiple H3/H4 subheadings under each H2 to cover depth. If research reveals content gaps, fold them into the most relevant existing H2 as subheadings - do NOT create additional H2s.
8. **Mandatory WIN Flavor Solution Heading**: One of the 5 H2s MUST be a "Giải pháp từ WIN Flavor" section that maps WIN Flavor products/services to the article topic.
9. **B2B F&B Tone**: Write for **enterprise F&B clients** (B2B manufacturers, production facilities, R&D teams). Use professional but accessible language. Avoid consumer-facing marketing tone.
10. **Content Depth Hierarchy**: Classify content blocks by priority:
    - **Nội dung cốt lõi** (Core): Deep, detailed writing about the primary keyword topic. This is the bulk of the article.
    - **Nội dung phụ bổ trợ** (Supporting): Related info that needs detailed explanation to understand the core topic. Write thoroughly but less than core.
    - **Kiến thức thêm** (Supplementary knowledge): Write briefly - this is extra context, not the main focus.
    - **Giải nghĩa ngắn** (Quick definitions): Explain in 1 paragraph maximum. Get to the point fast.
11. **Internal Link Matching**: When writing, cross-reference the internal link database in `Persona Brand/MQ - WIN Flavor/internal-links-WIN-Flavor.md` (~900 URLs). Insert 3-7 relevant internal links per article using natural anchor text. Match links by topical relevance to the article content.

---

## 1. Preparation
- **Input**: User provides a target keyword.
- **Action**: Create a designated folder: `Keywords/WIN Flavor/[keyword-slug]` (Ensure parent folder `Keywords/WIN Flavor` exists)
- **Prerequisite Check**: Ensure these files exist in the workspace:
    - `Persona Brand/MQ - WIN Flavor/source-context-WIN-Flavor.md`
    - `Persona Brand/MQ - WIN Flavor/central-entity-WIN-Flavor.md`

## 2. Phase 1: Search Intent Analysis (Optimized)
**Goal**: Decode the user's hidden Micro-Intent (Know/Do/Go) using live SERP data.

- **Action**: Use `search_web [keyword]` to analyze current SERP features (Featured Snippets, Shopping, PAA) to confirm Micro-Intent.
- **Skill**: `.agent/skills/analyzing-search-intent/SKILL.md`
- **Output**: `search-intent.md`

## 3. Phase 2: Semantic & Contextual Research (Optimized)
**Goal**: Establish the semantic foundation with real-time entity and regulatory discovery.

- **Action**: Use `search_web` with operators:
    - `"nghiên cứu [keyword]"` or `"thành phần [keyword]"` to find technical entities.
    - `site:vfa.gov.vn OR site:moh.gov.vn "[keyword]"` for official F&B regulations.
- **Skill**: `.agent/skills/extracting-keywords/SKILL.md`
- **Inputs**:
    - Target Keyword
    - `search-intent.md`
    - `Persona Brand/MQ - WIN Flavor/source-context-WIN-Flavor.md`
- **Legal Check**: If topic involves Regulations:
    - **Load Input**: `Persona Brand/MQ - WIN Flavor/legal-references-2026.md`.
    - **Search**: Use `search_web` to check for 2026 updates to Decree 15/148.
- **Output**: `research.md` (Must aggregate live search data and brand context).

## 4. Phase 3: Competitor Intelligence (Turbo)
**Goal**: Benchmark against top ranking content structures.

// turbo
- **Skill**: `.agent/skills/analyzing-competitors/SKILL.md`
- **Action**: Use the `browser_subagent` tool to perform a live Google search for the target keyword on the user's machine.
- **Action**: Create a subdirectory `competitors/` inside the keyword folder.
- **Action**: Visit the Top 3 Organic Results. Extract H1, H2, H3 headers and save each to `competitors/competitor_[n]_[domain].md`.
- **Output**: `competitor-insights.md` (Save summary in root, raw details in `competitors/`)

## 5. Phase 4: Strategic Outline
**Goal**: Create a scientific and solution-oriented outline merging semantic data and WIN Flavor capabilities.

- **Skill**: `.agent/skills/generating-outlines/SKILL.md`
- **Inputs**:
    - `search-intent.md` (For Format & Micro-Intent alignment)
    - `research.md`
    - `competitor-insights.md`
    - `Persona Brand/MQ - WIN Flavor/central-entity-WIN-Flavor.md` (To map relevant Solutions, Flavors & Ingredients)
- **Structural Constraints**:
    1. **Maximum 5 H2 headings**. Use H3/H4 subheadings for depth and subtopics.
    2. If competitor analysis or research reveals content gaps, integrate them as subheadings under the most relevant H2 - NEVER add a 6th H2.
    3. One H2 MUST be dedicated to "Giải pháp từ WIN Flavor" (or contextually equivalent).
    4. Label each outline section with its Content Depth type: `[CỐT LÕI]`, `[BỔ TRỢ]`, `[KIẾN THỨC THÊM]`, or `[GIẢI NGHĨA]`.
    5. MUST map at least one WIN Flavor Solution/Ingredient (from `central-entity`) as a key solution.
- **Output**: `outline.md`

## 6. Phase 5: Authority Writing (Drafting)
**Goal**: Write the "Expert Scientist" draft for B2B F&B audience.

- **Skill**: `.agent/skills/writing-semantic-content/SKILL.md`
- **Inputs**:
    - `search-intent.md` (For Tone & CTA alignment)
    - `research.md`
    - `outline.md`
    - `Persona Brand/MQ - WIN Flavor/source-context-WIN-Flavor.md` (Mandatory Stylistic Context)
    - `Persona Brand/MQ - WIN Flavor/legal-references-2026.md` (Load ONLY if legal content is present in Research).
    - `Persona Brand/MQ - WIN Flavor/internal-links-WIN-Flavor.md` (For internal link matching)
- **Constraint**: 
    1. Writer must strict follow "WIN Flavor" identity (Never use "chúng tôi").
    2. Maintain "Professional but Simple" voice (Grade 5 readability, No Fluff) as per `persona-WIN-Flavor-skill.md`. 
    3. Follow the "Ingredient-First" rule.
    4. **Max 5 H2s** - use rich subheadings (H3/H4) for depth.
    5. **Content Depth Hierarchy**: Apply depth labels from outline. Core content gets full treatment; supplementary knowledge stays brief; definitions fit in 1 paragraph.
    6. **B2B Tone**: Address enterprise F&B clients directly - xưởng sản xuất, nhà máy, đội ngũ R&D, doanh nghiệp F&B. Avoid consumer-facing language.
    7. **Internal Links**: Cross-reference `internal-links-WIN-Flavor.md` to insert 3-7 topically relevant internal links with natural Vietnamese anchor text.
- **Output**: `article.md` (Draft 1)
- **MANDATORY**: The article MUST start with an **SEO Metadata Table** before the H1 heading. Use this exact format (use short dashes `-`/`--` for outline hierarchy, never em dashes):

```markdown
| | |
|---|---|
| **Keyword chính** | [primary keyword] |
| **Keyword phụ** | [secondary keyword 1] |
| | [secondary keyword 2] |
| | ... |
| **Slug** | [keyword-slug] |
| **Meta title** | [optimized title with keyword + freshness year] |
| **Meta description** | [compelling 155-char description with keyword] |
| **Outline** | H1: [title] |
| | - H2: [section] |
| | -- H3: [subsection] |
| | ... |

---
```

## 7. Phase 6: WIN Flavor Brand Calibration
**Goal**: Polish the draft into a true WIN Flavor asset.

- **Skill**: `Persona Brand/MQ - WIN Flavor/persona-WIN-Flavor-skill.md`
- **Input**: `article.md` (Draft 1)
- **Actions**:
    1.  **Identity Check**: Ensure ALL references use "**WIN Flavor**" (Remove all "chúng tôi").
    2.  **Simplicity Audit**: Enforce Grade 5 readability. Remove jargon/fluff unless explained simply.
    3.  **Tone Audit**: Apply "Expert Scientist" and "Solution-Oriented" filters. Ensure B2B F&B tone throughout.
    4.  **Signature**: Ensure correct Signature from `central-entity-WIN-Flavor.md`.
    5.  **Expert Remarks**: Inject 1-2 blockquotes containing expert advice or insights. Do NOT prefix with "Chuyên gia WIN Flavor:" or any brand name. The blockquote should stand alone as objective expert insight.
    6.  **H2 Cap Check**: Verify article has maximum 5 H2 headings. Merge any excess into existing H2s as subheadings.
    7.  **Internal Link Audit**: Verify 3-7 internal links from `internal-links-WIN-Flavor.md` are present with natural anchor text.
    8.  **Content Depth Check**: Verify core content is detailed, supplementary is brief, definitions are 1-paragraph.
- **Output**: `article.md` (WIN Flavor Branded Version)

## 8. Phase 7: Fact-Checking & Deep Research (Optimized)
**Goal**: 100% scientific accuracy via targeted validation.

- **Skill**: `.agent/skills/rechecking-facts/SKILL.md`
- **Action**: Use `search_web` with **Advanced Operators**:
    - `site:vfa.gov.vn "[Decree_Number]"` to verify regulatory compliance.
    - `"[Chemical_Name] solubility/dosage"` to verify technical specs.
    - Search for WIN Flavor specific solutions in `central-entity-WIN-Flavor.md` to ensure correct attribution.
- **Output**: `fact-check-report.md` + Corrected `article.md`

## 10. Phase 9: Final Audit & Validation
**Goal**: Zero-defect delivery. Ensure the article matches Research, Outline, AND Persona.

- **Skill**: `.agent/skills/auditing-content/SKILL.md`
- **Inputs**:
    - `article.md` (Final Candidate)
    - `search-intent.md` (Intent Baseline)
    - `outline.md` (Structure Baseline)
    - `research.md` (Semantic Baseline)
    - `Persona Brand/MQ - WIN Flavor/source-context-WIN-Flavor.md` (Context Baseline)
    - `Persona Brand/MQ - WIN Flavor/central-entity-WIN-Flavor.md` (Entity Baseline)
- **Action**:
    - Auto-run `/content-audit`.
    - If Critical Issues found: **Auto-fix** or Request User Review.
- **Output**: `audit-report.md` + Final `article.md`

## 10. Final Delivery
- Notify user of completion.
- List all artifacts: `search-intent.md`, `research.md`, `competitor-insights.md`, `outline.md`, `fact-check-report.md`, `article.md`, `audit-report.md`.
