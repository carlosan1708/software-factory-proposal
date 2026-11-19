# Software Factory on Azure

An architecture proposal for an Azure software factory that uses Claude Code to build web applications and independent CI to verify each change.

[Technical walkthrough](https://software-factory-proposal.web.app/technical) · [Executive overview](https://software-factory-proposal.web.app/)

This repository contains the architecture and delivery specifications, a Bicep template for the coding sandbox, and the source for the interactive presentation.

## How a change reaches production

Phase 1 takes requests through the team’s GitHub intake repository. A signed-in form or an approved internal service could later submit directly to the same intake API. Every channel uses the same approval rules. The factory routes bounded repairs directly to Claude Code under a scoped grant. New capabilities and unclear requests go through planning. An independent verifier checks each proposed revision. Sponsors and data owners approve scope on a pull request or through a signed-in email invitation. Engineers review code on GitHub pull requests. Release owners approve the staged image for Azure in GitHub Actions. The factory tracks deferred decisions.

## Specifications

| Document | What it covers |
| --- | --- |
| [Software factory architecture](specs/architecture/SOFTWARE_FACTORY_ARCHITECTURE.md) | The delivery workflow, Azure topology, identity and network boundaries, data access, and phased rollout. |
| [State-of-the-art evaluation](specs/architecture/STATE-OF-ART-EVALUATION.md) | Existing tools, evaluation criteria, the recommended stack, and acceptance checks for a beta that generates working apps. |
| [Presentation website specification](specs/presentation/PRESENTATION_SITE_SPEC.md) | The design of the Screening Desk walkthrough, example repairs and features, the Azure architecture diagram, and the delivery forecast. |
| [Factory beta and production release](specs/architecture/BETA_TO_PRODUCTION_SPEC.md) | Working beta, open-ended feedback intake and monitoring, and the production release that concludes delivery. |

## Delivery in two phases

**Phase 1 delivers the factory to one internal team.** Target a working beta around Week 10 that generates a replacement for the release operations team’s legacy shift tracker. Rehearse migrating open items from one export, reconcile them at cutover and switch staff to the new app. One legacy booking feed supplies deadlines and delivery status. An independently verified repair keeps an assigned blocker visible. Keep beta open for feedback. Allow 2–4 weeks from sign-off to healthy production and accepted handover.

**Phase 2 extends the running factory.** The same team delivers the next integration or onboards another team based on actual use. Use a database view, legacy app, external API or ERP tool where the workflow calls for it. An illustrative allowance for one read-only ERP ticket lookup is 3–5 weeks once the contract, owner and test access are ready. A second team or an inbound ERP event has its own scope and estimate.

## Proposed internal beta

Start with one internal team and one Next.js starter. The Claude Agent SDK runs coding tasks in disposable Azure Container Apps Sandboxes. A separate sandbox verifies each change. PostgreSQL stores plans and approvals, and pg-boss dispatches short jobs so a project can pause and resume across milestones.

The [Azure sandbox Bicep template](infra/azure-poc/main.bicep) defines a sandbox group, a dedicated controller identity, and a data-plane role assignment scoped to that group. The trusted controller service uses that identity to create disposable sandboxes per run. The template can be compiled locally with `bicep build infra/azure-poc/main.bicep --stdout`. Deployment requires an approved resource group and permission to create the resources and role assignment.

## Presentation

The presentation follows four examples. A team replaces a legacy shift tracker, adds an ERP ticket lookup, repairs a hidden overdue booking, and applies the same factory to a second app. Executive mode introduces the architecture and delivery schedule. Technical mode covers access controls, verification evidence, cost and operations. The [local HTML](site/index.html) opens directly in a browser.

The header offers both Executive and Technical PDF downloads in either mode. Both editions include the four scenario transcripts and expanded FAQ answers. The website starts with the answers collapsed and opens a matching question when a reader follows a search result. When sharing the offline HTML, include its adjacent `downloads` folder.

Regenerate both PDFs after editing the page. The export script uses Python Playwright with a local Chromium browser. Install it once with `python -m pip install playwright` and `python -m playwright install chromium`, or use an installed Chrome with `--channel chrome`.

```sh
python scripts/export_pdfs.py
firebase deploy --only hosting --project software-factory-proposal
```

## Inspiration and learning

Microsoft’s article informed my choice to isolate each coding task in its own sandbox. ZazenCodes’ walkthrough helped me learn how to build a software factory around Claude Code.

- Microsoft Community Hub · [Azure Container Apps Sandboxes, Now Generally Available](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-container-apps-sandboxes-now-generally-available/4559125)
- ZazenCodes on YouTube · [Build Your Own AI Software Factory with Claude Code](https://www.youtube.com/watch?v=ctoaIC4LHmI)
