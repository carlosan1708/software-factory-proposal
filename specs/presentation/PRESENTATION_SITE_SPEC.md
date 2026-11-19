# Software Factory presentation specification

This design brief describes the interactive architecture proposal for engineering and product teams. The page supports both a short walkthrough and independent reading.

Display the author byline Carlos Andres Rodriguez Trigueros with LinkedIn, GitHub profile and Source repository links in the header. The Source repository link opens the public proposal repository.

## Reading modes

Show Executive and Technical as two adjacent, outlined buttons in the page header. Use a solid fill and a marked radio indicator for the active mode. Make the mode names the largest text in each control, with reading times on a smaller second line. On phones, give the pair its own full-width row. In print, show the selected edition.

Budget about 10 minutes for the Executive main presentation and 20 minutes for Technical at 200 words per minute. Show the selected estimate below the opening title in the HTML and PDF. Count all four walkthroughs once, including their results, diagrams and tables. Exclude the FAQ and time spent pausing the animation. Check the estimates against the exported text after substantive edits.

The header scrolls away with the page in both modes. Open in Executive by default. Lead with one animation and four selectable scenarios, then show the pipeline users, architecture and delivery forecast. Technical mode adds implementation details, evidence, access boundaries and operational responsibilities in place. Both modes show all four guardrails and the conditional release timeline. Support keyboard selection, /technical, legacy ?mode=technical links and section fragments. Include technical diagrams of the base/candidate regression check, interrupted worker recovery and digest-bound promotion. Show the caller, permitted operation and destination for each data path.

## What the audience sees first

The header includes a client-side **Search proposal** field in both modes. Index the HTML already in the file, including sections, FAQ answers and all four scenario transcripts. A result that needs Technical mode opens that view. A matched step opens its scenario paused at that step. Search supports keyboard navigation, direct links and the standalone offline file. Queries stay in the browser.

**A software factory on Azure**

Name the software factory as the client deliverable and Screening Desk as its first generated app. GitHub Issues is the Phase 1 intake channel. Show how a signed-in internal form or an authenticated service API could also submit a change request after the pilot. Each channel feeds the same workflow directly. The Executive diagram hands a work request to the Build Orchestrator. In Technical mode, show where the intake API verifies who may submit for the team, records each request once, and dispatches approved work. Explain the alternative channels in a searchable FAQ with a concrete example. Sponsor approval or a matching standing repair policy authorizes coding regardless of the source.

Open with an assumptions paragraph. The team understands the software factory concept and wants to see how to put it into practice. Use worked examples to show who authorizes a connector operation and how an engineer verifies a bug fix before release. The factory must adapt to a complex GitHub and Azure environment with legacy apps, an ERP, multiple databases and external services. Prior factory experience can inform the starter and runbooks. State that the organization ruled out AI app builders for this project. It chose a software factory so engineers can adapt connectors and access rules as the existing systems change, review the code in GitHub and release it to Azure. Link directly to architecture, forecast and FAQ. Use one automatically advancing scene in Executive and Technical modes. Put a single-choice selector above the scene for the three Screening Desk scenarios and the second-team Project Library scenario. Place Previous, Next, Pause/Resume and Restart in the scene header. Manual stepping pauses the current scenario. Disable Previous at the first step and Next at the last. Restart returns the selected scenario to its first step with a fresh timer and preserves its playing or paused state. Each step shows the actor, tool or decision, result, and a short description. Label human decisions explicitly, with a distinct shape in the timeline. Name the channel on each human approval step. Sponsors and data owners use a scope PR or an email invitation that requires sign-in and explicit confirmation. Engineers review the verified code on its GitHub PR. Release owners approve the protected GitHub Actions production job for the staged image and target. The approvals FAQ names the person and channel for each decision. A system owner participates when the change requires a new grant. Technical mode also covers a protected release PR when the private repository’s plan lacks Actions environment reviewers. Jira may mirror status after handover and has no approval role. Approvals and confirmations are illustrated steps. All external calls are fictional. Preserve scenario fragments, pause while offscreen, and supply a static transcript for offline/no-script and print. Keep the later architecture reference diagrams static.

| Scenario | Systems and outcome | Human intervention |
| --- | --- | --- |
| Replace the legacy shift tracker · `#new-project` | Generate Screening Desk to replace one aging app. Migrate open issues, owners, deadlines and notes from an approved export, and use a single read-only booking feed. Rehearse with 24 fictional open items, reconcile the fields and test repeat import. Use the late Hall B master as one booking example. | The sponsor approves scope, the engineer reviews the PR and the release owner approves promotion. The operations lead accepts the team’s first shift in the new app after a reconciled final import. |
| Add a handoff note to a screening · `#one-feature` | Add the custom ERP connector to the existing notes workflow. The agent maps its approved contract using fixtures. At runtime a coordinator can open a note and look up the assigned hall’s ticket. An approved ERP ticket-change event can also start a pending handoff. The app validates the event, handles duplicate delivery, and uses its own runtime grant to retrieve the current ticket. The coordinator confirms before the app saves the note with its ERP reference. An ERP event reaches the released app only. A different app could receive a specific ERP write grant. | Authorize ERP lookup and event delivery separately, review and release the change, then let the coordinator confirm the actual note. |
| Keep an assigned blocker visible · `#bug-repair` | The base revision hides an overdue booking when an owner is assigned. A pre-authorized fix changes the list query. The verifier repeats the assignment on both revisions and changes the fixture to received to check that the blocker clears. | An engineer reviews the verified change and the release owner approves rollout. |
| A second team launches Project Library · `#second-team` | The portfolio team uses the factory starter, verifier and release process with its own GitHub repository, read-only catalog view and editor-note database. Trace a Depot retrofit search and a saved note. | The sponsor and data owner approve the project scope, the engineer reviews the verified revision and the portfolio release owner approves the staged image. |

The opening distinguishes **Phase 1 · One team in production** from **Phase 2 · Extend the running factory**. Label the whole-project and automated-repair scenarios as Phase 1, the ERP feature and Project Library as alternative Phase 2 examples. Keep those labels visible on mobile and in print. For Phase 1, retrieve the versioned runbook and app schema from the starter. The old shift tracker exports open issues once and stays authoritative during beta. At cutover, freeze edits, reconcile the final import and leave closed history in the old tracker. One separate read-only booking feed supplies the screening time, master deadline and receipt status. The app owns assignments, follow-up times and notes. Confirm those fields in Week 1. Compare time from deadline to named owner with the previous shift log during beta. The feature animation may illustrate event delivery beyond the first ERP lookup. Say which part its estimate covers.

## Who uses the pipeline?

Place this section immediately after the opening flow, before the architecture drawing. Use one compact table. Follow the same Screening Desk overdue-booking repair across roles. Each row should name something the person can actually open and the decision or task it supports. On mobile, keep each role with its own two descriptions.

| Person | What they can see | What they do |
| --- | --- | --- |
| Requester · festival coordinator | Their project's brief, progress, shareable test summary and approved preview. | Confirm that an overdue booking stays visible after assignment and clears on receipt. |
| Project sponsor | The proposed scope, affected repository and paths, requested permissions and outstanding decisions for the project they sponsor. | Authorize a repair class or approve a feature plan. |
| Engineer | The assigned change's diff, base and candidate revisions, test results and findings. | The engineer validates the regression and approves the verified revision when review is required. |
| Data or security owner | The affected resource, requested access, data classification and relevant audit evidence within their remit. | Decide whether a change to note permissions or an export is allowed. |
| Release owner | The target environment, staged artifact digest, approvals, smoke checks and rollback revision for their release. | Authorize production promotion or rollback. |
| Platform on-call (optional) | Redacted queue, retry, budget and incident signals for the services they support. | At low volume the owning engineer responds in agreed hours. Add dedicated coverage when workload or service hours require it. An operator with the stop grant can pause automation. |

Add one sentence beneath the table. Festival staff using the released app see the overdue bookings and follow-ups their app role permits. Access to a factory project, its source or its review evidence requires a separate assignment.

## Architecture

Use the six-stage overview in Executive mode. Give each stage a distinct line icon, a responsibility, and an arrow labeled with its outgoing artifact. Place a short introduction directly below the architecture title. In Technical mode, lead with the deployment map for the Phase 1 booking app. Show the processes, identities and artifacts involved in taking an approved change to production. Introduce the Phase 2 ERP ticket in its worked example. Draw four separately labeled nodes attached to the Claude Code worker in both architecture maps and their PDFs. Label them Discovery, Code review, Security & data access, and UX & accessibility. In the technical map, place the four in one coding sandbox, give each a concrete task and show the independent CI runner in the separate verification stage. Keep the reference drawing static and readable in print. Give the architecture the width of the page. Use one connected drawing, with short labels placed on the lines that carry the work. The main path reads **Intake → Build Orchestrator → Claude Code worker → independent verifier → GitHub review and Azure release**. Label the two final actions separately so an approved merge cannot be mistaken for a deployment. Annotate the handoffs with “scoped task”, “candidate patch”, “verification evidence” and “approved revision”.

Label the subagents as read-only in Phase 1 on both architecture maps. Explain in the FAQ that the builder owns edits while the specialists report findings. Show that the Claude Code builder invokes discovery, code review, security/data-access review and UX/accessibility review inside the coding sandbox. In the replacement walkthrough, show discovery gathering the migration map, the builder editing the app, and applicable reviewers inspecting the patch. The low-risk bug can take the builder-only path. The separate CI verifier runs protected checks without an LLM. Human approval and the one-repair budget apply to the tested revision.

Use two short annotations beneath the drawing. PostgreSQL and pg-boss persist the work item while people decide or a worker restarts. Explain the lease as a time-limited claim. Explain the choice of PostgreSQL through atomic checkpoint and enqueue, shared availability, and reconciliation for external writes. The connector reads the approved schedule and the generated app writes its own notes. Preserve the same reading order on mobile by stacking the main path and leaving optional work indented beside its parent.

In Technical mode, follow the handoff-note change through intake, a leased work item, a disposable coding sandbox, the sponsor-scoped GitHub broker, independent verification, a merged image, staging and the production runtime. Show what the Build Orchestrator reads and persists, how it creates a sandbox and how a replacement worker reconciles an uncertain pull request. Link three illustrative records across dispatch, verification and release by run ID. Present MCP as the agent-facing tool protocol with owner-approved adapters behind it. Use a legacy festival sample for the concrete call, with a permitted result and a cross-festival denial. Also show a database view, schema projection, partner API, RAG lookup and synthetic ERP tool. Place `#legacy-cutover` alongside the production release discussion and link to the FAQ for mapping, rehearsal and switchback conditions. Additional integrations sit outside the one-connector estimate. Present ERP as one possible backend among databases, legacy applications, knowledge and external services. Name the granted tool in each applicable animation step. The full project uses MCP for guidance, a legacy booking and delivery sample and the projected schema. The feature uses it for guidance and a synthetic ERP ticket. The app performs the actual ticket lookup with the coordinator’s runtime access. The low-risk repair uses local fixtures. Show the per-call access check and the outcome of revocation. See the [agent access design](../architecture/SOFTWARE_FACTORY_ARCHITECTURE.md#agent-access-through-mcp).

In the Technical reading path, compare the current and proposed factory policies on the same labeled historical and held-out cases. Use clearly illustrative counts for unsafe changes allowed, safe changes blocked from automatic merge and reviewer minutes. Explain which policy to keep and how to retest the rejected rule.

## Security guardrails

Compare three levels of authority side by side in both modes. A verified copy correction may qualify for automatic merge after a trial and repository sign-off. The Hall B logic repair requires engineer review. The database owner approves a migration plan and tested recovery before human authorization for production. Suspend automatic merge for a class if an unsafe change gets through.

Place four short captions along the architecture flow, all visible at once. Each names an enforcement point and what happens when its check fails. Keep the detailed permission matrix in the engineering documentation.

| Where | Guardrail and outcome |
| --- | --- |
| **At intake and on every read** | The server checks current project membership, role and resource access, including direct links to previews and evidence. A forwarded link from another project is denied. |
| **While the agent works** | The sandbox receives a pinned source copy and expiring, task-scoped tools. The broker rejects ungranted calls, including a write to the programming API. An instruction in a ticket or retrieved document cannot widen the grant. The gateway stops new calls at the run budget. |
| **Before merge** | The verifier runs protected checks on the actual revision. A new commit invalidates the old evidence and review. An overdue-list repair that also changes permissions leaves the automatic route for engineer and owner review. |
| **Before production** | A separate release identity may promote only the staged digest the release owner approved. A missing approval or mismatched digest holds promotion. The factory records the decision and its evidence. |

Use one plain-language visibility example in the narration. The coordinator opens the corrected preview, the engineer opens the exact diff and test evidence, and the assigned responder opens the redacted trace. Operational logs exclude raw prompts, source, credentials and staff notes. Each linked artifact enforces its own access check.

## Cost and observability

Give each topic a short section with a concrete example. Use headings and aligned text on a shared canvas.

| Section | Content for the page |
| --- | --- |
| **Cost — what drives the bill?** | Separate one-time team effort, recurring platform costs and per-run model and sandbox usage. Use the sentence “A retry adds model and compute cost even if it produces no accepted change.” Track cost per accepted change during beta. Leave rates, calculator inputs and line-item pricing in engineering material. |
| **Observability — where is the delay?** | Use three short signal-and-owner pairs. **Waiting preview.** the assigned engineer or on-call responder checks runnable queue age and retries. **Slow schedule.** the app owner follows the request to the programming API with the connector owner. **Release health.** the release owner checks the serving revision and restores the healthy one if canary checks fail. One footnote can name OpenTelemetry and Azure Monitor. |

## Forecast

Both modes show the same acceptance test. First, the factory generates Screening Desk and the shift lead confirms that importing the 24 sample issues twice preserves owners and notes without duplicates. Second, the coordinator reports the Hall B bug through GitHub. The same factory produces a fix, the independent check fails on the original and passes on the candidate, and the corrected preview keeps the assigned booking visible. Production cutover follows feedback and monitoring sign-off.

Open with the two Week 10 beta acceptance checks, followed by the Gantt and a paired table of drivers by milestone beneath it, **What speeds delivery up** and **What slows it down**. Title the chart “Phase 1 · Working beta around Week 10”. Follow its production row with a Phase 2 row showing additional time after handover. Draw the first two rows against calendar weeks from kickoff. Give the open beta a visible open end. Anchor the Phase 1 production row to feedback sign-off with a break in the time axis, so its position cannot imply a promised production date.

| Gantt row | Label and treatment |
| --- | --- |
| Discovery and access | Weeks 1–3. Fixed-width bar. |
| Build and verify the beta | Weeks 4–9. Fixed-width bar. |
| Beta live | Around Week 10 onward. Invited users generate apps while the team collects feedback and monitors use. |
| Production and handover | 2–4 weeks after feedback and monitoring sign-off. End marker means healthy production and accepted ownership. |
| Phase 2 extension | After handover and ready access, illustrate 1 week to confirm fields, 1–2 weeks to build the lookup and 1–2 weeks to test and release. |

For each milestone, pair an accelerator with the corresponding schedule risk. Beta opening depends on cloud quota and routes, repo and identity grants, data contracts, repeatable tests and protected engineering time. Production sign-off depends on participation, authority and evidence, load and cost, restore and rollback, and agreed support coverage. Show the two-week access delay example separately from the post-sign-off production estimate.

Lead the drivers with **access to information** as the biggest schedule risk. Name the business expert and source owner, the interface definitions, representative records and decisions they must provide, and the effect of delays on connector and test work. Put the one-team, one-starter, one-read-connector beta deliverable next to the Week 10 heading. For Phase 2, present several connector choices and use the Hall B maintenance lookup as one worked 3–5 week example from handover and ready access, with allowed, denied and unavailable paths as acceptance evidence. The ERP event subscription and second-team onboarding require separate estimates. In Technical mode, put the Week 3 readiness decision and staffing assumption beside the forecast and the conditional handover calculation in the Week 10 FAQ.

## Architecture FAQ

In both modes, ground the opening assumptions in the pilot team's access to a sample legacy export and a real shift handoff. Explain how engineers use those examples to check that open issues retain their owners and follow-up times. Describe the Build Orchestrator, Claude Code worker and verifier in the architecture section. In the opening Assumptions, state in one sentence that the proposal chose an Azure-hosted Claude Code worker over Claude Code’s GitHub integration to keep intake, connectors and approvals flexible across projects. The former FAQ link should lead to this assumption. GitHub retains code review and release approvals.

Include a linked Technical-mode branching diagram at `#review-flow`. Start with the recorded work request, show the owner decision when scope or access is missing, and follow authorized work through one coding worker, independent verification, one possible repair, engineer review and the separate production approval. Preserve the existing `#azure-controller` and `#factory-coordinator` deep links when using `#build-orchestrator`.

In both web modes and both PDFs, answer who runs the subagents, whether the orchestrator uses an LLM, where the worker lives, how many sandboxes a passing or repaired change allocates, and why independent CI verification runs without Claude. Give the option of a test-design specialist as a future example. Use the Hall B before-and-after test as evidence.

Add searchable FAQ answers for infinite loops and human intervention. Use the Hall B repair to show the 20-minute generation timeout, one repair attempt, up to two transient infrastructure retries and run-wide token and spending limits. Explain which failures stop automation, what an engineer receives, and who decides scope, new data access, merge and production release.

Keep the main forecast to a short comparison by milestone. Link to the full ten-risk table in a shared FAQ answer. In Technical mode keep the worked MCP call, orchestrator recovery sequence and production evidence in the main reading path. Put the detailed legacy cutover checks, six-system MCP tool catalog and PostgreSQL trade-offs in linked, searchable FAQ answers.

Show FAQ questions as native disclosures in both modes. Start with answers collapsed. A search result or direct question link opens its answer. Include every applicable answer in print and PDF. Explain the factory’s role alongside GitHub and Azure, what a second team supplies and inherits, how a released app uses owner-approved ERP reads, writes or optional events, the stale-revision failure case, the Week 10 boundary, how the same team chooses its next extension and measures the extra time, and how to evaluate prior factory assets. Explain the choice of a software factory using a shift handoff that crosses three data owners. In Technical mode, show how an engineer changes an ERP adapter and verifies both hall-level access and behavior during an outage before release. Technical mode can add evidence and authorization details. Support the `#faq` link and print.

In Technical mode, add a linked **Deployment troubleshooting** subsection at `/technical#deployment-faq`. Cover the first sandbox failing to start, a model gateway timeout, a staging ERP lookup denied after a passing fixture test, an unready Container Apps revision and a failed canary after a database migration. Give the responsible role, first diagnostic and evidence required to resume for each case. Use the existing FAQ question-and-answer layout and link to primary Azure guidance where it helps. Returning to Executive mode from the subsection should land in the shared FAQ.

## Visual direction

Use the palette below for the presentation and its diagrams.

| Color | Assignment |
| --- | --- |
| Warm white `#F4F3EB` | Continuous page background and reversed text on dark surfaces. |
| Near black `#0F0F0F` | Headlines, body text, diagram labels and baseline Gantt bars. |
| Red-orange `#FF2B00` | The route being traced, the branch marker and the beta milestone. Accompany each meaningful mark with a text label or distinctive shape. |
| Light gray `#D0D3D4` | Quiet rules and secondary grid lines. Use near-black for essential outlines. |

Use bold system sans-serif headlines, regular sentence-case labels and generous space between sections. Start the flow on the first screen. Give the diagram more space than its introduction. Put dark text beside orange marks on the light canvas. In print, line styles and labels carry the paths and milestone without color. Place “Proposed factory · fictional example” once near the opening.

Close both modes and their print editions with a shared Inspiration and learning section. Credit Microsoft’s Azure Container Apps Sandboxes article and ZazenCodes’ Claude Code walkthrough and link directly to both sources.

## Acceptance for the HTML revision

- Choose Executive or Technical at the top and read the selected mode using only scroll. Keep the reading-mode switch and scenario selector outside the animated scene. Provide Previous, Next, Pause/Resume and Restart as native playback controls. Offer both Executive and Technical PDF links in the header in either reading mode. Generate searchable static PDFs from the same HTML with all four numbered scenario transcripts. Set connector names and descriptions as plain diagram labels in a definition list. Name the active connector beside its unboxed icon in the animated flow. Keep descriptions readable on mobile and in print. Show the content of each mode without additional interactions.
- In one glance, a reader can trace the bug fix around the plan and see where the feature requires a decision. Both routes reach independent verification.
- From the architecture drawing, a reader can identify the primary worker, optional discovery role, verifier and release authority. A specialist is never implied to run on every task.
- A reader can tell which view the coordinator, reviewer and assigned responder each use for the same fix, and distinguish a festival staff account from a factory role. Every human role in the table has a scoped view and a task.
- The diagram makes four outcomes legible without interaction: a cross-project link is denied, an ungranted tool call is refused, a changed revision needs fresh evidence, and an unapproved artifact cannot reach production.
- Cost fits in three short lines and one example. Observability identifies a signal and responder for each case. Forecast contains the four Gantt rows and the schedule drivers.
- At 390, 768 and 1440 pixels, labels stay legible and lines terminate at the correct nodes. Reflow rather than shrinking a desktop diagram. Check keyboard scrolling, reduced motion, print and the standalone offline file.
- Ship one self-contained HTML file with local CSS and optional JavaScript. Distribute the two downloadable editions alongside it in the downloads folder. Keep the existing Firebase presentation target. All examples are illustrative.
