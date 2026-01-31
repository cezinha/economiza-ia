"""
Configuracoes do Dashboard Economiza+ MVP
"""

import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent.parent
DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed"
MODELS_DIR = BASE_DIR / "models"
OUTPUTS_DIR = BASE_DIR / "outputs"

# Arquivos de dados
USUARIOS_FILE = DATA_RAW_DIR / "usuarios.csv"
TRANSACOES_FILE = DATA_RAW_DIR / "transacoes.csv"
USUARIOS_CLUSTERED_FILE = DATA_PROCESSED_DIR / "usuarios_clustered.csv"
ECONOMIA_PROJETADA_FILE = DATA_PROCESSED_DIR / "economia_projetada.csv"

# Arquivos de modelos
PIPELINE_FILE = MODELS_DIR / "pipeline_completo.pkl"
KMEANS_FILE = MODELS_DIR / "kmeans_best.pkl"
SCALER_FILE = MODELS_DIR / "scaler.pkl"
ISOLATION_FOREST_FILE = MODELS_DIR / "isolation_forest.pkl"
RECOMENDACOES_FILE = MODELS_DIR / "recomendacoes_regras.json"

# Configuracoes dos clusters
CLUSTER_NAMES = {
    0: "Endividados Moderados",
    1: "Em Alerta",
    2: "Endividados Severos",
    3: "Poupadores"
}

CLUSTER_COLORS = {
    0: "#FF6B6B",  # Vermelho claro
    1: "#FFE66D",  # Amarelo
    2: "#FF4757",  # Vermelho escuro
    3: "#2ED573"   # Verde
}

CLUSTER_PRIORITIES = {
    0: "ALTA",
    1: "MODERADA",
    2: "CRITICA",
    3: "BAIXA"
}

PRIORITY_COLORS = {
    "CRITICA": "#FF4757",
    "ALTA": "#FF6B6B",
    "MODERADA": "#FFE66D",
    "BAIXA": "#2ED573"
}

# Metricas gerais do projeto
TOTAL_USUARIOS = 500
ECONOMIA_MENSAL_PROJETADA = 144912.93
ECONOMIA_ANUAL_PROJETADA = 1738955.16
PCT_USUARIOS_RISCO = 77.2

# Configuracoes do Streamlit
PAGE_CONFIG = {
    "page_title": "Economiza+ MVP",
    "page_icon": "💰",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}
