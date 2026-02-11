---
description: Premium B2B Semantic SEO Workflow with Trung Nguyên TNT Brand Integration & Quality Audit
---

# Trung Nguyên TNT Branded SEO Workflow

This is the **Premium Content Pipeline** for Trung Nguyên TNT (The Automation Engineer).
It enforces strict adherence to **Semantic SEO**, **Competitor Benchmarking**, and the **Trung Nguyên TNT Brand Persona** ("Efficiency through Automation").

**Command:** `/trung-nguyen-seo [keyword]`

---

## 1. Preparation
- **Input**: User provides a target keyword.
- **Action**: Create a designated folder: `Keywords/Trung Nguyên TNT/[keyword-slug]` (Ensure parent folder `Keywords/Trung Nguyên TNT` exists)
- **Prerequisite Check**: Ensure these files exist in the workspace:
    - `Persona Brand/Trung Nguyên TNT/source-context-Trung-Nguyen-TNT.md`
    - `Persona Brand/Trung Nguyên TNT/central-entity-Trung-Nguyen-TNT.md`

## 2. Phase 1: Search Intent Analysis (New)
**Goal**: Decode the user's hidden Micro-Intent (Know/Do/Go) before researching.

- **Skill**: `.agent/skills/analyzing-search-intent/SKILL.md`
- **Input**: Target Keyword
- **Output**: `search-intent.md`

## 3. Phase 2: Semantic & Contextual Research
**Goal**: Establish the semantic foundation filtered by Industrial Automation intent.

- **Skill**: `.agent/skills/extracting-keywords/SKILL.md`
- **Inputs**:
    - Target Keyword
    - `search-intent.md` (To align keywords with the verified intent)
    - `Persona Brand/Trung Nguyên TNT/source-context-Trung-Nguyen-TNT.md` (To filter for Plastics/Automation relevance)
    - `.agent/skills/analyzing-semantic-seo/references/entity-patterns.md` (For entity extraction rules)
- **Constraint**: Must use the "Automation Focus" and "Taiwan Quality" lens from `source-context-Trung-Nguyen-TNT.md` when selecting entities.
- **Constraint**: Ensure "Máy chấm keo PVC" (PVC Dispensing Machines) are EXCLUDED from the research unless the keyword specifically targets them.
- **Output**: `research.md` (Use **Template 2** from `references/output-templates.md` but enhanced with "Brand Context" notes).

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
- **Constraint**: MUST map at least one Trung Nguyên TNT Machine/Solution (from `central-entity`) as a key solution in the outline. EXCLUDE "Máy chấm keo PVC" (PVC Dispensing Machines) unless explicitly requested.
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
    2. Maintain "Technical & Accurate" voice (No Fluff, Data Speaks) as per `skill-persona-Trung-Nguyen-TNT.md`. 
    3. Follow the "Machine-Efficiency" Rule (Translate features to economic value).
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
    5.  **Expert Remarks**: Inject 1-2 `> **Kỹ sư Trung Nguyên TNT:**` blocks (as defined in `skill-persona-Trung-Nguyen-TNT.md`).
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

## 9. Phase 8: Final Audit & Validation
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
- List all artifacts: `search-intent.md`, `research.md`, `competitor-insights.md`, `outline.md`, `article.md`, `audit-report.md`.
