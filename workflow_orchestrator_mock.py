"""Deterministic mock of the AI-native product workflow.

This file does NOT call an LLM. It demonstrates data flow, evidence gates,
counter-evidence handling, and decision auditing. Replace each agent function
with an actual model/API call in a later milestone.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def evidence_gate(hypothesis_id: str, evidence: list[dict[str, Any]]) -> dict[str, Any]:
    supporting = [e for e in evidence if hypothesis_id in e.get("supports", [])]
    non_synthetic = [e for e in supporting if e.get("type") != "synthetic_user"]
    high_quality = [e for e in non_synthetic if e.get("strength") in {"high", "medium_high"}]

    if len(high_quality) >= 2:
        status = "eligible_for_core_definition"
    elif len(non_synthetic) >= 1:
        status = "keep_as_hypothesis"
    else:
        status = "blocked"

    return {
        "hypothesis_id": hypothesis_id,
        "supporting_evidence_ids": [e["id"] for e in supporting],
        "high_quality_count": len(high_quality),
        "gate_status": status,
    }


def audit_claims(data: dict[str, Any]) -> list[dict[str, Any]]:
    evidence = data["evidence"]
    return [evidence_gate(h["id"], evidence) for h in data["hypotheses"]]


def load_candidate_scores(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def build_report(audit: list[dict[str, Any]], candidates: list[dict[str, str]]) -> str:
    ranked = sorted(candidates, key=lambda x: float(x["加权总分"]), reverse=True)

    lines = [
        "# Mock AI-Native Workflow Report",
        "",
        "> Deterministic demonstration only; no LLM was called.",
        "",
        "## Evidence Gates",
        "",
        "| Hypothesis | Supporting evidence | High-quality count | Gate |",
        "|---|---|---:|---|",
    ]
    for item in audit:
        lines.append(
            f"| {item['hypothesis_id']} | {', '.join(item['supporting_evidence_ids']) or 'None'} "
            f"| {item['high_quality_count']} | {item['gate_status']} |"
        )

    lines += [
        "",
        "## Candidate Ranking",
        "",
        "| Rank | Concept | Score |",
        "|---:|---|---:|",
    ]
    for i, candidate in enumerate(ranked, start=1):
        lines.append(f"| {i} | {candidate['候选方案']} | {candidate['加权总分']} |")

    lines += [
        "",
        "## Human Decision Required",
        "",
        "- A score does not approve a product automatically.",
        "- H04 remains a hypothesis until real users or review data support charge-interruption assurance.",
        "- H05 remains on hold because a battery module may add weight and certification complexity.",
        "- Atlas Relay currently leads, but it must pass physical socket-load and user-complexity tests.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    data = load_json(REPO / "prototype" / "sample_project_data.json")
    audit = audit_claims(data)
    candidates = load_candidate_scores(REPO / "results" / "candidate_scoring.csv")
    report = build_report(audit, candidates)

    output = REPO / "results" / "workflow_demo_report.md"
    output.write_text(report, encoding="utf-8")
    print(report)
    print(f"Saved to: {output}")


if __name__ == "__main__":
    main()
