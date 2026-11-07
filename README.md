# Smart Hardware Crowdfunding

English | [简体中文](README.zh-CN.md)

An agent skill for smart hardware teams preparing a Kickstarter or other crowdfunding campaign. Review your product, pre-launch plan, pricing, advertising, and production schedule to decide whether to launch and what to fix first.

Share the product brief, campaign page, video script, or business data you already have. The skill reviews the material, recommends changes, and drafts the copy, tests, or budget calculations you need.

## Features

| Area | What it helps with |
| --- | --- |
| Product definition | Identify target customers, use cases, and alternatives. Work out why someone would buy and which features justify the price. |
| Pre-launch validation | Check leads, deposits, paid orders, and refunds. Plan pricing and payment tests, and estimate first-day orders. |
| Campaign page and video | Review selling points, demonstrations, customer stories, and endorsements. Rewrite the hero section, video opening, or shooting script. |
| Pricing and advertising | Calculate order margins, agency fees, affordable acquisition costs, and cash shortfalls. Revise the ad budget. |
| Production and delivery | Review prototypes, pilot production, quality checks, schedules, and support. Revise the first batch and delivery plan. |

It starts with the material available and asks about gaps that could change the decision. Bring new data back to review the same project again.

## Installation

Run this in a tool that supports Agent Skills.

```bash
npx skills add chenapq1018-jpg/review-hardware-crowdfunding --skill review-hardware-crowdfunding
```

Check the installer documentation for environment requirements. The budget script requires Python 3. [Installer documentation](https://github.com/vercel-labs/skills)

## Usage

After installation, ask a question and attach your existing material.

```text
Use $review-hardware-crowdfunding to review our crowdfunding plan.
Here are the product brief, pre-launch data, and cost breakdown.
Are we ready to launch? Which problems should we fix first?
```

You can also focus on one task.

```text
Use $review-hardware-crowdfunding to review this campaign page and video script.
Find what could prevent a purchase, then rewrite the hero section and the first 30 seconds.
```

Paste text, share links, or upload files. The review instructions and detailed examples are currently written in Chinese. You can ask your agent to respond in English. [Try without installing](TRY_IT.md)

## Example

FrameDock is a fictional film-digitizing device used in the worked example. Its team is choosing between families digitizing old photos and photographers who regularly shoot film. The campaign promises ten times the speed and zero effort, while the user records only support easier film positioning.

The example covers audience selection, revised hero copy and video opening, a payment test, and an ad budget. Under its stated costs and sales assumptions, the proposed $9,000 ad spend produces a $1,954 project loss. The break-even ad budget is $7,046. [Read the full example in Chinese](skills/review-hardware-crowdfunding/references/example.md)

## Files

- Review scope and instructions. [SKILL.md](skills/review-hardware-crowdfunding/SKILL.md)
- Common crowdfunding problems and how to assess them. [Review methods](skills/review-hardware-crowdfunding/references/decision-patterns.md)
- Examples of product definitions, copy, tests, and delivery plans. [Sample outputs](skills/review-hardware-crowdfunding/references/deliverables.md)
- Budget, acquisition cost, and cash-flow calculations. [Calculation guide](skills/review-hardware-crowdfunding/references/calculation.md)

## Feedback

Free for individual and team use. The skill has been tested on fictional projects, and the calculations have been checked. Its usefulness on real projects still needs user feedback.

Tell us which recommendations you used, whether the copy worked for your team, and what was wrong or missing. Remove company, customer, and other sensitive details before posting. Your GitHub username and feedback will be public. [Send feedback](https://github.com/chenapq1018-jpg/review-hardware-crowdfunding/issues/new?template=trial-feedback.yml)
