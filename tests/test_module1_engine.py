"""Tests for Tier 1: Ingestion & Validation Engine."""

from module1_core_engine.chemical_validator import validate_chemical_smiles
from module1_core_engine.schemas import NanoparticleBatchSchema


def test_aspirin_smiles_validation():
    smiles = "CC(=O)Oc1ccccc1C(=O)O"
    res = validate_chemical_smiles(smiles)
    assert res["valid"] is True
    assert res["molecular_weight"] == 180.16
    assert res["drug_like"] is True


def test_invalid_smiles_rejected():
    res = validate_chemical_smiles("INVALID_CHEMICAL_STRING")
    assert res["valid"] is False


def test_nanoparticle_schema_and_stability():
    payload = {
        "batch_id": "NP-TEST-01",
        "sample_name": "Test Gold Nanoparticles",
        "nanoparticle_type": "Metallic",
        "core_composition": "Au",
        "hydrodynamic_diameter_nm": 32.5,
        "polydispersity_index": 0.120,
        "zeta_potential_mv": -38.4,
        "suspension_ph": 7.4
    }
    batch = NanoparticleBatchSchema(**payload)
    assert batch.hydrodynamic_diameter_nm == 32.5
    assert batch.stability_profile["is_monodisperse"] is True
    assert batch.stability_profile["status_color"] == "green"
