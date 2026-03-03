---
description: Automated Semantic SEO Content Creation Process (Research -> Outline -> Article)
---

# Semantic SEO Workflow

This workflow automates the creation of high-quality SEO content based on the Semantic SEO methodology.

**Command:** `/semantic-seo [keyword]`

## 1. Preparation
- **Input**: User provides a target keyword.
- **Action**: Create a designated folder for the keyword.
   > `Keywords/keyword/[keyword-slug]`

## 2. Phase 1: Semantic Research & Intent Discovery
- **Action**: Use `search_web` to analyze current Google SERP features (Snippet, PAA, Local Pack) to confirm Micro-Intent.
- **Skill**: `.agent/skills/analyzing-search-intent/SKILL.md` (to document intent)
- **Skill**: `.agent/skills/extracting-keywords/SKILL.md` (to build entity map)
- **Optimization**: Use search operators like `"[keyword]"` for exact volume context and `site:.vn` for localized entities.
- **Output**: `research.md`
- **Goal**: Analyze Entity Map, Query Clusters, and User Intent with real-time data.

## 3. Phase 2: Content Outline
- **Skill**: `.agent/skills/generating-outlines/SKILL.md`
- **Input**: `research.md` (now containing real-time search data)
- **Output**: `outline.md`
- **Goal**: Create a structured outline with Header, Hook, Body, Semantic Expansion, and FAQ.

## 4. Phase 3: Content Writing
- **Skill**: `.agent/skills/writing-semantic-content/SKILL.md`
- **Input**: `research.md` + `outline.md`
- **Output**: `article.md`
- **Goal**: Draft the complete article following the 6-part Semantic SEO structure.

## 5. Phase 4: Fact-Checking & Deep Research (Optimized)
- **Skill**: `.agent/skills/rechecking-facts/SKILL.md`
- **Action**: Use `search_web` with **Advanced Operators**:
    - `site:[competitor_url] [claim]` to verify claims.
    - `"[technical_spec]"` to find official data sheets.
    - `lang:vi` or `lang:en` for specific source validation.
- **Input**: `article.md`
- **Output**: `fact_check_report.md` (and corrected `article.md`)
- **Goal**: Safeguard against AI hallucinations. Verify all technical claims against authoritative sources.

## 6. Final Output
- Notify user that the process is complete.
- Provide paths to all 4 artifacts: `research.md`, `outline.md`, `fact-check-report.md`, `article.md`.

---
