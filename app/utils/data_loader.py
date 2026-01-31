"""
Funcoes para carregamento de dados do Economiza+ MVP
"""

import pandas as pd
import pickle
import json
import streamlit as st
from pathlib import Path

from .config import (
    USUARIOS_FILE,
    TRANSACOES_FILE,
    USUARIOS_CLUSTERED_FILE,
    ECONOMIA_PROJETADA_FILE,
    PIPELINE_FILE,
    KMEANS_FILE,
    SCALER_FILE,
    ISOLATION_FOREST_FILE,
    RECOMENDACOES_FILE
)


@st.cache_data
def load_usuarios():
    """Carrega dados dos usuarios."""
    return pd.read_csv(USUARIOS_FILE)


@st.cache_data
def load_transacoes():
    """Carrega dados das transacoes."""
    return pd.read_csv(TRANSACOES_FILE)


@st.cache_data
def load_usuarios_clustered():
    """Carrega usuarios com clusters atribuidos."""
    return pd.read_csv(USUARIOS_CLUSTERED_FILE)


@st.cache_data
def load_economia_projetada():
    """Carrega economia projetada por usuario."""
    return pd.read_csv(ECONOMIA_PROJETADA_FILE)


@st.cache_resource
def load_pipeline():
    """Carrega pipeline completo (pode falhar por incompatibilidade de versao)."""
    try:
        with open(PIPELINE_FILE, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        st.warning(f"Pipeline pickle nao carregado (incompatibilidade de versao). Usando fallback.")
        return None


@st.cache_resource
def load_kmeans():
    """Carrega modelo K-means."""
    try:
        with open(KMEANS_FILE, 'rb') as f:
            return pickle.load(f)
    except Exception:
        return None


@st.cache_resource
def load_scaler():
    """Carrega scaler."""
    try:
        with open(SCALER_FILE, 'rb') as f:
            return pickle.load(f)
    except Exception:
        return None


@st.cache_resource
def load_isolation_forest():
    """Carrega modelo Isolation Forest."""
    try:
        with open(ISOLATION_FOREST_FILE, 'rb') as f:
            return pickle.load(f)
    except Exception:
        return None


@st.cache_data
def load_recomendacoes_regras():
    """Carrega regras de recomendacao."""
    with open(RECOMENDACOES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_user_list():
    """Retorna lista de user_ids disponiveis."""
    usuarios = load_usuarios_clustered()
    return sorted(usuarios['user_id'].unique().tolist())


def get_cluster_distribution():
    """Retorna distribuicao dos clusters."""
    usuarios = load_usuarios_clustered()
    return usuarios['cluster'].value_counts().sort_index()


def get_economia_por_cluster():
    """Retorna economia agregada por cluster."""
    economia = load_economia_projetada()
    return economia.groupby('cluster').agg({
        'economia_total': ['sum', 'mean', 'count']
    }).round(2)
