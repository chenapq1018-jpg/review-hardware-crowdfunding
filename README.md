# Smart Hardware Crowdfunding

**智能硬件众筹评审**

中文 | [English](README.en.md)

为准备做 Kickstarter 等众筹的智能硬件团队提供产品和运营评审。覆盖产品定义、预热、定价、广告投放和量产交付，帮助团队判断产品是否适合众筹、什么时候上线、哪些问题要先解决。

把已有的产品介绍、页面、视频脚本或经营数据发给 AI 就可以开始。它会结合资料提出建议，并完成需要修改的文案、测试方案或预算测算。

## 功能

| 方向 | 可以做什么 |
| --- | --- |
| 产品定义 | 分析目标用户、使用场景和替代方案，梳理购买理由，检查新增功能是否值得用户付钱 |
| 预热与需求验证 | 核对留资、订金、全款和退款数据，设计价格测试与付费测试，估算首日订单 |
| 页面与主视频 | 检查卖点、演示、用户故事和背书，改写首屏文案、视频开场及拍摄脚本 |
| 定价与广告 | 计算订单利润、服务商费用、可承受的获客成本和资金缺口，调整投放预算 |
| 量产与交付 | 检查样机、试产、质量、生产排期和售后准备，修改首批计划与交付说明 |

资料不全时，会先分析已有内容，再问影响判断的问题。团队拿到新数据后，可以继续评审同一个项目。

## 安装

在支持 Agent Skills 的工具中运行。

```bash
npx skills add chenapq1018-jpg/review-hardware-crowdfunding --skill review-hardware-crowdfunding
```

安装环境要求见官方说明，预算计算脚本需要 Python 3。[安装工具说明](https://github.com/vercel-labs/skills)

## 使用

安装后直接提问，并附上现有资料。

```text
请用 $review-hardware-crowdfunding 看一下我们的众筹方案。
下面是产品介绍、预热数据和成本表。
现在适合上线吗？最需要先解决哪几个问题？
```

也可以只处理一个具体问题。

```text
请用 $review-hardware-crowdfunding 看这份众筹页面和视频脚本。
帮我找出影响购买的地方，改好首屏和视频前30秒。
```

可以直接粘贴文字、提供链接或上传文件。[免安装试用](TRY_IT.md)

## 示例

FrameDock 是案例中虚构的一款底片翻拍器。团队在“家庭旧照片”和“胶片摄影爱好者”两个方向之间犹豫，页面写着“十倍快、零操作”，但试用记录只说明固定和对齐底片更省事。

案例展示了如何选择目标用户、重写首屏和视频开场、安排付费测试，以及核算广告预算。按案例中的报价和销量，原定 9,000 美元广告费会让这轮项目亏损 1,954 美元，盈亏平衡时最多能花 7,046 美元。[查看完整案例](skills/review-hardware-crowdfunding/references/example.md)

## 文件说明

- 评审范围和使用步骤。[SKILL.md](skills/review-hardware-crowdfunding/SKILL.md)
- 众筹中常见的问题，以及如何判断和修改。[评审方法](skills/review-hardware-crowdfunding/references/decision-patterns.md)
- 产品定义、文案、测试和交付计划的写法。[方案示例](skills/review-hardware-crowdfunding/references/deliverables.md)
- 预算、获客成本和现金收支的计算方法。[计算说明](skills/review-hardware-crowdfunding/references/calculation.md)

## 反馈

个人和团队可以免费使用。目前完成了虚构案例测试和计算检查，真实项目中的效果还需要使用反馈。

欢迎告诉我们哪条建议被采用了、改稿能不能用、哪里算错或漏看了。提交前请删去公司、客户及其他敏感信息，GitHub 用户名和反馈内容会公开显示。[提交反馈](https://github.com/chenapq1018-jpg/review-hardware-crowdfunding/issues/new?template=trial-feedback.yml)
