#!/usr/bin/env python3
"""Calculate one stated crowdfunding scenario without filling unknown inputs."""

import argparse
import json
import sys
from datetime import date
from decimal import Decimal, InvalidOperation


ZERO = Decimal("0")


def number(value, field, optional=False, signed=False):
    if value is None and optional:
        return None
    try:
        result = Decimal(str(value))
    except InvalidOperation as error:
        raise ValueError(f"{field} requires a decimal value or explicit zero") from error
    if not result.is_finite() or (not signed and result < ZERO):
        raise ValueError(f"{field} has an invalid amount")
    return result


def count(value, field):
    result = number(value, field, optional=True)
    if result is None:
        return None
    if result != result.to_integral_value():
        raise ValueError(f"{field} must be a nonnegative integer")
    return int(result)


def ratio(numerator, denominator):
    if numerator is None or denominator is None or denominator == 0:
        return None
    return Decimal(numerator) / Decimal(denominator)


def campaign(data):
    required = ["net_orders", "receipt_per_order", "unit_costs", "receipt_fee_rate",
                "agency_fixed_fee", "agency_commission_rate", "agency_commission_base",
                "fixed_offsets_commission", "other_fixed_costs", "ad_spend"]
    missing = [key for key in required if data.get(key) is None]
    if data.get("costs_complete") is not True:
        missing.append("confirmed_complete_costs")
    if missing:
        return {"status": "unknown", "missing": missing}
    orders = count(data["net_orders"], "net_orders")
    if not orders:
        raise ValueError("campaign.net_orders must be positive")
    if not isinstance(data["unit_costs"], dict) or not data["unit_costs"]:
        raise ValueError("unit_costs needs named costs, including explicit zero when applicable")
    unit_cost = sum((number(value, f"unit_costs.{key}")
                     for key, value in data["unit_costs"].items()), ZERO)
    amounts = {key: number(data[key], key) for key in required
               if key not in {"net_orders", "unit_costs", "fixed_offsets_commission"}}
    target_profit = number(data.get("target_profit"), "target_profit", optional=True, signed=True)
    if type(data["fixed_offsets_commission"]) is not bool:
        raise ValueError("fixed_offsets_commission must be true or false")
    if amounts["receipt_fee_rate"] > 1 or amounts["agency_commission_rate"] > 1:
        raise ValueError("Rates must be decimal fractions between zero and one")
    revenue = orders * amounts["receipt_per_order"]
    receipt_fees = revenue * amounts["receipt_fee_rate"]
    commission = amounts["agency_commission_base"] * amounts["agency_commission_rate"]
    fixed_fee = amounts["agency_fixed_fee"]
    fixed_top_up = max(fixed_fee - commission, ZERO) if data["fixed_offsets_commission"] else fixed_fee
    before_ads = revenue - orders * unit_cost - receipt_fees - commission
    after_ads = before_ads - amounts["ad_spend"]
    fixed_total = amounts["other_fixed_costs"] + fixed_top_up
    profit_before_ads = before_ads - fixed_total
    break_even_ads = profit_before_ads if profit_before_ads >= ZERO else None
    ad_capacity = None if target_profit is None else profit_before_ads - target_profit
    target_ads = ad_capacity if ad_capacity is not None and ad_capacity >= ZERO else None
    return {
        "status": "calculated_for_stated_scenario", "net_orders": orders,
        "revenue": revenue, "receipt_fees": receipt_fees,
        "agency_commission": commission, "agency_fixed_top_up": fixed_top_up,
        "agency_total_fee": commission + fixed_top_up,
        "contribution_before_ads_per_order": before_ads / orders,
        "net_order_cac": amounts["ad_spend"] / orders,
        "contribution_after_ads_per_order": after_ads / orders,
        "remaining_fixed_costs": fixed_total, "project_profit": after_ads - fixed_total,
        "profit_before_ads": profit_before_ads,
        "break_even_ad_spend": break_even_ads, "break_even_cac": ratio(break_even_ads, orders),
        "target_profit": target_profit,
        "max_ad_spend_for_target": target_ads, "max_cac_for_target": ratio(target_ads, orders),
        "gap_to_target_before_ads": None if ad_capacity is None else max(-ad_capacity, ZERO),
    }


def net_count(data, gross_key, refund_key):
    gross = count(data.get(gross_key), gross_key)
    refunded = count(data.get(refund_key), refund_key)
    if gross is None or refunded is None:
        return None
    if refunded > gross:
        raise ValueError(f"{refund_key} exceeds {gross_key}")
    return gross - refunded


def cohort(data):
    if not data.get("id") or not data.get("basis"):
        raise ValueError("Each cohort needs its own id and evidence basis")
    deposits = net_count(data, "deposit_payers", "deposit_refunds")
    orders = net_count(data, "full_payers", "full_refunds")
    deposit_spend = number(data.get("deposit_spend"), "deposit_spend", optional=True)
    total_spend = number(data.get("total_spend"), "total_spend", optional=True)
    converted = count(data.get("net_full_from_net_depositors"), "net_full_from_net_depositors")
    if converted is not None:
        for limit in (deposits, orders):
            if limit is not None and converted > limit:
                raise ValueError("Matched conversions exceed the corresponding cohort count")
    if deposit_spend is not None and total_spend is not None and deposit_spend > total_spend:
        raise ValueError("total_spend must include deposit_spend and later conversion spending")
    return {
        "id": data["id"], "basis": data["basis"],
        "net_deposit_payers": deposits, "net_full_payers_as_of_snapshot": orders,
        "net_deposit_cac": ratio(deposit_spend, deposits),
        "net_full_cac": ratio(total_spend, orders),
        "matched_deposit_to_full_rate": ratio(converted, deposits),
    }


def cash_flow(data):
    events = data.get("events")
    if data.get("opening_cash") is None or not isinstance(events, list):
        return {"status": "unknown", "reason": "Opening cash and dated events are required"}
    if any(event.get("date") is None or event.get("amount") is None for event in events):
        return {"status": "unknown", "reason": "Some cash events have unknown dates or amounts"}
    balance = number(data["opening_cash"], "opening_cash", signed=True)
    minimum = balance
    previous_date = date.min
    balances = []
    for event in events:
        event_date = date.fromisoformat(event["date"])
        if event_date < previous_date:
            raise ValueError("Cash events must be supplied in chronological order")
        balance += number(event["amount"], "cash event amount", signed=True)
        minimum = min(minimum, balance)
        balances.append({"date": event["date"], "label": event.get("label"), "balance": balance})
        previous_date = event_date
    assessment = "unknown"
    if data.get("events_complete") is True and data.get("timing_confirmed") is True:
        assessment = "funding_gap" if minimum < ZERO else "covered_for_stated_scope"
    return {
        "status": assessment, "minimum_balance_for_listed_sequence": minimum,
        "funding_gap_for_listed_sequence": max(-minimum, ZERO),
        "ending_balance_for_listed_sequence": balance, "balances": balances,
    }


def calculate(data):
    currency = data.get("currency", "")
    if len(currency) != 3 or not currency.isascii() or not currency.isalpha() or not currency.isupper():
        raise ValueError("Provide one three-letter currency code for all amounts")
    if not isinstance(data.get("basis"), str) or not data["basis"].strip():
        raise ValueError("basis must state the scope, cost coverage and evidence date")
    result = {"currency": currency, "basis": data["basis"]}
    if "campaign" in data:
        result["campaign"] = campaign(data["campaign"])
    if "cohorts" in data:
        ids = [row.get("id") for row in data["cohorts"]]
        if len(ids) != len(set(ids)):
            raise ValueError("Cohort ids must be unique")
        result["cohorts"] = [cohort(row) for row in data["cohorts"]]
    if "cash_flow" in data:
        result["cash_flow"] = cash_flow(data["cash_flow"])
    if len(result) == 2:
        raise ValueError("Provide campaign, cohorts or cash_flow")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="JSON file path, or - for stdin")
    args = parser.parse_args()
    try:
        if args.input == "-":
            data = json.load(sys.stdin, parse_float=Decimal)
        else:
            with open(args.input, encoding="utf-8") as source:
                data = json.load(source, parse_float=Decimal)
        print(json.dumps(calculate(data), ensure_ascii=False, indent=2, default=str))
    except (ValueError, TypeError, KeyError, OSError, AttributeError) as error:
        print(json.dumps({"status": "error", "error": str(error)}, ensure_ascii=False))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
