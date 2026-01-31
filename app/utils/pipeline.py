"""
Wrapper do Pipeline Economiza+ MVP para uso no Streamlit
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional
import pickle

from .data_loader import (
    load_transacoes,
    load_usuarios_clustered,
    load_economia_projetada,
    load_recomendacoes_regras
)
from .config import CLUSTER_NAMES, CLUSTER_PRIORITIES, ISOLATION_FOREST_FILE


class PipelineWrapper:
    """Wrapper para facilitar uso do pipeline no Streamlit."""

    def __init__(self):
        self.transacoes = load_transacoes()
        self.usuarios_clustered = load_usuarios_clustered()
        self.economia_projetada = load_economia_projetada()
        self.regras = load_recomendacoes_regras()

        # Tentar carregar isolation forest (unico que funciona)
        try:
            with open(ISOLATION_FOREST_FILE, 'rb') as f:
                self.isolation_forest = pickle.load(f)
        except Exception:
            self.isolation_forest = None

    def analisar_usuario(self, user_id: str) -> Dict:
        """
        Analisa um usuario e retorna perfil, recomendacoes e anomalias.

        Args:
            user_id: ID do usuario

        Returns:
            Dict com perfil, financeiro, recomendacoes, economia e anomalias
        """
        # Verificar se usuario existe
        user_data = self.usuarios_clustered[
            self.usuarios_clustered['user_id'] == user_id
        ]

        if len(user_data) == 0:
            return {'erro': f'Usuario {user_id} nao encontrado'}

        user_row = user_data.iloc[0]
        cluster = int(user_row['cluster'])

        # Dados financeiros
        financeiro = {
            'renda_media': float(user_row.get('media_renda', 0)),
            'gasto_medio': float(user_row.get('media_gasto', 0)),
            'taxa_poupanca': float(user_row.get('taxa_poupanca', 0)),
            'pct_essenciais': float(user_row.get('pct_gastos_essenciais', 0))
        }

        # Perfil
        perfil = {
            'cluster': cluster,
            'cluster_nome': CLUSTER_NAMES.get(cluster, f'Cluster {cluster}'),
            'prioridade': CLUSTER_PRIORITIES.get(cluster, 'MEDIA')
        }

        # Recomendacoes do cluster
        recomendacoes = self._get_recomendacoes(user_id, cluster, financeiro)

        # Economia projetada
        economia_user = self.economia_projetada[
            self.economia_projetada['user_id'] == user_id
        ]
        if len(economia_user) > 0:
            row = economia_user.iloc[0]
            total_mensal = float(row.get('economia_total', 0))
            # Tentar diferentes nomes de coluna para percentual
            pct_renda = 0
            for col_name in ['pct_economia_renda', 'economia_pct_renda', 'pct_da_renda']:
                if col_name in economia_user.columns:
                    pct_renda = float(row.get(col_name, 0))
                    break
            if pct_renda == 0 and financeiro['renda_media'] > 0:
                pct_renda = (total_mensal / financeiro['renda_media']) * 100
            economia = {
                'total_mensal': total_mensal,
                'pct_da_renda': pct_renda
            }
        else:
            economia = {'total_mensal': 0, 'pct_da_renda': 0}

        # Anomalias
        anomalias = self._detectar_anomalias(user_id)

        return {
            'user_id': user_id,
            'perfil': perfil,
            'financeiro': financeiro,
            'recomendacoes': recomendacoes,
            'economia': economia,
            'anomalias': anomalias
        }

    def _get_recomendacoes(self, user_id: str, cluster: int, financeiro: Dict) -> List[Dict]:
        """Obtem recomendacoes para o usuario baseado no cluster."""
        recomendacoes = []

        cluster_key = str(cluster)
        # Estrutura do JSON: {"clusters": {"0": {"regras": [...]}}}
        clusters_data = self.regras.get('clusters', self.regras)
        if cluster_key in clusters_data:
            cluster_info = clusters_data[cluster_key]
            regras_cluster = cluster_info.get('regras', cluster_info)

            # Obter gastos do usuario por categoria
            transacoes_user = self.transacoes[
                (self.transacoes['user_id'] == user_id) &
                (self.transacoes['categoria'] != 'Renda')
            ]
            gastos_por_categoria = transacoes_user.groupby('categoria')['valor'].sum()

            for regra in regras_cluster:
                categoria = regra.get('categoria', '')
                # O JSON usa 'percentual' como decimal (0.5 = 50%)
                pct_corte = regra.get('percentual', regra.get('pct_corte', 0))
                if pct_corte < 1:  # Se for decimal, converter para percentual
                    pct_corte = pct_corte * 100

                # Calcular economia potencial
                gasto_categoria = gastos_por_categoria.get(categoria, 0)
                # Dividir por 5 meses para obter media mensal
                gasto_mensal = gasto_categoria / 5
                economia_potencial = gasto_mensal * (pct_corte / 100)

                recomendacoes.append({
                    'titulo': regra.get('titulo', ''),
                    'categoria': categoria,
                    'acao': regra.get('acao', ''),
                    'pct_corte': pct_corte,
                    'economia_potencial': round(economia_potencial, 2),
                    'dica': regra.get('dica', '')
                })

        return recomendacoes

    def _detectar_anomalias(self, user_id: str) -> Dict:
        """Detecta anomalias nas transacoes do usuario."""
        transacoes_user = self.transacoes[
            (self.transacoes['user_id'] == user_id) &
            (self.transacoes['categoria'] != 'Renda')
        ]

        # Usar coluna is_anomalia se existir (ground truth ou predicao)
        if 'is_anomalia_pred' in transacoes_user.columns:
            anomalias = transacoes_user[transacoes_user['is_anomalia_pred'] == True]
        elif 'is_anomalia' in transacoes_user.columns:
            anomalias = transacoes_user[transacoes_user['is_anomalia'] == True]
        else:
            # Detectar por valor alto (>3x media da categoria)
            transacoes_user = transacoes_user.copy()
            media_por_categoria = transacoes_user.groupby('categoria')['valor'].transform('mean')
            transacoes_user['is_anomalia_calc'] = transacoes_user['valor'] > (3 * media_por_categoria)
            anomalias = transacoes_user[transacoes_user['is_anomalia_calc'] == True]

        transacoes_anomalas = []
        for _, row in anomalias.head(10).iterrows():  # Limitar a 10
            transacoes_anomalas.append({
                'data': str(row.get('data', '')),
                'categoria': row.get('categoria', ''),
                'valor': float(row.get('valor', 0))
            })

        return {
            'total_anomalias': len(anomalias),
            'transacoes_anomalas': transacoes_anomalas
        }

    def get_resumo_geral(self) -> Dict:
        """Retorna resumo geral do sistema."""
        total_usuarios = len(self.usuarios_clustered)

        # Distribuicao por cluster
        distribuicao = self.usuarios_clustered['cluster'].value_counts().sort_index()

        # Economia total
        economia_total = self.economia_projetada['economia_total'].sum()
        economia_media = self.economia_projetada['economia_total'].mean()

        # Usuarios em risco (clusters 0, 1, 2)
        usuarios_risco = len(self.usuarios_clustered[
            self.usuarios_clustered['cluster'].isin([0, 1, 2])
        ])
        pct_risco = (usuarios_risco / total_usuarios) * 100

        return {
            'total_usuarios': total_usuarios,
            'distribuicao_clusters': distribuicao.to_dict(),
            'economia_mensal_total': round(economia_total, 2),
            'economia_media_usuario': round(economia_media, 2),
            'economia_anual_total': round(economia_total * 12, 2),
            'usuarios_em_risco': usuarios_risco,
            'pct_usuarios_risco': round(pct_risco, 1)
        }


# Instancia global para uso no Streamlit
_pipeline_wrapper = None

def get_pipeline() -> PipelineWrapper:
    """Retorna instancia singleton do pipeline wrapper."""
    global _pipeline_wrapper
    if _pipeline_wrapper is None:
        _pipeline_wrapper = PipelineWrapper()
    return _pipeline_wrapper
