"""Interactive Nanomaterials & DLS Analytics Dashboard Component."""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def generate_dls_curve(mean_diameter: float, pdi: float):
    """Simulates Dynamic Light Scattering (DLS) Log-Normal Intensity distribution curve."""
    sigma = np.sqrt(np.log(1.0 + max(0.01, pdi)))
    mu = np.log(mean_diameter) - (sigma**2 / 2.0)
    diameters = np.logspace(np.log10(max(1.0, mean_diameter * 0.1)), np.log10(mean_diameter * 5.0), 300)
    intensity = (1.0 / (diameters * sigma * np.sqrt(2.0 * np.pi))) * np.exp(-((np.log(diameters) - mu)**2) / (2.0 * sigma**2))
    intensity_pct = (intensity / np.max(intensity)) * 100.0
    return diameters, intensity_pct


def render_nanomaterials_dashboard(batches: list):
    st.header("🔬 Nanoparticles & Advanced Materials Analytics")
    st.caption("Standardized DLS hydrodynamic size distribution, polydispersity profiling, and DLVO colloidal stability evaluation.")

    col1, col2 = st.columns([2, 1])
    with col1:
        batch_options = [f"{b['batch_id']} — {b['sample_name']}" for b in batches]
        selected_idx = st.selectbox("Select Batch:", range(len(batch_options)), format_func=lambda x: batch_options[x])
        b = batches[selected_idx]

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Hydrodynamic Size (dH)", f"{b['hydrodynamic_diameter_nm']} nm")
    m2.metric("Polydispersity (PDI)", f"{b['polydispersity_index']:.3f}", delta="Monodisperse" if b['polydispersity_index'] <= 0.2 else "Polydisperse")
    m3.metric("Zeta Potential (ζ)", f"{b['zeta_potential_mv']:+.1f} mV")
    m4.metric("Suspension pH", f"pH {b['suspension_ph']:.1f}")

    d, intensity = generate_dls_curve(b['hydrodynamic_diameter_nm'], b['polydispersity_index'])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=d, y=intensity, mode='lines', fill='tozeroy', line=dict(color='#047857', width=2.5), name='DLS Curve'))
    fig.add_vline(x=b['hydrodynamic_diameter_nm'], line_dash="dash", line_color="#b45309", annotation_text=f"Peak: {b['hydrodynamic_diameter_nm']} nm")
    fig.update_layout(xaxis_type="log", xaxis_title="Hydrodynamic Diameter (nm)", yaxis_title="Relative Intensity (%)", height=320, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
