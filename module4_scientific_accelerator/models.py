import hashlib
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Optional, List, Dict, Any

class ReadinessStatus(str, Enum):
    READY = "ready"
    READY_WITH_WARNINGS = "ready_with_warnings"
    REQUIRES_REMEDIATION = "requires_remediation"
    REJECTED = "rejected"

class ExecutionLane(str, Enum):
    AIMNET2_FAST_INFERENCE = "aimnet2_fast_inference"
    PYTORCH_WORKFLOW = "pytorch_neural_workflow"
    ADVANCED_ASE_PYSISYPHUS = "advanced_ase_pysisyphus"
    REJECTED_LANE = "rejected_lane"

@dataclass
class RawCompoundInput:
    source_id: str
    smiles: str
    compound_name: Optional[str] = None
    charge: int = 0
    multiplicity: int = 1
    requested_task: str = "single_point_energy"
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class NormalizedCompoundRecord:
    record_id: str
    source_id: str
    canonical_smiles: str
    formula: str
    molecular_weight: float
    heavy_atom_count: int
    charge: int
    multiplicity: int
    requested_task: str
    raw_hash: str
    ingested_at: str

@dataclass
class SimulationReadinessReport:
    record_id: str
    status: ReadinessStatus
    passed_chemical_checks: bool
    passed_tensor_checks: bool
    assigned_lane: ExecutionLane
    warnings: List[str]
    errors: List[str]
    triage_timestamp: str

@dataclass
class GovernedExecutionResult:
    job_id: str
    record_id: str
    source_id: str
    lane_used: ExecutionLane
    potential_energy_ev: float
    max_force_ev_per_angstrom: float
    dipole_moment_debye: float
    uncertainty_score: float
    ood_flag: bool
    execution_time_ms: float
    model_version: str
    provenance_hash: str
    timestamp: str
