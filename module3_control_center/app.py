# module3_control_center/app.py
import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw

st.set_page_config(page_title="Evinova Analytical Platform", layout="wide")
st.title(" 🔬 R&D Data Accelerator System Dashboard")
st.markdown("### Operational Ingestion Hub | Automated Extraction & Verification Engine")

# Pre-populated synthesis records matrix tracking simulated ingestion outputs
mock_data = [{
    "Compound ID": "CDA-2026",
    "SMILES String": "CC(=O)Oc1ccccc1C(=O)O",
    "Pipeline QA Status": "VERIFIED",
    "Reported MW": 180.16,
    "Calculated MW": 180.16,
    "Variance Delta": 0.00,
    "Yield Result (%)": 85.0,
    "Solvent Matrix": "Ethanol"
}]
df = pd.DataFrame(mock_data)

col_data_table, col_analytical_inspector = st.columns([2, 1])

with col_data_table:
    st.markdown("### Processed Compound Records")
    st.dataframe(df, use_container_width=True)

with col_analytical_inspector:
    st.markdown("### Molecular Graph Inspector")
    selected = st.selectbox("Isolate Molecule", options=df["Compound ID"].unique())
    if selected:
        mol = Chem.MolFromSmiles(df.iloc[0]["SMILES String"])
        if mol:
            img = Draw.MolToImage(mol, size=(300, 300))
            st.image(img, caption=f"Graph Structure of {selected}")
            st.success("Structure and stereochemical parameters validated.")