# Software Factory presentation redesign

**Historical presentation brief.** This document records the prior six-tab implementation and its detailed technical examples. The [current presentation specification](PRESENTATION_SITE_SPEC.md) supersedes its interface and presentation acceptance criteria. References below to simulated Jira issues describe the retired walkthrough. The current [approval design](../architecture/SOFTWARE_FACTORY_ARCHITECTURE.md#approvals-and-deferred-work) uses scope reviews, authenticated email invitations and protected GitHub Actions deployments.

This revision specifies the next presentation draft and the architecture decisions it explains. Use the [factory architecture](../architecture/SOFTWARE_FACTORY_ARCHITECTURE.md) for delivery gates and [evaluation](../architecture/STATE-OF-ART-EVALUATION.md) for the reuse decision. This document supersedes the first draft's vertical layout and Project Library story. All screenshots, evidence, costs, and incident examples in the presentation are illustrative.

## 1. Navigation and visual design

Use a compact cinema-inspired opening for **Screening Desk**, a fictional film-festival operations app. Show a single original visual of an empty screening venue or an abstract program card, followed by the proposed production window. Keep the main panels light and legible with deep navy and warm accent colors. Use fictional film titles and venues, generic role names, and public vendor references throughout.

| Tab | Purpose |
| --- | --- |
| **Walkthrough** | Follow one project from a festival coordinator's request to a verified, usable preview. |
| **Architecture** | Trace the Azure workflow, internal API calls, retrieval, data roles, and session recovery. |
| **Security** | Inspect authority at each boundary, try allowed and denied operations, and invalidate a PR approval by changing its head. |
| **Cost** | Adjust usage and cost assumptions, see the monthly run rate, and separate build staffing from ongoing operating cost. |
| **Monitoring** | Explore the signals that would trigger a response during the live beta or after go-live, the responding role, and the action taken. |
| **Delivery** | See the Gantt, app-producing beta, open-ended feedback intake and monitoring, and final production release. |

Render one tab panel at a time. Default to Walkthrough and preserve walkthrough, calculator, and simulator state when changing tabs. Use linkable fragments `#walkthrough`, `#architecture`, `#security`, `#cost`, `#monitoring`, and `#delivery`. Map old bookmarks for `#workflow`, `#review`, and `#azure-poc` to the corresponding panel or Azure infrastructure example. Browser back and forward restore the selected tab. On mobile, keep the active tab visible in a horizontally scrollable tab strip. Each panel remains readable when printing or opening the file with JavaScript disabled.

Implement keyboard tabs with one tab stop, Arrow keys and Home/End to move focus, and Enter or Space to activate. Animate panel entry, the active tab indicator, and walkthrough state changes over about 180–260 ms. Use a short fade and directional movement when moving through the walkthrough. Under reduced motion, switch immediately and keep focus and status behavior identical. Complete state updates immediately and keep buttons responsive to rapid switching.

## 2. Screening Desk walkthrough

A film-festival coordinator requests a web app to browse screenings after a venue change. Staff need a day and venue filter, a visible cue when a screening moves, and the ability to save a coordinator note. The programming API controls the lineup and times. The app owns its notes. A bulk export of the program and rights notes waits for a decision about which fields and recipients are authorized.

| Step | Visitor action and visible outcome |
| --- | --- |
| **Brief** | Read the screening day and venue change. Open three acceptance criteria for filtering, changed-venue status, and the staff note. Press **Review plan**. |
| **Plan** | Approve the core as the sponsor. Open **Why this plan** to see an approved runbook excerpt and the programming API contract with their fixture citations. Defer export to simulated Jira issue `DEMO-104`. The approved core can advance while the export remains open. |
| **Build** | Open **Source**, **Tests**, or **Delivery** excerpts for the candidate. Show which work the primary agent used the discovery subagent for and what evidence it returned. Keep the separate test and release checks visible. |
| **Verify** | Inspect the candidate and its base, a failing baseline check that passes on the candidate, and separate checks for the changed venue and note permissions. Show one advisory finding and who can resolve it. Label the evidence as simulated. |
| **Preview** | Use venue and day filters, inspect a relocated screening, and save a sample note scoped to that screening. Show the empty state when filters yield no screenings. Link to the Security tab for database and release decisions. |

Use these fixture screenings. All times are festival-local and illustrative.

| Title | Schedule | Change |
| --- | --- | --- |
| Tin Moon Postcard | Friday, 18:30 · Hall B | Moved from Hall A |
| Umbrella Comet | Friday, 21:00 · Hall A | On schedule |
| Last Train to Aster | Saturday, 19:00 · Open-air screen | On schedule |

Give the walkthrough one primary action per step. Show a persistent summary with current step, core approval, deferred Jira issue, and candidate. Use count and empty-state updates after filtering and a visible confirmation after saving a note. Moving backward preserves decisions. **Reset walkthrough** clears the plan, sample notes, and preview filters. Use short transitions for evidence rows and preview cards. Keep synthetic verification results distinguishable from real operations in every view.

## 3. Architecture, internal systems, and retrieval

The Architecture tab uses a selectable map from request to release. Include the controller, primary Claude Code agent, discovery subagent, independent verifier, GitHub and Jira brokers, deployment identity, policy-gated connector gateway, retrieval broker, and separate data roles. Each node explains its inputs, outputs, owner, and what happens when access is unavailable.

### Databases and internal systems

| Role | Baseline and choices |
| --- | --- |
| **Factory workflow state** | PostgreSQL with pg-boss is the reference implementation for durable state and jobs. A different factory database is possible once the replacement DB and scheduler pass the same atomic enqueue, lease, recovery, and idempotency tests. |
| **Approved source data** | Use a read-only internal API or an approved database view or replica. SQL Server, MySQL, PostgreSQL, and existing document stores are adapter candidates. Pick provider and operations per project with the data owner. |
| **Generated app-owned data** | The app writes its own records using a separately scoped runtime identity. For example, the Screening Desk demo can depict Azure SQL for notes alongside a separate factory PostgreSQL store. Confirm the chosen target and its migration and restore path before provisioning. |

Register every connection per project and environment with its owner, allowed operations, data classification, network path, identity, and fixture. Use named calls such as `getScreeningSchedule` and `getPosterMetadata` through a trusted connector broker. The agent gets a short-lived run grant. The broker checks current project and sponsor scope, caller scope where delegated access is required, and the specific resource and operation. It applies timeouts, rate limits, and audit logging. Prefer delegated Entra access where the target supports it. Use a narrowly scoped workload identity for approved background operations. Keep provider credentials on the trusted side of the broker, and allowlist the broker route from the generation sandbox. The verifier uses isolated fixtures. For connector failures, show stale-data status or pause the affected work item. [Microsoft Entra on-behalf-of flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow) · [Azure API Management managed identity](https://learn.microsoft.com/en-us/azure/api-management/authentication-managed-identity-policy)

The initial scope assumes one approved read connector and one app write store. Put additional connectors, write operations, and engine adapters through individual approval and testing. Migration approval is scoped to the app database. Each adapter needs realistic fixtures and explicit read, write, and failure contract tests.

### Retrieval-augmented generation

Use RAG to ground planning in approved internal API contracts, runbooks, and repository guidance. In the example, **Why this plan** cites the synthetic venue-change runbook and programming API contract. Current screening times come from a typed API call. The authorization broker checks permissions at the action boundary.

- Index approved documents with project, data classification, source ID, version, document permissions, and last verification time. Use a commit-keyed symbol index plus exact-code search for call sites and tests.
- Use Azure AI Search hybrid retrieval as the proposed option for the bounded document corpus. The trusted broker applies project and principal filters before ranking, rechecks current access and source version before returning excerpts, and attaches a citation to each result. Route removed or inaccessible sources to a retrieval miss. Keep live records and secrets out of the corpus.
- Treat retrieved text as untrusted context. When a required source is missing or stale, show the uncertainty and route to a reviewer or an approved exact lookup. Use a small approved corpus and measure citation accuracy, known-source recall, freshness, retrieval latency, and access denials before expanding. [Azure AI Search hybrid retrieval](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) · [Security-filter pattern](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search)

### Agent roles and subagents

| Role | Scope |
| --- | --- |
| **Primary coding agent** | Claude Code reads the approved plan and pinned repo, edits its disposable workspace, and produces a patch and tests. |
| **Discovery subagent** | Trace source fields, callers and tests with read-only tools before the builder edits the legacy replacement. Return citations and open questions. |
| **Review subagents** | Claude can delegate code, security/data-access and UX/accessibility review of the candidate in parallel. Each specialist returns findings within the same run budget. |
| **Independent verifier and approvers** | A fresh CI sandbox executes protected checks without Claude and binds evidence to the candidate. The policy gate and designated humans control merge and release. |

Define the four available specialists in factory-owned SDK configuration. The Build Orchestrator determines required reviews using policy and the Claude Code worker invokes the selected subagents. Scope tools to the run and role. Correlate child traces and spending with the parent run. Compare review outcomes and costs on broad changes and short repairs. [Claude Agent SDK subagents](https://code.claude.com/docs/en/agent-sdk/subagents)

### Sessions and durable project state

| State | Owner and lifetime |
| --- | --- |
| **Presentation state** | Browser memory holds selections, sample notes, and forecasts. The URL records the selected tab. Reload starts a fresh demo with the requested tab visible. |
| **Factory sign-in session** | Microsoft Entra and a secure server-side app session identify the human. Recheck project membership and current grants before privileged operations. |
| **Project and run checkpoints** | Persist plan version, milestones, approval decisions, run status, base and candidate SHAs, issued Jira/PR IDs, and references to verified evidence in the factory database and controlled storage. Store repository revisions in Git. Keep job IDs and external operation IDs stable across retries. |
| **Claude execution session** | Start a fresh short-lived session per task or recovery attempt. Reconstruct context from the approved plan, pinned repo, authorized retrieval, and the previous checkpoint. Retain a session ID for correlation if needed under the retention policy. Give each attempt a fresh sandbox and scoped grant. |
| **Generated app state** | Store real Screening Desk notes in the configured app database under the app's own authorization rules. The demo uses one in-memory sample note per screening. |

On restart, reclaim the expired lease, reload the persisted checkpoint, verify the current repo and approval, and reconcile any previous external operation before sending it again. If scope, base, or permissions changed, require the relevant new approval or verification. In the Architecture tab, **Simulate worker restart** replaces the run ID and restores the approved core, deferred Jira issue, and pinned revision from a fixture checkpoint. Show what gets checked before work continues.

## 4. Security tab

Show the user, sponsor, scoped agent tools, connector and release identities, and the independent verifier in a compact authority diagram. Keep the exact-head PR exercise here. Approve `demo-head-a`, simulate `demo-head-b`, and block merge eligibility until verification and approval both match the new head.

Include a selector for the following scenarios with textual decisions, reason, owner, and evidence.

| Request | Expected decision |
| --- | --- |
| Agent reads the approved schedule API | **Allow** through the broker for the approved festival scope. |
| Agent reads a restricted rights document | **Deny** at retrieval. Show no excerpt, title, or citation for the restricted item. |
| App writes a coordinator note | **Allow** to the app-owned database for an authorized staff identity. |
| App writes to the source data store | **Deny**. The source identity has read scope. |
| Agent requests an export or schema write | **Approval required** and route to its owner. A later execution uses a dedicated identity and approved target. |
| Release attempt with stale evidence | **Deny** until checks and approval match the exact revision or image digest. |

Use existing controls for secret storage, private routes, review and release gates, and evidence retention. Show an audit record with synthetic actor, grant, request ID, resource, policy version, and outcome. A retrieved instruction or agent suggestion has no authority to expand scope.

## 5. Cost tab

Show **Illustrative assumptions · USD** prominently. Separate build effort from monthly operating cost. Display the staffing and week assumptions from Delivery. Accept an optional loaded weekly team cost to calculate the build range. Use editable fields for the monthly estimate and keep rate definitions in an expandable detail.

| Input | Demo value |
| --- | --- |
| Fixed platform, database, search, and telemetry costs per month | $200 |
| Attempted runs per month, including retries | 100 |
| Accepted changes per month | 60 |
| Model cost per attempt | $0.60 |
| Generation and verification compute per attempt | $0.30 |
| Incremental retrieval and embedding cost per attempt | $0.10 |

Calculate monthly cloud cost as fixed cost plus attempts multiplied by the sum of per-attempt costs. Divide by accepted changes for the unit cost. The demo therefore shows **$300/month** and **$5.00 per accepted change**. Validate finite nonnegative values, whole-number volumes, and accepted changes at most attempted runs. When accepted changes are zero, show the incurred cost and a dash for unit cost. Separate staffing, licenses, subscriptions, and taxes from the cloud subtotal. Preserve inputs across tabs and provide **Reset assumptions**.

In the proposal, price the actual footprint from measured token/cache use, sandbox CPU and memory time, failed attempts, database and private network SKUs, search/embeddings, and log ingestion and retention. Confirm contract and region rates during the beta build and calibrate usage costs from monitored beta runs. Enforce per-run and workspace limits in the gateway and dispatcher. Azure budget alerts provide notification. [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) · [Foundry Claude billing](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-billing) · [Azure Cost Management budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)

## 6. Monitoring and delivery tabs

Add telemetry and rehearse alerts and rollback during the build. Monitor the running beta and the apps participants generate from its first day. Review that evidence at feedback exit, then monitor the production revision from its first traffic shift. Use Azure Monitor, Application Insights, Log Analytics, and Action Groups in the proposed design. Keep authorization and release evidence in an unsampled audit store. Use redacted operational events to link request, run, repository revision, connector/RAG outcome, and deployed digest. [Container Apps observability](https://learn.microsoft.com/en-us/azure/container-apps/observability) · [Azure Monitor Action Groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)

Show simulated **Healthy**, **Queue stalled**, **Internal schedule API delayed**, **Evidence mismatch**, and **Unhealthy canary** scenarios. Include signal, alert destination, and a response with drill-down. Distinguish an API failure or stale guidance from a release failure. Pause evidence-dependent promotion on an authority incident and show rollback after two failed canary smoke checks. Include queue age, retries, model budget, connector latency/errors, RAG freshness, and per-revision health. Display the named operator role and response, with private-system details replaced by synthetic records.

Follow the [beta and production release spec](../architecture/BETA_TO_PRODUCTION_SPEC.md) for the Gantt and forecast controls. Show Weeks 1–3 for access and Weeks 4–9 for the beta build, then a working factory that generates apps from around Week 10. Keep beta live during open-ended feedback intake and monitoring. Show production release completion as pending until sign-off. Close the project at healthy production handover. Show the scope, staffing, participation and network approvals that can change the estimate.

## 7. Acceptance checks

- Switch all six tabs using click, keyboard, direct URLs, and browser history. Verify mobile tab navigation, visible focus, rapid transitions, reduced motion, and print and offline views.
- Complete the screening request from brief through preview. Confirm sponsor gating, deferred export and independent progress, venue and day filtering, missing-result handling, and one note per screening. Check reset and state preservation across tabs.
- Exercise authorized retrieval, revoked access, a missing approved source, source-store write denial, app note permissions, and stale PR approval. Keep protected source details out of denied responses.
- Simulate a restart. Confirm the run ID changes and the approved plan, deferred issue, and pinned revision remain visible. Require fresh verification when the candidate changes.
- Check the default cost arithmetic, cost changes after retries or higher fixed charges, zero accepted changes, and invalid input handling. Verify all costs carry the illustrative label.
- Run each incident drill and check the signal, recipient, evidence trail and recovery. Verify that beta stays open while feedback or monitoring evidence is outstanding. An explicit feedback sign-off scenario produces a conditional completion estimate. A successful production handover concludes delivery.
