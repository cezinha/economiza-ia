"""
Página 2: Análise de Usuário Individual
Seleção e análise detalhada de um usuário específico
"""

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import CLUSTER_NAMES, CLUSTER_COLORS, PRIORITY_COLORS
from utils.data_loader import load_usuarios_clustered, load_transacoes, get_user_list
from utils.pipeline import get_pipeline
from components.cards import profile_card, recommendation_card, anomaly_card
from components.charts import financial_gauge

st.title("🔍 Análise de Usuário")
st.markdown("Análise detalhada e recomendações personalizadas")

st.markdown("---")

# Carregar dados
try:
    pipeline = get_pipeline()
    usuarios = load_usuarios_clustered()
    user_list = get_user_list()
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

# Seleção de usuário
col1, col2 = st.columns([3, 1])

with col1:
    selected_user = st.selectbox(
        "Selecione o usuário para analisar:",
        options=user_list,
        index=0,
        help="Escolha um usuário para ver sua análise completa"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_btn = st.button("📊 Analisar", type="primary", use_container_width=True)

# Se usuário selecionado
if selected_user and analyze_btn:
    st.markdown("---")

    with st.spinner(f"Analisando {selected_user}..."):
        resultado = pipeline.analisar_usuario(selected_user)

    if 'erro' in resultado:
        st.error(resultado['erro'])
        st.stop()

    # Perfil do usuário
    st.subheader(f"📊 Perfil: {selected_user}")

    perfil = resultado['perfil']
    financeiro = resultado['financeiro']
    cluster = perfil['cluster']
    color = CLUSTER_COLORS.get(cluster, '#666666')

    # Card de perfil estilizado
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {color}33, {color}11);
        border-left: 5px solid {color};
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1.5rem;
    ">
        <h2 style="margin: 0; color: {color};">{perfil['cluster_nome']}</h2>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem;">
            Prioridade: <strong>{perfil['prioridade']}</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Métricas financeiras
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        renda = financeiro['renda_media']
        st.metric("💵 Renda Média",
                 f"R$ {renda:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

    with col2:
        gasto = financeiro['gasto_medio']
        st.metric("💳 Gasto Médio",
                 f"R$ {gasto:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

    with col3:
        taxa = financeiro['taxa_poupanca']
        delta_color = "normal" if taxa >= 0 else "inverse"
        st.metric("📊 Taxa Poupança", f"{taxa:.1f}%", delta_color=delta_color)

    with col4:
        pct_ess = financeiro.get('pct_essenciais', 0)
        st.metric("🏠 Gastos Essenciais", f"{pct_ess:.1f}%")

    st.markdown("---")

    # Layout em duas colunas
    col_left, col_right = st.columns([3, 2])

    with col_left:
        # Recomendações
        st.subheader("💡 Recomendações Personalizadas")

        recomendacoes = resultado['recomendacoes']
        if recomendacoes:
            for i, rec in enumerate(recomendacoes, 1):
                economia = rec.get('economia_potencial', 0)
                economia_str = f"R$ {economia:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

                st.markdown(f"""
                <div style="
                    background: #f8f9fa;
                    border-left: 4px solid #2ED573;
                    padding: 1rem;
                    border-radius: 0.5rem;
                    margin-bottom: 0.5rem;
                ">
                    <h4 style="margin: 0; color: #333;">
                        {i}. {rec.get('titulo', 'Recomendação')}
                    </h4>
                    <p style="margin: 0.5rem 0;">
                        <strong>Categoria:</strong> {rec.get('categoria', '-')} |
                        <strong>Redução:</strong> {rec.get('pct_corte', 0)}%
                    </p>
                    <p style="margin: 0; color: #2ED573; font-size: 1.1rem; font-weight: bold;">
                        Economia: {economia_str}/mês
                    </p>
                    <p style="margin: 0.5rem 0 0 0; color: #666; font-style: italic;">
                        💡 {rec.get('dica', '')}
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Nenhuma recomendação específica para este perfil.")

        # Economia total
        st.markdown("### 💰 Economia Projetada")
        economia = resultado['economia']

        col_e1, col_e2 = st.columns(2)
        with col_e1:
            total = economia['total_mensal']
            st.metric("Total Mensal",
                     f"R$ {total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
        with col_e2:
            pct = economia['pct_da_renda']
            st.metric("% da Renda", f"{pct:.1f}%")

    with col_right:
        # Gauge
        st.subheader("📈 Saúde Financeira")
        financial_gauge(
            financeiro['taxa_poupanca'],
            title="Taxa de Poupança",
            min_val=-100,
            max_val=50
        )

        # Anomalias
        st.subheader("⚠️ Alertas de Anomalias")
        anomalias = resultado['anomalias']
        total_anomalias = anomalias['total_anomalias']

        if total_anomalias > 0:
            st.warning(f"**{total_anomalias}** transações suspeitas detectadas")

            transacoes_anomalas = anomalias.get('transacoes_anomalas', [])
            if transacoes_anomalas:
                st.markdown("**Últimas transações:**")
                for t in transacoes_anomalas[:5]:
                    valor = f"R$ {t['valor']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
                    st.markdown(f"- {t['data']} | {t['categoria']} | {valor}")
        else:
            st.success("✅ Nenhuma anomalia detectada")

elif selected_user:
    st.info("👆 Clique em **Analisar** para ver os detalhes do usuário selecionado.")
