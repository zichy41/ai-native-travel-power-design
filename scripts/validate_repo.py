"""Lightweight repository integrity check.

This script checks required files, JSON/CSV readability, and prominent disclosure text.
It does not verify external URLs or engineering correctness.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "PROJECT_STATUS.md",
    "DISCLOSURE.md",
    "docs/10_current_product_definition_v1.md",
    "research/public_user_evidence_v2.csv",
    "research/source_index_v2.csv",
    "engineering/architecture_v1.md",
    "engineering/physical_experiment_protocol_v1.md",
    "product/industrial_design_v1.md",
    "application/form_text_copy_ready.txt",
    "prototype/workflow_orchestrator_mock.py",
    "prototype/dashboard/index.html",
]
JSON_FILES = [
    "prototype/sample_project_data.json",
    "workflow/roles.json",
    "workflow/evidence_schema.json",
    "workflow/hypothesis_schema.json",
    "workflow/concept_schema.json",
    "results/phase3_metadata.json",
    "results/phase4_metadata.json",
]
CSV_FILES = [
    "research/public_user_evidence_v2.csv",
    "research/source_index_v2.csv",
    "research/hypothesis_register.csv",
    "research/competitor_matrix_v2.csv",
    "results/candidate_scoring.csv",
    "engineering/test_matrix_v1.csv",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"Missing or empty required file: {rel}")

    for rel in JSON_FILES:
        with (ROOT / rel).open("r", encoding="utf-8") as f:
            json.load(f)

    for rel in CSV_FILES:
        with (ROOT / rel).open("r", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.reader(f))
            if len(rows) < 2:
                fail(f"CSV has no data rows: {rel}")

    disclosure = (ROOT / "DISCLOSURE.md").read_text(encoding="utf-8")
    for phrase in ["不是实体实验结果", "不得声称", "AI 合成用户"]:
        if phrase not in disclosure:
            fail(f"Disclosure is missing phrase: {phrase}")

    evidence_rows = sum(1 for _ in (ROOT / "research/public_user_evidence_v2.csv").open("r", encoding="utf-8-sig")) - 1
    source_rows = sum(1 for _ in (ROOT / "research/source_index_v2.csv").open("r", encoding="utf-8-sig")) - 1
    print("Repository validation passed.")
    print(f"- Evidence rows: {evidence_rows}")
    print(f"- Source links: {source_rows}")
    print(f"- Root: {ROOT}")


if __name__ == "__main__":
    main()
