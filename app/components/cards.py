"""
Componentes de cards para o Dashboard Economiza+ MVP
"""

import streamlit as st
from typing import Dict, List, Optional
import sys
sys.path.append('..')
from utils.config import CLUSTER_COLORS, PRIORITY_COLORS, CLUSTER_NAMES


def metric_card(title: str, value: str, delta: Optional[str] = None,
                delta_color: str = "normal", help_text: Optional[str] = None):
    """
    Renderiza um card de métrica.

    Args:
        title: Titulo da metrica
        value: Valor principal
        delta: Variacao (opcional)
        delta_color: Cor do delta ("normal", "inverse", "off")
        help_text: Texto de ajuda (tooltip)
    """
    if help_text:
        st.metric(label=title, value=value, delta=delta,
                  delta_color=delta_color, help=help_text)
    else:
        st.metric(label=title, value=value, delta=delta, delta_color=delta_color)


def profile_card(perfil: Dict, financeiro: Dict):
    """
    Renderiza card com perfil do usuário.

    Args:
        perfil: Dict com cluster, cluster_nome, prioridade
        financeiro: Dict com renda_media, gasto_medio, taxa_poupanca
    """
    cluster = perfil.get('cluster', 0)
    cluster_nome = perfil.get('cluster_nome', 'Desconhecido')
    prioridade = perfil.get('prioridade', 'MEDIA')

    color = CLUSTER_COLORS.get(cluster, '#666666')
    priority_color = PRIORITY_COLORS.get(prioridade, '#666666')

    # Card do perfil
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {color}22, {color}11);
        border-left: 4px solid {color};
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    ">
        <h3 style="margin: 0; color: {color};">📊 {cluster_nome}</h3>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">
            Prioridade: <span style="
                background: {priority_color};
                color: white;
                padding: 2px 8px;
                border-radius: 4px;
                font-weight: bold;
            ">{prioridade}</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Métricas financeiras
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Renda Média",
            f"R$ {financeiro.get('renda_media', 0):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        )

    with col2:
        st.metric(
            "Gasto Médio",
            f"R$ {financeiro.get('gasto_medio', 0):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        )

    with col3:
        taxa = financeiro.get('taxa_poupanca', 0)
        color_taxa = "normal" if taxa >= 0 else "inverse"
        st.metric(
            "Taxa de Poupança",
            f"{taxa:.1f}%",
            delta_color=color_taxa
        )


def recommendation_card(recomendacoes: List[Dict]):
    """
    Renderiza cards de recomendações.

    Args:
        recomendacoes: Lista de dicts com titulo, categoria, economia_potencial, dica
    """
    st.markdown("### 💡 Recomendações Personalizadas")

    if not recomendacoes:
        st.info("Nenhuma recomendação disponível para este usuário.")
        return

    for i, rec in enumerate(recomendacoes, 1):
        economia = rec.get('economia_potencial', 0)
        economia_str = f"R$ {economia:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

        with st.container():
            st.markdown(f"""
            <div style="
                background: #f8f9fa;
                border-left: 4px solid #2ED573;
                padding: 1rem;
                border-radius: 0.5rem;
                margin-bottom: 0.5rem;
            ">
                <h4 style="margin: 0; color: #333;">
                    {i}. {rec.get('titulo', 'Recomendacao')}
                </h4>
                <p style="margin: 0.5rem 0; color: #666;">
                    <strong>Categoria:</strong> {rec.get('categoria', '-')} |
                    <strong>Corte:</strong> {rec.get('pct_corte', 0)}%
                </p>
                <p style="margin: 0; color: #2ED573; font-size: 1.2rem; font-weight: bold;">
                    Economia potencial: {economia_str}/mes
                </p>
                <p style="margin: 0.5rem 0 0 0; color: #888; font-style: italic;">
                    💡 {rec.get('dica', '')}
                </p>
            </div>
            """, unsafe_allow_html=True)


def anomaly_card(anomalias: Dict):
    """
    Renderiza card de anomalias detectadas.

    Args:
        anomalias: Dict com total_anomalias e transacoes_anomalas
    """
    total = anomalias.get('total_anomalias', 0)
    transacoes = anomalias.get('transacoes_anomalas', [])

    # Header
    if total > 0:
        st.markdown(f"""
        <div style="
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        ">
            <h4 style="margin: 0; color: #856404;">
                ⚠️ {total} Transações Suspeitas Detectadas
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Lista de transações
        if transacoes:
            st.markdown("**Últimas transações suspeitas:**")
            for t in transacoes[:5]:  # Mostrar apenas 5
                valor_str = f"R$ {t.get('valor', 0):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
                st.markdown(f"""
                - **{t.get('data', '-')}** | {t.get('categoria', '-')} | {valor_str}
                """)

            if len(transacoes) > 5:
                st.caption(f"... e mais {len(transacoes) - 5} transações")
    else:
        st.success("✅ Nenhuma transação suspeita detectada")


def cluster_summary_card(cluster: int, stats: Dict):
    """
    Renderiza card resumo de um cluster.

    Args:
        cluster: Número do cluster
        stats: Dict com estatísticas do cluster
    """
    nome = CLUSTER_NAMES.get(cluster, f'Cluster {cluster}')
    color = CLUSTER_COLORS.get(cluster, '#666666')

    n_usuarios = stats.get('n_usuarios', 0)
    economia_media = stats.get('economia_media', 0)
    taxa_poupanca = stats.get('taxa_poupanca_media', 0)

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {color}33, {color}11);
        border: 2px solid {color};
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    ">
        <h4 style="margin: 0; color: {color};">{nome}</h4>
        <p style="margin: 0.5rem 0; font-size: 2rem; font-weight: bold;">{n_usuarios}</p>
        <p style="margin: 0; color: #666;">usuários</p>
        <hr style="border-color: {color}33;">
        <p style="margin: 0.5rem 0;">
            <strong>Economia média:</strong> R$ {economia_media:,.0f}/mês
        </p>
        <p style="margin: 0;">
            <strong>Taxa poupança:</strong> {taxa_poupanca:.1f}%
        </p>
    </div>
    """, unsafe_allow_html=True)
