---
description: Premium B2B Semantic SEO Workflow with Heritage Vietnam Airlines Brand Integration & Quality Audit
---

# Heritage Branded SEO Workflow

This is the **Premium Content Pipeline** for **Heritage Vietnam Airlines**.
It enforces strict adherence to **Semantic SEO**, **Cultural Depth**, and the **Heritage Brand Persona** ("The Cultural Bridge").

**Command:** `/heritage-seo [keyword]`

**Global Quality Rules:**
1. **Content Freshness**: MUST use `search_web` to verify the latest cultural events, travel information, and destination details before writing. Always reference the most current sources. Never rely on outdated information.
2. **No Emoji**: Articles must NOT contain any emoji characters (⭐, ⚠️, 🔥, etc.). Use text labels like **(MỚI)**, **Lưu ý**, **Quan trọng** instead.
3. **No Em Dash**: Never use em dash (—) in articles. Always use short dash (-) instead.
4. **Key Takeaways**: Every article MUST include a `[key_takeaways]...[/key_takeaways]` shortcode block after the intro paragraph (before the first image). Contains 5-7 bullet points summarizing the most important facts. MUST have a blank line before `[/key_takeaways]`.
5. **No Brand Prefix in Expert Remarks**: Blockquote expert remarks must NOT be prefixed with brand name. The blockquote stands alone as objective expert insight.
6. **Keyword Density**: The **primary keyword** MUST appear **5-10 times** in the article body (excluding metadata table), scaled by content length. All **secondary keywords** and **semantic/LSI keywords** from `research.md` MUST also appear at least once naturally in the article. Verify keyword presence during the Audit phase.

---

## 1. Preparation
- **Input**: User provides a target keyword (e.g., "du lịch huế", "văn hóa trà việt").
- **Action**: Create a designated folder: `Keywords/Heritage/[keyword-slug]` (Ensure parent folder `Keywords/Heritage` exists).
- **Prerequisite Check**: Ensure these files exist in the workspace:
    - `Persona Brand/Heritage Vietnam Airlines/source-context-Heritage.md`
    - `Persona Brand/Heritage Vietnam Airlines/central-entity-Heritage.md`
    - `Persona Brand/Heritage Vietnam Airlines/persona-Heritage-skill.md`

## 2. Phase 1: Search Intent Analysis
**Goal**: Decode the traveler's intent (Inspiration vs. Planning vs. Booking).

- **Action**: Use `search_web [keyword]` to analyze SERP features.
- **Skill**: `.agent/skills/analyzing-search-intent/SKILL.md`
- **Output**: `search-intent.md`

## 3. Phase 2: Semantic & Cultural Research
**Goal**: Establish the semantic foundation with deep cultural entities.

- **Action**: Use `search_web` to find historical facts, cultural significance, and "hidden gems".
- **Action**: Search for related articles on `heritagevietnamairlines.com` to ensure consistency.
- **Skill**: `.agent/skills/extracting-keywords/SKILL.md`
- **Output**: `research.md` (Must include core cultural entities).

## 4. Phase 3: Competitor Intelligence
**Goal**: Benchmark against other high-end travel and lifestyle magazines.

- **Action**: Analyze Top 3 ranking results for the keyword.
- **Skill**: `.agent/skills/analyzing-competitors/SKILL.md`
- **Output**: `competitor-insights.md`

## 5. Phase 4: Strategic Outline
**Goal**: Create a superior outline merging semantic data, cultural storytelling, and Heritage's unique angle.

- **Skill**: `.agent/skills/generating-outlines/SKILL.md`
- **Inputs**: `search-intent.md`, `research.md`, `competitor-insights.md`, `Persona Brand/Heritage/central-entity-Heritage.md`.
- **Constraint**: Every outline MUST have a section dedicated to "Cultural Significance" or "Heritage Insight".
- **Constraint**: If listing travel destinations, the outline MUST include a comprehensive list (minimum 8-12 locations) to ensure topical authority.
- **Output**: `outline.md`

## 6. Phase 5: Aesthetic Writing (Drafting)
**Goal**: Write the "Poetic & Evocative" draft.

- **Skill**: `.agent/skills/writing-semantic-content/SKILL.md`
- **Inputs**: `outline.md`, `research.md`, `Persona Brand/Heritage Vietnam Airlines/source-context-Heritage.md`.
- **Constraint**: Use the rich, descriptive lexicon defined in `persona-Heritage-skill.md`. 
- **Constraint**: Every listed destination/location MUST explicitly include a detailed, exact address in its Hard Data section (e.g., number, street, ward).
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

## 7. Phase 6: Heritage Brand Calibration
**Goal**: Polish the draft into a true Heritage masterpiece.

- **Skill**: `Persona Brand/Heritage Vietnam Airlines/persona-Heritage-skill.md`
- **Input**: `article.md` (Draft 1)
- **Actions**:
    1. **Tone Audit**: Apply "Elegance" and "Sophistication" filters.
    2. **Aviation Integration**: If relevant, subtly mention Vietnam Airlines' flights to the destination.
- **Output**: `article.md` (Heritage Branded Version)

## 8. Phase 7: Fact-Checking & Deep Research
**Goal**: Verify historical dates, cultural terminology, and aviation details.

- **Skill**: `.agent/skills/rechecking-facts/SKILL.md`
- **Output**: `fact-check-report.md` + Corrected `article.md`

## 10. Phase 9: Final Audit & Validation
**Goal**: Zero-defect delivery for a national-level publication.

- **Skill**: `.agent/skills/auditing-content/SKILL.md`
- **Output**: `audit-report.md` + Final `article.md`
