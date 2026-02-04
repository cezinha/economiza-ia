# Economiza+ MVP
## Sistema de Análise Financeira e Recomendações Personalizadas

**Curso**: Data Science - XP Educação
**Orientador**: Marcos Prochnow
**Data**: Fevereiro 2026

---

# Agenda

1. Problema e Contexto
2. Solução Proposta
3. Metodologia
4. Resultados - Sprint 1 (Segmentação)
5. Resultados - Sprint 2 (Recomendações)
6. Dashboard
7. Validação das Hipóteses
8. Lições Aprendidas
9. Próximos Passos

---

# 1. Problema e Contexto

## O Cenário Brasileiro

| Indicador | Valor | Fonte |
|-----------|-------|-------|
| Inadimplentes | 80,6 milhões | Serasa |
| Famílias endividadas | 79,5% | CNC |
| Não conseguem poupar | 60% | IBGE |
| Dívida média | R$ 4.042 | Serasa |

## O Problema

- Famílias das classes C e D gastam mais do que ganham
- Falta de visibilidade sobre padrões de gastos
- Recomendações genéricas não funcionam
- Necessidade de personalização por perfil

---

# 2. Solução Proposta

## Economiza+ MVP

Sistema inteligente que:

1. **Analisa** comportamentos financeiros
2. **Segmenta** usuários em perfis distintos
3. **Recomenda** ações personalizadas de economia
4. **Detecta** transações anômalas
5. **Visualiza** através de dashboard interativo

## Diferenciais

- Baseado em dados reais brasileiros
- Recomendações específicas por perfil
- Interface amigável para usuário final
- Pipeline automatizado e reproduzível

---

# 3. Metodologia

## Estrutura em 3 Sprints (21 dias)

| Sprint | Foco | Entregas |
|--------|------|----------|
| **Sprint 1** (Dias 1-7) | Segmentação | EDA, Features, K-means |
| **Sprint 2** (Dias 8-14) | Recomendações | Regras, Anomalias, Pipeline |
| **Sprint 3** (Dias 15-21) | Dashboard | Streamlit, Documentação |

## Stack Tecnológica

- **Python 3.11+** com pandas, numpy, scikit-learn
- **Machine Learning**: K-means, Isolation Forest
- **Visualização**: Matplotlib, Seaborn, Plotly
- **Dashboard**: Streamlit
- **Versionamento**: Git

---

# 4. Resultados - Sprint 1

## Dataset Sintético

- **500 usuários** com perfis demográficos realistas
- **191.231 transações** em 10 categorias
- **5 features** de clustering selecionadas

## Clustering K-means (K=4)

| Cluster | Nome | % | Taxa Poupança |
|---------|------|---|---------------|
| 0 | Endividados Moderados | 17,2% | -36,8% |
| 1 | Em Alerta | 45,6% | -24,6% |
| 2 | Endividados Severos | 22,4% | -79,7% |
| 3 | Poupadores | 14,8% | +26,0% |

**Descoberta chave**: 85,2% dos usuários em risco financeiro

---

# 5. Resultados - Sprint 2

## Sistema de Recomendações (v1.1)

| Perfil | Prioridade | Recomendação Principal |
|--------|------------|------------------------|
| Moderados | ALTA | Cortar Alimentação Fora 70% |
| Em Alerta | MODERADA | Reduzir Alimentação Fora 60% |
| Severos | CRÍTICA | Eliminar Vestuário 90% |
| Poupadores | BAIXA | Otimizar Transporte 15% |

## Impacto Projetado

| Período | Economia |
|---------|----------|
| Mensal (500 usuários) | R$ 188.746 |
| Anual | R$ 2,26 milhões |

---

# 6. Dashboard

## 5 Páginas Implementadas

1. **Início** - Métricas gerais e navegação
2. **Visão Geral** - Distribuição dos perfis
3. **Análise de Usuário** - Perfil individual + recomendações
4. **Comparativo** - Comparação entre clusters
5. **Diagnóstico** - Saúde do sistema

## Tecnologias

- Streamlit para interface web
- Plotly para gráficos interativos
- Cache para performance
- Tratamento robusto de erros

---

# 7. Validação das Hipóteses

## H1: Recomendações geram economia (Target: 15-20%)

| Cluster | Antes | Depois | Status |
|---------|-------|--------|--------|
| Moderados | 10,98% | **15,97%** | ✅ |
| Em Alerta | 5,19% | 10,03% | ⚠️ |
| Severos | 17,41% | **17,56%** | ✅ |

**Resultado**: 2 de 3 clusters atingem o target

## H2: K-means identifica perfis (Silhouette > 0.50)

- Silhouette Score: 0,267 (abaixo do target)
- PCA Variance: 82,7% (acima do target)
- **Resultado**: Parcialmente validada - clusters são interpretáveis

## H6: Isolation Forest detecta anomalias (Precision > 0.85)

- Precision: 47,3% | Recall: 47,4%
- **Resultado**: Não validada (limitação do dataset)

---

# 8. Lições Aprendidas

## Técnicas

| Lição | Descrição |
|-------|-----------|
| Interpretabilidade > Métricas | Clusters úteis mesmo com Silhouette baixo |
| Simplicidade funciona | 5 features foram suficientes |
| Taxa de poupança é chave | Feature mais discriminante |

## Processo

| Lição | Descrição |
|-------|-----------|
| Documentação contínua | Economiza tempo no longo prazo |
| Pipeline modular | Facilita iteração e debugging |
| Ground truth importa | H6 falhou por anomalias aleatórias |

## Negócio

| Lição | Descrição |
|-------|-----------|
| Perfis diferentes, abordagens diferentes | Cluster 1 precisa de educação financeira |
| Regras agressivas para casos críticos | Cluster 2 atingiu target com cortes de 90% |

---

# 9. Próximos Passos

## Curto Prazo

- [ ] Validação com usuários reais
- [ ] Deploy em cloud (Streamlit Community)
- [ ] Coleta de feedback

## Médio Prazo

- [ ] Integração com dados bancários reais
- [ ] App mobile
- [ ] Notificações push

## Longo Prazo

- [ ] Modelo preditivo de inadimplência
- [ ] Gamificação de metas
- [ ] Parcerias com instituições financeiras

---

# Obrigado!

## Economiza+ MVP

**Repositório**: github.com/seu-usuario/economiza-ia

**Contato**: [seu-email]

---

*Desenvolvido como projeto de conclusão de curso*
*Data Science - XP Educação*
*Fevereiro 2026*
