"""
Página 3: Comparativo entre Perfis
Comparação detalhada entre os 4 clusters
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import CLUSTER_NAMES, CLUSTER_COLORS
from utils.data_loader import load_usuarios_clustered, load_economia_projetada
from utils.pipeline import get_pipeline

st.title("📊 Comparativo entre Perfis")
st.markdown("Análise comparativa dos 4 perfis financeiros identificados")

st.markdown("---")

# Carregar dados
try:
    usuarios = load_usuarios_clustered()
    economia = load_economia_projetada()
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

# Calcular estatísticas por cluster
stats = usuarios.groupby('cluster').agg({
    'user_id': 'count',
    'media_renda': 'mean',
    'media_gasto': 'mean',
    'taxa_poupanca': 'mean',
    'pct_gastos_essenciais': 'mean',
    'std_gasto': 'mean'
}).round(2)

stats.columns = ['N Usuários', 'Renda Média', 'Gasto Médio', 'Taxa Poupança',
                 'Pct Essenciais', 'Variabilidade Gasto']

# Adicionar economia
economia_stats = economia.groupby('cluster')['economia_total'].agg(['sum', 'mean']).round(2)
economia_stats.columns = ['Economia Total', 'Economia Média']
stats = stats.join(economia_stats)

# Adicionar nomes dos clusters
stats['Cluster Nome'] = stats.index.map(CLUSTER_NAMES)
stats = stats.reset_index()

# Gráfico 1: Renda vs Gasto por Cluster
st.subheader("💵 Renda vs Gasto por Perfil")

fig1 = go.Figure()

colors = [CLUSTER_COLORS[i] for i in range(4)]
cluster_nomes = [CLUSTER_NAMES[i] for i in range(4)]

fig1.add_trace(go.Bar(
    name='Renda Média',
    x=cluster_nomes,
    y=stats['Renda Média'],
    marker_color='#2ED573',
    text=[f"R$ {v:,.0f}" for v in stats['Renda Média']],
    textposition='outside'
))

fig1.add_trace(go.Bar(
    name='Gasto Médio',
    x=cluster_nomes,
    y=stats['Gasto Médio'],
    marker_color='#FF6B6B',
    text=[f"R$ {v:,.0f}" for v in stats['Gasto Médio']],
    textposition='outside'
))

fig1.update_layout(
    barmode='group',
    xaxis_title="",
    yaxis_title="Valor (R$)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    height=400
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# Gráfico 2: Taxa de Poupança
st.subheader("📈 Taxa de Poupança por Perfil")

col1, col2 = st.columns([2, 1])

with col1:
    fig2 = go.Figure()

    fig2.add_trace(go.Bar(
        x=cluster_nomes,
        y=stats['Taxa Poupança'],
        marker_color=colors,
        text=[f"{v:.1f}%" for v in stats['Taxa Poupança']],
        textposition='outside'
    ))

    # Linha de referência em 0
    fig2.add_hline(y=0, line_dash="dash", line_color="gray")

    fig2.update_layout(
        xaxis_title="",
        yaxis_title="Taxa de Poupança (%)",
        showlegend=False,
        height=350
    )

    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.markdown("**Interpretação:**")
    st.markdown("""
    - **Valores negativos**: Usuário gasta mais do que ganha
    - **Valores positivos**: Usuário consegue poupar

    **Clusters:**
    - 🔴 Endividados Moderados: -37%
    - 🟡 Em Alerta: -25%
    - ⚫ Endividados Severos: -80%
    - 🟢 Poupadores: +26%
    """)

st.markdown("---")

# Gráfico 3: Economia Projetada
st.subheader("💰 Economia Projetada por Perfil")

col1, col2 = st.columns([2, 1])

with col1:
    fig3 = go.Figure()

    fig3.add_trace(go.Bar(
        x=cluster_nomes,
        y=stats['Economia Total'],
        marker_color=colors,
        text=[f"R$ {v:,.0f}" for v in stats['Economia Total']],
        textposition='outside'
    ))

    fig3.update_layout(
        xaxis_title="",
        yaxis_title="Economia Total Mensal (R$)",
        showlegend=False,
        height=350
    )

    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.markdown("**Destaque:**")

    # Maior economia
    max_idx = stats['Economia Total'].idxmax()
    max_cluster = stats.loc[max_idx, 'Cluster Nome']
    max_economia = stats.loc[max_idx, 'Economia Total']

    st.markdown(f"""
    O perfil **{max_cluster}** tem o maior
    potencial de economia:

    **R$ {max_economia:,.0f}/mes**

    Isso representa **{(max_economia / stats['Economia Total'].sum() * 100):.1f}%**
    do total projetado.
    """)

st.markdown("---")

# Tabela comparativa completa
st.subheader("📋 Tabela Comparativa Completa")

# Preparar tabela formatada
tabela = stats[['Cluster Nome', 'N Usuários', 'Renda Média', 'Gasto Médio',
                'Taxa Poupança', 'Economia Média', 'Economia Total']].copy()

tabela.columns = ['Perfil', 'Usuários', 'Renda Média', 'Gasto Médio',
                  'Taxa Poupança', 'Economia Média', 'Economia Total']

# Formatar
tabela['Renda Média'] = tabela['Renda Média'].apply(
    lambda x: f"R$ {x:,.0f}".replace(',', '.')
)
tabela['Gasto Médio'] = tabela['Gasto Médio'].apply(
    lambda x: f"R$ {x:,.0f}".replace(',', '.')
)
tabela['Taxa Poupança'] = tabela['Taxa Poupança'].apply(
    lambda x: f"{x:.1f}%"
)
tabela['Economia Média'] = tabela['Economia Média'].apply(
    lambda x: f"R$ {x:,.0f}".replace(',', '.')
)
tabela['Economia Total'] = tabela['Economia Total'].apply(
    lambda x: f"R$ {x:,.0f}".replace(',', '.')
)

st.dataframe(tabela.set_index('Perfil'), use_container_width=True)

st.markdown("---")

# Gráfico Radar
st.subheader("🎯 Perfil Comparativo (Radar)")

# Usar dados originais para radar (nao os agregados)
radar_source = usuarios.groupby('cluster').agg({
    'media_renda': 'mean',
    'media_gasto': 'mean',
    'taxa_poupanca': 'mean',
    'pct_gastos_essenciais': 'mean',
    'std_gasto': 'mean'
}).reset_index()

# Normalizar dados para radar (0-100)
radar_data = radar_source[['media_renda', 'media_gasto', 'taxa_poupanca',
                           'pct_gastos_essenciais', 'std_gasto']].copy()

# Renomear colunas
radar_data.columns = ['Renda', 'Gasto', 'Poupança', 'Essenciais', 'Variabilidade']

# Normalizar cada coluna
for col in radar_data.columns:
    min_val = radar_data[col].min()
    max_val = radar_data[col].max()
    if max_val != min_val:
        radar_data[col] = ((radar_data[col] - min_val) / (max_val - min_val)) * 100
    else:
        radar_data[col] = 50

fig4 = go.Figure()

for i in range(4):
    values = radar_data.iloc[i].tolist()
    values.append(values[0])  # Fechar o polígono

    fig4.add_trace(go.Scatterpolar(
        r=values,
        theta=['Renda', 'Gasto', 'Poupança', 'Essenciais', 'Variabilidade', 'Renda'],
        fill='toself',
        name=CLUSTER_NAMES[i],
        line_color=CLUSTER_COLORS[i],
        opacity=0.6
    ))

fig4.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=-0.2),
    height=500
)

st.plotly_chart(fig4, use_container_width=True)

st.caption("*Valores normalizados de 0 a 100 para comparação visual")
