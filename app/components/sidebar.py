"""
Componente de Sidebar para o Dashboard Economiza+ MVP
"""

import streamlit as st
from typing import List, Optional, Tuple
import sys
sys.path.append('..')
from utils.data_loader import get_user_list
from utils.config import CLUSTER_NAMES


def render_sidebar() -> Tuple[Optional[str], bool]:
    """
    Renderiza a sidebar com selecao de usuario.

    Returns:
        Tuple com (user_id selecionado, botao_analisar clicado)
    """
    with st.sidebar:
        # Logo/Titulo
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <h1 style="color: #2ED573; margin: 0;">💰</h1>
            <h2 style="margin: 0;">Economiza+</h2>
            <p style="color: #666; margin: 0;">MVP Dashboard</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # Selecao de usuario
        st.subheader("🔍 Análise Individual")

        # Carregar lista de usuários
        try:
            user_list = get_user_list()
        except Exception as e:
            st.error(f"Erro ao carregar usuários: {e}")
            user_list = []

        # Dropdown de seleção
        selected_user = st.selectbox(
            "Selecione o usuário:",
            options=[""] + user_list,
            format_func=lambda x: "Escolha um usuário..." if x == "" else x,
            help="Selecione um usuário para ver sua análise detalhada"
        )

        # Botão de análise
        analyze_button = st.button(
            "📊 Analisar Usuário",
            disabled=selected_user == "",
            use_container_width=True,
            type="primary"
        )

        st.markdown("---")

        # Legenda dos clusters
        st.subheader("📋 Legenda dos Perfis")

        cluster_info = [
            ("🔴", "Endividados Moderados", "Risco Alto"),
            ("🟡", "Em Alerta", "Risco Moderado"),
            ("⚫", "Endividados Severos", "Risco Critico"),
            ("🟢", "Poupadores", "Risco Baixo"),
        ]

        for emoji, nome, risco in cluster_info:
            st.markdown(f"{emoji} **{nome}**  \n_{risco}_")

        st.markdown("---")

        # Info do projeto
        st.caption("""
        **Economiza+ MVP**
        Projeto acadêmico de Data Science
        XP Educação - 2026

        [📖 Documentação](https://github.com/cezinha/economiza-ia)
        """)

    return selected_user if selected_user != "" else None, analyze_button


def render_filter_sidebar(usuarios_df) -> dict:
    """
    Renderiza sidebar com filtros avancados.

    Args:
        usuarios_df: DataFrame com usuarios

    Returns:
        Dict com filtros selecionados
    """
    with st.sidebar:
        st.subheader("🎛️ Filtros")

        # Filtro por cluster
        clusters_selecionados = st.multiselect(
            "Clusters:",
            options=[0, 1, 2, 3],
            default=[0, 1, 2, 3],
            format_func=lambda x: CLUSTER_NAMES.get(x, f'Cluster {x}')
        )

        # Filtro por taxa de poupança
        taxa_range = st.slider(
            "Taxa de Poupança (%):",
            min_value=-100,
            max_value=100,
            value=(-100, 100),
            step=5
        )

        # Filtro por renda
        if 'media_renda' in usuarios_df.columns:
            renda_min = float(usuarios_df['media_renda'].min())
            renda_max = float(usuarios_df['media_renda'].max())
            renda_range = st.slider(
                "Renda Média (R$):",
                min_value=renda_min,
                max_value=renda_max,
                value=(renda_min, renda_max),
                step=500.0
            )
        else:
            renda_range = (0, 999999)

        return {
            'clusters': clusters_selecionados,
            'taxa_poupanca': taxa_range,
            'renda': renda_range
        }
