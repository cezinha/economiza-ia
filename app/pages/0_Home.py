"""
Página Inicial: Visão Geral do Sistema
Dashboard principal do Economiza+ MVP
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import CLUSTER_NAMES, CLUSTER_COLORS
from utils.data_loader import load_usuarios_clustered, load_economia_projetada
from utils.pipeline import get_pipeline
from components.sidebar import render_sidebar
from components.cards import profile_card, recommendation_card, anomaly_card
from components.charts import cluster_pie_chart, economia_bar_chart, financial_gauge

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2ED573;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-container {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .stMetric {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


def main():
    """Função principal do dashboard."""

    # Sidebar
    selected_user, analyze_clicked = render_sidebar()

    # Header principal
    st.markdown('<h1 class="main-header">💰 Economiza+ MVP</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Sistema de Análise Financeira e Recomendações Personalizadas</p>',
        unsafe_allow_html=True
    )

    # Carregar dados
    try:
        pipeline = get_pipeline()
        resumo = pipeline.get_resumo_geral()
        usuarios = load_usuarios_clustered()
        economia = load_economia_projetada()
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        st.info("Verifique se os arquivos de dados e modelos estão nos diretórios corretos.")
        st.stop()

    # Se usuário selecionado e botão clicado, mostrar análise individual
    if selected_user and analyze_clicked:
        render_analise_usuario(pipeline, selected_user)
    else:
        # Mostrar visão geral
        render_visao_geral(resumo, usuarios, economia)


def render_visao_geral(resumo: dict, usuarios, economia):
    """Renderiza a visão geral do sistema."""

    st.markdown("---")

    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Total Usuários",
            f"{resumo['total_usuarios']:,}",
            help="Total de usuários no sistema"
        )

    with col2:
        economia_str = f"R$ {resumo['economia_mensal_total']:,.0f}".replace(',', '.')
        st.metric(
            "💰 Economia Mensal",
            economia_str,
            help="Economia projetada total por mês"
        )

    with col3:
        st.metric(
            "⚠️ Usuários em Risco",
            f"{resumo['pct_usuarios_risco']}%",
            f"{resumo['usuarios_em_risco']} usuários",
            delta_color="inverse",
            help="Percentual de usuários em situação de risco financeiro"
        )

    with col4:
        economia_anual = f"R$ {resumo['economia_anual_total']:,.0f}".replace(',', '.')
        st.metric(
            "📈 Economia Anual",
            economia_anual,
            help="Projeção anual de economia"
        )

    st.markdown("---")

    # Gráficos
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("📊 Distribuição dos Perfis")
        cluster_pie_chart(resumo['distribuicao_clusters'])

    with col_right:
        st.subheader("💵 Economia por Perfil")

        # Preparar dados para gráfico
        economia_cluster = economia.groupby('cluster').agg({
            'economia_total': 'sum'
        }).reset_index()

        economia_bar_chart(economia_cluster.set_index('cluster'))

    st.markdown("---")

    # Tabela resumo dos clusters
    st.subheader("📋 Resumo dos Perfis Financeiros")

    # Calcular estatísticas por cluster
    stats_cluster = usuarios.groupby('cluster').agg({
        'user_id': 'count',
        'media_renda': 'mean',
        'media_gasto': 'mean',
        'taxa_poupanca': 'mean'
    }).round(2)

    stats_cluster.columns = ['Usuários', 'Renda Média', 'Gasto Médio', 'Taxa Poupança (%)']
    stats_cluster.index = stats_cluster.index.map(CLUSTER_NAMES)

    # Adicionar economia média
    economia_media = economia.groupby('cluster')['economia_total'].mean().round(2)
    economia_media.index = economia_media.index.map(CLUSTER_NAMES)
    stats_cluster['Economia Média'] = economia_media

    # Formatar valores monetários
    stats_cluster['Renda Média'] = stats_cluster['Renda Média'].apply(
        lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    )
    stats_cluster['Gasto Médio'] = stats_cluster['Gasto Médio'].apply(
        lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    )
    stats_cluster['Economia Média'] = stats_cluster['Economia Média'].apply(
        lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    )
    stats_cluster['Taxa Poupança (%)'] = stats_cluster['Taxa Poupança (%)'].apply(
        lambda x: f"{x:.1f}%"
    )

    st.dataframe(stats_cluster, use_container_width=True)

    # Call to action
    st.markdown("---")
    st.info("👈 **Selecione um usuário na barra lateral** para ver sua análise detalhada e recomendações personalizadas.")


def render_analise_usuario(pipeline, user_id: str):
    """Renderiza análise individual de um usuário."""

    st.markdown("---")

    # Analisar usuário
    with st.spinner(f"Analisando usuário {user_id}..."):
        resultado = pipeline.analisar_usuario(user_id)

    if 'erro' in resultado:
        st.error(resultado['erro'])
        return

    # Header do usuário
    st.subheader(f"📊 Análise do Usuário: {user_id}")

    # Perfil e dados financeiros
    profile_card(resultado['perfil'], resultado['financeiro'])

    st.markdown("---")

    # Layout em colunas
    col_left, col_right = st.columns([2, 1])

    with col_left:
        # Recomendações
        recommendation_card(resultado['recomendacoes'])

        # Economia projetada
        st.markdown("### 💰 Economia Projetada")
        economia = resultado['economia']
        col1, col2 = st.columns(2)
        with col1:
            economia_str = f"R$ {economia['total_mensal']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            st.metric("Economia Mensal", economia_str)
        with col2:
            st.metric("% da Renda", f"{economia['pct_da_renda']:.1f}%")

    with col_right:
        # Gauge da taxa de poupança
        st.markdown("### 📈 Saúde Financeira")
        financial_gauge(
            resultado['financeiro']['taxa_poupanca'],
            title="Taxa de Poupança"
        )

        # Anomalias
        st.markdown("### ⚠️ Alertas")
        anomaly_card(resultado['anomalias'])

    # Botão para voltar
    st.markdown("---")
    if st.button("← Voltar para Visão Geral"):
        st.rerun()


if __name__ == "__main__":
    main()
