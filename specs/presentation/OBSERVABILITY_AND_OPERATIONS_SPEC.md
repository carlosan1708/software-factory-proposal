# Observability and operating the software factory

**Historical presentation brief.** This document preserves the operating scenarios, instrumentation and handover detail used in the previous presentation. The [current presentation specification](PRESENTATION_SITE_SPEC.md) supersedes its interface and presentation acceptance criteria.

This feedback spec extends the [presentation redesign](PRESENTATION_REDESIGN_SPEC.md) and the [factory architecture](../architecture/SOFTWARE_FACTORY_ARCHITECTURE.md). It specifies what the next presentation should show using fictional Screening Desk records. The scope covers one team, one application and one approved internal read connector.

## Make observability visible

Label the existing Monitoring tab **Observability**. Keep `#monitoring` as a working link to the same panel and accept `#observability` as the preferred link. Keep six top-level tabs. Open with two choices an operator would recognize.

| View | Operator question | What the visitor can inspect |
| --- | --- | --- |
| Factory run | Why is the coordinator still waiting for a verified preview? | Time in the queue, time waiting for human approval, agent and optional discovery calls, retrieval outcomes, verifier results, retries, and which stage owns the delay. |
| Released app | Why is the screening schedule slow for staff right now? | A synthetic schedule read, the serving revision, app and connector spans, dependency latency and errors, and which owner receives the incident. |

Give the trusted services OpenTelemetry instrumentation. Export redacted traces, metrics and structured logs to Azure Monitor using Application Insights and Log Analytics. Route actionable alerts through Action Groups. During discovery the platform engineer verifies the permitted telemetry network path, ingestion access, budget and retention with security. Exercise that path during the beta build and observe real app-generation runs from beta opening. [Application Insights and OpenTelemetry](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

Within a factory run, keep a durable work-item ID and a distinct attempt ID for each execution. Propagate trace context across trusted HTTP calls. Link asynchronous jobs, retries and optional subagent work to their initiating attempt across queue boundaries. Record approved identifiers for the policy version, source revision, evidence and release digest. A new app request starts its own trace. Its deployed revision links back to the factory release record. This lets an operator investigate a deployed app weeks after the agent session ended. Use run IDs for trace and log lookup. Use bounded dimensions such as stage, environment and outcome for metric aggregation.

**Interactive example.** On **Released app**, choose **Schedule is slow**. The synthetic trace shows 2.4 seconds end to end, with 2.1 seconds inside the programming API call. Selecting that span shows a timeout on the first attempt and success on the bounded retry. The release digest matches the previous healthy interval. The app owner checks dependency health with the connector owner. Show the observed timings and leave the underlying cause open. On **Factory run**, choose **Preview is late**. Show a runnable job waiting 17 minutes, inspect its dispatch attempt and route it to the platform owner. A separate example waiting for sponsor approval appears in the requester’s elapsed time and is excluded from the dispatch alert.

Retain the existing failed-canary and evidence-mismatch drills. Operational traces may be sampled. Record every gate outcome, including passes, and all privileged approvals in the protected, unsampled evidence store. Use opaque references across the two stores and enforce access when opening evidence. Allowlist emitted fields. Exclude prompts, retrieved excerpts, internal payloads, tokens, free-text notes and staff identities from operational telemetry. If export stops, show **Telemetry unavailable** with the last successful observation. If the verifier cannot durably record mandatory evidence, hold promotion.

## Show how the team earns more autonomy

The architecture already defines replay, shadow decisions and policy review. Make the release decision visible inside **Delivery**, at feedback exit. Give the visitor a **Compare policy versions** action. QA owns the evaluation cases, the factory lead recommends a decision, and the release owner records the approved policy version and can restore its predecessor.

Use the same pinned, labeled holdout cases for the current and candidate policy. Include routine copy, a permissions change disguised as copy, a missing call site and a flaky check. Record expected and actual decisions, false allows, false blocks, reviewer minutes and a link to each gate record. Show counts and denominators per risk class. Keep cases used for tuning out of the holdout. Compare reviewer effort and time to accepted change against manually handled work of similar risk during feedback.

In the fictional replay, each policy sees the same 12 cases. The candidate reduces unnecessary escalations on routine cases from three to one, but routes one of four high-risk cases to automatic merge. The decision is **Keep the current policy**. A reviewer opens the affected case, sees the access change, and records the reason. This small fixture demonstrates the decision rule. The real feedback gate needs representative evidence. A weekly incident review can add regression cases, and the monthly policy review can tighten, relax or retire rules.

## Assign ownership when an app goes live

Include a compact **Production handover** card in Delivery for the first generated app. The factory lead owns the generation policy and verifier. The platform on-call owns workers, queues and shared telemetry. The generated app’s service owner accepts its runtime, dependencies, user support, and release or rollback decisions. The internal API owner handles dependency incidents. Identify the primary, backup, support hours and escalation path before first traffic.

| Discovery decision | Evidence at production handover |
| --- | --- |
| Which user journey must work, and what level of service does the owner accept? | A service-level objective for a successful, timely schedule read with its agreed target, measurement window, denominator and alert recipient. Track factory time to verified preview separately. |
| How long can the team tolerate downtime and how much saved work can it lose? | The app and data owners agree a recovery time objective and recovery point objective. A timed staging restore records actual recovery time and the newest recovered coordinator note. Record exceptions and the accountable decision before promotion. |
| Who maintains the app as its dependencies age or its sponsor changes? | Record the repo, release digest, runbook, data owner, patch owner and cost owner in the existing service inventory. On retirement, the service owner disables integrations, revokes grants, handles retained data under the approved policy and stops unused Azure resources. |

The forecast assumes an existing telemetry workspace and permitted ingestion path, an available responder for the first app, and a staged restore. Confirm owners and target values in Weeks 1–3. Trace a real generation run and rehearse alerts as part of the Weeks 4–9 beta build. Starting around Week 10, monitor factory and app health while participants submit briefs and feedback. Keep beta open until the sponsor and operator have reviewed that evidence and release blockers are resolved. Verify production health and complete handover to close delivery. The [release spec](../architecture/BETA_TO_PRODUCTION_SPEC.md) defines the conditional production estimate.

## Presentation acceptance

- Both fragments open Observability. Visitors can switch between a factory run and an app request, open the slow span, identify the responsible service and find its owner. All timings and decisions carry a simulation label.
- Recover a factory attempt and show the same work item with a new attempt ID. Trace the deployed revision to its release evidence. A missing trace and an unavailable evidence store produce their distinct expected states.
- Compare the two replay results, inspect the high-risk false allow and identify the decision and decision maker. The presentation reports the simulated sample size and the manual baseline measures to collect.
- Before first traffic, Delivery identifies the app owner, support window, service objective, restore test and escalation path. Any pending real target is labeled for discovery.
