# Validação da Hipótese H6 - Detecção de Anomalias

**Data:** 27 de January de 2026
**Sprint:** 2 - Dia 11

---

## Hipótese

**H6:** Isolation Forest detecta transações anômalas com Precision > 0.85 e Recall > 0.80

## Metodologia

- **Modelo:** Isolation Forest (sklearn)
- **Features:** feat_valor_norm, feat_ratio_mediana
- **Contamination:** 0.05
- **Ground Truth:** Coluna `is_anomalia` no dataset (5% das transações)

## Resultados

| Métrica | Valor | Target | Status |
|---------|-------|--------|--------|
| Precision | 0.4732 | > 0.85 | ✗ NÃO ATINGIDO |
| Recall | 0.4736 | > 0.8 | ✗ NÃO ATINGIDO |
| F1-Score | 0.4734 | - | - |
| Specificity | 0.9723 | - | - |

## Matriz de Confusão

|  | Pred Normal | Pred Anomalia |
|--|-------------|---------------|
| **Real Normal** | 176645 | 5036 |
| **Real Anomalia** | 5027 | 4523 |

## Conclusão

**>>> HIPÓTESE H6: ✗ NÃO VALIDADA**

O modelo não atingiu todos os targets. Recomenda-se investigar features adicionais ou algoritmos alternativos.

## Artefatos Gerados

- `models/isolation_forest.pkl` - Modelo treinado
- `models/scaler_anomalias.pkl` - Scaler para normalização
- `models/stats_categoria_anomalias.csv` - Estatísticas por categoria
- `models/config_anomalias.json` - Configuração do modelo
- `data/processed/transacoes_com_anomalias_pred.csv` - Predições
- `outputs/metricas_anomalias.csv` - Métricas de validação
- `outputs/validacao_h6_matriz_confusao.png` - Visualização
- `outputs/validacao_h6_scores.png` - Distribuição de scores
- `outputs/validacao_h6_por_categoria.png` - Análise por categoria

---

*Documento gerado automaticamente - Economiza+ MVP*
