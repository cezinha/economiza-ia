"""
Página 1: Visão Geral
Dashboard com métricas e distribuição dos clusters
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import CLUSTER_NAMES, CLUSTER_COLORS, CLUSTER_PRIORITIES
from utils.data_loader import load_usuarios_clustered, load_economia_projetada, load_recomendacoes_regras
from utils.pipeline import get_pipeline
from components.charts import cluster_pie_chart, economia_bar_chart

st.title("📊 Visão Geral")
st.markdown("Panorama completo do sistema Economiza+ MVP")

st.markdown("---")

# Carregar dados
try:
    pipeline = get_pipeline()
    resumo = pipeline.get_resumo_geral()
    usuarios = load_usuarios_clustered()
    economia = load_economia_projetada()
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

# Métricas principais
st.subheader("📈 Métricas Gerais")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Usuários",
        f"{resumo['total_usuarios']:,}",
    )

with col2:
    economia_str = f"R$ {resumo['economia_mensal_total']:,.0f}".replace(',', '.')
    st.metric(
        "💰 Economia Mensal",
        economia_str,
    )

with col3:
    st.metric(
        "⚠️ Em Risco",
        f"{resumo['pct_usuarios_risco']}%",
        f"{resumo['usuarios_em_risco']} usuários",
        delta_color="inverse"
    )

with col4:
    economia_media = f"R$ {resumo['economia_media_usuario']:,.0f}".replace(',', '.')
    st.metric(
        "👤 Média/Usuário",
        economia_media,
    )

st.markdown("---")

# Gráficos lado a lado
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🥧 Distribuição dos Perfis")
    cluster_pie_chart(resumo['distribuicao_clusters'])

with col_right:
    st.subheader("💵 Economia por Perfil")
    economia_cluster = economia.groupby('cluster').agg({
        'economia_total': 'sum'
    }).reset_index()
    economia_bar_chart(economia_cluster.set_index('cluster'))

st.markdown("---")

# Top Recomendações por Cluster
st.subheader("💡 Top Recomendações por Perfil")

try:
    regras = load_recomendacoes_regras()
    clusters_regras = regras.get('clusters', {})

    col1, col2 = st.columns(2)

    for idx, cluster in enumerate(range(4)):
        cluster_key = str(cluster)
        nome = CLUSTER_NAMES[cluster]
        color = CLUSTER_COLORS[cluster]
        prioridade = CLUSTER_PRIORITIES[cluster]

        if cluster_key in clusters_regras:
            cluster_info = clusters_regras[cluster_key]
            regras_cluster = cluster_info.get('regras', [])

            with col1 if idx % 2 == 0 else col2:
                st.markdown(f"""
                <div style="
                    background: {color}15;
                    border-left: 4px solid {color};
                    padding: 1rem;
                    border-radius: 0.5rem;
                    margin-bottom: 1rem;
                ">
                    <h4 style="margin: 0; color: {color};">{nome}</h4>
                    <p style="margin: 0.3rem 0; font-size: 0.85rem; color: #666;">
                        Prioridade: <strong>{prioridade}</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)

                for regra in regras_cluster[:2]:
                    categoria = regra.get('categoria', '')
                    percentual = regra.get('percentual', 0)
                    pct_display = f"{int(percentual * 100)}%" if percentual < 1 else f"{int(percentual)}%"
                    titulo = regra.get('titulo', '')

                    st.markdown(f"""
                    <div style="
                        background: #f8f9fa;
                        padding: 0.5rem 1rem;
                        border-radius: 0.3rem;
                        margin-bottom: 0.5rem;
                        font-size: 0.9rem;
                    ">
                        <strong>{categoria}</strong>: Reduzir {pct_display}<br>
                        <span style="color: #666;">{titulo}</span>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

except Exception as e:
    st.warning(f"Não foi possível carregar recomendações: {e}")

st.markdown("---")

# Detalhamento por cluster
st.subheader("📋 Detalhamento por Perfil")

for cluster in range(4):
    nome = CLUSTER_NAMES[cluster]
    color = CLUSTER_COLORS[cluster]

    usuarios_cluster = usuarios[usuarios['cluster'] == cluster]
    economia_cluster = economia[economia['cluster'] == cluster]

    n = len(usuarios_cluster)
    pct = (n / len(usuarios)) * 100
    taxa_media = usuarios_cluster['taxa_poupanca'].mean()
    economia_total = economia_cluster['economia_total'].sum()
    economia_media = economia_cluster['economia_total'].mean()

    with st.expander(f"{nome} ({n} usuários - {pct:.1f}%)", expanded=False):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Usuários", n)
        with col2:
            st.metric("Taxa Poupança Média", f"{taxa_media:.1f}%")
        with col3:
            st.metric("Economia Total/Mês",
                     f"R$ {economia_total:,.0f}".replace(',', '.'))
        with col4:
            st.metric("Economia Média",
                     f"R$ {economia_media:,.0f}".replace(',', '.'))

        # Estatísticas adicionais
        st.markdown("**Estatísticas Financeiras:**")
        stats = usuarios_cluster[['media_renda', 'media_gasto', 'taxa_poupanca']].describe()
        stats = stats.loc[['mean', 'std', 'min', 'max']]
        stats.index = ['Média', 'Desvio Padrão', 'Mínimo', 'Máximo']
        stats.columns = ['Renda Média', 'Gasto Médio', 'Taxa Poupança']
        st.dataframe(stats.round(2), use_container_width=True)

st.markdown("---")

# Impacto projetado
st.subheader("🎯 Impacto Projetado")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background: #2ED57322; padding: 1.5rem; border-radius: 0.5rem; text-align: center;">
        <h2 style="margin: 0; color: #2ED573;">R$ 144.912</h2>
        <p style="margin: 0.5rem 0 0 0;">Economia Mensal</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: #2ED57322; padding: 1.5rem; border-radius: 0.5rem; text-align: center;">
        <h2 style="margin: 0; color: #2ED573;">R$ 1,74M</h2>
        <p style="margin: 0.5rem 0 0 0;">Economia Anual</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: #2ED57322; padding: 1.5rem; border-radius: 0.5rem; text-align: center;">
        <h2 style="margin: 0; color: #2ED573;">77.2%</h2>
        <p style="margin: 0.5rem 0 0 0;">Usuários Beneficiados</p>
    </div>
    """, unsafe_allow_html=True)
