"""Hypothetical IMPERIAL Core Class A/B shares; never an issuance or stock ledger."""
import argparse
import json
from decimal import Decimal, ROUND_HALF_UP

AUTH_B = 8_000_000
AUTH_A = 2_000_000
VOTES_B = 10
VOTES_A = 1
PAR_USD = "0.00001"

def percent(numerator, denominator):
    if not denominator:
        return None
    return str((Decimal(numerator) * 100 / Decimal(denominator)).quantize(
        Decimal("0.0001"), rounding=ROUND_HALF_UP))

def scenario(label, *, founder_b=0, team_a=0, investor_a=0, other_a=0,
             team_unissued_earmark_a=0):
    values = (founder_b, team_a, investor_a, other_a, team_unissued_earmark_a)
    if any(type(x) is not int or x < 0 for x in values):
        raise ValueError("Share counts must be nonnegative integers")
    if not isinstance(label, str) or not label.strip():
        raise ValueError("Scenario label required")
    issued_a = team_a + investor_a + other_a
    if founder_b > AUTH_B or issued_a > AUTH_A:
        raise ValueError("More shares than proposed authorization")
    if team_unissued_earmark_a > AUTH_A - issued_a:
        raise ValueError("Unissued team earmark exceeds remaining authorization")
    outstanding = founder_b + issued_a
    votes = founder_b * VOTES_B + issued_a * VOTES_A
    return {
        "scenario": label,
        "status": "HYPOTHETICAL_NOT_EVIDENCE_OF_ISSUANCE",
        "founder_b_hypothetically_issued": founder_b,
        "team_a_hypothetically_issued": team_a,
        "investor_a_hypothetically_issued": investor_a,
        "other_a_hypothetically_issued": other_a,
        "authorized_shares": AUTH_B + AUTH_A,
        "total_hypothetical_outstanding": outstanding,
        "class_a_remaining_unissued": AUTH_A - issued_a,
        "class_b_remaining_unissued": AUTH_B - founder_b,
        "class_a_team_earmarked_unissued": team_unissued_earmark_a,
        "founder_economic_percent": percent(founder_b, outstanding),
        "founder_ordinary_voting_percent": percent(founder_b * VOTES_B, votes),
        "ordinary_votes_total": votes,
        "preferred_shares_authorized_under_this_plan": False
    }

def examples():
    return [
        scenario("preformation_not_issued", team_unissued_earmark_a=1_000_000),
        scenario("founder_only", founder_b=8_000_000, team_unissued_earmark_a=1_000_000),
        scenario("500k_a_investor_team_pool_not_issued", founder_b=8_000_000,
                 investor_a=500_000, team_unissued_earmark_a=1_000_000),
        scenario("1m_a_team_all_issued", founder_b=8_000_000, team_a=1_000_000),
        scenario("all_2m_a_issued", founder_b=8_000_000,
                 team_a=1_000_000, investor_a=1_000_000),
    ]

def main():
    parser = argparse.ArgumentParser(description="Planning calculation; NO legal stock issuance")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {
        "schema": "imperial_proposed_equity_scenarios_v1",
        "company_formation_verified": False,
        "stock_issuance_verified": False,
        "class_b_authorized": AUTH_B,
        "class_a_authorized": AUTH_A,
        "class_b_votes_per_share": VOTES_B,
        "class_a_votes_per_share": VOTES_A,
        "proposed_par_usd_per_share": PAR_USD,
        "scenarios": examples(),
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("IMPERIAL Core — illustrative scenarios, NOT issued shares")
        for r in result["scenarios"]:
            print(r["scenario"], r["founder_economic_percent"],
                  r["founder_ordinary_voting_percent"])

if __name__ == "__main__":
    main()
