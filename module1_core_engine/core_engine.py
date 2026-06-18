# module1_core_engine/core_engine.py
from pydantic import BaseModel, Field, field_validator
from typing import Optional
from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem

class ChemicalConditions(BaseModel):
    temperature_c: Optional[float] = Field(None, description="Reaction temperature in Celsius.")
    solvent: Optional[str] = Field(None, description="The primary reaction solvent.")
    reaction_time_hrs: Optional[float] = Field(None, description="The length of the reaction process in hours.")

class SynthesisOutput(BaseModel):
    compound_name: str = Field(description="Name of the compound.")
    smiles_string: str = Field(description="Isomeric Canonical SMILES notation.")
    reported_mw: float = Field(description="Molecular mass stated in the paper.")
    conditions: ChemicalConditions = Field(description="Experimental environment blocks.")
    source_quote: str = Field(description="Exact quote for auditing.")

class ChemicalValidationGate:
    @staticmethod
    def audit_structure(smiles: str) -> dict:
        mol = Chem.MolFromSmiles(smiles)
        if not mol:
            return {"error": "Invalid Chemical Structure Trace"}
        
        calculated_mw = round(Descriptors.MolWt(mol), 2)
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
        
        chiral_centers = Chem.FindMolChiralCenters(mol, includeUnassigned=True)
        defined_centers = [c for c in chiral_centers if c[1] != '?']
        has_cis_trans = any(bond.GetStereo() != Chem.rdchem.BondStereo.STEREONONE for bond in mol.GetBonds())
        completeness_ratio = 1.0 if not chiral_centers else len(defined_centers) / len(chiral_centers)
        
        return {
            "calculated_mw": calculated_mw,
            "stereo_audit": {
                "total_chiral_centers": len(chiral_centers),
                "completeness_ratio": round(completeness_ratio, 2)
            }
        }

if __name__ == "__main__":
    test_smiles = "CC(=O)Oc1ccccc1C(=O)O"  # Aspirin
    results = ChemicalValidationGate.audit_structure(test_smiles)
    print(f"Calculated Weight: {results['calculated_mw']} Da")
    print("Demo 1: Core Engine and Chemical Validation Gate compiled and ran successfully!")
    