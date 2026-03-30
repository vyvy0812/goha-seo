---
description: Premium B2B Semantic SEO Workflow with Trung Nguyên TNT Brand Integration & Quality Audit
---

# Trung Nguyên TNT Branded SEO Workflow

This is the **Premium Content Pipeline** for Trung Nguyên TNT (The Automation Engineer).
It enforces strict adherence to **Semantic SEO**, **Competitor Benchmarking (Flow Alignment)**, and the **Trung Nguyên TNT Brand Persona** ("Helpful Industrial Engineer").
9: **MANDATORY**: Minimum **2500 words** with deep "Technical Gap Content".

**Command:** `/trung-nguyen-seo [keyword]`

**Global Quality Rules:**
1. **Content Freshness**: MUST use `search_web` to verify the latest technical specifications, machine models, and industry standards before writing. Always reference the most current sources. Never rely on outdated information.
2. **No Emoji**: Articles must NOT contain any emoji characters (⭐, ⚠️, 🔥, etc.). Use text labels like **(MỚI)**, **Lưu ý**, **Quan trọng** instead.
3. **No Em Dash**: Never use em dash (—) in articles. Always use short dash (-) instead.
4. **Key Takeaways**: Every article MUST include a `[key_takeaways]...[/key_takeaways]` shortcode block after the intro paragraph (before the first image). Contains 5-7 bullet points summarizing the most important facts. MUST have a blank line before `[/key_takeaways]`.
5. **No Brand Prefix in Expert Remarks**: Blockquote expert remarks must NOT be prefixed with brand name (e.g., "Kỹ sư Trung Nguyên TNT:", "Chuyên gia X:"). The blockquote stands alone as objective expert insight.
6. **Keyword Density**: The **primary keyword** MUST appear **5-10 times** in the article body (excluding metadata table), scaled by content length. All **secondary keywords** and **semantic/LSI keywords** from `research.md` MUST also appear at least once naturally in the article. Verify keyword presence during the Audit phase.

---

## 1. Preparation
- **Input**: User provides a target keyword.
- **Action**: Create a designated folder: `Keywords/Trung Nguyên TNT/[keyword-slug]` (Ensure parent folder `Keywords/Trung Nguyên TNT` exists)
- **Prerequisite Check**: Ensure these files exist in the workspace:
    - `Persona Brand/Trung Nguyên TNT/source-context-Trung-Nguyen-TNT.md`
    - `Persona Brand/Trung Nguyên TNT/central-entity-Trung-Nguyen-TNT.md`

## 2. Phase 1: Search Intent Analysis (Optimized)
**Goal**: Decode the user's hidden Micro-Intent (Know/Do/Go) using live SERP data.

- **Action**: Use `search_web [keyword]` to analyze SERP features:
    - If **Local Pack**: Searcher is looking for nearby factories/suppliers.
    - If **Featured Snippet**: Informational (Know).
- **Skill**: `.agent/skills/analyzing-search-intent/SKILL.md`
- **Output**: `search-intent.md`

## 3. Phase 2: Semantic & Contextual Research (Optimized)
**Goal**: Establish the semantic foundation with real-time industrial entity discovery.

- **Action**: Use `search_web` with operators:
    - `"máy [keyword] thông số kỹ thuật"` to find machine specs.
    - `site:trungnguyentnt.vn "[keyword]"` to verify existing brand alignment.
    - Analyze related searches to compile **Secondary Keywords** and **LSI/Semantic Keywords** (e.g., related pain points, parts, actions).
- **Skill**: `.agent/skills/extracting-keywords/SKILL.md`
- **Inputs**:
    - Target Keyword
    - `search-intent.md`
    - `Persona Brand/Trung Nguyên TNT/source-context-Trung-Nguyen-TNT.md`
- **Constraint**: Ensure "Máy chấm keo PVC" are EXCLUDED unless specifically targeted.
- **Constraint**: MUST explicitly provide a list of "Secondary Keywords" and "Semantic Constraints" in the output file.
- **Output**: `research.md` (Integrate live specs, brand context, and secondary keywords).

## 4. Phase 3: Competitor Intelligence (Turbo)
**Goal**: Benchmark against top ranking content structures.

// turbo
- **Skill**: `.agent/skills/analyzing-competitors/SKILL.md`
- **Action**: Use the `browser_subagent` tool to perform a live Google search for the target keyword on the user's machine.
- **Action**: Create a subdirectory `competitors/` inside the keyword folder.
- **Action**: Visit the Top 3 Organic Results. Extract H1, H2, H3 headers and save each to `competitors/competitor_[n]_[domain].md`.
- **Output**: `competitor-insights.md` (Save summary in root, raw details in `competitors/`)

## 5. Phase 4: Strategic Outline
**Goal**: Create a technical and efficiency-driven outline merging semantic data and Trung Nguyên TNT capabilities.

- **Skill**: `.agent/skills/generating-outlines/SKILL.md`
- **Inputs**:
    - `search-intent.md` (For Format & Micro-Intent alignment)
    - `research.md`
    - `competitor-insights.md`
    - `Persona Brand/Trung Nguyên TNT/central-entity-Trung-Nguyen-TNT.md` (To map relevant Machines & Solutions)
- **Constraint**: MUST map at least one Trung Nguyên TNT Machine/Solution (from `central-entity`) as a key solution in the outline.
- **MANDATORY STRUCTURE**: Follow top competitors' successful flow (likely: Definitions -> Deep Comparison -> Selection Guide -> FAQ).
- **MANDATORY DEPTH**: Must plan for 2500+ words by including Technical Data Sheets (TDS), polymer physics, and "Gap Content" (e.g., Burn tests) identified in Phase 3.
- **MANDATORY COMPETITOR INTEGRATION**: 
    - Review ALL individual competitor files in `competitors/competitor_[n]_[domain].md`.
    - Identify heading topics (H2/H3) from competitors that are **useful for SEO** (e.g., "Cấu tạo chung", "Ứng dụng trong sản xuất", specific product categories).
    - **MUST incorporate** these useful competitor heading topics into the outline as H2 or H3 sections.
    - Do NOT copy competitor headings verbatim — adapt them with deeper technical content and TNT's "Kỹ sư công nghiệp" voice.
    - Mark integrated competitor topics with `[FROM COMPETITOR]` tag in the outline for traceability.
- **Output**: `outline.md`

## 6. Phase 5: Authority Writing (Drafting)
**Goal**: Write the "Industrial Engineer" draft.

- **Skill**: `.agent/skills/writing-semantic-content/SKILL.md`
- **Inputs**:
    - `search-intent.md` (For Tone & CTA alignment)
    - `research.md` (For Specs & Secondary Keywords)
    - `outline.md`
    - `competitors/` directory (Reference competitor heading structures to ensure no important SEO topic is missed)
    - `Persona Brand/Trung Nguyên TNT/source-context-Trung-Nguyen-TNT.md` (Mandatory Stylistic Context)
- **Constraint**: 
    1. Writer must follow "Trung Nguyên TNT" identity.
    2. Maintain "Helpful Industrial Engineer" voice (Value-First, Non-Promotional) as per `skill-persona-Trung-Nguyen-TNT.md`. 
    3. Follow the "Machine-Efficiency" Rule (Translate features to economic value).
    4. **Word Count**: Target **2500+ words** by providing exhaustive technical detail.
    5. **Semantic Injection**: Naturally weave the compiled Secondary and LSI keywords from `research.md` into the text to maximize entity coverage.
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

## 7. Phase 6: Trung Nguyên TNT Brand Calibration
**Goal**: Polish the draft into a true Trung Nguyên TNT asset.

- **Skill**: `Persona Brand/Trung Nguyên TNT/skill-persona-Trung-Nguyen-TNT.md`
- **Input**: `article.md` (Draft 1)
- **Actions**:
    1.  **Identity Check**: Ensure proper branding "Trung Nguyên TNT".
    2.  **Simplicity Audit**: Enforce clarity for factory owners.
    3.  **Tone Audit**: Apply "Industrial Engineer" and "Problem-Solver" filters.
    4.  **Signature**: Ensure correct Signature from `central-entity-Trung-Nguyen-TNT.md`.
8.  **Expert Remarks**: Inject 1-2 blockquotes containing expert advice or warnings. DO NOT prefix these quotes with "Kỹ sư Trung Nguyên TNT:" or any brand name. They should stand alone as objective expert insights (as defined in `skill-persona-Trung-Nguyen-TNT.md`).
- **Output**: `article.md` (Trung Nguyên TNT Branded Version)

## 8. Phase 7: Fact-Checking & Deep Research (Optimized)
**Goal**: 100% technical accuracy via targeted search validation.

- **Skill**: `.agent/skills/rechecking-facts/SKILL.md`
- **Action**: Use `search_web` with **Advanced Operators**:
    - `"[Machine_Model] datasheet"` to verify performance metrics.
    - `site:trungnguyentnt.vn` to confirm pricing or warranty claims.
    - Search for economic benefit metrics (e.g., labor reduction rates in plastics industry).
- **Output**: `fact-check-report.md` + Corrected `article.md`

## 10. Phase 9: Final Audit & Validation
**Goal**: Zero-defect delivery. Ensure the article matches Research, Outline, AND Persona.

- **Skill**: `.agent/skills/auditing-content/SKILL.md`
- **Inputs**:
    - `article.md` (Final Candidate)
    - `search-intent.md` (Intent Baseline)
    - `outline.md` (Structure Baseline)
    - `research.md` (Semantic Baseline)
    - `Persona Brand/Trung Nguyên TNT/source-context-Trung-Nguyen-TNT.md` (Context Baseline)
    - `Persona Brand/Trung Nguyên TNT/central-entity-Trung-Nguyen-TNT.md` (Entity Baseline)
- **Action**:
    - Auto-run `/content-audit`.
    - If Critical Issues found: **Auto-fix** or Request User Review.
- **Output**: `audit-report.md` + Final `article.md`

## 10. Final Delivery
- Notify user of completion.
- List all artifacts: `search-intent.md`, `research.md`, `competitor-insights.md`, `outline.md`, `fact-check-report.md`, `article.md`, `audit-report.md`.
