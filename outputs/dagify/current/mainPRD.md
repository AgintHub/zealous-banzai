# fda_device_submission_plan - Complete PRD Documentation

## Overview
PRDs for nodes in the 'fda_device_submission_plan' module.

## Table of Contents

- [address_fda_comments_and_questions](#address_fda_comments_and_questions)

- [clarify_device_type](#clarify_device_type)

- [develop_device_documentation](#develop_device_documentation)

- [identify_required_fda_submissions](#identify_required_fda_submissions)

- [obtain_fda_clearance_or_approval](#obtain_fda_clearance_or_approval)

- [perform_competitive_analysis](#perform_competitive_analysis)

- [prepare_fda_submission_package](#prepare_fda_submission_package)

- [research_fda_regulations](#research_fda_regulations)

- [submit_fda_application](#submit_fda_application)

- [track_fda_review_progress](#track_fda_review_progress)



---

## address_fda_comments_and_questions

### Description
Verify that all comments and questions are resolved and that the submission meets the FDA's requirements.

### Implementation Plan

#### 1. Extract the list of pending FDA comments and questions from the parent node 'track_fda_review_progress' output field 'pending_requests', mapping each entry to a structured object containing its identifier, title, and the associated query text.

| Category | Details |
| --- | --- |
| **Reason** | Provides a concrete, machine‑readable set of items to address, eliminating ambiguity in the resolution process. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use JSON parsing to read the 'pending_requests' array, then apply a regex or NLP tokenization to separate identifiers and titles; store results in a local list of dictionaries. |

#### 2. For each extracted comment, locate the corresponding detailed query text within the submission package (e.g., design control files, testing reports) by cross‑referencing the identifier with document metadata stored in a central index.

| Category | Details |
| --- | --- |
| **Reason** | Ensures that the response is based on the most accurate and up‑to‑date information available in the submission documentation. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Maintain a mapping table of document IDs to file paths; query the table using the comment identifier, then load the document content (PDF/Word) via a document‑processing library (e.g., PyMuPDF, python-docx). |

#### 3. Generate a concise, FDA‑compliant response for each comment by summarizing the relevant section of the document and explicitly stating how the query is resolved, using a template that includes the comment identifier, the resolution statement, and any supporting evidence (e.g., page numbers, figure references).

| Category | Details |
| --- | --- |
| **Reason** | Provides a standardized response format that satisfies FDA expectations and facilitates downstream review. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Apply a templating engine (e.g., Jinja2) to inject extracted data into the response template; optionally use a summarization model (e.g., T5) to condense long excerpts. |

#### 4. Aggregate all individual responses into a single resolution summary string, ensuring that each entry is clearly delineated (e.g., by comment ID) and that the overall summary adheres to the FDA's word‑limit guidelines.

| Category | Details |
| --- | --- |
| **Reason** | Creates a coherent document that can be attached to the submission and read by FDA reviewers without needing to navigate multiple files. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Concatenate response strings with newline separators; enforce length constraints using a simple character count check. |

#### 5. Determine the 'resolved_all' boolean flag by comparing the count of resolved comments (length of 'resolved_comments' list) with the total number of pending comments extracted initially; set to true only if they match.

| Category | Details |
| --- | --- |
| **Reason** | Provides a clear, binary indicator for downstream nodes whether all issues have been addressed. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Use an equality check: resolved_all = (len(resolved_comments) == len(pending_requests)). |

#### 6. Write the output fields (resolved_all, resolved_comments, resolution_summary) to the node's output schema, ensuring proper data types (bool, list of strings, string) and validate against the schema before returning.

| Category | Details |
| --- | --- |
| **Reason** | Guarantees data integrity and compatibility with downstream nodes that consume this output. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Serialize the data to JSON, then run a schema validation routine (e.g., using jsonschema) to confirm type conformity. |


---

## clarify_device_type

### Description
Identify the appropriate device type, e.g., Class I, II, or III, and determine any specific regulations or requirements that apply.

### Implementation Plan

#### 1. Collect all relevant device attributes (intended use, indications, technology, performance metrics, and risk factors) from the product data repository or user input forms.

| Category | Details |
| --- | --- |
| **Reason** | These attributes provide the foundational information needed to map the device to FDA risk categories and classification criteria. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Implement a data ingestion module that parses structured product specifications (JSON/XML) and validates required fields. Prompt the user for missing attributes via a guided questionnaire. |

#### 2. Map the collected attributes to FDA risk categories (low, moderate, high) using the risk tables defined in 21 CFR Part 801.

| Category | Details |
| --- | --- |
| **Reason** | Risk level directly influences the device class determination. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Create lookup tables that associate specific technology types, intended uses, and performance thresholds with risk levels. Apply a scoring algorithm that aggregates attribute scores to produce a single risk category. |

#### 3. Determine the device class by cross‑referencing the risk category with FDA classification criteria (Class I for low risk, Class II for moderate risk, Class III for high risk).

| Category | Details |
| --- | --- |
| **Reason** | Ensures the classification aligns with regulatory definitions. |
| **Impact** | HIGH |
| **Complexity** | LOW |
| **Method** | Use straightforward conditional logic: if risk == 'low' then class = 'Class I'; if risk == 'moderate' then class = 'Class II'; else class = 'Class III'. |

#### 4. Retrieve the specific regulatory requirements for the determined class by consulting FDA guidance documents, 21 CFR subparts, and pre‑market notification requirements (e.g., 510(k), PMA, De Novo).

| Category | Details |
| --- | --- |
| **Reason** | Provides the downstream node with the exact compliance checklist needed for documentation and submission. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Leverage the FDA Regulatory Information API or web‑scrape the FDA website to fetch relevant guidance titles and subpart references. Filter results by the identified class and store them as a list of strings. |

#### 5. Calculate a classification confidence score by evaluating data completeness, consistency with classification criteria, and presence of ambiguous attributes.

| Category | Details |
| --- | --- |
| **Reason** | Offers an audit trail and helps downstream processes decide whether expert review is needed. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Implement a weighted scoring algorithm: assign points for each mandatory attribute present, deduct points for conflicts or missing data, and normalize to a 0‑1 scale. |

#### 6. Assemble the output fields (device_class, device_class_code, regulatory_requirements, classification_confidence) into the node’s expected JSON structure.

| Category | Details |
| --- | --- |
| **Reason** | Ensures the node’s contract is fulfilled and downstream nodes receive correctly typed data. |
| **Impact** | LOW |
| **Complexity** | LOW |
| **Method** | Map internal variables to the output keys, convert the class code to its short form (I/II/III), and serialize the list of requirements as an array of strings. |

#### 7. Validate the assembled output against the defined schema and perform a cross‑check with the parent node’s expectations (e.g., ensure that regulatory_requirements are non‑empty for Class II/III).

| Category | Details |
| --- | --- |
| **Reason** | Prevents data quality issues that could cascade through the DAG. |
| **Impact** | LOW |
| **Complexity** | LOW |
| **Method** | Run unit tests that assert field types, required fields, and logical consistency. Log any validation failures for manual review. |


---

## develop_device_documentation

### Description
Prepare all necessary documents, such as design control files, testing reports, and labeling specifications, to support the device's FDA submission.

### Implementation Plan

#### 1. Extract required document categories from the regulatory requirements provided by research_fda_regulations (regulation_summary, guidance_documents, regulation_areas, compliance_checklist, required_documents). Map each required category to a concrete document type (e.g., Design History File, Risk Management Report, Software Verification Plan).

| Category | Details |
| --- | --- |
| **Reason** | Ensures the documentation package aligns with FDA guidance and covers all mandatory document types. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Parse the required_documents list; create a mapping table; use a template engine to generate placeholder documents. |

#### 2. Incorporate differentiation factors and competitor weaknesses from perform_competitive_analysis to identify unique design features that must be documented in the design control files (e.g., novel sensor architecture, proprietary software algorithm).

| Category | Details |
| --- | --- |
| **Reason** | Highlights device-specific innovations that are critical for regulatory justification and market positioning. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Cross‑reference differentiation_factors with design specifications; add sections in the Design History File documenting each unique feature. |

#### 3. Generate a structured list of design control files (design_control_files) using standardized FDA templates (e.g., 21 CFR Part 820 Design History File, ISO 14971 Risk Management File). Include file names, version numbers, and responsible personnel.

| Category | Details |
| --- | --- |
| **Reason** | Provides traceability and ensures each design element is documented per regulatory expectations. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use a document generation library (e.g., Jinja2) to fill placeholders with data from the design database. |

#### 4. Create testing report titles (testing_reports) that correspond to each validation activity required by the regulatory checklist (e.g., Bench Validation Report, Clinical Study Report, Software Validation Report). Ensure each report title includes a unique identifier and links back to the relevant design control file.

| Category | Details |
| --- | --- |
| **Reason** | Facilitates easy navigation for reviewers and demonstrates compliance with verification/validation requirements. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Iterate over the compliance_checklist; for each checklist item, generate a report title and store in a list. |

#### 5. Draft labeling specification documents (labeling_specifications) that cover device name, intended use, contraindications, warnings, instructions for use, and packaging details. Reference FDA labeling guidance (e.g., 21 CFR Part 801) and ensure all required information is present.

| Category | Details |
| --- | --- |
| **Reason** | Labeling is a critical component of the submission; missing information can delay approval. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Create a labeling template; populate fields using data from the device description and regulatory guidance. |

#### 6. Compile a regulatory compliance summary (regulatory_compliance_summary) that maps each document in design_control_files, testing_reports, and labeling_specifications to the specific FDA requirement or guidance it satisfies.

| Category | Details |
| --- | --- |
| **Reason** | Provides a quick reference for reviewers and internal audit teams. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Use a mapping dictionary to link document types to requirement IDs; generate a narrative summary. |

#### 7. Count the total number of documents (number_of_documents) by summing the lengths of design_control_files, testing_reports, and labeling_specifications lists.

| Category | Details |
| --- | --- |
| **Reason** | Ensures completeness and aids in package validation. |
| **Impact** | LOW |
| **Complexity** | LOW |
| **Method** | Simple integer addition. |

#### 8. Set the submission_package_ready flag (submission_package_ready) to true only after verifying that all required document categories identified in required_documents are present and that no required items are missing.

| Category | Details |
| --- | --- |
| **Reason** | Prevents incomplete submissions and reduces the risk of rejections. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Implement a validation routine that checks presence of each required document type. |


---

## identify_required_fda_submissions

### Description
Identify the necessary submissions, including Pre-Submission communications, and prepare accordingly.

### Implementation Plan

#### 1. Extract the list of regulation areas (e.g., '510(k)', 'PMA', 'De Novo') and the corresponding required documents from the output of research_fda_regulations.

| Category | Details |
| --- | --- |
| **Reason** | These fields directly indicate the permissible submission pathways and the baseline documentation set mandated by the FDA for the device class. |
| **Impact** | HIGH |
| **Complexity** | LOW |
| **Method** | Parse the regulation_areas and required_documents arrays from research_fda_regulations output; store them in temporary variables for downstream logic. |

#### 2. Determine the most appropriate submission_type by matching the device’s regulatory classification (implied by required_documents) with the regulation_areas list.

| Category | Details |
| --- | --- |
| **Reason** | The device class dictates whether a 510(k), PMA, or De Novo route is applicable; selecting the correct type is critical for compliance. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Implement a decision matrix: if required_documents include '510(k) premarket notification' → submission_type = '510(k)'; else if they include 'PMA premarket approval' → submission_type = 'PMA'; else default to 'De Novo'. |

#### 3. Query the internal pre‑submission communication tracker (or a designated database) for any records of inquiries or feedback sent to the FDA prior to this node’s execution.

| Category | Details |
| --- | --- |
| **Reason** | Pre‑submission communications are essential for clarifying submission requirements and can affect the required document set. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Execute a SQL/NoSQL query filtering by device identifier and submission_type; return a list of communication IDs or titles. |

#### 4. Aggregate required_documents by merging the list from research_fda_regulations with the design_control_files, testing_reports, and labeling_specifications from develop_device_documentation.

| Category | Details |
| --- | --- |
| **Reason** | The final submission package must contain both regulatory‑mandated documents and device‑specific technical documents. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Perform a set union operation on the three document lists; de‑duplicate by file name; output the combined list. |

#### 5. Calculate the submission_deadline by adding the standard FDA review lead time (e.g., 180 days) to the current date, then format the result in ISO 8601 (YYYY-MM-DD).

| Category | Details |
| --- | --- |
| **Reason** | Providing a concrete deadline helps schedule downstream activities and ensures timely submission. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Use a date‑library function to add 180 days to today’s date; format with ISO8601(). |

#### 6. Set is_submission_complete to true only if all documents in required_documents are present in the current repository and the current date is before submission_deadline.

| Category | Details |
| --- | --- |
| **Reason** | This flag signals readiness for the next node (prepare_fda_submission_package) and prevents premature submission. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Iterate over required_documents; for each, verify existence via a file‑system or database lookup; compare current date to submission_deadline; set boolean accordingly. |


---

## obtain_fda_clearance_or_approval

### Description
Verify that the device has received the necessary clearance or approval, and obtain a copy of the approval letter or certificate.

### Implementation Plan

#### 1. Extract the 'resolved_all' flag from the parent node's output and use it as the primary decision point for proceeding with clearance verification.

| Category | Details |
| --- | --- |
| **Reason** | The parent node guarantees that all comments have been addressed; this flag determines whether the device is eligible for clearance. |
| **Impact** | HIGH |
| **Complexity** | LOW |
| **Method** | Parse the JSON output of 'address_fda_comments_and_questions', retrieve the boolean 'resolved_all', and store it in a local variable. |

#### 2. If 'resolved_all' is False, set 'clearance_status' to False, leave other fields empty or null, and log the failure reason for audit.

| Category | Details |
| --- | --- |
| **Reason** | No clearance can be granted until all comments are resolved; early exit prevents unnecessary processing. |
| **Impact** | HIGH |
| **Complexity** | LOW |
| **Method** | Conditional branching in the workflow engine; populate 'clearance_status' = False, set remaining keys to null, and emit an audit event. |

#### 3. If 'resolved_all' is True, query the FDA's electronic submission portal (e.g., FDA's 510(k) database) using the device's unique identifier to locate the clearance letter.

| Category | Details |
| --- | --- |
| **Reason** | The clearance letter is the primary source of official confirmation and contains the approval date. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use FDA's public API or web‑scraping with authentication; construct a request with the device's 510(k) number or PMA ID; handle pagination and JSON/XML responses. |

#### 4. Download the clearance letter PDF, store it in the secure document repository, and record the file path in 'approval_letter_path'.

| Category | Details |
| --- | --- |
| **Reason** | A persistent, indexed copy is required for compliance audits and future reference. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Use secure file transfer (SFTP/HTTPS), generate a UUID for the file name, store metadata (timestamp, checksum) in a database, and assign the repository path to the output field. |

#### 5. Extract the approval date from the letter's metadata (e.g., PDF 'CreationDate' or a structured table) and format it as ISO 8601; assign to 'approval_date'.

| Category | Details |
| --- | --- |
| **Reason** | The approval date is a critical compliance attribute and must be machine‑readable. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Parse PDF with a library like PyPDF2 or pdfminer; locate date patterns using regex; convert to ISO format; validate against a calendar. |

#### 6. Count the number of resolved comments by summing the length of 'resolved_comments' from the parent output; assign to 'comments_resolved_count'.

| Category | Details |
| --- | --- |
| **Reason** | Provides a quantitative metric of how many issues were addressed before clearance. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Retrieve 'resolved_comments' list, compute len(), store in the output field. |

#### 7. Determine 'comments_pending_count' by subtracting 'comments_resolved_count' from the total number of FDA comments recorded in the parent output; assign to the field.

| Category | Details |
| --- | --- |
| **Reason** | Ensures that any remaining comments are tracked for future action. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Retrieve total comments count from parent (e.g., length of 'resolved_comments' + pending list), compute difference. |

#### 8. Validate the clearance document against FDA formatting requirements (e.g., PDF/A compliance, presence of required sections like 'Device Name', 'Approval Number'); set 'clearance_document_valid' accordingly.

| Category | Details |
| --- | --- |
| **Reason** | Non‑compliant documents can invalidate the clearance status and trigger re‑submission. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Run PDF/A validation using veraPDF, check for mandatory fields via OCR or text extraction, and flag any deviations. |

#### 9. Aggregate all populated fields into the final output JSON, ensuring type consistency (bool, str, int) and include an audit trail timestamp for traceability.

| Category | Details |
| --- | --- |
| **Reason** | A well‑structured output is required for downstream nodes and regulatory reporting. |
| **Impact** | HIGH |
| **Complexity** | LOW |
| **Method** | Serialize the output object to JSON, enforce schema validation, and attach a UTC timestamp. |


---

## perform_competitive_analysis

### Description
Conduct a competitive analysis to understand the market and regulatory environment for the device.

### Implementation Plan

#### 1. Gather a list of all FDA‑registered medical devices that serve the same clinical indication and share similar technology or intended use.

| Category | Details |
| --- | --- |
| **Reason** | Ensures the analysis covers the complete competitive set relevant to the device’s regulatory pathway. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use FDA’s 510(k) database, PMA database, and De Novo database; filter by product code, indication, and technology classification; export results to a CSV. |

#### 2. Parse the exported CSV to extract competitor names, product codes, and regulatory status, and store them in structured data frames.

| Category | Details |
| --- | --- |
| **Reason** | Provides a clean, machine‑readable format for downstream calculations and reporting. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Apply Python pandas to read CSV, rename columns, and handle missing values; output DataFrame with columns: Name, RegStatus. |

#### 3. Calculate the market share percentage for each competitor by aggregating sales data from publicly available sources (e.g., IQVIA, FDA reports) and normalizing against total market sales.

| Category | Details |
| --- | --- |
| **Reason** | Quantifies each competitor’s market footprint, which is critical for strategic positioning. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Scrape sales data, clean and merge with competitor list; compute share = (competitor sales / total market sales) * 100; round to two decimals. |

#### 4. Map each competitor’s regulatory status to the appropriate pathway (510(k), PMA, De Novo) using FDA’s classification tables and cross‑reference with the research_fda_regulations output.

| Category | Details |
| --- | --- |
| **Reason** | Aligns market analysis with regulatory constraints, ensuring compliance considerations are integrated. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Create a lookup dictionary from research_fda_regulations; apply to competitor DataFrame; store results in the regulatory_status list. |

#### 5. Identify differentiation factors by comparing the device’s technical specifications (e.g., sensor type, algorithmic processing, cost) against each competitor’s documented features.

| Category | Details |
| --- | --- |
| **Reason** | Highlights unique selling propositions that can be leveraged in the submission and marketing. |
| **Impact** | HIGH |
| **Complexity** | HIGH |
| **Method** | Extract feature sets from product datasheets and regulatory submissions; use set operations to compute differences; generate descriptive strings for each factor. |

#### 6. Summarize strengths and weaknesses for each competitor by reviewing FDA clearance letters, clinical study results, and post‑market surveillance data.

| Category | Details |
| --- | --- |
| **Reason** | Provides a balanced view of the competitive landscape, informing risk mitigation and product development. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Parse clearance letters for performance metrics; extract adverse event statistics; create bullet points using natural language generation templates. |

#### 7. Draft a concise analysis summary that synthesizes market share trends, regulatory environment, and differentiation insights into strategic recommendations for the device.

| Category | Details |
| --- | --- |
| **Reason** | Delivers a high‑level narrative that can be used by stakeholders to make informed decisions. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Aggregate key findings into a structured paragraph; include tables or charts for visual emphasis; ensure alignment with the device’s regulatory strategy. |

#### 8. Validate the final output fields against the defined output structure, ensuring type consistency (List[str], List[float], str) and completeness.

| Category | Details |
| --- | --- |
| **Reason** | Guarantees that downstream nodes receive correctly formatted data, preventing integration errors. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Implement unit tests that check each field’s type and presence; run a validation script before exporting results. |


---

## prepare_fda_submission_package

### Description
Ensure that the package includes all required information, e.g., device description, technical specifications, and clinical data.

### Implementation Plan

#### 1. Generate a globally unique package_id by concatenating the device_class_code from identify_required_fda_submissions, current ISO 8601 date, and a sequential counter stored in a central registry.

| Category | Details |
| --- | --- |
| **Reason** | Ensures traceability and prevents collisions across multiple submissions. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use a UUID v4 generator combined with a deterministic prefix; store and increment the counter in a thread‑safe database table. |

#### 2. Extract the device_description from the device_control_files list in develop_device_documentation, summarizing the device name, intended use, and key features into a concise paragraph.

| Category | Details |
| --- | --- |
| **Reason** | Provides a clear, FDA‑acceptable overview required for the submission package. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Apply a natural language summarization model (e.g., T5 fine‑tuned on regulatory texts) to the concatenated design control file contents. |

#### 3. Compile technical_specifications by aggregating all testing_reports and labeling_specifications from develop_device_documentation, formatting each as a separate section with tables and figures as per FDA guidance.

| Category | Details |
| --- | --- |
| **Reason** | Ensures that all performance and safety data are presented in a structured, compliant manner. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Parse each report using a PDF extraction library, normalize data into JSON, then render to Markdown/HTML using a templating engine. |

#### 4. Generate clinical_data_summary by summarizing the clinical study reports referenced in identify_required_fda_submissions, extracting key endpoints, sample sizes, and statistical significance.

| Category | Details |
| --- | --- |
| **Reason** | Clinical data is a mandatory component for most FDA submissions; a concise summary facilitates reviewer understanding. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use a domain‑specific NLP pipeline to extract study metadata, then produce a one‑page summary with bullet points. |

#### 5. Create the required_documents list by merging the required_documents from identify_required_fda_submissions with all filenames from design_control_files, testing_reports, and labeling_specifications, then de‑duplicate and sort alphabetically.

| Category | Details |
| --- | --- |
| **Reason** | Provides a definitive inventory of all files that must accompany the submission. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Implement a set union operation in Python, then output as a List[str]. |

#### 6. Validate format_compliant by checking each document against the FDA's electronic submission format (e.g., CDISC SDTM, DICOM) using a schema validator; set format_compliant to true only if all documents pass.

| Category | Details |
| --- | --- |
| **Reason** | Ensures the package meets technical submission requirements, avoiding delays. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Leverage open‑source validators (e.g., SDTM Validator) and aggregate results. |

#### 7. Calculate total_pages by rendering the assembled document to PDF and counting pages, then store the integer value.

| Category | Details |
| --- | --- |
| **Reason** | Page count is often required for submission cost estimation and compliance checks. |
| **Impact** | LOW |
| **Complexity** | LOW |
| **Method** | Use a PDF library (e.g., PyPDF2) to open the generated file and read the page count. |

#### 8. Set submission_status to 'ready' if format_compliant is true and total_pages > 0; otherwise, set to 'pending' and log missing components.

| Category | Details |
| --- | --- |
| **Reason** | Provides a clear indicator for downstream nodes (submit_fda_application) to act upon. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Implement a conditional assignment in the final assembly script. |

#### 9. Record submission_timestamp as the current UTC time in ISO 8601 format at the moment the package is finalized.

| Category | Details |
| --- | --- |
| **Reason** | Timestamping is essential for audit trails and regulatory timelines. |
| **Impact** | LOW |
| **Complexity** | LOW |
| **Method** | Use Python's datetime.utcnow().isoformat() + 'Z' for UTC. |


---

## research_fda_regulations

### Description
Review the FDA's Code of Federal Regulations, Guidance Documents, and other relevant resources to ensure compliance.

### Implementation Plan

#### 1. Extract the device class and class code from the clarify_device_type output (device_class and device_class_code) to determine the primary regulatory pathway (e.g., Class I → 510(k), Class III → PMA).

| Category | Details |
| --- | --- |
| **Reason** | The regulatory pathway is the foundation for all subsequent regulation and guidance document selection. |
| **Impact** | HIGH |
| **Complexity** | LOW |
| **Method** | Parse the clarify_device_type JSON; map class to pathway using a static lookup table. |

#### 2. Identify the relevant CFR parts (e.g., 21 CFR Part 820 for quality systems, 21 CFR Part 820 for medical device reporting) based on the device class and any special features indicated in regulatory_requirements.

| Category | Details |
| --- | --- |
| **Reason** | CFR parts define the statutory requirements that must be satisfied. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use a rule‑based engine to cross‑reference device class and feature flags against a curated CFR part matrix. |

#### 3. Query the FDA Guidance Documents database (or an internal repository) for guidance documents whose titles or identifiers match the identified CFR parts and device class.

| Category | Details |
| --- | --- |
| **Reason** | Guidance documents provide clarifications, best practices, and implementation examples. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Implement a keyword‑matching algorithm that searches titles, abstracts, and document IDs; retrieve metadata (title, effective date, version). |

#### 4. Aggregate the retrieved guidance documents into the guidance_documents list, ensuring each entry includes a unique identifier (e.g., GUID or FDA document number).

| Category | Details |
| --- | --- |
| **Reason** | A structured list enables downstream nodes to reference the correct documents. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Normalize the document metadata into a standard JSON array. |

#### 5. Construct a concise regulation_summary by summarizing the statutory requirements from the identified CFR parts and highlighting key obligations (e.g., premarket submission, quality system, labeling).

| Category | Details |
| --- | --- |
| **Reason** | The summary provides a quick reference for compliance checks. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Apply a summarization model (e.g., T5 or GPT‑4) fine‑tuned on regulatory texts; limit to 150‑200 words. |

#### 6. Create the regulation_areas list by extracting the names of regulatory pathways (e.g., "510(k)", "PMA", "De Novo") that are relevant to the device based on class and guidance documents.

| Category | Details |
| --- | --- |
| **Reason** | Regulation areas guide the selection of submission types and required documents. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Map CFR part identifiers to pathway names using a predefined dictionary. |

#### 7. Develop a compliance_checklist that enumerates mandatory actions (e.g., "Prepare 510(k) summary", "Submit premarket notification", "Establish quality system") derived from the CFR parts and guidance documents.

| Category | Details |
| --- | --- |
| **Reason** | A checklist ensures no regulatory requirement is omitted. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Generate checklist items via a rule‑based template engine; include references to specific CFR sections. |

#### 8. Extract version numbers and effective dates for each CFR part and guidance document to populate regulation_versions.

| Category | Details |
| --- | --- |
| **Reason** | Regulatory versions affect compliance deadlines and scope. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Parse metadata fields from the guidance document repository; format as "CFR Part 820 (Effective 2023-01-01)". |

#### 9. Determine is_compliant by cross‑checking that all required regulatory actions (as listed in compliance_checklist) are either already satisfied (e.g., prior FDA clearance) or planned within the submission timeline.

| Category | Details |
| --- | --- |
| **Reason** | A preliminary compliance flag informs risk assessment. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Implement a boolean expression that evaluates the presence of each checklist item in the current project status repository. |

#### 10. Compile required_documents by aggregating all documents mandated by the identified CFR parts and guidance documents (e.g., "Device Description", "Design History File", "Risk Analysis", "Labeling Specification").

| Category | Details |
| --- | --- |
| **Reason** | This list directly feeds into the submission package. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Map each regulation area to its document requirements using a regulatory requirement matrix; deduplicate entries. |


---

## submit_fda_application

### Description
Verify that the submission is complete and accurately reflects the device's information, then transmit the FDA application package using the FDA’s electronic submission portal or other approved method.

### Implementation Plan

#### 1. Extract the prepared submission package data from the parent node output, mapping each required field (package_id, device_description, technical_specifications, clinical_data_summary, required_documents, format_compliant, total_pages) into a structured payload for the FDA submission API.

| Category | Details |
| --- | --- |
| **Reason** | Ensures that the submission payload contains all mandatory information in the format expected by the FDA portal. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use a JSON schema validator to map parent fields to API fields; include error handling for missing or mismatched fields. |

#### 2. Generate a globally unique submission_id using a UUIDv4 generator and store it alongside the payload for traceability.

| Category | Details |
| --- | --- |
| **Reason** | Provides a reliable reference for downstream tracking and audit purposes. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Invoke a UUID library (e.g., uuid4 in Python) and embed the value in the submission payload. |

#### 3. Validate the format_compliant flag from the parent node; if false, abort submission and log a detailed error message indicating which format requirements were not met.

| Category | Details |
| --- | --- |
| **Reason** | Prevents transmitting incomplete or non‑compliant packages that would be rejected by the FDA, saving time and resources. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Implement a conditional check; if false, set success_flag to false, submission_status to 'Failed', and return an early response. |

#### 4. Authenticate with the FDA submission portal using OAuth2 client credentials flow, retrieving an access token scoped for the 'submit' endpoint.

| Category | Details |
| --- | --- |
| **Reason** | Securely obtains the necessary token to authorize the submission request. |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Use a standard OAuth2 library to request a token from the FDA token endpoint; cache the token until expiration. |

#### 5. Send the submission payload via HTTPS POST to the FDA’s electronic submission endpoint, including the access token in the Authorization header and all documents as multipart/form-data attachments.

| Category | Details |
| --- | --- |
| **Reason** | Ensures that the submission is transmitted in the correct protocol and format required by the FDA. |
| **Impact** | HIGH |
| **Complexity** | HIGH |
| **Method** | Construct a multipart/form-data request; attach each document from required_documents as a separate part; set appropriate content‑disposition headers. |

#### 6. Parse the FDA response; if the HTTP status code is 200 OK and the JSON body contains a 'submission_id' and 'status', map these to the output fields; otherwise, set success_flag to false and capture the error message.

| Category | Details |
| --- | --- |
| **Reason** | Provides a reliable way to confirm successful transmission and retrieve the FDA‑assigned submission identifier. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use a JSON parser to extract fields; implement retry logic for transient network errors. |

#### 7. Record the current timestamp in ISO 8601 format as submission_date and set submission_status to the status received from the FDA (e.g., 'Submitted').

| Category | Details |
| --- | --- |
| **Reason** | Creates an audit trail and enables downstream nodes to track the submission timeline. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Use a datetime library to generate the timestamp. |

#### 8. Determine review_response_received by checking if the FDA response includes a 'request_for_additional_info' flag; set to true if present, otherwise false.

| Category | Details |
| --- | --- |
| **Reason** | Allows the system to know whether immediate follow‑up is required. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Simple boolean mapping from response field. |

#### 9. Persist all output fields (submission_id, submission_status, documents_submitted, submission_date, success_flag, review_response_received) to the central workflow database, linking them to the parent package_id for traceability.

| Category | Details |
| --- | --- |
| **Reason** | Ensures that downstream nodes (e.g., track_fda_review_progress) can retrieve the submission metadata. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use an ORM or direct SQL INSERT; enforce foreign key constraint on package_id. |

#### 10. If success_flag is false, generate an alert to the compliance team with details of the failure (e.g., missing documents, authentication error) and halt further progression until resolved.

| Category | Details |
| --- | --- |
| **Reason** | Prevents cascading failures and ensures that the submission is corrected before re‑submission. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Integrate with the company's incident management system (e.g., ServiceNow) via webhook. |


---

## track_fda_review_progress

### Description
Track the review progress, including any updates or changes to the review timeline.

### Implementation Plan

#### 1. 1️⃣ Retrieve the submission metadata (submission_id, submission_date, success_flag, review_response_received) from the output of submit_fda_application using a secure API call or database query.

| Category | Details |
| --- | --- |
| **Reason** | The submission identifier and date are required to query the FDA review status and to calculate elapsed time for timeline estimation. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use OAuth2‑protected REST endpoint to fetch submission record; validate success_flag before proceeding. |

#### 2. 2️⃣ Query the FDA Electronic Submissions Gateway (ESG) or equivalent API endpoint with the submission_id to obtain the current review status code and any pending request objects.

| Category | Details |
| --- | --- |
| **Reason** | FDA provides a structured response that maps to our review_status field and lists pending information requests. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Send GET request to ESG /status/{submission_id}; parse JSON response; map FDA status codes to 'Pending', 'In Review', 'Completed'. |

#### 3. 3️⃣ Calculate timeline_estimate_days by subtracting the number of days elapsed since submission_date from the standard review period for the device class (e.g., 180 days for 510(k)).

| Category | Details |
| --- | --- |
| **Reason** | Provides a realistic estimate for stakeholders and helps trigger timely follow‑ups. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Use Python datetime library to compute days_since_submission = (current_date - submission_date).days; timeline_estimate_days = max(0, standard_period - days_since_submission). |

#### 4. 4️⃣ Extract pending_requests by iterating over the FDA response payload’s request list, normalizing each entry to a concise identifier (e.g., 'REQ-2025-001') and storing them in a List[str].

| Category | Details |
| --- | --- |
| **Reason** | Ensures that all FDA requests are captured for tracking and future response handling. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Map each request object to its 'request_id' field; validate against a regex pattern; collect into a list. |

#### 5. 5️⃣ Record last_update_timestamp as the current UTC time in ISO 8601 format at the moment the FDA status is retrieved.

| Category | Details |
| --- | --- |
| **Reason** | Provides an audit trail for when the review information was last verified. |
| **Impact** | LOW |
| **Complexity** | LOW |
| **Method** | Use datetime.utcnow().isoformat() + 'Z' to generate the timestamp. |

#### 6. 6️⃣ Determine responded_to_requests by checking if any pending_requests remain after any response handling logic (initially set to False; later updated when responses are submitted).

| Category | Details |
| --- | --- |
| **Reason** | Tracks whether the FDA has received all required information, which influences downstream nodes. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Set responded_to_requests = (len(pending_requests) == 0) after initial poll; update flag after response submission. |

#### 7. 7️⃣ Generate response_summary by concatenating the count of responses sent (if review_response_received is True) and a brief status message, e.g., '2 responses submitted, awaiting FDA review.'

| Category | Details |
| --- | --- |
| **Reason** | Summarizes the current state of communication with the FDA for quick reference. |
| **Impact** | LOW |
| **Complexity** | LOW |
| **Method** | If review_response_received: response_summary = f'{response_count} responses submitted, awaiting FDA review.'; else response_summary = 'No responses submitted yet.' |

#### 8. 8️⃣ Assemble all derived values into the output structure, ensuring type integrity (str, int, bool, List[str]), and serialize to JSON for downstream consumption.

| Category | Details |
| --- | --- |
| **Reason** | Guarantees that the node's contract is satisfied and that downstream nodes receive correctly typed data. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use a data class or schema validation library (e.g., Pydantic) to enforce types; serialize with json.dumps(). |
