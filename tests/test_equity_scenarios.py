"""Public equity planning math: tests must not imply actual securities were issued."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from equity_scenarios import scenario,examples,AUTH_A,AUTH_B,PAR_USD

class EquityScenarioChecks(unittest.TestCase):
    def test_approved_authorized_ceiling(self):
        self.assertEqual(AUTH_A+AUTH_B,10_000_000)
    def test_par_is_not_company_valuation(self):
        self.assertEqual(PAR_USD,"0.00001")
    def test_preformation_not_fake_100_percent(self):
        s=examples()[0]
        self.assertIsNone(s["founder_economic_percent"])
        self.assertIsNone(s["founder_ordinary_voting_percent"])
        self.assertEqual(s["total_hypothetical_outstanding"],0)
    def test_founder_only(self):
        s=scenario("founder",founder_b=8_000_000,team_unissued_earmark_a=1_000_000)
        self.assertEqual(s["founder_economic_percent"],"100.0000")
        self.assertEqual(s["founder_ordinary_voting_percent"],"100.0000")
        self.assertEqual(s["class_a_remaining_unissued"],2_000_000)
    def test_reservation_is_not_issuance(self):
        s=scenario("pool",team_unissued_earmark_a=1_000_000)
        self.assertEqual(s["team_a_hypothetically_issued"],0)
        self.assertEqual(s["class_a_remaining_unissued"],2_000_000)
    def test_half_million_investor(self):
        s=scenario("investor",founder_b=8_000_000,investor_a=500_000,team_unissued_earmark_a=1_000_000)
        self.assertEqual(s["founder_economic_percent"],"94.1176")
        self.assertEqual(s["founder_ordinary_voting_percent"],"99.3789")
    def test_full_authorization_used(self):
        s=scenario("all",founder_b=8_000_000,team_a=1_000_000,investor_a=1_000_000)
        self.assertEqual(s["founder_economic_percent"],"80.0000")
        self.assertEqual(s["founder_ordinary_voting_percent"],"97.5610")
        self.assertEqual(s["ordinary_votes_total"],82_000_000)
        self.assertEqual(s["class_a_remaining_unissued"],0)
    def test_oversubscription_denied(self):
        with self.assertRaises(ValueError): scenario("bad",founder_b=8_000_001)
        with self.assertRaises(ValueError): scenario("bad",team_a=1_000_001,investor_a=1_000_000)
    def test_noninteger_and_negative_denied(self):
        for value in (-1,0.5,True):
            with self.assertRaises(ValueError): scenario("bad",investor_a=value)
    def test_earmark_exceeds_capacity(self):
        with self.assertRaises(ValueError): scenario("bad",team_a=1_500_000,team_unissued_earmark_a=600_000)
    def test_never_claims_legal_issuance(self):
        for s in examples():
            self.assertEqual(s["status"],"HYPOTHETICAL_NOT_EVIDENCE_OF_ISSUANCE")
            self.assertFalse(s["preferred_shares_authorized_under_this_plan"])
    def test_json_cli_status(self):
        p=subprocess.run([sys.executable,str(ROOT/"tools"/"equity_scenarios.py"),"--json"],
                         check=True,capture_output=True,text=True)
        data=json.loads(p.stdout)
        self.assertFalse(data["company_formation_verified"])
        self.assertFalse(data["stock_issuance_verified"])
        self.assertEqual(len(data["scenarios"]),5)

if __name__=="__main__":
    unittest.main()
