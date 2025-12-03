# address_fda_comments_and_questions PRD

## Description
Verify that all comments and questions are resolved and that the submission meets the FDA's requirements.


## Implementation Plan

### 1. Extract the list of pending FDA comments and questions from the parent node 'track_fda_review_progress' output field 'pending_requests', mapping each entry to a structured object containing its identifier, title, and the associated query text.

| Category | Details |
| --- | --- |
| **Reason** | Provides a concrete, machine‑readable set of items to address, eliminating ambiguity in the resolution process. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use JSON parsing to read the 'pending_requests' array, then apply a regex or NLP tokenization to separate identifiers and titles; store results in a local list of dictionaries. |

### 2. For each extracted comment, locate the corresponding detailed query text within the submission package (e.g., design control files, testing reports) by cross‑referencing the identifier with document metadata stored in a central index.

| Category | Details |
| --- | --- |
| **Reason** | Ensures that the response is based on the most accurate and up‑to‑date information available in the submission documentation. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Maintain a mapping table of document IDs to file paths; query the table using the comment identifier, then load the document content (PDF/Word) via a document‑processing library (e.g., PyMuPDF, python-docx). |

### 3. Generate a concise, FDA‑compliant response for each comment by summarizing the relevant section of the document and explicitly stating how the query is resolved, using a template that includes the comment identifier, the resolution statement, and any supporting evidence (e.g., page numbers, figure references).

| Category | Details |
| --- | --- |
| **Reason** | Provides a standardized response format that satisfies FDA expectations and facilitates downstream review. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Apply a templating engine (e.g., Jinja2) to inject extracted data into the response template; optionally use a summarization model (e.g., T5) to condense long excerpts. |

### 4. Aggregate all individual responses into a single resolution summary string, ensuring that each entry is clearly delineated (e.g., by comment ID) and that the overall summary adheres to the FDA's word‑limit guidelines.

| Category | Details |
| --- | --- |
| **Reason** | Creates a coherent document that can be attached to the submission and read by FDA reviewers without needing to navigate multiple files. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Concatenate response strings with newline separators; enforce length constraints using a simple character count check. |

### 5. Determine the 'resolved_all' boolean flag by comparing the count of resolved comments (length of 'resolved_comments' list) with the total number of pending comments extracted initially; set to true only if they match.

| Category | Details |
| --- | --- |
| **Reason** | Provides a clear, binary indicator for downstream nodes whether all issues have been addressed. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Use an equality check: resolved_all = (len(resolved_comments) == len(pending_requests)). |

### 6. Write the output fields (resolved_all, resolved_comments, resolution_summary) to the node's output schema, ensuring proper data types (bool, list of strings, string) and validate against the schema before returning.

| Category | Details |
| --- | --- |
| **Reason** | Guarantees data integrity and compatibility with downstream nodes that consume this output. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Serialize the data to JSON, then run a schema validation routine (e.g., using jsonschema) to confirm type conformity. |
