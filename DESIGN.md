# PURPOSE

This document explains the design architecture behind the Agentic Email Management System. It outlines core architectural decisions, agent responsibilities, communication patterns, and future development plans.

# DESIGN DECISIONS AND TRADEOFFS

### Multi-Agent Pattern

- **Reasoning:** Each agent handles a single responsibility (SRP), increasing modularity and testability.
- **Trade-off:** Adds complexity in coordination, hence a dedicated orchestrator is used.

### 3. JSON over SQLite

- **Reasoning:** For simplicity and readability, report outputs are stored in JSON format.
- **Trade-off:** Lacks querying capability; might be limiting for high-volume use cases.

### 4. Retry Logic

- **Reasoning:** LLM APIs can intermittently fail. A retry wrapper ensures resilience.
- **Trade-off:** Needs tuning to avoid long wait times in case of persistent failures.

# AGENT COMMUNICATION PATTERN

GMAIL API INPUT
|
v
|
Orchestator
|
v
|
v--------------------v-------------------v
Classifier | Response Generator | Quality Checker

Output: Saved JSON report (if applicable)

# SCALING

- Adding parallel processing to process multiple emails concurrently
- Replace JSON logs with a centralized database

# FUTURE IMPROVEMENTS

- Multi-language support: use claude’s multilingual capabilities to detect/respond in sender’s language.
- Sentiment detection: Prioritize escalations based on emotional tone or urgency.
- Auto-sending responses: integrate gmail sending instead of saving draft responses.
- Admin dashboard: visualize response history, and agent accuracy.
