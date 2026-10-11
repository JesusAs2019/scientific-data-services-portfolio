"""SQLAlchemy database models for molecular and nanomaterial data."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CompoundRecord(Base):
    __tablename__ = "compounds"

    id = Column(Integer, primary_key=True, autoincrement=True)
    record_id = Column(String(50), unique=True, nullable=False, index=True)
    compound_name = Column(String(120), nullable=False)
    smiles = Column(String(500), nullable=False)
    molecular_weight = Column(Float, nullable=True)
    logp = Column(Float, nullable=True)
    purity_pct = Column(Float, default=98.5)
    created_at = Column(DateTime, default=datetime.utcnow)


class NanoparticleBatchRecord(Base):
    __tablename__ = "nanoparticle_batches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    batch_id = Column(String(50), unique=True, nullable=False, index=True)
    sample_name = Column(String(150), nullable=False)
    nanoparticle_type = Column(String(80), nullable=False)
    core_composition = Column(String(80), nullable=False)
    shell_composition = Column(String(120), nullable=True)
    hydrodynamic_diameter_nm = Column(Float, nullable=False)
    polydispersity_index = Column(Float, nullable=False)
    zeta_potential_mv = Column(Float, nullable=False)
    suspension_ph = Column(Float, default=7.0)
    stability_rating = Column(String(100), nullable=False)
    target_application = Column(String(200), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
