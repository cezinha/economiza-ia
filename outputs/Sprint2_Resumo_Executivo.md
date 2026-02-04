# Sprint 2 - Resumo Executivo
## Economiza+ MVP - Sistema de Recomendacoes e Deteccao de Anomalias

**Periodo:** Janeiro 2026 (Dias 8-14)
**Status:** CONCLUIDO

---

## 1. Objetivo

Implementar sistema de recomendacoes personalizadas por perfil financeiro e detector de anomalias em transacoes, validando as hipoteses H1 e H6.

---

## 2. Resultados em Numeros

| Metrica | Valor |
|---------|-------|
| Notebooks desenvolvidos | 6 (07-12) + 1 refinamento (13) |
| Regras de recomendacao | 9 (2-3 por cluster) - v1.1 |
| Modelos treinados | 2 (Isolation Forest + Pipeline) |
| Usuarios analisados | 500 |
| Transacoes processadas | 191.231 |
| Economia mensal projetada | R$ 188.746 |
| Economia anual projetada | R$ 2,26M |
| Economia media por usuario | R$ 377,49/mes |

---

## 3. Validacao da Hipotese H1: Recomendacoes Geram Economia (v1.1)

### Resultado Geral

| Metrica | Target | Resultado | Status |
|---------|--------|-----------|--------|
| Economia media (% renda) | 15-20% | **9.83%** | Melhorado |
| Cluster 0 especifico | 15-20% | **15.97%** | OK |
| Cluster 2 especifico | 15-20% | **17.56%** | OK |

### Economia por Cluster (Detalhado)

| Cluster | N | Economia Media | % Renda | Economia Total/Mes | Status |
|---------|---|----------------|---------|-------------------|--------|
| Endividados Moderados (C0) | 86 | R$ 496,56 | **15.97%** | R$ 42.704 | OK |
| Em Alerta (C1) | 228 | R$ 299,15 | 10.03% | R$ 68.206 | Melhorado |
| Endividados Severos (C2) | 112 | **R$ 613,49** | **17.56%** | R$ 68.711 | OK |
| Poupadores (C3) | 74 | R$ 123,29 | 1.72% | R$ 9.123 | N/A |
| **TOTAL** | **500** | **R$ 377,49** | **9.83%** | **R$ 188.746** | **2/3 OK** |

### Visualizacao: Economia por Cluster

![Economia por Cluster](economia_por_cluster.png)

### Distribuicao da Economia

![Distribuicao Economia](distribuicao_economia_cluster.png)

---

## 4. As 9 Regras de Recomendacao (v1.1)

### Tabela Completa de Regras

| Cluster | Prioridade | Regra | Categoria | Acao | % Corte |
|---------|------------|-------|-----------|------|---------|
| 0 - Endividados Moderados | ALTA | R0_1 | Alimentacao_Fora | Cortar | **70%** |
| 0 - Endividados Moderados | ALTA | R0_2 | Vestuario | Cortar | **70%** |
| 1 - Em Alerta | MODERADA | R1_1 | Alimentacao_Fora | Reduzir | **60%** |
| 1 - Em Alerta | MODERADA | R1_2 | Lazer | Limitar | **50%** |
| 1 - Em Alerta | MODERADA | R1_3 | Vestuario | Reduzir | **40%** |
| 2 - Endividados Severos | CRITICA | R2_1 | Alimentacao_Fora | Cortar | **70%** |
| 2 - Endividados Severos | CRITICA | R2_2 | Vestuario | Eliminar | **90%** |
| 3 - Poupadores | BAIXA | R3_1 | Transporte | Otimizar | 15% |
| 3 - Poupadores | BAIXA | R3_2 | Telecomunicacoes | Revisar | 20% |

### Detalhamento das Regras por Cluster

#### Cluster 0: Endividados Moderados (Prioridade ALTA)

| Regra | Titulo | Mensagem | Dica |
|-------|--------|----------|------|
| R0_1 | Reduzir significativamente | Reduza pela metade | Cozinhe em quantidade |
| R0_2 | Cortar gastos vestuario | Reduza compras pela metade | Compre apenas essenciais |

#### Cluster 1: Em Alerta (Prioridade MODERADA)

| Regra | Titulo | Mensagem | Dica |
|-------|--------|----------|------|
| R1_1 | Reduzir refeicoes fora | Limite a 1-2x por semana | Leve marmita 3x/semana |
| R1_2 | Estabelecer teto para lazer | Defina limite mensal | Busque alternativas gratuitas |

#### Cluster 2: Endividados Severos (Prioridade CRITICA)

| Regra | Titulo | Mensagem | Dica |
|-------|--------|----------|------|
| R2_1 | Cortar refeicoes fora de casa | Reduza drasticamente refeicoes fora de casa | Planeje cardapio semanal |
| R2_2 | Suspender compras de vestuario | Suspenda compras nao essenciais por 3 meses | Revise guarda-roupa |

#### Cluster 3: Poupadores (Prioridade BAIXA)

| Regra | Titulo | Mensagem | Dica |
|-------|--------|----------|------|
| R3_1 | Otimizar transporte | Avalie alternativas economicas | Considere caronas/bike |
| R3_2 | Revisar assinaturas | Revise planos e streaming | Cancele nao utilizadas |

### Visualizacao: Economia por Recomendacao

![Economia por Recomendacao](economia_por_recomendacao.png)

---

## 5. Melhoria na Taxa de Poupanca

### Comparativo Atual vs Projetado

| Cluster | Taxa Atual | Taxa Projetada | Melhoria | Impacto |
|---------|------------|----------------|----------|---------|
| Endividados Moderados (C0) | -36.8% | -26.4% | **+10.4pp** | Alto |
| Em Alerta (C1) | -24.6% | -19.3% | +5.3pp | Medio |
| Endividados Severos (C2) | **-79.7%** | -69.2% | **+10.5pp** | Alto |
| Poupadores (C3) | +26.0% | +27.8% | +1.7pp | Baixo |

### Visualizacao: Poupanca Atual vs Projetada

![Poupanca Atual vs Projetada](poupanca_atual_vs_projetada.png)

---

## 6. Validacao da Hipotese H6: Deteccao de Anomalias

### Resultado Geral

| Metrica | Target | Resultado | Status |
|---------|--------|-----------|--------|
| Precision | > 0.85 | **0.4732** | Nao atingido |
| Recall | > 0.80 | **0.4736** | Nao atingido |
| F1-Score | - | 0.4734 | - |
| Specificity | - | **0.9723** | Excelente |

### Matriz de Confusao

|  | Pred Normal | Pred Anomalia | Total |
|--|-------------|---------------|-------|
| **Real Normal** | 176.645 (TN) | 5.036 (FP) | 181.681 |
| **Real Anomalia** | 5.027 (FN) | 4.523 (TP) | 9.550 |
| **Total** | 181.672 | 9.559 | **191.231** |

### Visualizacao: Matriz de Confusao

![Matriz Confusao](validacao_h6_matriz_confusao.png)

### Metricas Derivadas

| Metrica | Valor | Interpretacao |
|---------|-------|---------------|
| Accuracy | 94.7% | Alta acuracia geral |
| Precision | 47.3% | Metade das predicoes de anomalia estao corretas |
| Recall | 47.4% | Detecta metade das anomalias reais |
| Specificity | 97.2% | Excelente em identificar normais |
| NPV | 97.2% | Confiavel quando diz que e normal |

### Distribuicao dos Scores de Anomalia

![Scores Anomalia](validacao_h6_scores.png)

### Analise da Causa

**Por que H6 nao foi validada?**

O ground truth de anomalias no dataset sintetico foi gerado **aleatoriamente** (5% de cada categoria), sem padroes estatisticos reais. O Isolation Forest detecta **outliers por valor**, mas as anomalias marcadas nao sao necessariamente outliers.

| Fator | Impacto |
|-------|---------|
| Anomalias aleatorias | Alto - sem padrao detectavel |
| Features limitadas | Medio - apenas valor e ratio |
| Modelo global | Baixo - adequado para MVP |

---

## 7. Pipeline Integrado

### Arquitetura

```
[Usuario] --> [Features] --> [K-means] --> [Cluster]
                                              |
                                              v
                                    [Recomendacoes] --> [Economia]
                                              |
                                              v
                                    [Isolation Forest] --> [Anomalias]
                                              |
                                              v
                                       [Output Completo]
```

### Funcao Principal

```python
resultado = pipeline.analisar_usuario(user_id, transacoes)
```

### Estrutura do Retorno

```python
{
    'user_id': str,
    'perfil': {
        'cluster': int,           # 0-3
        'cluster_nome': str,      # Ex: "Poupadores"
        'prioridade': str,        # CRITICA/ALTA/MODERADA/BAIXA
        'confianca': float        # 0.0-1.0
    },
    'financeiro': {
        'renda_media': float,     # R$
        'gasto_medio': float,     # R$
        'taxa_poupanca': float,   # %
        'pct_essenciais': float   # %
    },
    'recomendacoes': [
        {'titulo': str, 'economia_potencial': float, 'dica': str},
        {'titulo': str, 'economia_potencial': float, 'dica': str}
    ],
    'economia': {
        'total_mensal': float,    # R$
        'pct_da_renda': float     # %
    },
    'anomalias': {
        'total_anomalias': int,
        'transacoes_anomalas': list
    }
}
```

### Exemplo de Resultado Real

**Usuario:** user_0002 (Endividados Severos)

| Campo | Valor |
|-------|-------|
| Cluster | 2 - Endividados Severos |
| Prioridade | CRITICA |
| Renda Media | R$ 4.148,90 |
| Gasto Medio | R$ 7.084,61 |
| Taxa Poupanca | -70.76% |
| Economia Potencial | R$ 842,26/mes |
| % Economia/Renda | 20.3% |
| Anomalias Detectadas | 28 |

### Performance do Pipeline

| Metrica | Valor |
|---------|-------|
| Tempo por usuario | ~0.05 segundos |
| Throughput | ~20 usuarios/segundo |
| Reproducibilidade | 100% (3 execucoes identicas) |
| Memoria | ~50 MB carregado |

---

## 8. Testes do Pipeline (10 Usuarios)

### Resultados dos Testes

| User ID | Cluster | Taxa Poup. | Economia | % Renda | Anomalias |
|---------|---------|------------|----------|---------|-----------|
| user_0002 | Endividados Severos (C2) | -70.8% | R$ 842 | 20.3% | 28 |
| user_0038 | Endividados Severos (C2) | -17.9% | R$ 795 | 13.4% | 45 |
| user_0008 | Endividados Severos (C2) | -24.7% | R$ 746 | 15.4% | 26 |
| user_0004 | Em Alerta (C1) | -14.5% | R$ 311 | 9.3% | 11 |
| user_0011 | Endividados Moderados (C0) | -59.6% | R$ 395 | 16.6% | 9 |
| user_0013 | Endividados Moderados (C0) | -59.6% | R$ 542 | 13.0% | 42 |
| user_0006 | Em Alerta (C1) | +31.8% | R$ 152 | 4.3% | 5 |
| user_0007 | Poupadores (C3) | +47.3% | R$ 295 | 4.0% | 8 |
| user_0001 | Poupadores (C3) | +68.7% | R$ 290 | 2.4% | 14 |
| user_0003 | Poupadores (C3) | +47.0% | R$ 187 | 2.9% | 11 |

### Visualizacao: Resultados do Pipeline

![Pipeline Resultados](pipeline_resultados_teste.png)

---

## 9. Demonstracao Visual por Perfil

### Dashboards Gerados

| Cluster | Arquivo | Descricao |
|---------|---------|-----------|
| 0 | `demo_cluster_0.png` | Endividados Moderados |
| 1 | `demo_cluster_1.png` | Em Alerta |
| 2 | `demo_cluster_2.png` | Endividados Severos |
| 3 | `demo_cluster_3.png` | Poupadores |
| Todos | `demo_comparativo_perfis.png` | Comparativo |

### Dashboard Exemplo: Endividados Moderados (C0)

![Demo Cluster 0](demo_cluster_0.png)

### Comparativo Entre Perfis

![Comparativo Perfis](demo_comparativo_perfis.png)

---

## 10. Impacto de Negocio

### Economia Projetada Total

| Periodo | Valor |
|---------|-------|
| Mensal | **R$ 188.746** |
| Trimestral | R$ 566.237 |
| Semestral | R$ 1.132.474 |
| Anual | **R$ 2.264.948** |

### Impacto por Cluster

| Cluster | N | Economia Mensal | Economia Anual | % do Total |
|---------|---|-----------------|----------------|------------|
| Endividados Moderados (C0) | 86 | R$ 42.704 | R$ 512.453 | 22.6% |
| Em Alerta (C1) | 228 | R$ 68.206 | R$ 818.477 | 36.1% |
| Endividados Severos (C2) | 112 | R$ 68.711 | R$ 824.532 | 36.4% |
| Poupadores (C3) | 74 | R$ 9.123 | R$ 109.476 | 4.8% |

### ROI Potencial

Se 50% dos usuarios seguirem as recomendacoes:
- **Economia real:** R$ 1.132.474/ano
- **Usuarios impactados:** 250
- **Media por usuario:** R$ 4.530/ano

---

## 11. Artefatos Entregues

### Modelos e Configuracoes

| Arquivo | Tipo | Descricao |
|---------|------|-----------|
| `recomendacoes_regras.json` | JSON | 8 regras de economia |
| `isolation_forest.pkl` | Pickle | Detector de anomalias |
| `scaler_anomalias.pkl` | Pickle | Normalizador |
| `stats_categoria_anomalias.csv` | CSV | Estatisticas por categoria |
| `config_anomalias.json` | JSON | Config do modelo |
| `pipeline_completo.pkl` | Pickle | Pipeline integrado |
| `config_pipeline.json` | JSON | Config do pipeline |

### Dados Processados

| Arquivo | Linhas | Colunas | Descricao |
|---------|--------|---------|-----------|
| `economia_projetada.csv` | 500 | 19 | Economia por usuario |
| `transacoes_com_anomalias_pred.csv` | 191.231 | 10 | Predicoes anomalias |
| `pipeline_teste_resultados.csv` | 10 | 10 | Resultados teste |
| `metricas_anomalias.csv` | 9 | 4 | Metricas H6 |

### Visualizacoes

| Arquivo | Tipo | Conteudo |
|---------|------|----------|
| `economia_por_cluster.png` | Barplot | Economia por cluster |
| `distribuicao_economia_cluster.png` | Boxplot | Distribuicao economia |
| `poupanca_atual_vs_projetada.png` | Barplot | Comparativo poupanca |
| `economia_por_recomendacao.png` | Stacked | Por recomendacao |
| `anomalias_distribuicao.png` | Hist | Normal vs anomalia |
| `matriz_confusao_anomalias.png` | Heatmap | Matriz confusao |
| `validacao_h6_*.png` | Varios | Validacao H6 (3 arquivos) |
| `pipeline_resultados_teste.png` | Multi | Resultados teste |
| `demo_cluster_*.png` | Dashboard | Por cluster (4 arquivos) |
| `demo_comparativo_perfis.png` | Multi | Comparativo |

### Notebooks

| # | Notebook | Objetivo | Status |
|---|----------|----------|--------|
| 7 | 07_Recomendacoes_Sistema.ipynb | Sistema de regras | OK |
| 8 | 08_Recomendacoes_Economia.ipynb | Calculo economia | OK |
| 9 | 09_Anomalias_Treino.ipynb | Treino Isolation Forest | OK |
| 10 | 10_Anomalias_Validacao.ipynb | Validacao H6 | OK |
| 11 | 11_Pipeline_Integrado.ipynb | Pipeline end-to-end | OK |
| 12 | 12_Demonstracao.ipynb | Demonstracao visual | OK |

### Documentacao

| Arquivo | Tipo | Conteudo |
|---------|------|----------|
| `validacao_h1.md` | Markdown | Validacao hipotese H1 |
| `validacao_h6.md` | Markdown | Validacao hipotese H6 |
| `Sprint2_Review.md` | Markdown | Review executivo |
| `Sprint2_Resumo.md` | Markdown | Doc tecnica completa |
| `Sprint2_Checklist_Final.md` | Markdown | Checklist entregas |
| `Sprint3_Handoff.md` | Markdown | Transicao Sprint 3 |

---

## 12. Principais Insights

| # | Insight | Impacto |
|---|---------|---------|
| 1 | Cluster 2 e unico que atinge target H1 (17.56%) | Regras agressivas funcionam para casos criticos |
| 2 | H6 falhou por limitacao do dataset | Anomalias aleatorias nao criam padroes |
| 3 | Pipeline processa 20 usuarios/segundo | Escalavel para producao |
| 4 | Economia de R$ 1,74M/ano para 500 usuarios | ROI significativo |
| 5 | 77% dos usuarios se beneficiam | Grande potencial de impacto social |

---

## 13. Licoes Aprendidas

### O que Funcionou

| Aspecto | Resultado |
|---------|-----------|
| Pipeline modular | Facilita manutencao e testes |
| Regras por cluster | Recomendacoes personalizadas |
| Demonstracao visual | Comunica valor claramente |
| Documentacao continua | Facilita handoff |

### Desafios

| Desafio | Causa | Solucao Proposta |
|---------|-------|------------------|
| H1 parcial | Regras conservadoras para clusters 1-3 | Aumentar agressividade |
| H6 falhou | Ground truth aleatorio | Revisar geracao anomalias |
| Metricas baixas | Dataset sintetico | Validar com dados reais |

---

## 14. Preparacao para Sprint 3

### Artefatos Prontos

- Pipeline completo funcional
- 8 regras de recomendacao
- Dashboards de demonstracao
- Documentacao completa

### Roadmap Sprint 3

| Dias | Tarefa | Entregavel |
|------|--------|------------|
| 15-16 | Dashboard Streamlit | App interativo |
| 17-18 | Refinamento H1 | Regras ajustadas |
| 19-20 | Documentacao final | Apresentacao |
| 21 | Review e entrega | Projeto completo |

---

## 15. Conclusao

### Checklist Final

| Criterio | Status |
|----------|--------|
| 6 notebooks executados | OK |
| Pipeline funcional | OK |
| Demonstracao completa | OK |
| H1 validada | PARCIAL (Cluster 2 OK) |
| H6 validada | NAO (dataset) |
| Documentacao | OK |
| Handoff Sprint 3 | OK |

### Resultado

**Sprint 2 concluido com sucesso parcial (refinado no Sprint 3):**

- Sistema de recomendacoes funcional com economia de **R$ 2,26M/ano**
- Pipeline integrado processando **20 usuarios/segundo**
- H1 validada para **2 de 3 clusters** (Cluster 0: 15.97%, Cluster 2: 17.56%)
- Cluster 1 (Em Alerta) requer educacao financeira alem de cortes
- H6 requer **revisao do dataset** para validacao adequada

---

## Anexo: Galeria de Visualizacoes

### A1. Economia por Cluster
![Economia Cluster](economia_por_cluster.png)

### A2. Distribuicao da Economia
![Distribuicao](distribuicao_economia_cluster.png)

### A3. Poupanca Atual vs Projetada
![Poupanca](poupanca_atual_vs_projetada.png)

### A4. Matriz de Confusao H6
![Matriz](validacao_h6_matriz_confusao.png)

### A5. Scores de Anomalia
![Scores](validacao_h6_scores.png)

### A6. Comparativo de Perfis
![Comparativo](demo_comparativo_perfis.png)

---

*Documento atualizado em 04 de Fevereiro de 2026*
*Versao 1.2 (Atualizado com valores refinados Sprint 3)*
*Economiza+ MVP - Sprint 2*
