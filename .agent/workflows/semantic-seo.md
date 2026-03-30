---
description: Automated Semantic SEO Content Creation Process (Research -> Outline -> Article)
---

# Semantic SEO Workflow

This workflow automates the creation of high-quality SEO content based on the Semantic SEO methodology.

**Command:** `/semantic-seo [keyword]`

**Global Quality Rules:**
1. **Content Freshness**: MUST use `search_web` to verify the latest information, regulations, and industry data before writing. Always reference the most current sources. Never rely on outdated information.
2. **No Emoji**: Articles must NOT contain any emoji characters (⭐, ⚠️, 🔥, etc.). Use text labels like **(MỚI)**, **Lưu ý**, **Quan trọng** instead.
3. **No Em Dash**: Never use em dash (—) in articles. Always use short dash (-) instead.
4. **Key Takeaways**: Every article MUST include a `[key_takeaways]...[/key_takeaways]` shortcode block after the intro paragraph (before the first image). Contains 5-7 bullet points summarizing the most important facts. MUST have a blank line before `[/key_takeaways]`.
5. **No Brand Prefix in Expert Remarks**: Blockquote expert remarks must NOT be prefixed with brand name. The blockquote stands alone as objective expert insight.
6. **Keyword Density**: The **primary keyword** MUST appear **5-10 times** in the article body (excluding metadata table), scaled by content length. All **secondary keywords** and **semantic/LSI keywords** from `research.md` MUST also appear at least once naturally in the article. Verify keyword presence during the Audit phase.

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
