# 硬件众筹评审与改进

给准备做众筹的硬件公司使用。交出已有产品资料、页面、视频、预热导出或报价，得到一份能直接交给团队执行的修订，以及下一笔投入该怎样决定。

**[看完整输入与成品](skills/review-hardware-crowdfunding/references/example.md)** · **[免安装使用](TRY_IT.md)** · **[提交脱敏反馈](https://github.com/chenapq1018-jpg/review-hardware-crowdfunding/issues/new?template=trial-feedback.yml)**

## 拿现有材料来

| 你交给它什么 | 应该拿回什么 |
| --- | --- |
| 产品定义、功能和用户记录 | 推荐的核心用户、一个主要购买理由、功能取舍与最小验证 |
| 众筹页面、主视频或脚本 | 原句与改稿对照、可替换首屏、15—30 秒分镜及补拍清单 |
| 预热和付款导出 | 按批次复算的漏斗、证据能支持的决定及一份付费验证安排 |
| 成本、服务合同和预算 | 可复算的订单贡献、佣金抵扣、广告上限与现金缺口 |
| 量产状态和交期承诺 | 关键验证、首批范围、角色分工与可采用的交付沟通草稿 |

它先读已有材料，选择最影响当前决策的问题，完成对应成果。必要追问集中在最后。结论保持简短，改稿、实验与测算按任务需要交完整。

例如，完整虚构案例里，CEO 给了一份翻拍器草稿。页面承诺“十倍快、零操作”，实测只支持固定底片和逐格对齐更省事。成果包含面向胶片摄影者的购买理由、首屏、30 秒视频脚本及付费实验。

同一案例中，200 个净订单最多支持 **7,046 美元**广告费才能打平。团队原定 9,000 美元，计算出的本轮亏损为 **1,954 美元**。改稿与预算共同决定先验证什么。[查看完整案例](skills/review-hardware-crowdfunding/references/example.md)

## 内置的方法与工具

- [十类判断模式](skills/review-hardware-crowdfunding/references/decision-patterns.md) 将材料中的信号连到决策错误、具体改法与证据边界，涵盖使用负担、尝鲜人群、首日预热、视频、信任、KOL、价格、代理执行及交付。
- [五类成品规格与示例](skills/review-hardware-crowdfunding/references/deliverables.md) 展示产品定义、首屏分镜、实验安排、预算与交付修订应做到什么程度。
- [计算工具与输入说明](skills/review-hardware-crowdfunding/references/calculation.md) 使用 Python 标准库复算预算、独立批次和现金时点。AI 从现有资料整理输入，缺失成本保持未知。
- [核心工作流程](skills/review-hardware-crowdfunding/SKILL.md) 约束读取、判断、改进、核算与复评。支持明确批准的有限亏损试验，并显示实际损益。

## 安装

在支持 Skills 的 AI 环境中运行下面一行，按提示选择工具。

```bash
npx skills add chenapq1018-jpg/review-hardware-crowdfunding --skill review-hardware-crowdfunding
```

安装工具的环境要求见官方说明，计算脚本需要 Python 3。[安装工具说明](https://github.com/vercel-labs/skills)

安装后直接提交已有材料。

```text
请用 $review-hardware-crowdfunding 处理下面这份众筹材料。
我们这次要决定下一笔钱投在哪里。
请先读材料，给结论，并完成最值得先做的一份改稿、验证方案或预算。
```

## 使用与反馈

本版本免费提供给个人和团队用于项目评审与改进。成果以给定材料和明确假设为依据，当前平台规则与竞品信息由使用时查证。

本版包含完整的虚构输入与成品示例，计算脚本已执行数值校验，修订流程已用虚构创业项目独立试跑。真实公司是否采用改稿、是否重复使用、是否改善决策，仍需实际反馈。

反馈最有价值的内容是你实际采用了哪一段成果、据此改了什么，以及哪一处依然空泛或算错。反馈和 GitHub 用户名会公开显示，请只提交去掉身份和敏感信息的摘要。[反馈入口](https://github.com/chenapq1018-jpg/review-hardware-crowdfunding/issues/new?template=trial-feedback.yml)
