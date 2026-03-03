---
description: Premium B2B Semantic SEO Workflow with Trung Nguyên TNT Brand Integration & Quality Audit
---

# Trung Nguyên TNT Branded SEO Workflow

This is the **Premium Content Pipeline** for Trung Nguyên TNT (The Automation Engineer).
It enforces strict adherence to **Semantic SEO**, **Competitor Benchmarking (Flow Alignment)**, and the **Trung Nguyên TNT Brand Persona** ("Helpful Industrial Engineer").
9: **MANDATORY**: Minimum **2500 words** with deep "Technical Gap Content".

**Command:** `/trung-nguyen-seo [keyword]`

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
- **Skill**: `.agent/skills/extracting-keywords/SKILL.md`
- **Inputs**:
    - Target Keyword
    - `search-intent.md`
    - `Persona Brand/Trung Nguyên TNT/source-context-Trung-Nguyen-TNT.md`
- **Constraint**: Ensure "Máy chấm keo PVC" are EXCLUDED unless specifically targeted.
- **Output**: `research.md` (Integrate live specs and brand context).

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
- **Output**: `outline.md`

## 6. Phase 5: Authority Writing (Drafting)
**Goal**: Write the "Industrial Engineer" draft.

- **Skill**: `.agent/skills/writing-semantic-content/SKILL.md`
- **Inputs**:
    - `search-intent.md` (For Tone & CTA alignment)
    - `research.md`
    - `outline.md`
    - `Persona Brand/Trung Nguyên TNT/source-context-Trung-Nguyen-TNT.md` (Mandatory Stylistic Context)
- **Constraint**: 
    1. Writer must follow "Trung Nguyên TNT" identity.
    2. Maintain "Helpful Industrial Engineer" voice (Value-First, Non-Promotional) as per `skill-persona-Trung-Nguyen-TNT.md`. 
    3. Follow the "Machine-Efficiency" Rule (Translate features to economic value).
    4. **Word Count**: Target **2500+ words** by providing exhaustive technical detail.
- **Output**: `article.md` (Draft 1)

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

## 8. Phase 7: Visual Enhancement
**Goal**: Add visual depth with relevant industrial automation images.

- **Skill**: `.agent/skills/visualizing-content/SKILL.md`
- **Input**: `article.md` (Trung Nguyên TNT Branded Version)
- **Action**:
    1.  **Analyze**: Identify key sections for visual aid.
    2.  **Search**: Find high-quality, relevant images (or placeholders).
    3.  **Insert**: Add `![Alt](Url)` to `article.md`.
- **Output**: `article.md` (Visualized Version)

## 9. Phase 8: Fact-Checking & Deep Research (Optimized)
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
