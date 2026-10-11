"""Pydantic data schemas for small molecules and advanced nanomaterials."""

from enum import Enum
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator


class QualityStatus(str, Enum):
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"


class ChemicalRecordSchema(BaseModel):
    """Schema for small organic molecules."""
    record_id: str = Field(..., description="Unique record ID, e.g. CHEM-001")
    compound_name: str = Field(..., description="IUPAC or common name")
    smiles: str = Field(..., description="Valid chemical SMILES string")
    molecular_weight: Optional[float] = Field(None, ge=1.0, le=2000.0)
    logp: Optional[float] = Field(None, ge=-10.0, le=15.0)
    purity_pct: float = Field(98.5, ge=0.0, le=100.0)
    storage_temp_c: float = Field(20.0, ge=-80.0, le=100.0)


class NanoparticleBatchSchema(BaseModel):
    """Schema for nanoparticle synthesis batches and colloidal characterization."""
    batch_id: str = Field(..., description="Unique batch ID, e.g. NP-2026-AU01")
    sample_name: str = Field(..., description="Sample name")
    nanoparticle_type: str = Field(..., description="Metallic, LNP, Quantum Dot, etc.")
    core_composition: str = Field(..., description="Core chemical formula, e.g. Au, Fe3O4, InP")
    shell_composition: Optional[str] = Field(None, description="Surface coating or ligand")
    hydrodynamic_diameter_nm: float = Field(..., ge=1.0, le=2000.0)
    polydispersity_index: float = Field(..., ge=0.01, le=1.0)
    zeta_potential_mv: float = Field(..., ge=-120.0, le=120.0)
    suspension_ph: float = Field(7.0, ge=1.0, le=14.0)
    target_application: str = Field("Therapeutics / SERS / Energy Materials")

    @field_validator("polydispersity_index")
    @classmethod
    def round_pdi(cls, v: float) -> float:
        return round(v, 3)

    @property
    def stability_profile(self) -> Dict[str, Any]:
        """Calculates colloidal stability classification based on DLVO electrokinetic theory."""
        abs_zeta = abs(self.zeta_potential_mv)
        if abs_zeta >= 30.0:
            rating = "Highly Stable (No aggregation risk)"
            color = "green"
        elif abs_zeta >= 20.0:
            rating = "Moderately Stable"
            color = "blue"
        elif abs_zeta >= 10.0:
            rating = "Incipient Instability (Aggregation risk)"
            color = "amber"
        else:
            rating = "Critical Instability / Rapid Precipitation"
            color = "red"
            
        return {
            "rating": rating,
            "status_color": color,
            "is_monodisperse": self.polydispersity_index <= 0.20,
            "abs_zeta_mv": abs_zeta
        }
