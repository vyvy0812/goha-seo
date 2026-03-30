---
name: auditing-content
description: >
  Validates SEO article quality against Outline and Research data.
  Ensures structural compliance, entity coverage, and search intent alignment.
  Triggers: audit content, check article, review draft, /audit-content
---

# Auditing Content

## Purpose
Ensures consistency and quality of the generated article (`article.md`) by cross-referencing it with the Outline (`outline.md`) and Research Data (`research.md`).

## Process

### Phase 1: Input Validation

#### Entry Check
```
IF files exist (article.md AND outline.md AND research.md):
    → Proceed to Phase 2
ELSE:
    → Identify missing file.
    → Ask user to provide or generate the missing artifact.
```

#### Optional Context Check
```
IF `search-intent.md` exists:
    → Load as Intent Baseline.
IF brand context files exist:
    → Activate Phase 3.5 (Brand Audit)
```

### Phase 2: Structural Verification (Outline vs Article)

#### Actions
For each section in `outline.md`:
1.  **Check Existence**: Is the corresponding heading present in `article.md`?
2.  **Evaluate Coverage**: Does the content reflect the outline's intent?
3.  **Note Discrepancies**: Missing sub-headings or "drifted" topics.

#### Output: Structure Check
```markdown
### 1. Structural Audit
| Outline Section | Article Match | Status | Notes |
|-----------------|---------------|--------|-------|
| [H2 Heading] | [Existing H2] | ✅/❌ | [Note coverage quality] |
```

### Phase 3: Semantic Verification (Research vs Article)

#### Actions
For entities in `research.md` (and `search-intent.md` if available):
1.  **Scan Usage**: Are key entities mentioned in `article.md`?
2.  **Context Check**: Are they used naturally?
3.  **Intent Check**:
    *   *Primary Source*: Check against `search-intent.md` (Micro-Intent: Know/Do/Go).
    *   *Secondary Source*: Check against `research.md` clusters (Info/Comm/Trans).
    *   **Verify**: Does the content answer the specific "User Motivation"?

#### Output: Semantic Check
```markdown
### 2. Semantic Audit
- **Primary Entities Used**: [List found]
- **Missing Entities**: [List missing vital entities]
- **Intent Alignment**: [Score 1-10] (Based on `search-intent.md`)
```

### Phase 3.5: Brand & Context Validation (Conditional)

#### Actions
*Only runs if context files are present.*
1.  **Vertical Check**: Does it stick to the domain defined in `source-context`?
2.  **Entity Check**: Are contact details/services consistent with `central-entity`?
3.  **Voice Check**: Does it sound like the defined persona?

### Phase 4: Reporting & Recommendations

#### Output Generation
Generate `audit-report.md`:
1.  **Summary Score** (1-10)
2.  **Critical Issues List**
3.  **Actionable Recommendations** (Specific additions, not generic advice)

## Self-Check (Read before auditing)

□ Did I actually read the content of all 3 files?
  → Don't guess based on filenames.

□ Am I being fair about heading variations?
  → If "Introduction" became "Getting Started", that's a match if content aligns.

□ Is the Semantic Check strict on "Entities"?
  → Ensure key terms from research are actually present contextually.

□ Are recommendations actionable?
  → "Add a paragraph about X in section Y" > "Make it better".
