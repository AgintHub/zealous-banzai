# perform_competitive_analysis PRD

## Description
Conduct a competitive analysis to understand the market and regulatory environment for the device.


## Implementation Plan

### 1. Gather a list of all FDA‑registered medical devices that serve the same clinical indication and share similar technology or intended use.

| Category | Details |
| --- | --- |
| **Reason** | Ensures the analysis covers the complete competitive set relevant to the device’s regulatory pathway. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use FDA’s 510(k) database, PMA database, and De Novo database; filter by product code, indication, and technology classification; export results to a CSV. |

### 2. Parse the exported CSV to extract competitor names, product codes, and regulatory status, and store them in structured data frames.

| Category | Details |
| --- | --- |
| **Reason** | Provides a clean, machine‑readable format for downstream calculations and reporting. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Apply Python pandas to read CSV, rename columns, and handle missing values; output DataFrame with columns: Name, RegStatus. |

### 3. Calculate the market share percentage for each competitor by aggregating sales data from publicly available sources (e.g., IQVIA, FDA reports) and normalizing against total market sales.

| Category | Details |
| --- | --- |
| **Reason** | Quantifies each competitor’s market footprint, which is critical for strategic positioning. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Scrape sales data, clean and merge with competitor list; compute share = (competitor sales / total market sales) * 100; round to two decimals. |

### 4. Map each competitor’s regulatory status to the appropriate pathway (510(k), PMA, De Novo) using FDA’s classification tables and cross‑reference with the research_fda_regulations output.

| Category | Details |
| --- | --- |
| **Reason** | Aligns market analysis with regulatory constraints, ensuring compliance considerations are integrated. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Create a lookup dictionary from research_fda_regulations; apply to competitor DataFrame; store results in the regulatory_status list. |

### 5. Identify differentiation factors by comparing the device’s technical specifications (e.g., sensor type, algorithmic processing, cost) against each competitor’s documented features.

| Category | Details |
| --- | --- |
| **Reason** | Highlights unique selling propositions that can be leveraged in the submission and marketing. |
| **Impact** | HIGH |
| **Complexity** | HIGH |
| **Method** | Extract feature sets from product datasheets and regulatory submissions; use set operations to compute differences; generate descriptive strings for each factor. |

### 6. Summarize strengths and weaknesses for each competitor by reviewing FDA clearance letters, clinical study results, and post‑market surveillance data.

| Category | Details |
| --- | --- |
| **Reason** | Provides a balanced view of the competitive landscape, informing risk mitigation and product development. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Parse clearance letters for performance metrics; extract adverse event statistics; create bullet points using natural language generation templates. |

### 7. Draft a concise analysis summary that synthesizes market share trends, regulatory environment, and differentiation insights into strategic recommendations for the device.

| Category | Details |
| --- | --- |
| **Reason** | Delivers a high‑level narrative that can be used by stakeholders to make informed decisions. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Aggregate key findings into a structured paragraph; include tables or charts for visual emphasis; ensure alignment with the device’s regulatory strategy. |

### 8. Validate the final output fields against the defined output structure, ensuring type consistency (List[str], List[float], str) and completeness.

| Category | Details |
| --- | --- |
| **Reason** | Guarantees that downstream nodes receive correctly formatted data, preventing integration errors. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Implement unit tests that check each field’s type and presence; run a validation script before exporting results. |
