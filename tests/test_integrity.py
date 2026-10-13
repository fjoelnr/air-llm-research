import copy
import unittest
from pathlib import Path
from scripts.validate import check_records, load, validate

class EvidenceIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.sources = load("sources.json")["sources"]
        self.claims = load("claims.json")["claims"]

    def test_current_project(self):
        self.assertEqual(validate(), [])

    def test_unavailable_source_cannot_be_validated(self):
        claim = copy.deepcopy(self.claims[2])
        claim["status"] = "validated"
        errors = check_records(self.sources, [claim], [], Path("."))
        self.assertTrue(any("unavailable source" in e for e in errors))
        self.assertTrue(any("completed experiment" in e for e in errors))

    def test_scientific_claim_cannot_use_access_status(self):
        claim = copy.deepcopy(self.claims[0])
        claim["kind"] = "hypothesis"
        errors = check_records(self.sources, [claim], [], Path("."))
        self.assertTrue(any("reserved for access" in e for e in errors))

    def test_completed_run_needs_real_artifacts(self):
        runs = [{"id": "E01", "status": "completed", "command": "python run.py",
                 "code_commit": "placeholder", "artifacts": ["missing-test-artifact.json"]}]
        errors = check_records(self.sources, self.claims, runs, Path(__file__).parent)
        self.assertTrue(any("artifact missing" in e for e in errors))

    def test_unknown_source_is_rejected(self):
        claim = copy.deepcopy(self.claims[0])
        claim["source_ids"] = ["DOES-NOT-EXIST"]
        errors = check_records(self.sources, [claim], [], Path("."))
        self.assertTrue(any("unknown source" in e for e in errors))

    def test_duplicate_claim_is_rejected(self):
        errors = check_records(self.sources, [self.claims[0], self.claims[0]], [], Path("."))
        self.assertTrue(any("duplicate ID" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
