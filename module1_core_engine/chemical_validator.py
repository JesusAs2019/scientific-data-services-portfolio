"""RDKit-powered chemical structure validator."""

from typing import Dict, Any, Optional
from rdkit import Chem
from rdkit.Chem import Descriptors


def validate_chemical_smiles(smiles: str) -> Dict[str, Any]:
    """Parses and sanitizes SMILES string, computing fundamental molecular descriptors."""
    if not smiles or not isinstance(smiles, str):
        return {"valid": False, "error": "Empty or non-string SMILES provided."}
    
    mol = Chem.MolFromSmiles(smiles.strip())
    if mol is None:
        return {"valid": False, "error": f"Invalid SMILES chemical syntax: {smiles}"}
    
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)
    rotatable_bonds = Descriptors.NumRotatableBonds(mol)
    
    # Lipinski's Rule of 5 evaluation
    lipinski_violations = 0
    if mw > 500: lipinski_violations += 1
    if logp > 5.0: lipinski_violations += 1
    if hbd > 5: lipinski_violations += 1
    if hba > 10: lipinski_violations += 1

    return {
        "valid": True,
        "canonical_smiles": Chem.MolToSmiles(mol, canonical=True),
        "molecular_weight": round(mw, 2),
        "logp": round(logp, 2),
        "hbd": hbd,
        "hba": hba,
        "rotatable_bonds": rotatable_bonds,
        "lipinski_violations": lipinski_violations,
        "drug_like": lipinski_violations <= 1
    }
