---
description: Automated Semantic SEO Content Creation Process (Research -> Outline -> Article)
---

# Semantic SEO Workflow

This workflow automates the creation of high-quality SEO content based on the Semantic SEO methodology.

**Command:** `/semantic-seo [keyword]`

## 1. Preparation
- **Input**: User provides a target keyword (e.g., "Cách report DMCA website").
- **Action**: Create a designated folder for the keyword.
   > `Keywords/keyword/[keyword-slug]`

## 2. Phase 1: Semantic Research
- **Skill**: `.agent/skills/extracting-keywords/SKILL.md`
- **Output**: `research.md`
- **Goal**: Analyze Entity Map, Query Clusters, and User Intent.

## 3. Phase 2: Content Outline
- **Skill**: `.agent/skills/generating-outlines/SKILL.md`
- **Input**: `research.md`
- **Output**: `outline.md`
- **Goal**: Create a structured outline with Header, Hook, Body (Google/Hosting/Social), Semantic Expansion, and FAQ.

## 4. Phase 3: Content Writing
- **Skill**: `.agent/skills/writing-semantic-content/SKILL.md`
- **Input**: `research.md` + `outline.md`
- **Output**: `article.md`
- **Goal**: Draft the complete article following the 6-part Semantic SEO structure.



## 5. Phase 4: Fact-Checking & Deep Research
- **Skill**: `.agent/skills/rechecking-facts/SKILL.md`
- **Input**: `article.md`
- **Output**: `fact_check_report.md` (and corrected `article.md`)
- **Goal**: Safeguard against AI hallucinations. Verify all technical claims, pricing, and entities against authoritative sources.

## 6. Final Output
- Notify user that the process is complete.
- Provide paths to all 4 artifacts: `research.md`, `outline.md`, `fact-check-report.md`, `article.md`.

---

**Example Usage:**
> User: /semantic-seo "cach cham soc meo con"
> Agent: I will now execute the Semantic SEO workflow for "cach cham soc meo con"...
