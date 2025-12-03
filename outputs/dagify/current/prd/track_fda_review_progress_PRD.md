# track_fda_review_progress PRD

## Description
Track the review progress, including any updates or changes to the review timeline.


## Implementation Plan

### 1. 1️⃣ Retrieve the submission metadata (submission_id, submission_date, success_flag, review_response_received) from the output of submit_fda_application using a secure API call or database query.

| Category | Details |
| --- | --- |
| **Reason** | The submission identifier and date are required to query the FDA review status and to calculate elapsed time for timeline estimation. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use OAuth2‑protected REST endpoint to fetch submission record; validate success_flag before proceeding. |

### 2. 2️⃣ Query the FDA Electronic Submissions Gateway (ESG) or equivalent API endpoint with the submission_id to obtain the current review status code and any pending request objects.

| Category | Details |
| --- | --- |
| **Reason** | FDA provides a structured response that maps to our review_status field and lists pending information requests. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Send GET request to ESG /status/{submission_id}; parse JSON response; map FDA status codes to 'Pending', 'In Review', 'Completed'. |

### 3. 3️⃣ Calculate timeline_estimate_days by subtracting the number of days elapsed since submission_date from the standard review period for the device class (e.g., 180 days for 510(k)).

| Category | Details |
| --- | --- |
| **Reason** | Provides a realistic estimate for stakeholders and helps trigger timely follow‑ups. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Use Python datetime library to compute days_since_submission = (current_date - submission_date).days; timeline_estimate_days = max(0, standard_period - days_since_submission). |

### 4. 4️⃣ Extract pending_requests by iterating over the FDA response payload’s request list, normalizing each entry to a concise identifier (e.g., 'REQ-2025-001') and storing them in a List[str].

| Category | Details |
| --- | --- |
| **Reason** | Ensures that all FDA requests are captured for tracking and future response handling. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Map each request object to its 'request_id' field; validate against a regex pattern; collect into a list. |

### 5. 5️⃣ Record last_update_timestamp as the current UTC time in ISO 8601 format at the moment the FDA status is retrieved.

| Category | Details |
| --- | --- |
| **Reason** | Provides an audit trail for when the review information was last verified. |
| **Impact** | LOW |
| **Complexity** | LOW |
| **Method** | Use datetime.utcnow().isoformat() + 'Z' to generate the timestamp. |

### 6. 6️⃣ Determine responded_to_requests by checking if any pending_requests remain after any response handling logic (initially set to False; later updated when responses are submitted).

| Category | Details |
| --- | --- |
| **Reason** | Tracks whether the FDA has received all required information, which influences downstream nodes. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Set responded_to_requests = (len(pending_requests) == 0) after initial poll; update flag after response submission. |

### 7. 7️⃣ Generate response_summary by concatenating the count of responses sent (if review_response_received is True) and a brief status message, e.g., '2 responses submitted, awaiting FDA review.'

| Category | Details |
| --- | --- |
| **Reason** | Summarizes the current state of communication with the FDA for quick reference. |
| **Impact** | LOW |
| **Complexity** | LOW |
| **Method** | If review_response_received: response_summary = f'{response_count} responses submitted, awaiting FDA review.'; else response_summary = 'No responses submitted yet.' |

### 8. 8️⃣ Assemble all derived values into the output structure, ensuring type integrity (str, int, bool, List[str]), and serialize to JSON for downstream consumption.

| Category | Details |
| --- | --- |
| **Reason** | Guarantees that the node's contract is satisfied and that downstream nodes receive correctly typed data. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use a data class or schema validation library (e.g., Pydantic) to enforce types; serialize with json.dumps(). |
