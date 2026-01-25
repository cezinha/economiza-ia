# Sprint 1 Review - Economiza+ MVP

## Resumo

| Metrica | Valor |
|---------|-------|
| Usuarios analisados | 500 |
| Clusters identificados | 4 |
| Usuarios em risco | 386 (77.2%) |
| Taxa poupanca media | -31.6% |

## Validacao da Hipotese H2

**H2: Deteccao de Padroes** - Algoritmos de clustering podem identificar padroes de gastos com precisao superior a 80%.

| Metrica | Target | Resultado | Status |
|---------|--------|-----------|--------|
| Silhouette Score | > 0.5 | 0.2568 | NAO ATINGIDO |
| Davies-Bouldin Index | < 1.0 | 1.1959 | NAO ATINGIDO |
| Clusters interpretaveis | Sim | Sim | ATINGIDO |

### Analise

- **Silhouette Score (0.26)**: Abaixo do target (0.5), indicando sobreposicao entre clusters
- **Davies-Bouldin (1.20)**: Acima do target (1.0), confirmando clusters nao bem separados
- **Interpretabilidade**: Apesar das metricas, os 4 clusters sao claramente interpretaveis com perfis distintos de risco financeiro

### Decisao

Para o MVP, **aceitamos os resultados** pois:
1. Os clusters tem significado de negocio claro
2. Permitem recomendacoes personalizadas por perfil e nivel de risco
3. Melhorias podem ser feitas no Sprint 2 (ajuste de features, remocao de outliers)

## Entregas Concluidas

- [x] EDA Basico
- [x] Feature Engineering (5 features)
- [x] Clustering K-means (K=4)
- [x] Validacao do Modelo
- [x] Interpretacao dos Clusters
- [x] Analise de Recomendacoes

## Perfis Identificados

- **Endividados Severos**: 59 usuarios (-88.6% poupanca)
- **Endividados Moderados**: 167 usuarios (-57.7% poupanca)
- **Em Alerta**: 196 usuarios (-14.8% poupanca)
- **Poupadores**: 78 usuarios (+25.4% poupanca)

## Top 3 Categorias para Economia

(gasto mensal medio por usuario - nao essenciais)

1. **Alimentacao_Fora** - R$ 411.64/mes
2. **Vestuario** - R$ 197.60/mes
3. **Lazer** - R$ 154.78/mes

## Preparacao Sprint 2

### Proximos Passos

1. Implementar sistema de recomendacoes por perfil (H1)
2. Treinar detector de anomalias Isolation Forest (H6)
3. Integrar clustering + recomendacao + anomalias
4. Criar notebook de demonstracao

### Melhorias Identificadas para Clustering

- Testar remocao de outliers antes do clustering
- Considerar adicionar features comportamentais
- Avaliar normalizacao alternativa (MinMaxScaler)
- Refinar limites entre categorias de risco

---
*Sprint 1 concluido em Janeiro/2026*
