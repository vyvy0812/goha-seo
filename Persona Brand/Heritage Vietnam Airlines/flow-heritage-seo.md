---
description: Premium B2B Semantic SEO Workflow with Heritage Vietnam Airlines Brand Integration & Quality Audit
---

# Heritage Branded SEO Workflow

This is the **Premium Content Pipeline** for **Heritage Vietnam Airlines**.
It enforces strict adherence to **Semantic SEO**, **Cultural Depth**, and the **Heritage Brand Persona** ("The Cultural Bridge").

**Command:** `/heritage-seo [keyword]`

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
- **Output**: `outline.md`

## 6. Phase 5: Aesthetic Writing (Drafting)
**Goal**: Write the "Poetic & Evocative" draft.

- **Skill**: `.agent/skills/writing-semantic-content/SKILL.md`
- **Inputs**: `outline.md`, `research.md`, `Persona Brand/Heritage Vietnam Airlines/source-context-Heritage.md`.
- **Constraint**: Use the rich, descriptive lexicon defined in `persona-Heritage-skill.md`. 
- **Constraint**: **Paragraphs must not exceed 4 lines** for optimal readability (UX).
- **Output**: `article.md` (Draft 1)

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

## 9. Phase 8: Final Audit & Validation
**Goal**: Zero-defect delivery for a national-level publication.

- **Skill**: `.agent/skills/auditing-content/SKILL.md`
- **Output**: `audit-report.md` + Final `article.md`
