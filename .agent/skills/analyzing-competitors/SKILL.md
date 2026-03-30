---
name: analyzing-competitors
description: >
  Analyzes top 3 Google SERP competitors to extract heading structures and content gaps.
  Saves detailed outlines to separate files for precise referencing.
  Triggers: analyze competitors, phan tich doi thu, competitor research, /analyze-competitors
---

# Analyzing Competitors (Live SERP)

## Purpose
To extract real-time data from Search Engine Results Pages (SERP) and capture the **exact** heading structure (H1-H3) of top competitors. This raw data is saved into separate files to ensure high fidelity and ease of reference for subsequent content creation steps.

## Process

### Phase 1: Input Validation

#### Entry Check
```
IF target keyword is provided:
    → Proceed to Phase 2
ELSE:
    → Ask: "What is the target keyword you want to analyze?"
```

### Phase 2: Live Search & Selection

#### Actions
1.  **Execute Search**: Use `search_web` with the **Target Keyword**.
2.  **Filter Results**:
    *   Select **Top 3 Organic Results**.
    *   **EXCLUDE**: Youtube, E-commerce (Shopee/Lazada), Social Media, Forums (Reddit/Voz).
    *   **INCLUDE**: Articles, Blogs, Landing Pages.

### Phase 3: Extraction & File Generation

#### Actions
For each selected URL (Top 3):
1.  **Read Content**: Use `read_url_content`.
2.  **Extract Structure**:
    *   Identify H1, H2, H3 hierarchy.
    *   *Constraint*: Must be exact heading text from the page. Do not summarize.
3.  **Generate Individual Files**:
    *   Create a directory `competitors` if it doesn't exist.
    *   Create file: `competitors/competitor_[N]_[domain].md` (e.g., `competitors/competitor_1_searchenginejournal.md`).
    *   **File Content Pattern**:
        ```markdown
        # Competitor [N] Analysis
        **Source URL**: [URL]
        **Title**: [Page Title]

        ## Heading Structure
        [Paste exact H1, H2, H3 hierarchy here]
        ```

### Phase 4: Insight Synthesis

#### Actions
Create (or overwrite) `competitor-insights.md` to summarize the findings.

**File Content Pattern**:
```markdown
# Competitor Insights: [Target Keyword]

## Overview
I have analyzed the following top competitors and saved their detailed outlines to the `competitors/` directory:
1.  [Title](competitors/competitor_1_domain.md)
2.  [Title](competitors/competitor_2_domain.md)
3.  [Title](competitors/competitor_3_domain.md)

## SEO-Useful Headings from Competitors
Review ALL H2/H3 headings across competitors and classify:
| Heading Topic | Source | Classification | Notes |
|--------------|--------|---------------|-------|
| [Topic] | Competitor [N] | MUST INCLUDE / NICE TO HAVE / SKIP | [Why] |

*MUST INCLUDE items will be integrated into the outline in Phase 4.*

## Strategic Analysis
*   **Common Angles**: [Patterns common across all 3]
*   **Content Gaps**: [What crucial topics did they ALL miss?]
*   **Structure Recommendations**: [How should we organize our H2s based on this?]
```

## Self-Check (Read before outputting)

□ Did I create SEPARATE files for each competitor?
  → This is critical for the user to "view_file" them later without noise.

□ Is the heading extraction EXACT?
  → Do not paraphrase. We need to see exactly what keywords they used in headers.

□ Did I link the separate files in the summary?
  → The user needs clickable links in the report.

□ Did I exclude generic sites?
  → No Shopee, no Youtube. Only content competitors.

□ Did I classify competitor headings by SEO usefulness?
  → Every H2/H3 must be tagged as MUST INCLUDE, NICE TO HAVE, or SKIP. This feeds directly into the outline generation phase.
