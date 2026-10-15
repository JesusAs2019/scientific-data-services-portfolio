"""
Module 4 CLI Runner & Demo Execution
"""

from module4_scientific_accelerator.models import ReadinessStatus, RawCompoundInput
from module4_scientific_accelerator.engine import (
    IngestionEngine,
    ValidationEngine,
    AIMNet2ExecutionEngine,
    GovernedDataVault
)

def main():
    print("=" * 80)
    print(" SCIENTIFIC DATA ACCELERATOR: MODULE 4 EXECUTION DEMO")
    print(" Scientific Data Platform — ChemData AI Solutions")
    print("=" * 80)

    ingestor = IngestionEngine()
    validator = ValidationEngine()
    executor = AIMNet2ExecutionEngine()
    vault = GovernedDataVault()

    dataset = [
        RawCompoundInput("SMI-001", "CC(=O)Oc1ccccc1C(=O)O", "Aspirin", requested_task="single_point_energy"),
        RawCompoundInput("SMI-002", "CN1C=NC2=C1C(=O)N(C(=O)N2C)C", "Caffeine", requested_task="single_point_energy"),
        RawCompoundInput("SMI-003", "CCO", "Ethanol", requested_task="geometry_relaxation"),
        RawCompoundInput("SMI-004", "CC(C)Cc1ccc(cc1)C(C)C(=O)O", "Ibuprofen", requested_task="single_point_energy"),
        RawCompoundInput("SMI-005", "c1ccccc1", "Benzene Radical Cation", charge=1, multiplicity=2, requested_task="single_point_energy"),
        RawCompoundInput("SMI-006", "Cl[Pt](Cl)(N)N", "Cisplatin (Coordination Complex)", requested_task="single_point_energy"),
        RawCompoundInput("SMI-007", "INVALID_SMILES#99", "Corrupted SMILES (Negative Control)", requested_task="single_point_energy")
    ]

    print(f"\n[TRIAGE] Processing batch of {len(dataset)} chemical records...\n")

    for raw in dataset:
        norm = ingestor.parse_and_normalize(raw)
        report = validator.evaluate_readiness(norm)
        
        status_color = report.status.value.upper()
        print(f"--> {raw.source_id:<8} | {raw.compound_name:<34} | STATUS: [{status_color}]")
        print(f"    Assigned Lane: {report.assigned_lane.value}")
        
        result = None
        if report.status != ReadinessStatus.REJECTED:
            result = executor.execute(norm, report.assigned_lane)
            print(f"    ⚡ Energy: {result.potential_energy_ev:.2f} eV | Latency: {result.execution_time_ms:.1f} ms | Hash: {result.provenance_hash[:16]}...")
        else:
            print("    ⛔ Execution Blocked: Invalid chemical syntax / valence failure.")

        vault.record_transaction(raw, norm, report, result)
        print("-" * 70)

    print("\n✔ All records successfully triaged and persisted to Governed Vault.")
    print("=" * 80)

if __name__ == "__main__":
    main()
