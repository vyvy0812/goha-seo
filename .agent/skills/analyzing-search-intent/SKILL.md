---
name: analyzing-search-intent
description: >
  Deeply analyzes search intent using a 7-type classification model and Google's Micro-Intent framework.
  Provides specific content format recommendations and SERP feature predictions.
  Triggers: analyze intent, search intent analysis, check user intent, /analyze-intent
---

# Analyzing Search Intent

## Purpose
To move beyond basic "Info/Trans" labeling and provide a granular 7-point analysis of what the user actually wants, aligned with Google's latest Quality Rater Guidelines (Know/Do/Go).

## Process

### Phase 1: Context Gathering

#### Entry Check
```
IF User provided (Keyword/Topic):
    → Proceed to Phase 2
ELSE:
    → Ask: "What keyword or topic would you like me to analyze?"
```

### Phase 2: Classification (The 7-Type Model)

#### Actions
Analyze the keyword against the 7 primary types (see `references/intent-definitions.md`).

1.  **Identify Primary Intent**: Is it mostly Info, Trans, Comm, Nav, Brand, News, or Local?
2.  **Identify Secondary Intent**: (e.g., "Best Italian restaurant" is both Commercial and Local).
3.  **Micro-Intent Check**:
    *   Is it **Know Simple**? (Fact check, e.g., "Height of Eiffel Tower") -> *Warning: Low generic traffic potential.*
    *   Is it **Do**? (Buy, Download) -> *Requires clear CTA.*
    *   Is it **Visit**? -> *Requires Local SEO.*

### Phase 3: Content & SERP Mapping

#### Actions
Based on the classification, determine the required content vehicle.

| Intent Found | Mandatory Content Elements |
|--------------|----------------------------|
| **Informational** | Comprehensive Guide, Definitions, "How-to" steps, Images/Video. |
| **Commercial** | Comparison data, Top X lists, Reviews, Buying guides. |
| **Transactional** | Clear "Buy/Download" buttons, Trust signals, Pricing. |
| **Local** | Map embed, Address, Phone, Hours, Local schema. |
| **Brand** | About page, Homepage, Official profiles. |

### Phase 4: Output Generation

Generate a succinct Intent Report:

> **Keyword**: [Keyword]
> **Primary Intent**: [Type] (Confidence: High/Med/Low)
> **Micro-Intent**: [Know/Do/Go]
> **User Motivation**: [One sentence describing what the user wants to achieve]
> **Recommended Format**: [Blog/LP/Product/Tool/etc.]
> **SERP Features**: [Predicted features like Snippets, Maps, etc.]

## Self-Check (Read before outputting)

□ Did I distinguish between "Commercial" (investigation) and "Transactional" (action)?
  → "Best shoes" is Commercial. "Buy Nike Air Max" is Transactional.

□ Did I check for "Know Simple"?
  → If the answer is a single number or name, warn the user about "Zero-click" risk.

□ Is the Local intent overlooked?
  → Words like "near me", city names, or service searches (plumber) often imply Local.

## References
*   `references/intent-definitions.md`: Complete definitions of the 7 intent types and Know/Do/Go framework.
