"""2D SVG Structure Drawing and 3D WebGL Conformer Visualizer."""

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D
import py3Dmol
import streamlit as st


def render_2d_molecule_svg(smiles: str, width: int = 380, height: int = 280) -> str:
    """Generates clean vector SVG for 2D molecular representation."""
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return "<svg><text>Invalid SMILES</text></svg>"
    
    drawer = rdMolDraw2D.MolDraw2DSVG(width, height)
    drawer.drawOptions().addAtomIndices = False
    drawer.DrawMolecule(mol)
    drawer.FinishDrawing()
    return drawer.GetDrawingText()


def render_3d_conformer_html(smiles: str, width: int = 400, height: int = 300) -> str:
    """Generates 3D WebGL conformer interactive viewer."""
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return "<div>Invalid molecule for 3D</div>"
    
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, AllChem.ETKDGv3())
    mol_block = Chem.MolToMolBlock(mol)
    
    viewer = py3Dmol.view(width=width, height=height)
    viewer.addModel(mol_block, "mol")
    viewer.setStyle({"stick": {"radius": 0.15}, "sphere": {"scale": 0.25}})
    viewer.zoomTo()
    return viewer._make_html()
