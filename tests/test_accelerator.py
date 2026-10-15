import pytest
from module4_scientific_accelerator.models import ReadinessStatus, ExecutionLane, RawCompoundInput
from module4_scientific_accelerator.engine import IngestionEngine, ValidationEngine, AIMNet2ExecutionEngine, GovernedDataVault

@pytest.fixture
def engines():
    return {
        "ingestor": IngestionEngine(),
        "validator": ValidationEngine(),
        "executor": AIMNet2ExecutionEngine(),
        "vault": GovernedDataVault()
    }

def test_ready_compound_aspirin(engines):
    raw = RawCompoundInput(source_id="TEST-001", smiles="CC(=O)Oc1ccccc1C(=O)O", compound_name="Aspirin")
    norm = engines["ingestor"].parse_and_normalize(raw)
    report = engines["validator"].evaluate_readiness(norm)
    assert report.status == ReadinessStatus.READY
    assert report.assigned_lane == ExecutionLane.AIMNET2_FAST_INFERENCE

def test_open_shell_warning_benzene_radical(engines):
    raw = RawCompoundInput(source_id="TEST-002", smiles="c1ccccc1", compound_name="Benzene Radical", charge=1, multiplicity=2)
    norm = engines["ingestor"].parse_and_normalize(raw)
    report = engines["validator"].evaluate_readiness(norm)
    assert report.status == ReadinessStatus.READY_WITH_WARNINGS
    assert report.assigned_lane == ExecutionLane.ADVANCED_ASE_PYSISYPHUS

def test_transition_metal_remediation_cisplatin(engines):
    raw = RawCompoundInput(source_id="TEST-003", smiles="Cl[Pt](Cl)(N)N", compound_name="Cisplatin")
    norm = engines["ingestor"].parse_and_normalize(raw)
    report = engines["validator"].evaluate_readiness(norm)
    assert report.status == ReadinessStatus.REQUIRES_REMEDIATION
    assert report.assigned_lane == ExecutionLane.ADVANCED_ASE_PYSISYPHUS

def test_rejected_corrupted_smiles(engines):
    raw = RawCompoundInput(source_id="TEST-004", smiles="INVALID_SMILES#99", compound_name="Corrupted SMILES")
    norm = engines["ingestor"].parse_and_normalize(raw)
    report = engines["validator"].evaluate_readiness(norm)
    assert report.status == ReadinessStatus.REJECTED
    assert report.assigned_lane == ExecutionLane.REJECTED_LANE

def test_governed_vault_provenance(engines):
    raw = RawCompoundInput(source_id="TEST-005", smiles="CCO", compound_name="Ethanol")
    norm = engines["ingestor"].parse_and_normalize(raw)
    report = engines["validator"].evaluate_readiness(norm)
    result = engines["executor"].execute(norm, report.assigned_lane)
    entry = engines["vault"].record_transaction(raw, norm, report, result)
    assert entry["record_id"] == norm.record_id
    assert len(result.provenance_hash) == 64
