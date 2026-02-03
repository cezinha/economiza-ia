"""
Funcoes para carregamento de dados do Economiza+ MVP
Com tratamento de erros robusto (Day 18)
"""

import pandas as pd
import pickle
import json
import streamlit as st
from pathlib import Path
from typing import Optional, Dict, Any

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


class DataLoadError(Exception):
    """Excecao customizada para erros de carregamento de dados."""
    pass


def _check_file_exists(filepath: Path, description: str) -> bool:
    """Verifica se arquivo existe e retorna True/False."""
    if not filepath.exists():
        return False
    return True


def _get_file_status() -> Dict[str, Dict[str, Any]]:
    """Retorna status de todos os arquivos necessarios."""
    files = {
        'usuarios': {'path': USUARIOS_FILE, 'required': True, 'type': 'data'},
        'transacoes': {'path': TRANSACOES_FILE, 'required': True, 'type': 'data'},
        'usuarios_clustered': {'path': USUARIOS_CLUSTERED_FILE, 'required': True, 'type': 'data'},
        'economia_projetada': {'path': ECONOMIA_PROJETADA_FILE, 'required': True, 'type': 'data'},
        'pipeline': {'path': PIPELINE_FILE, 'required': False, 'type': 'model'},
        'kmeans': {'path': KMEANS_FILE, 'required': False, 'type': 'model'},
        'scaler': {'path': SCALER_FILE, 'required': False, 'type': 'model'},
        'isolation_forest': {'path': ISOLATION_FOREST_FILE, 'required': False, 'type': 'model'},
        'recomendacoes': {'path': RECOMENDACOES_FILE, 'required': True, 'type': 'config'},
    }

    for name, info in files.items():
        info['exists'] = info['path'].exists()
        if info['exists']:
            info['size'] = info['path'].stat().st_size
        else:
            info['size'] = 0

    return files


@st.cache_data(show_spinner=False)
def load_usuarios() -> pd.DataFrame:
    """Carrega dados dos usuarios com tratamento de erro."""
    if not USUARIOS_FILE.exists():
        raise DataLoadError(
            f"Arquivo de usuarios nao encontrado: {USUARIOS_FILE}\n"
            "Execute: python scripts/gerar_dataset_financeiro.py"
        )
    try:
        df = pd.read_csv(USUARIOS_FILE)
        if df.empty:
            raise DataLoadError("Arquivo de usuarios esta vazio")
        return df
    except pd.errors.EmptyDataError:
        raise DataLoadError("Arquivo de usuarios esta vazio ou corrompido")
    except Exception as e:
        raise DataLoadError(f"Erro ao carregar usuarios: {str(e)}")


@st.cache_data(show_spinner=False)
def load_transacoes() -> pd.DataFrame:
    """Carrega dados das transacoes com tratamento de erro."""
    if not TRANSACOES_FILE.exists():
        raise DataLoadError(
            f"Arquivo de transacoes nao encontrado: {TRANSACOES_FILE}\n"
            "Execute: python scripts/gerar_dataset_financeiro.py"
        )
    try:
        df = pd.read_csv(TRANSACOES_FILE)
        if df.empty:
            raise DataLoadError("Arquivo de transacoes esta vazio")
        return df
    except pd.errors.EmptyDataError:
        raise DataLoadError("Arquivo de transacoes esta vazio ou corrompido")
    except Exception as e:
        raise DataLoadError(f"Erro ao carregar transacoes: {str(e)}")


@st.cache_data(show_spinner=False)
def load_usuarios_clustered() -> pd.DataFrame:
    """Carrega usuarios com clusters atribuidos."""
    if not USUARIOS_CLUSTERED_FILE.exists():
        raise DataLoadError(
            f"Arquivo de usuarios clusterizados nao encontrado: {USUARIOS_CLUSTERED_FILE}\n"
            "Execute os notebooks 01-05 para gerar este arquivo."
        )
    try:
        df = pd.read_csv(USUARIOS_CLUSTERED_FILE)
        if df.empty:
            raise DataLoadError("Arquivo de usuarios clusterizados esta vazio")

        # Validar colunas obrigatorias
        required_cols = ['user_id', 'cluster']
        missing = [col for col in required_cols if col not in df.columns]
        if missing:
            raise DataLoadError(f"Colunas obrigatorias ausentes: {missing}")

        return df
    except pd.errors.EmptyDataError:
        raise DataLoadError("Arquivo de usuarios clusterizados esta vazio ou corrompido")
    except DataLoadError:
        raise
    except Exception as e:
        raise DataLoadError(f"Erro ao carregar usuarios clusterizados: {str(e)}")


@st.cache_data(show_spinner=False)
def load_economia_projetada() -> pd.DataFrame:
    """Carrega economia projetada por usuario."""
    if not ECONOMIA_PROJETADA_FILE.exists():
        raise DataLoadError(
            f"Arquivo de economia projetada nao encontrado: {ECONOMIA_PROJETADA_FILE}\n"
            "Execute o notebook 08_Recomendacoes_Economia.ipynb"
        )
    try:
        df = pd.read_csv(ECONOMIA_PROJETADA_FILE)
        if df.empty:
            raise DataLoadError("Arquivo de economia projetada esta vazio")

        # Validar colunas obrigatorias
        required_cols = ['user_id', 'economia_total']
        missing = [col for col in required_cols if col not in df.columns]
        if missing:
            raise DataLoadError(f"Colunas obrigatorias ausentes em economia_projetada: {missing}")

        return df
    except pd.errors.EmptyDataError:
        raise DataLoadError("Arquivo de economia projetada esta vazio ou corrompido")
    except DataLoadError:
        raise
    except Exception as e:
        raise DataLoadError(f"Erro ao carregar economia projetada: {str(e)}")


@st.cache_resource(show_spinner=False)
def load_pipeline() -> Optional[Dict]:
    """Carrega pipeline completo (pode falhar por incompatibilidade de versao)."""
    if not PIPELINE_FILE.exists():
        return None
    try:
        with open(PIPELINE_FILE, 'rb') as f:
            return pickle.load(f)
    except Exception:
        return None


@st.cache_resource(show_spinner=False)
def load_kmeans():
    """Carrega modelo K-means."""
    if not KMEANS_FILE.exists():
        return None
    try:
        with open(KMEANS_FILE, 'rb') as f:
            return pickle.load(f)
    except Exception:
        return None


@st.cache_resource(show_spinner=False)
def load_scaler():
    """Carrega scaler."""
    if not SCALER_FILE.exists():
        return None
    try:
        with open(SCALER_FILE, 'rb') as f:
            return pickle.load(f)
    except Exception:
        return None


@st.cache_resource(show_spinner=False)
def load_isolation_forest():
    """Carrega modelo Isolation Forest."""
    if not ISOLATION_FOREST_FILE.exists():
        return None
    try:
        with open(ISOLATION_FOREST_FILE, 'rb') as f:
            return pickle.load(f)
    except Exception:
        return None


@st.cache_data(show_spinner=False)
def load_recomendacoes_regras() -> Dict:
    """Carrega regras de recomendacao."""
    if not RECOMENDACOES_FILE.exists():
        raise DataLoadError(
            f"Arquivo de regras nao encontrado: {RECOMENDACOES_FILE}\n"
            "Execute o notebook 07_Recomendacoes_Sistema.ipynb"
        )
    try:
        with open(RECOMENDACOES_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not data:
            raise DataLoadError("Arquivo de regras esta vazio")
        return data
    except json.JSONDecodeError as e:
        raise DataLoadError(f"Erro ao decodificar JSON de regras: {str(e)}")
    except DataLoadError:
        raise
    except Exception as e:
        raise DataLoadError(f"Erro ao carregar regras: {str(e)}")


def get_user_list() -> list:
    """Retorna lista de user_ids disponiveis."""
    try:
        usuarios = load_usuarios_clustered()
        return sorted(usuarios['user_id'].unique().tolist())
    except DataLoadError:
        return []


def get_cluster_distribution() -> pd.Series:
    """Retorna distribuicao dos clusters."""
    try:
        usuarios = load_usuarios_clustered()
        return usuarios['cluster'].value_counts().sort_index()
    except DataLoadError:
        return pd.Series(dtype=int)


def get_economia_por_cluster() -> pd.DataFrame:
    """Retorna economia agregada por cluster."""
    try:
        economia = load_economia_projetada()
        return economia.groupby('cluster').agg({
            'economia_total': ['sum', 'mean', 'count']
        }).round(2)
    except DataLoadError:
        return pd.DataFrame()


def check_system_health() -> Dict[str, Any]:
    """Verifica saude do sistema e retorna diagnostico."""
    status = _get_file_status()

    health = {
        'status': 'ok',
        'files': status,
        'errors': [],
        'warnings': []
    }

    # Verificar arquivos obrigatorios
    for name, info in status.items():
        if info['required'] and not info['exists']:
            health['errors'].append(f"Arquivo obrigatorio ausente: {name} ({info['path']})")
            health['status'] = 'error'
        elif not info['required'] and not info['exists']:
            health['warnings'].append(f"Arquivo opcional ausente: {name}")
            if health['status'] == 'ok':
                health['status'] = 'warning'

    return health
