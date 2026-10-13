"""Offline project integrity checks; does not validate scientific hypotheses."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {"verified_access", "source_missing", "hypothesis", "model_unverified",
            "simulation_unverified", "empirical_unverified", "validated",
            "refuted", "contested"}

def load(name, root=ROOT):
    return json.loads((root / "registries" / name).read_text(encoding="utf-8"))

def index_records(records, label, errors):
    indexed = {}
    for record in records:
        rid = record.get("id")
        if not rid or rid in indexed:
            errors.append(f"{label}: missing or duplicate ID {rid}")
        indexed[rid] = record
    return indexed

def check_records(sources, claims, experiments, root):
    errors = []
    source_map = index_records(sources, "source", errors)
    experiment_map = index_records(experiments, "experiment", errors)
    claim_map = index_records(claims, "claim", errors)
    for source in sources:
        if source.get("availability") not in {"available", "metadata_only", "missing"}:
            errors.append(f"{source.get('id')}: invalid availability")
        if source.get("availability") == "available" and not source.get("locator"):
            errors.append(f"{source.get('id')}: available source needs locator")
    for experiment in experiments:
        eid = experiment.get("id")
        if experiment.get("status") not in {"planned", "running", "completed", "failed"}:
            errors.append(f"{eid}: invalid experiment status")
        for cid in experiment.get("claim_ids", []):
            if cid not in claim_map:
                errors.append(f"{eid}: unknown claim {cid}")
        if experiment.get("status") == "completed":
            artifacts = experiment.get("artifacts", [])
            if not artifacts or not experiment.get("command") or not experiment.get("code_commit"):
                errors.append(f"{eid}: completed run needs command, commit and artifacts")
            for artifact in artifacts:
                path = (root / artifact).resolve()
                if not path.is_relative_to(root.resolve()) or not path.is_file():
                    errors.append(f"{eid}: artifact missing or outside project: {artifact}")
    required = {"id", "statement", "kind", "status", "source_ids", "locators",
                "assumptions", "uncertainty", "verification", "experiment_ids"}
    for claim in claims:
        cid = claim.get("id")
        if required - claim.keys():
            errors.append(f"{cid}: missing fields {sorted(required - claim.keys())}")
        if claim.get("status") not in STATUSES:
            errors.append(f"{cid}: invalid status")
        if claim.get("status") == "verified_access" and claim.get("kind") != "access":
            errors.append(f"{cid}: verified_access reserved for access observations")
        for sid in claim.get("source_ids", []):
            if sid not in source_map:
                errors.append(f"{cid}: unknown source {sid}")
        for eid in claim.get("experiment_ids", []):
            if eid not in experiment_map:
                errors.append(f"{cid}: unknown experiment {eid}")
        if claim.get("status") == "validated":
            refs = claim.get("source_ids", [])
            if not refs or not claim.get("locators"):
                errors.append(f"{cid}: validated claim needs sources and locators")
            if any(source_map.get(sid, {}).get("availability") != "available" for sid in refs):
                errors.append(f"{cid}: validated claim has unavailable source")
            runs = claim.get("experiment_ids", [])
            if not runs or any(experiment_map.get(eid, {}).get("status") != "completed" for eid in runs):
                errors.append(f"{cid}: validated claim needs completed experiment")
    return errors

def validate(root=ROOT):
    errors = check_records(load("sources.json", root)["sources"],
                           load("claims.json", root)["claims"],
                           load("experiments.json", root)["experiments"], root)
    required = ["README.md", "docs/CHARTER.md", "docs/RESEARCH_PLAN.md",
                "docs/DOSSIER_REVIEW.md", "docs/CLAIMS_REGISTER.md",
                "docs/MUNIN_ACCESS.md", "docs/BACKLOG.md", "docs/VERIFICATION.md"]
    errors.extend(f"Missing {path}" for path in required if not (root / path).is_file())
    for name in ["sources.json", "claims.json", "experiments.json", "access-audit.json",
                 "issues.json", "verification.json"]:
        if load(name, root).get("schema_version") != 1:
            errors.append(f"{name}: unexpected schema version")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in link or link.startswith("#"):
                continue
            target = link.split("#")[0]
            if target and not (path.parent / target).is_file():
                errors.append(f"{path.relative_to(root)}: broken link {link}")
    audit = load("access-audit.json", root)
    if audit.get("read_only") is not True or audit.get("write_attempted") is not False:
        errors.append("Access audit must preserve verified read-only/no-write status")
    if audit.get("restricted_access_attempted") is not False or audit.get("sync_performed") is not False:
        errors.append("Unexpected restricted access or synchronization claim")
    return errors

if __name__ == "__main__":
    problems = validate()
    if problems:
        for problem in problems:
            print("ERROR:", problem)
        raise SystemExit(1)
    print("PASS: project structure, links, registers and evidence constraints")
    print("Scientific validation: NOT PERFORMED")
