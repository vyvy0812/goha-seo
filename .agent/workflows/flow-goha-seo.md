---
description: Premium B2B Semantic SEO Workflow with GOHA Brand Integration & Quality Audit
---

# GOHA Branded SEO Workflow

This is the **Premium Content Pipeline** for GOHA (B2B Growth Architect).
It enforces strict adherence to **Semantic SEO**, **Competitor Benchmarking**, and the **GOHA Brand Persona** ("Evidence-Based Strategy").

**Command:** `/goha-seo [keyword]`

---

## 1. Preparation
- **Input**: User provides a target keyword.
- **Action**: Create a designated folder: `Keywords/GOHA/[keyword-slug]` (Ensure parent folder `Keywords/GOHA` exists)
- **Prerequisite Check**: Ensure these files exist in the workspace:
    - `Persona Brand/GOHA/source-context-GOHA.md`
    - `Persona Brand/GOHA/central-entity-GOHA.md`

## 2. Phase 1: Search Intent Analysis (Optimized)
**Goal**: Decode the user's hidden Micro-Intent (Know/Do/Go) using live SERP data.

- **Action**: Use `search_web [keyword]` to analyze SERP features:
    - If **Featured Snippet**: Informational (Know).
    - If **People Also Ask**: Query Clusters.
    - If **Ads/Products**: Transactional (Do).
- **Skill**: `.agent/skills/analyzing-search-intent/SKILL.md`
- **Output**: `search-intent.md`

## 3. Phase 2: Semantic & Contextual Research (Optimized)
**Goal**: Establish the semantic foundation with real-time entity discovery.

- **Action**: Use `search_web` with operators:
    - `"định nghĩa [keyword]"` to find core entities.
    - `site:.gov.vn OR site:.edu.vn "[keyword]"` for authority context.
- **Skill**: `.agent/skills/extracting-keywords/SKILL.md`
- **Inputs**:
    - Target Keyword
    - `search-intent.md`
    - `Persona Brand/GOHA/source-context-GOHA.md`
- **Output**: `research.md` (Must include real-time entities found via search).

## 4. Phase 3: Competitor Intelligence (Turbo)
**Goal**: Benchmark against top ranking content structures.

// turbo
- **Skill**: `.agent/skills/analyzing-competitors/SKILL.md`
- **Action**: Use the `browser_subagent` tool for a live Google search. Focus on "Results from last year" for freshness.
- **Action**: Visit Top 3 results. Extract H1-H3.
- **Output**: `competitor-insights.md`

## 5. Phase 4: Strategic Outline
**Goal**: Create a superior outline merging semantic data, competitor gaps, and GOHA services.

- **Skill**: `.agent/skills/generating-outlines/SKILL.md`
- **Inputs**:
    - `search-intent.md` (For Format & Micro-Intent alignment)
    - `research.md`
    - `competitor-insights.md`
    - `Persona Brand/GOHA/central-entity-GOHA.md` (To map relevant Services & Industries)
- **Constraint**: MUST map at least one GOHA Service (from `central-entity`) as a solution in the outline.
- **Output**: `outline.md`

## 6. Phase 5: Authority Writing (Drafting)
**Goal**: Write the "Evidence-Based" draft.

- **Skill**: `.agent/skills/writing-semantic-content/SKILL.md`
- **Inputs**:
    - `search-intent.md` (For Tone & CTA alignment)
    - `research.md`
    - `outline.md`
    - `Persona Brand/GOHA/source-context-GOHA.md` (Mandatory Stylistic Context)
- **Constraint**: Writer must strictly follow the "Speak the Truth" and "Data Speaks" rules from `source-context-GOHA.md`.
- **Output**: `article.md` (Draft 1)

## 7. Phase 6: GOHA Brand Calibration
**Goal**: Polish the draft into a true GOHA asset.

- **Skill**: `Persona Brand/GOHA/persona-goha-skill.md`
- **Input**: `article.md` (Draft 1)
- **Actions**:
    1. **Tone Audit**: Apply "Directness" and "Strategic Vision" filters.
    2. **Signature**: Ensure correct Signature from `central-entity-GOHA.md`.
    3. **Agency Remarks**: Inject 1-2 `> **GOHA Note:**` blocks.
- **Output**: `article.md` (GOHA Branded Version)

## 8. Phase 7: Visual Enhancement
**Goal**: Add visual depth with relevant industrial/business images.

- **Skill**: `.agent/skills/visualizing-content/SKILL.md`
- **Input**: `article.md` (GOHA Branded Version)
- **Action**:
    1.  **Analyze**: Identify key sections for visual aid.
    2.  **Search**: Find high-quality, relevant images (or placeholders).
    3.  **Insert**: Add `![Alt](Url)` to `article.md`.
- **Output**: `article.md` (Visualized Version)

## 9. Phase 8: Fact-Checking & Deep Research
**Goal**: Safeguard against AI hallucinations. Verify all digital marketing claims, B2B statistics, and strategic frameworks against the source of truth.

- **Skill**: `.agent/skills/rechecking-facts/SKILL.md`
- **Input**: `article.md` (Visualized Version)
- **Action**:
    - Extract verifiable claims (marketing stats, algorithm updates, service definitions).
    - Perform deep targeted research using `search_web`.
    - Directly correct any inaccurate facts or hallucinated metrics in the article.
- **Output**: `fact-check-report.md` + Corrected `article.md`

## 10. Phase 9: Final Audit & Validation
**Goal**: Zero-defect delivery. Ensure the article matches Research, Outline, AND Persona.

- **Skill**: `.agent/skills/auditing-content/SKILL.md`
- **Inputs**:
    - `article.md` (Final Candidate)
    - `search-intent.md` (Intent Baseline)
    - `outline.md` (Structure Baseline)
    - `research.md` (Semantic Baseline)
    - `Persona Brand/GOHA/source-context-GOHA.md` (Context Baseline)
    - `Persona Brand/GOHA/central-entity-GOHA.md` (Entity Baseline)
- **Action**:
    - Auto-run `/content-audit`.
    - If Critical Issues found: **Auto-fix** or Request User Review.
- **Output**: `audit-report.md` + Final `article.md`

## 10. Final Delivery
- Notify user of completion.
- List all artifacts: `search-intent.md`, `research.md`, `competitor-insights.md`, `outline.md`, `fact-check-report.md`, `article.md`, `audit-report.md`.
