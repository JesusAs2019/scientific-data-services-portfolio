# ChemData Scientific Data Platform

## Enterprise Cheminformatics, Nanomaterials Suite & Scientific Data Accelerator

[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![RDKit](https://img.shields.io/badge/Cheminformatics-RDKit-green.svg)](https://www.rdkit.org/)
[![Pydantic v2](https://img.shields.io/badge/Data%20Contracts-Pydantic%20v2-orange.svg)](https://docs.pydantic.dev/)
[![AIMNet2 Enabled](https://img.shields.io/badge/AI%20Potential-AIMNet2-success.svg)](https://pubs.rsc.org/)
[![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy%202.0-red.svg)](https://www.sqlalchemy.org/)
[![Streamlit App](https://img.shields.io/badge/Streamlit%20App-Live-FF4B4B.svg)](https://technical-analytical-project.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

> **A production-grade, 4-tier scientific data architecture engineered for pharmaceutical, biotechnology, advanced nanomaterials, and high-throughput computational chemistry R&D workflows.**

---

## 🏛️ 4-Tier Enterprise Architecture

┌────────────────────────────────────────────────────────────────────────────────────────┐ │ TIER 4: SCIENTIFIC DATA ACCELERATOR (module4_scientific_accelerator) │ │ - 4-State Simulation Readiness Triage (READY, WARNING, REMEDIATION, REJECTED) │ │ - Task-Aware Execution Lanes (AIMNet2 Fast Inference, PyTorch Workflows, ASE Adapters)│ │ - Zero-Trust ALCOA+ Audit Vault with SHA-256 Provenance Hashes & OOD Uncertainty Flags│ └───────────────────────────────────────────┬────────────────────────────────────────────┘ │ ┌───────────────────────────────────────────▼────────────────────────────────────────────┐ │ TIER 3: INTERACTIVE CONTROL CENTER & ANALYTICS UI (module3_control_center) │ │ - Interactive 2D Structure Drawing (rdMolDraw2D with vector SVG rendering) │ │ - WebGL Interactive 3D Conformer Coordinates (py3Dmol / stmol) │ │ - Dynamic Light Scattering (DLS) Size Distribution Generator (Log-Normal Curves) │ │ - DLVO Colloidal Stability Risk Evaluator & Formulation Vault │ └───────────────────────────────────────────┬────────────────────────────────────────────┘ │ ┌───────────────────────────────────────────▼────────────────────────────────────────────┐ │ TIER 2: RELATIONAL VAULT & PERSISTENCE LAYER (module2_relational_vault) │ │ - Normalized Multi-Table SQLite / PostgreSQL Storage (SQLAlchemy ORM) │ │ - Batch Lineage Tracking, Synthesis Records & Metadata Versioning │ │ - High-Performance Indexed Querying for High-Throughput Screening (HTS) │ └───────────────────────────────────────────┬────────────────────────────────────────────┘ │ ┌───────────────────────────────────────────▼────────────────────────────────────────────┐ │ TIER 1: CORE INGESTION & VALIDATION ENGINE (module1_core_engine) │ │ - Molecular SMILES & Organic Compounds Validator (Pydantic, RDKit Sanitization) │ │ - Nanoparticles & Colloidal Characterization (DLS Size, PDI, Zeta Potential) │ │ - Automated Physical Bounds & Quality Anomaly Scoring (pH, Temp, Ionic Strength) │ └────────────────────────────────────────────────────────────────────────────────────────┘

---

---

## 📦 Key Modules & Capabilities

### 1. Tier 1: Core Ingestion & Validation Engine (`module1_core_engine`)

* **SMILES Parsing & Structure Verification:** Chemical validity verification using RDKit's Kekulization, valence rules, and aromaticity perception.
* **Nanomaterial Characterization:** Strict electrokinetic and size validation:
  * Hydrodynamic Diameter ($d_H \in [1.0, 2000.0]\text{ nm}$)
  * Polydispersity Index ($\text{PDI} \le 0.2$ for monodisperse formulations)
  * Zeta Potential ($\zeta \in [-120.0, +120.0]\text{ mV}$) with DLVO colloidal aggregation risk scoring.
* **Biophysical Bounds:** Automated pH, temperature, and ionic strength verification.

### 2. Tier 2: Relational Vault (`module2_relational_vault`)

* **Transactional Multi-Table Schema:** SQLAlchemy ORM database models mapping synthesis batches, physical measurements, stability scores, and audit timestamps.

* **Export-Ready Data Pipelines:** Serialization to CSV, Parquet, and structured JSON-LD schemas.

### 3. **Tier 3: Control Center UI** (`module3_control_center`)

* **Interactive 2D/3D Molecular Visualization:** High-performance ball-and-stick WebGL conformer rendering with real-time coordinate manipulation.
* **Nanoparticles & Advanced Materials Dashboard:** Real-time Dynamic Light Scattering (DLS) Gaussian/Log-Normal intensity curve generator and electrostatic stability classification (Highly Stable vs. Rapid Aggregation).

### 4. Tier 4: Scientific Data Accelerator (`module4_scientific_accelerator`) ⭐ *New*

* **Validation-First Simulation Triage:** 4-state classification gate ensuring zero corrupted molecules consume expensive GPU/DFT compute:
  * 🟢 `READY`: Dispatched to AIMNet2 Fast Inference Lane.
  * 🟡 `READY_WITH_WARNINGS`: Open-shell radicals routed to spin-polarized ASE adapters.
  * 🟠 `REQUIRES_REMEDIATION`: Heavy transition metals (Pt, etc.) flagged for DFT fallback.
  * 🔴 `REJECTED`: Blocked before execution due to syntax/valence contraventions.
* **High-Speed Neural Potentials:** AIMNet2 neural execution for single-point energies, atomic forces, and dipole moments with $<10\text{ ms}$ latency.
* **Zero-Trust ALCOA+ Audit Vault:** Cryptographic SHA-256 provenance hashes generated for every approved calculation to guarantee auditability and regulatory defensibility.

---

## ⚡ Quickstart & Local Verification

### 1. Clone the repository

```bash
git clone https://github.com/JesusAs2019/scientific-data-services-portfolio.git
cd scientific-data-services-portfolio
```

### 2. **Create virtual environment & install dependencies**

```bash
python -m venv .venv
```

#### **On Windows (PowerShell)**

```bash

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

#### **On macOS / Linux**

```bash
source .venv/bin/activate
```

#### **Install dependencies**

```bash
pip install -r requirements.txt
pip install pytest pydantic
```

### 3. **Run Automated Unit Tests (100% Passing)**

#### Windows PowerShell

```bash
$env:PYTHONPATH="."
python -m pytest -v tests/test_accelerator.py
```

#### macOS / Linux

```bash
PYTHONPATH=. pytest -v tests/test_accelerator.py
```

### 4. **Run the Scientific Data Accelerator Demo**

#### Run the 7-molecule batch triage demonstration

```bash
python -m module4_scientific_accelerator.run_accelerator
```

### 5. **Launch the Interactive Streamlit Control Center**

```bash
Copystreamlit run module3_control_center/app.py
```

## 🧪 **Accelerator Triage Verification Matrix**

```bash

| Source ID | Compound / Test Case | Formula | Validation Status | Assigned Execution Lane | Potential Energy |
| :--- | :--- | :--- | :---: | :--- | :---: |
| **SMI-001** | Aspirin | C<sub>9</sub>H<sub>8</sub>O<sub>4</sub> | 🟢 `READY` | AIMNet2 Fast Inference | -616.14 eV |
| **SMI-002** | Caffeine | C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub> | 🟢 `READY` | AIMNet2 Fast Inference | -664.13 eV |
| **SMI-003** | Ethanol | C<sub>2</sub>H<sub>6</sub>O | 🟢 `READY` | PyTorch Neural Workflow | -157.56 eV |
| **SMI-004** | Ibuprofen | C<sub>13</sub>H<sub>18</sub>O<sub>2</sub> | 🟢 `READY` | AIMNet2 Fast Inference | -705.48 eV |
| **SMI-005** | Benzene Radical Cation | C<sub>6</sub>H<sub>6</sub><sup>•+</sup> | 🟡 `READY_WITH_WARNINGS` | Advanced Adapters (ASE) | -267.15 eV |
| **SMI-006** | Cisplatin (Coordination Complex) | Cl<sub>2</sub>H<sub>6</sub>N<sub>2</sub>Pt | 🟠 `REQUIRES_REMEDIATION` | Advanced Adapters (PySisyphus) | -1026.17 eV |
| **SMI-007** | Corrupted SMILES (Negative Control) | `INVALID` | 🔴 `REJECTED` | `rejected_lane` | **Blocked (0 ms)** |
```

## 🎯 **Target Applications & Commercial Offerings**

Pharma & Biotech Discovery: High-throughput virtual screening, lipid nanoparticle (LNP) formulation triage, and pre-DFT candidate validation.
Energy, Materials & Catalysis: Nanocatalyst surface charge profiling, battery electrode material validation, and transition-state reaction pathway mapping.
Commercial Engagements: Available as the Scientific Edition of the ChemData AI Data Accelerator (from £9,500).

## 👨‍💻 **Author & Engineering Leadership**

Jean Pierre Assiana, MSc Applied Chemistry
Principal Informatics Engineer & Agency Director, ChemData AI Solutions

**Agency Portal**: https://chemdataai.com

**Scientific Data Accelerator**: https://chemdataai.com/scientific-data-accelerator

**Live Streamlit Suite**: technical-analytical-project.streamlit.app
GitHub Profile: @JesusAs2019

## 📜 **License**

Distributed under the MIT License. Developed and maintained by ChemData AI Solutions.
