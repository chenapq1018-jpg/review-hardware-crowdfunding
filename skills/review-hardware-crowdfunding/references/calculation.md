# 从已有材料复算预算与现金

让 AI 从用户给出的报价、合同、漏斗导出和付款计划提取输入。遇到未知项保留 `null`，说明待核对的记录。输入 JSON 由 AI 构造，使用者可以直接提交现有资料。

## 内容

- [公司预算](#公司预算)
- [分组预热](#分组预热)
- [现金时点](#现金时点)

```bash
python3 scripts/campaign_math.py input.json
```

也可通过标准输入传入 JSON。所有金额使用同一币种，建议以十进制字符串传入。脚本使用 Decimal，输出金额与比率也为字符串，中间计算不按分截断。展示预算上限时向下取到该币种的最小货币单位。

顶层必须填写 `currency` 和 `basis`。后者写清本轮增量或全项目口径、成本覆盖范围、数据日期，以及退款已如何处理。可按需要提供 `campaign`、`cohorts`、`cash_flow` 中的一项或多项。

## 公司预算

以下为完全虚构的数据。此例计算下一轮新增 1,000 张净有效订单，历史试销独立结算。每单实收为 149 美元，已按归属处理代收税费。退款和售后损失已摊入每张净订单的成本。

```json
{
  "currency": "USD",
  "basis": "虚构案例。下一轮新增1000张净订单，历史试销独立结算。2026-11-06核对全部成本，退款损失已摊入售后。",
  "campaign": {
    "net_orders": 1000,
    "receipt_per_order": "149",
    "unit_costs": {
      "manufacturing_and_quality": "105",
      "packaging_and_shipping": "18",
      "refunds_and_warranty": "6",
      "other_applicable_unit_costs": "0"
    },
    "receipt_fee_rate": "0.08",
    "agency_fixed_fee": "10000",
    "agency_commission_rate": "0.10",
    "agency_commission_base": "149000",
    "fixed_offsets_commission": true,
    "other_fixed_costs": "15000",
    "ad_spend": "25000",
    "target_profit": "0",
    "costs_complete": true
  }
}
```

`unit_costs` 逐项列出按净订单摊销的非广告变动成本，包含适用的生产、质检、包装物流、税费及退款售后。与收入同比例收取的费用可合并到 `receipt_fee_rate`，其基数固定为本轮实收，需按实际条款核对。基数不同的费用先计算金额，再列入每单成本。服务商费用放在 `agency_*`，其余固定投入放在 `other_fixed_costs`，各项只计一次。

`agency_commission_base` 必须来自合同约定，允许与本轮实收不同。固定费抵佣金时，脚本把佣金作为变动费用，仅把超出佣金的固定费余额列入固定成本。未抵扣时，两项相加。没有服务商时，明确填写三个金额或比率为 `"0"`，并提供抵扣布尔值。

用户只给出已核对的广告前单笔贡献时，可以按“每单实收减该贡献”列一项汇总成本，注明已含的费用，并把已包含、无需额外扣计的费率与佣金填为零。合同仍存在另付保底费时须另列。汇总数只是暂估时，把完整性设为待核，或明确另建依赖该估算成立的情景，保留补查项。

只有核对成本完整后才将 `costs_complete` 设为 `true`。缺少必需字段或尚未核全成本时，预算返回 `unknown`。字段中的 `null` 不会变成零，命名成本里的未知金额会返回明确错误。

`target_profit` 是公司明确给出的本轮结果下限。要求打平时填 `"0"`，要求保留利润时填写相应正数。用户明确批准本轮最多亏损 5,000 美元时，可填 `"-5000"`。此额度必须来自用户授权，AI 不自行假设。其他成本、费率和广告支出继续要求非负。

目标未知时可省略 `target_profit` 或填 `null`。工具仍复算当前报价、销量和广告投入下的 `project_profit`、广告前项目损益 `profit_before_ads`，并输出明确以盈亏平衡为条件的广告上限 `break_even_ad_spend` 和 CAC 上限 `break_even_cac`。公司目标对应的 `max_ad_spend_for_target`、`max_cac_for_target` 和 `gap_to_target_before_ads` 保持 `null`，输出中的 `target_profit` 也为 `null`。即使不花广告费仍亏损时，盈亏平衡上限保持 `null`。

该例结果应为代理总收费 14,900 美元、广告前单笔贡献 −6.82 美元、广告后单笔贡献 −31.82 美元，本轮亏损 46,820 美元。`max_ad_spend_for_target` 和 `max_cac_for_target` 均为 `null`，因为广告费为零时仍无法实现目标利润。

改变售价、销量或预算时，另算一份情景。输入销量是预测时明确注明，获客成本在新价格或扩量后能否复现须另行验证。已发生成本、未支付承诺和未来新增投入按口径分别归集，工具不会自行决定哪些成本可以忽略。

## 分组预热

以下两组来自不同渠道。每组的 `basis` 写清时间、售价、统计人数与退款窗口。`deposit_spend` 为取得订金的支出，`total_spend` 为该组包含后续转化费用的全部获客支出。

```json
{
  "currency": "USD",
  "basis": "虚构预热导出。2026-11-06，按去重付费人数统计，每人最多计一单。",
  "cohorts": [
    {
      "id": "cold-ad-deposits",
      "basis": "本轮冷广告，众筹目标价329美元，可退订金，尚无同批全款记录。",
      "deposit_spend": "1200",
      "total_spend": null,
      "deposit_payers": 180,
      "deposit_refunds": 30,
      "full_payers": null,
      "full_refunds": null,
      "net_full_from_net_depositors": null
    },
    {
      "id": "creator-orders",
      "basis": "独立达人渠道，实付329美元，退款窗口已过，费用待归集。",
      "deposit_spend": null,
      "total_spend": null,
      "deposit_payers": null,
      "deposit_refunds": null,
      "full_payers": 35,
      "full_refunds": 5,
      "net_full_from_net_depositors": null
    }
  ]
}
```

第一组净订金人数为 150，净订金成本为 8 美元。第二组净全款人数为 30，全款获客成本保持 `null`。工具逐组计算，不跨渠道拼接转化率。

把漏斗获客成本用于公司预算时，先对齐支出口径。同一笔达人或服务商费用已列在预算的固定或变动成本里时，不再计入 `ad_spend`。

`net_full_from_net_depositors` 只填能与本组净订金名单逐人匹配的净全款人数，才能计算订金到全款的转化率。全款也可能由直接付款者贡献，不能直接拿本组所有全款人数作分子。缺少退款数时净人数未知，明确零退款需填 `0`。退款窗口未关闭时，只描述截至数据日期的表现。

## 现金时点

金额正数为流入，负数为流出。事件按照实际发生顺序填写，同一天的先后也需核对。缺少日期或金额时，工具返回 `unknown`。事件未收集完整或先后顺序尚未确认时，计算仅对应所列顺序，资金覆盖结论保持 `unknown`。

```json
{
  "currency": "USD",
  "basis": "虚构现金计划。金额均为确定的实际收付，日期及同日顺序已核对。",
  "cash_flow": {
    "opening_cash": "10000",
    "events_complete": true,
    "timing_confirmed": true,
    "events": [
      {"date": "2026-11-10", "label": "工厂预付款", "amount": "-15000"},
      {"date": "2026-12-01", "label": "平台净回款", "amount": "20000"}
    ]
  }
}
```

该例最低余额为 −5,000 美元，已列计划存在 5,000 美元缺口。回款后的期末余额为正，仍需先解决前置付款。预算盈利与现金覆盖需要各自的输入证据。
