---
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1 {
    color: #2ED573;
  }
  h2 {
    color: #333;
  }
  table {
    font-size: 0.8em;
  }
---

# Economiza+ MVP

## Sistema de Análise Financeira e Recomendações Personalizadas

**Curso**: Data Science - XP Educação
**Orientador**: Marcos Prochnow
**Data**: Fevereiro 2026

---

# O Problema

## Cenário Financeiro Brasileiro

- **80,6 milhões** de inadimplentes (Serasa)
- **79,5%** das famílias endividadas (CNC)
- **60%** não conseguem poupar (IBGE)
- Dívida média de **R$ 4.042**

### Desafio
Famílias das classes C e D precisam de orientação **personalizada** para melhorar sua saúde financeira.

---

# A Solução: Economiza+

## Sistema Inteligente de 4 Etapas

1. **Análise** - Processa transações financeiras
2. **Segmentação** - Identifica perfil do usuário (K-means)
3. **Recomendação** - Sugere ações personalizadas
4. **Monitoramento** - Detecta anomalias (Isolation Forest)

### Diferencial
Recomendações específicas por perfil, não genéricas!

---

# Metodologia: 3 Sprints

| Sprint | Dias | Foco | Entregas |
|--------|------|------|----------|
| 1 | 1-7 | Segmentação | EDA, Features, Clustering |
| 2 | 8-14 | Recomendações | Regras, Anomalias, Pipeline |
| 3 | 15-21 | Dashboard | Streamlit, Docs |

### Stack
Python, scikit-learn, Streamlit, Plotly

---

# Sprint 1: 4 Perfis Identificados

| Perfil | % | Taxa Poupança | Risco |
|--------|---|---------------|-------|
| Endividados Moderados | 17,2% | -36,8% | ALTO |
| Em Alerta | 45,6% | -24,6% | MODERADO |
| **Endividados Severos** | 22,4% | **-79,7%** | CRÍTICO |
| Poupadores | 14,8% | +26,0% | BAIXO |

### Descoberta Chave
**85,2%** dos usuários em risco financeiro!

---

# Sprint 2: Recomendações Personalizadas

| Perfil | Ação Principal | Economia |
|--------|----------------|----------|
| Moderados | Cortar Alimentação Fora 70% | R$ 496/mês |
| Em Alerta | Reduzir Lazer 50% | R$ 299/mês |
| Severos | Eliminar Vestuário 90% | R$ 613/mês |
| Poupadores | Otimizar Transporte 15% | R$ 123/mês |

### Impacto Total
**R$ 188.746/mês** | **R$ 2,26M/ano**

---

# Sprint 3: Dashboard Interativo

## 5 Páginas Implementadas

- **Início** - Métricas gerais
- **Visão Geral** - Distribuição dos perfis
- **Análise de Usuário** - Recomendações individuais
- **Comparativo** - Perfis lado a lado
- **Diagnóstico** - Saúde do sistema

### Tecnologias
Streamlit + Plotly + Cache + Error Handling

---

# Validação das Hipóteses

## H1: Recomendações geram economia (✅ Parcial)

| Cluster | Target | Resultado |
|---------|--------|-----------|
| Moderados | 15-20% | **15,97%** ✅ |
| Em Alerta | 15-20% | 10,03% ⚠️ |
| Severos | 15-20% | **17,56%** ✅ |

## H2: Clustering funciona (✅ Parcial)
Silhouette: 0,267 | PCA: 82,7%

## H6: Detecção de anomalias (❌)
Precision: 47,3% (dataset limitation)

---

# Lições Aprendidas

### Técnicas
- **Interpretabilidade > Métricas** - Clusters úteis mesmo com scores baixos
- **Simplicidade funciona** - 5 features suficientes
- **Taxa de poupança é chave** - Feature mais discriminante

### Processo
- **Documentação contínua** economiza tempo
- **Pipeline modular** facilita iteração
- **Ground truth importa** - H6 falhou por dados sintéticos

---

# Próximos Passos

## Curto Prazo
- Validação com usuários reais
- Deploy em cloud

## Médio Prazo
- Integração com dados bancários
- App mobile

## Longo Prazo
- Modelo preditivo de inadimplência
- Parcerias com instituições financeiras

---

# Métricas Finais

| Métrica | Valor |
|---------|-------|
| Usuários analisados | 500 |
| Transações processadas | 191.231 |
| Perfis identificados | 4 |
| Notebooks desenvolvidos | 13 |
| Economia mensal projetada | R$ 188.746 |
| Economia anual projetada | R$ 2,26M |

---

# Obrigado!

## Economiza+ MVP v1.1.0

**Dashboard**: `streamlit run app/app.py`

**Documentação**: `CLAUDE.md`

---

*Data Science - XP Educação*
*Fevereiro 2026*
