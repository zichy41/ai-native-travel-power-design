"""Static wall-load torque model for the Anker Atlas Relay concept.

This is a simplified engineering pre-validation model, not a physical drop-rate test.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

G = 9.81


@dataclass(frozen=True)
class Component:
    name: str
    mass_kg: float
    lever_arm_m: float

    @property
    def torque_nm(self) -> float:
        return self.mass_kg * G * self.lever_arm_m


def calculate_cases() -> dict[str, float]:
    direct = Component("65W direct wall charger", 0.132, 0.03305)

    adapter = Component("travel adapter", 0.107, 0.01245)
    charger_after_adapter = Component("65W charger after adapter", 0.132, 0.05795)

    light_wall_head = Component("light region plug head", 0.025, 0.01000)

    return {
        "65W direct wall charger": direct.torque_nm,
        "Travel adapter + 65W charger": adapter.torque_nm + charger_after_adapter.torque_nm,
        "Light plug + short cable": light_wall_head.torque_nm,
    }


def save_results(output_dir: Path, cases: dict[str, float]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    stacked = cases["Travel adapter + 65W charger"]
    short = cases["Light plug + short cable"]
    reduction = 1 - short / stacked

    with (output_dir / "torque_results.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["case", "torque_Nm", "relative_to_stacked", "note"])
        for name, value in cases.items():
            writer.writerow([
                name,
                f"{value:.6f}",
                f"{value / stacked:.4f}",
                "Static gravitational torque only",
            ])
        writer.writerow(["Short-cable reduction vs stacked", f"{reduction:.4%}", "", "Not a real-world drop-rate reduction"])

    labels = list(cases.keys())
    values = list(cases.values())

    plt.figure(figsize=(9, 5))
    plt.bar(labels, values)
    plt.ylabel("Static wall-end torque (N·m)")
    plt.title("Wall-End Torque Comparison")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(output_dir / "torque_comparison.png", dpi=180)
    plt.close()

    masses_g = np.arange(20, 41, 2)
    distances_mm = np.arange(8, 16, 1)
    grid = np.zeros((len(distances_mm), len(masses_g)))

    for i, d_mm in enumerate(distances_mm):
        for j, m_g in enumerate(masses_g):
            grid[i, j] = (m_g / 1000) * G * (d_mm / 1000)

    plt.figure(figsize=(9, 5))
    image = plt.imshow(
        grid,
        aspect="auto",
        origin="lower",
        extent=[masses_g.min(), masses_g.max(), distances_mm.min(), distances_mm.max()],
    )
    plt.xlabel("Wall-head mass (g)")
    plt.ylabel("Lever arm (mm)")
    plt.title("Sensitivity: Light Wall-Head Torque")
    plt.colorbar(image, label="Torque (N·m)")
    plt.tight_layout()
    plt.savefig(output_dir / "sensitivity_analysis.png", dpi=180)
    plt.close()

    with (output_dir / "sensitivity_results.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["wall_head_mass_g", "lever_arm_mm", "torque_Nm", "reduction_vs_stacked"])
        for d_mm in distances_mm:
            for m_g in masses_g:
                torque = (m_g / 1000) * G * (d_mm / 1000)
                writer.writerow([m_g, d_mm, f"{torque:.6f}", f"{1 - torque / stacked:.4%}"])


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    output_dir = repo_root / "results"

    cases = calculate_cases()
    save_results(output_dir, cases)

    print("Static torque results:")
    for name, value in cases.items():
        print(f"- {name}: {value:.6f} N·m")

    stacked = cases["Travel adapter + 65W charger"]
    short = cases["Light plug + short cable"]
    print(f"- Reduction vs stacked: {(1 - short / stacked):.2%}")
    print("\nImportant: this is not a physical drop-rate test.")


if __name__ == "__main__":
    main()
