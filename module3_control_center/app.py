"""Main Streamlit Application for ChemData Scientific Platform."""

import streamlit as st
import pandas as pd
from module1_core_engine.chemical_validator import validate_chemical_smiles
from module3_control_center.molecular_viewer import render_2d_molecule_svg
from module3_control_center.nano_analytics import render_nanomaterials_dashboard

st.set_page_config(page_title="ChemData Scientific Platform", page_layout="wide", page_icon="🔬")

st.title("ChemData Scientific Control Center")
st.caption("A production-grade scientific analytics and validation platform for browsing chemistry records, rendering 2D/3D structures, and evaluating Nanoparticle DLS distributions with DLVO colloidal stability.")

# Seed Data
SAMPLE_MOLECULES = [
    {"name": "Aspirin (Acetylsalicylic acid)", "smiles": "CC(=O)Oc1ccccc1C(=O)O"},
    {"name": "Paracetamol (Acetaminophen)", "smiles": "CC(=O)Nc1ccc(O)cc1"},
    {"name": "Caffeine", "smiles": "Cn1cnc2c1c(=O)n(c(=O)n2C)C"},
]

SAMPLE_NANOPARTICLES = [
    {"batch_id": "NP-2026-LNP04", "sample_name": "mRNA Lipid Nanoparticle (LNP-mRNA-04)", "hydrodynamic_diameter_nm": 88.0, "polydispersity_index": 0.085, "zeta_potential_mv": -4.2, "suspension_ph": 7.2},
    {"batch_id": "NP-2026-AU01", "sample_name": "Gold Nanospheres (Citrate-capped)", "hydrodynamic_diameter_nm": 32.5, "polydispersity_index": 0.120, "zeta_potential_mv": -38.4, "suspension_ph": 7.4},
    {"batch_id": "NP-2026-FEOX", "sample_name": "Superparamagnetic Iron Oxide (SPIONs)", "hydrodynamic_diameter_nm": 115.0, "polydispersity_index": 0.185, "zeta_potential_mv": +32.1, "suspension_ph": 6.8},
]

tab1, tab2, tab3 = st.tabs(["🧪 Molecular Structure & Validation", "🔬 Nanoparticles & DLS Analytics", "📊 Operational Data Vault"])

with tab1:
    st.subheader("Chemical Validation & 2D Vector Structure")
    mol_choice = st.selectbox("Select Target Molecule:", SAMPLE_MOLECULES, format_func=lambda x: x["name"])
    
    col_a, col_b = st.columns([1, 1.2])
    with col_a:
        res = validate_chemical_smiles(mol_choice["smiles"])
        st.write(f"**Canonical SMILES:** `{res['canonical_smiles']}`")
        st.metric("Molecular Weight", f"{res['molecular_weight']} g/mol")
        st.metric("Calculated LogP", f"{res['logp']}")
        st.write(f"**Lipinski Rule of 5:** {'Passed (Drug-like)' if res['drug_like'] else 'Violations Detected'}")
    
    with col_b:
        svg_html = render_2d_molecule_svg(mol_choice["smiles"])
        st.components.v1.html(svg_html, height=300)

with tab2:
    render_nanomaterials_dashboard(SAMPLE_NANOPARTICLES)

with tab3:
    st.subheader("Data Vault Telemetry")
    st.dataframe(pd.DataFrame(SAMPLE_NANOPARTICLES), use_container_width=True)
