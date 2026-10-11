# ChemData Scientific Data Platform — Enterprise Cheminformatics & Nanomaterials Suite

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![RDKit](https://img.shields.io/badge/RDKit-2D%2F3D%20Cheminformatics-green.svg)](https://www.rdkit.org/)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2.0-red.svg)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM%20Vault-orange.svg)](https://www.sqlalchemy.org/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://technical-analytical-project.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **A production-grade, 3-tier scientific data architecture engineered for pharmaceutical, biotechnology, and advanced nanomaterials R&D workflows.**

---

## 🏛️ 3-Tier Enterprise Architecture

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐ │ CHEMDATA SCIENTIFIC DATA PLATFORM │ ├─────────────────────────────────────────────────────────────────────────────────────────────────┤ │ │ │ [TIER 1: CORE INGESTION & VALIDATION ENGINE] │ │ ├── Molecular SMILES & Organic Compounds Validator (Pydantic, RDKit Sanitization) │ │ ├── Nanoparticles & Colloidal Characterization (DLS Size, PDI, Zeta Potential, Core-Shell) │ │ └── Automated Physical Bounds & Quality Anomaly Scoring │ │ │ │ │ ▼ │ │ [TIER 2: RELATIONAL VAULT & PERSISTENCE LAYER] │ │ ├── Normalized Multi-Table SQLite / PostgreSQL Storage (SQLAlchemy ORM) │ │ ├── Batch Lineage Tracking, Synthesis Records & Metadata Versioning │ │ └── High-Performance Indexed Querying for High-Throughput Screening (HTS) │ │ │ │ │ ▼ │ │ [TIER 3: INTERACTIVE CONTROL CENTER & ANALYTICS UI] │ │ ├── Interactive 2D Structure Drawing (rdMolDraw2D with vector SVG rendering) │ │ ├── WebGL Interactive 3D Conformer Coordinates (py3Dmol / stmol) │ │ ├── Dynamic Light Scattering (DLS) Size Distribution Generator (Log-Normal Curves) │ │ └── DLVO Colloidal Stability Risk Evaluator & Formulation Vault │ │ │ └─────────────────────────────────────────────────────────────────────────────────────────────────┘

---

## 🚀 Key Modules & Capabilities

### 1. Tier 1 — Core Ingestion & Validation Engine (`module1_core_engine`)

* **SMILES Parsing & Structure Verification:** Automated chemical validity verification using RDKit's Kekulization and aromaticity perception.

* **Nanomaterial Characterization:** Strict electrokinetic and size validation for:
  * Hydrodynamic Diameter ($d_H \in [1.0, 2000.0] \text{ nm}$)
  * Polydispersity Index ($\text{PDI} \le 0.2$ for monodisperse formulations)
  * Zeta Potential ($\zeta \in [-120.0, +120.0] \text{ mV}$) with DLVO colloidal aggregation risk scoring.
* **Pharma & Bio bounds:** Automated pH, temperature, and ionic strength verification.

### 2. Tier 2 — Relational Vault (`module2_relational_vault`)

* **Transactional Multi-Table Schema:** Robust SQLAlchemy ORM database models mapping synthesis batches, physical measurements, stability scores, and audit timestamps.

* **Export-Ready Data Pipelines:** Seamless serialization to CSV, Parquet, and structured JSON-LD schemas.

### 3. Tier 3 — Control Center UI (`module3_control_center`)

* **Interactive 2D/3D Molecular Visualization:** High-performance ball-and-stick WebGL conformer rendering with real-time coordinate manipulation.
* **Nanoparticles & Advanced Materials Dashboard:**
  * Real-time Dynamic Light Scattering (DLS) Gaussian/Log-Normal intensity curve generator.
  * Electrostatic stability classification (Highly Stable vs. Rapid Aggregation thresholds).
  * Formulation Vault for batch comparison across LNPs, Gold nanospheres, and Quantum Dots.

---

## 📦 Quickstart & Installation

### 1. Clone the repository

```bash
git clone https://github.com/JesusAs2019/scientific-data-services-portfolio.git
cd scientific-data-services-portfolio
```

### 2.  **Create virtual environment & install dependencies**

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

### 3. **Launch Interactive Control Center**

streamlit run module3_control_center/app.py

### 4. **Run Pytest Suite**

pytest -v

## 🔬 **Target Applications**

Pharma & Biotech: Targeted Lipid Nanoparticle (LNP) mRNA drug delivery formulations.
Energy & Catalysis: Nanocatalyst surface charge profiling and battery electrode material validation.
Regulated R&D: ISO/GLP-compliant data lineage and batch-release reporting.

## 👨‍💻 **Author & Engineering Leadership**

**Jean Pierre Assiana** — MSc Chemistry · Data Engineer & Regulated AI Solutions Architect

**Agency Portal**: https://chemdataai.com
Live App 1 (Capital Markets & REMIT): chemdata-ai-platform.streamlit.app
Live App 2 (Molecular & Nanomaterials): technical-analytical-project.streamlit.app
**GitHub**: @JesusAs2019

