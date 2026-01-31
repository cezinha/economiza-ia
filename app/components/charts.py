"""
Componentes de gráficos para o Dashboard Economiza+ MVP
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List, Optional
import sys
sys.path.append('..')
from utils.config import CLUSTER_COLORS, CLUSTER_NAMES


def cluster_pie_chart(distribuicao: Dict[int, int], title: str = "Distribuição dos Clusters"):
    """
    Renderiza gráfico de pizza da distribuição dos clusters.

    Args:
        distribuicao: Dict com cluster -> contagem
        title: Título do gráfico
    """
    labels = [CLUSTER_NAMES.get(k, f'Cluster {k}') for k in distribuicao.keys()]
    values = list(distribuicao.values())
    colors = [CLUSTER_COLORS.get(k, '#666666') for k in distribuicao.keys()]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker_colors=colors,
        textinfo='label+percent',
        textposition='outside'
    )])

    fig.update_layout(
        title=title,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2),
        margin=dict(t=50, b=50, l=20, r=20),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)


def cluster_bar_chart(data: pd.DataFrame, x: str, y: str,
                      color: str = 'cluster', title: str = ""):
    """
    Renderiza gráfico de barras por cluster.

    Args:
        data: DataFrame com os dados
        x: Coluna para eixo X
        y: Coluna para eixo Y
        color: Coluna para cor
        title: Título do gráfico
    """
    # Mapear nomes dos clusters
    data = data.copy()
    if 'cluster' in data.columns:
        data['cluster_nome'] = data['cluster'].map(CLUSTER_NAMES)

    color_map = {CLUSTER_NAMES[k]: v for k, v in CLUSTER_COLORS.items()}

    fig = px.bar(
        data,
        x='cluster_nome' if 'cluster_nome' in data.columns else x,
        y=y,
        color='cluster_nome' if 'cluster_nome' in data.columns else color,
        color_discrete_map=color_map,
        title=title
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title=y.replace('_', ' ').title(),
        showlegend=False,
        margin=dict(t=50, b=30, l=50, r=20),
        height=350
    )

    st.plotly_chart(fig, use_container_width=True)


def comparison_chart(data: pd.DataFrame, metrics: List[str],
                     title: str = "Comparativo entre Clusters"):
    """
    Renderiza gráfico de barras agrupadas para comparação.

    Args:
        data: DataFrame com dados por cluster
        metrics: Lista de métricas para comparar
        title: Título do gráfico
    """
    data = data.copy()
    if 'cluster' in data.columns:
        data['cluster_nome'] = data['cluster'].map(CLUSTER_NAMES)

    fig = go.Figure()

    colors = list(CLUSTER_COLORS.values())

    for i, metric in enumerate(metrics):
        fig.add_trace(go.Bar(
            name=metric.replace('_', ' ').title(),
            x=data['cluster_nome'] if 'cluster_nome' in data.columns else data.index,
            y=data[metric],
            marker_color=colors[i % len(colors)]
        ))

    fig.update_layout(
        title=title,
        barmode='group',
        xaxis_title="",
        yaxis_title="Valor",
        legend=dict(orientation="h", yanchor="bottom", y=-0.3),
        margin=dict(t=50, b=80, l=50, r=20),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)


def financial_gauge(value: float, title: str = "Taxa de Poupança",
                    min_val: float = -100, max_val: float = 50):
    """
    Renderiza gauge (velocímetro) para indicador financeiro.

    Args:
        value: Valor atual
        title: Título do gauge
        min_val: Valor mínimo
        max_val: Valor máximo
    """
    # Determinar cor baseada no valor
    if value < -50:
        color = "#FF4757"  # Vermelho - crítico
    elif value < -20:
        color = "#FF6B6B"  # Vermelho claro - alto
    elif value < 0:
        color = "#FFE66D"  # Amarelo - alerta
    else:
        color = "#2ED573"  # Verde - bom

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 16}},
        number={'suffix': '%', 'font': {'size': 28}},
        gauge={
            'axis': {'range': [min_val, max_val], 'tickwidth': 1},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [min_val, -50], 'color': 'rgba(255, 71, 87, 0.2)'},
                {'range': [-50, -20], 'color': 'rgba(255, 107, 107, 0.2)'},
                {'range': [-20, 0], 'color': 'rgba(255, 230, 109, 0.2)'},
                {'range': [0, max_val], 'color': 'rgba(46, 213, 115, 0.2)'}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': value
            }
        }
    ))

    fig.update_layout(
        margin=dict(t=50, b=20, l=20, r=20),
        height=250
    )

    st.plotly_chart(fig, use_container_width=True)


def economia_bar_chart(economia_por_cluster: pd.DataFrame,
                       title: str = "Economia Projetada por Cluster"):
    """
    Renderiza gráfico de barras da economia por cluster.

    Args:
        economia_por_cluster: DataFrame com economia por cluster
        title: Título do gráfico
    """
    data = economia_por_cluster.reset_index()
    data['cluster_nome'] = data['cluster'].map(CLUSTER_NAMES)
    colors = [CLUSTER_COLORS.get(c, '#666666') for c in data['cluster']]

    fig = go.Figure(data=[
        go.Bar(
            x=data['cluster_nome'],
            y=data[('economia_total', 'sum')] if ('economia_total', 'sum') in data.columns
              else data.get('economia_total', [0] * len(data)),
            marker_color=colors,
            text=[f"R$ {v:,.0f}" for v in (
                data[('economia_total', 'sum')] if ('economia_total', 'sum') in data.columns
                else data.get('economia_total', [0] * len(data))
            )],
            textposition='outside'
        )
    ])

    fig.update_layout(
        title=title,
        xaxis_title="",
        yaxis_title="Economia Total (R$)",
        showlegend=False,
        margin=dict(t=50, b=30, l=50, r=20),
        height=350
    )

    st.plotly_chart(fig, use_container_width=True)


def trend_line_chart(data: pd.DataFrame, x: str, y: str,
                     title: str = "Tendência"):
    """
    Renderiza gráfico de linha para tendências.

    Args:
        data: DataFrame com os dados
        x: Coluna para eixo X
        y: Coluna para eixo Y
        title: Título do gráfico
    """
    fig = px.line(
        data,
        x=x,
        y=y,
        title=title,
        markers=True
    )

    fig.update_layout(
        xaxis_title=x.replace('_', ' ').title(),
        yaxis_title=y.replace('_', ' ').title(),
        margin=dict(t=50, b=30, l=50, r=20),
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)
