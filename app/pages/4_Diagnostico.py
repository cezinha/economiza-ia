"""
Página 4: Diagnóstico do Sistema
Verifica saúde dos dados e modelos (Day 18)
"""

import streamlit as st
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.data_loader import check_system_health, DataLoadError
from utils.config import (
    BASE_DIR, DATA_RAW_DIR, DATA_PROCESSED_DIR, MODELS_DIR,
    CLUSTER_NAMES, CLUSTER_PRIORITIES
)

st.title("🔧 Diagnóstico do Sistema")
st.markdown("Verificação de saúde dos dados e modelos do Economiza+ MVP")

st.markdown("---")

# Verificar saúde do sistema
health = check_system_health()

# Status geral
status = health['status']
if status == 'ok':
    st.success("✅ Sistema operacional - Todos os arquivos necessários estão presentes")
elif status == 'warning':
    st.warning("⚠️ Sistema operacional com alertas - Alguns arquivos opcionais estão ausentes")
else:
    st.error("❌ Sistema com erros - Arquivos obrigatórios estão ausentes")

st.markdown("---")

# Detalhes dos arquivos
st.subheader("📁 Status dos Arquivos")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Arquivos de Dados:**")
    for name, info in health['files'].items():
        if info['type'] == 'data':
            icon = "✅" if info['exists'] else "❌"
            size_str = f"({info['size'] / 1024:.1f} KB)" if info['exists'] else "(ausente)"
            required = "obrigatório" if info['required'] else "opcional"
            st.markdown(f"{icon} `{name}` {size_str} - {required}")

with col2:
    st.markdown("**Modelos e Configurações:**")
    for name, info in health['files'].items():
        if info['type'] in ['model', 'config']:
            icon = "✅" if info['exists'] else "❌"
            size_str = f"({info['size'] / 1024:.1f} KB)" if info['exists'] else "(ausente)"
            required = "obrigatório" if info['required'] else "opcional"
            st.markdown(f"{icon} `{name}` {size_str} - {required}")

st.markdown("---")

# Erros e avisos
if health['errors']:
    st.subheader("❌ Erros")
    for error in health['errors']:
        st.error(error)

if health['warnings']:
    st.subheader("⚠️ Avisos")
    for warning in health['warnings']:
        st.warning(warning)

st.markdown("---")

# Informações do ambiente
st.subheader("📋 Informações do Sistema")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Diretórios:**")
    st.code(f"""
BASE_DIR: {BASE_DIR}
DATA_RAW: {DATA_RAW_DIR}
DATA_PROCESSED: {DATA_PROCESSED_DIR}
MODELS: {MODELS_DIR}
    """)

with col2:
    st.markdown("**Configurações:**")
    st.markdown("**Clusters configurados:**")
    for cluster_id, name in CLUSTER_NAMES.items():
        priority = CLUSTER_PRIORITIES.get(cluster_id, 'N/A')
        st.markdown(f"- Cluster {cluster_id}: {name} ({priority})")

st.markdown("---")

# Instruções de correção
if health['status'] != 'ok':
    st.subheader("🔧 Como Corrigir")

    st.markdown("""
    **Se arquivos de dados raw estão ausentes:**
    ```bash
    cd /home/celina/economiza-ia
    python scripts/gerar_dataset_financeiro.py
    ```

    **Se arquivos processados estão ausentes:**
    Execute os notebooks na ordem:
    1. `01_EDA_Basico.ipynb`
    2. `02_Feature_Engineering.ipynb`
    3. `03_Clustering.ipynb`
    4. ... até `12_Demonstracao.ipynb`

    **Se modelos estão ausentes:**
    - K-means: Execute notebook `03_Clustering.ipynb`
    - Isolation Forest: Execute notebook `09_Anomalias_Treino.ipynb`
    - Regras: Execute notebook `07_Recomendacoes_Sistema.ipynb`
    """)

# Timestamp
st.markdown("---")
st.caption(f"Diagnóstico executado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
