# 这单值得接吗？

给硬件众筹服务商的一项免费 Skill。在签合同、锁定项目经理和投手之前，判断一个项目该**接、先补测，还是放弃**。

Hardware crowdfunding intake review for agencies. Evaluate paid demand, delivery readiness, contract economics and staffing.

**[免安装试用](TRY_IT.md)** · **[两轮虚构案例](skills/review-hardware-crowdfunding/references/example.md)** · **[提交脱敏反馈](https://github.com/chenapq1018-jpg/review-hardware-crowdfunding/issues/new?template=trial-feedback.yml)**

## 把眼前这单交给它

准备现有产品材料、同批用户的预热和付款记录、服务费条款，以及团队可用人手。缺失的信息写“未知”即可。

它会给出一屏结论。

- 这次该接、补测或放弃，适用哪版合同与交付范围。
- 最影响决定的一两条证据，以及能复算的项目收益。
- 下一步先查什么，什么结果出现后值得改判。

例如，两单都已有真实付款和交付验证。A 要占用投手 8 天，预计直接贡献 1,400 美元。B 要 5 天，直接贡献 2,400 美元。当期只有一名投手，优先签 B。若 B 错过，再按 A 自己的收益、排期和接单底线评估。

遇到产品卖得动、服务商却确定亏损的合同，也会直接指出。材料只证明有人付了可退订金时，会把全款和退款的证据缺口留在结论中。

## 安装到支持 Skills 的 AI

安装工具需要 Node.js 22.20 或更新版本。在希望使用它的项目目录运行下面一行，再选择自己的 AI 工具。

```bash
npx skills add chenapq1018-jpg/review-hardware-crowdfunding --skill review-hardware-crowdfunding
```

安装后可以这样提问。

```text
请用 $review-hardware-crowdfunding 判断这单值得接吗。
我下面会给产品资料、预热数据、合同和人手安排。
请先指出最可能改变决定的一条证据，再给一个能执行的下一步。
```

[安装工具说明](https://github.com/vercel-labs/skills)

## 免费试用与反馈

本版本免费提供给个人和团队用于项目评审。先记下自己原本准备怎么决定，使用后再记录实际多查了什么、调整了什么。反馈表也可以报告算错的账、遗漏的重要事实以及与普通 AI 相比没有改善的地方。

欢迎在第二个项目或取得新数据后再次使用。反馈会随你的 GitHub 用户名公开显示，请填写去掉客户身份和敏感信息的摘要。项目原始数据留在你所选的 AI 使用环境中。

## 当前验证范围

已完成 3 组虚构案例的独立试跑，覆盖项目排期比较、净订金与有效订单的区别、固定费抵扣佣金、确定亏损的合同，以及取得新证据后的改判。虚构样例已核对算术。真实项目中的复用率和商业价值仍待使用者反馈。

Skill 指令采用中文，要求按使用者的语言回答。[查看完整评审方法](skills/review-hardware-crowdfunding/SKILL.md)
