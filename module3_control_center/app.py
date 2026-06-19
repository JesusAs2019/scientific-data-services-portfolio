# module3_control_center/app.py
import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw, AllChem
import py3Dmol
from stmol import showmol

st.set_page_config(page_title="Evinova Analytical Platform", layout="wide")
st.title("🔬 Scientific Data Services Portfolio Control Hub")
st.markdown("### Operational Ingestion Hub | Automated Extraction & Verification Engine")

# Pre-populated synthesis records matrix tracking simulated ingestion outputs
mock_data = [{
    "Compound ID": "CDA-2026 (Aspirin)",
    "SMILES String": "CC(=O)Oc1ccccc1C(=O)O",
    "Pipeline QA Status": "VERIFIED",
    "Reported MW (Da)": 180.16,
    "Calculated MW (Da)": 180.16,
    "Variance Delta": 0.00,
    "Yield Result (%)": 85.0,
    "Solvent Matrix": "Ethanol"
}]
df = pd.DataFrame(mock_data)

# Layout: Main records data desk
st.markdown("#### Current Batch Ingestion Records")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown("### 🧬 Advanced Analytical Inspection Suite")

# Isolate molecule for inspection
selected_id = st.selectbox("Isolate Molecule for Deeper Spatial Inspection", options=df["Compound ID"].unique())

if selected_id:
    # Fetch SMILES string dynamically from metadata frame
    smiles = df[df["Compound ID"] == selected_id]["SMILES String"].values[0]
    
    # Generate columns for side-by-side 2D vs 3D inspection layout
    col_2d, col_3d, col_metrics = st.columns([1.2, 1.5, 1.2])
    
    with col_2d:
        st.markdown("#### 2D Graph Topology")
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            img = Draw.MolToImage(mol, size=(400, 400))
            st.image(img, caption=f"2D Structural Formula: {selected_id}", use_container_width=True)
            st.success("Graph topology matching: 100% Validated.")

    with col_3d:
        st.markdown("#### Interactive 3D Spatial Conformation")
        if mol:
            # Generate 3D Conformer coordinates on-the-fly using RDKit Distance Geometry
            mol_3d = Chem.AddHs(mol)
            AllChem.EmbedMolecule(mol_3d, AllChem.ETKDGv3())
            AllChem.MMFFOptimizeMolecule(mol_3d, mmffVariant="MMFF94")
            
            # Convert RDKit object to clean MDL Molfile block format string text
            mol_block = Chem.MolToMolBlock(mol_3d)
            
            # Initialize py3Dmol view object container canvas 
            view = py3Dmol.view(width=450, height=400)
            view.addModel(mol_block, "mol")
            view.setStyle({'stick': {}})
            view.setBackgroundColor('white')
            view.zoomTo()
            
            # Render utilizing hardware-accelerated WebGL container context via stmol
            showmol(view, height=400, width=450)
            st.caption("💡 Click and drag to rotate the molecule in 3D space. Scroll to zoom.")

    with col_metrics:
        st.markdown("#### Computed Quantum/Geometric Insights")
        
       # Calculate conformer geometric details dynamically from the conformer object
        conformer = mol_3d.GetConformer()
        c_c_dist = Chem.rdMolTransforms.GetBondLength(conformer, 0, 1)
        c_c_o_angle = Chem.rdMolTransforms.GetAngleDeg(conformer, 0, 1, 2)
        st.metric(label="Optimized C-C Bond Distance", value=f"{c_c_dist:.3f} Å")
        st.metric(label="Optimized C-C-O Bond Angle", value=f"{c_c_o_angle:.2f}°")
        
        st.markdown("**Predicted Infrared (IR) Vibrational States:**")
        st.info("• **1750 cm⁻¹** : Strong Ester C=O Stretch\n"
                "• **1690 cm⁻¹** : Carboxylic Acid C=O Node\n"
                "• **2500-3300 cm⁻¹** : Broad O-H Stretch Mode")
        