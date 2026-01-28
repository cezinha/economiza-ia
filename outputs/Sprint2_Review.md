# Sprint 2 Review - Economiza+ MVP
## Sistema de Recomendacoes e Deteccao de Anomalias

**Periodo:** 26-27 de Janeiro de 2026
**Duracao:** 7 dias (Dias 8-14)
**Status:** CONCLUIDO

---

## Resumo Executivo

| Metrica | Resultado |
|---------|-----------|
| Notebooks desenvolvidos | 6 (07-12) |
| Modelos treinados | 2 (Isolation Forest + Pipeline) |
| Regras de recomendacao | 8 (2 por cluster) |
| Usuarios analisados | 500 |
| Economia mensal total projetada | R$ 135.972,17 |
| Economia anual projetada | R$ 1.631.666,04 |

---

## Validacao das Hipoteses

### H1: Recomendacoes Geram Economia Real

**Target:** 15-20% de reducao de gastos
**Resultado:** 8.11% de economia media (% da renda)
**Status:** :x: **NAO VALIDADA** (parcialmente - Cluster 0 atingiu 19.22%)

#### Detalhamento por Cluster

| Cluster | Economia Media | % da Renda | Status |
|---------|----------------|------------|--------|
| **Endividados Severos** | R$ 698,53 | 19.22% | :white_check_mark: Atingido |
| **Em Alerta** | R$ 162,59 | 5.37% | :x: Abaixo |
| **Endividados Moderados** | R$ 320,13 | 10.38% | :x: Abaixo |
| **Poupadores** | R$ 120,90 | 1.72% | :x: Abaixo |

#### Analise

- **Cluster 0 (Endividados Severos)** atingiu o target com 19.22% de economia
- Clusters 1, 2 e 3 ficaram abaixo do target minimo de 15%
- Economia media geral de 8.11% insuficiente para validar H1 globalmente
- Impacto financeiro total ainda significativo: R$ 135k/mes para 500 usuarios

---

### H6: Deteccao de Anomalias com Isolation Forest

**Target:** Precision >0.85 e Recall >0.80
**Resultado:** Precision 47.3%, Recall 47.4%
**Status:** :x: **NAO VALIDADA**

#### Metricas Detalhadas

| Metrica | Valor | Target | Status |
|---------|-------|--------|--------|
| Precision | 0.4732 | > 0.85 | :x: Nao atingido |
| Recall | 0.4736 | > 0.80 | :x: Nao atingido |
| F1-Score | 0.4734 | - | - |
| Specificity | 0.9723 | - | - |

#### Matriz de Confusao

|  | Pred Normal | Pred Anomalia |
|--|-------------|---------------|
| **Real Normal** | 176.645 | 5.036 |
| **Real Anomalia** | 5.027 | 4.523 |

#### Analise

- O modelo detecta anomalias com ~47% de acuracia
- Alta especificidade (97.2%) - bom em identificar transacoes normais
- O ground truth sintetico (5% aleatorio) dificulta a deteccao baseada em padroes
- Recomendacao: revisar geracao de anomalias no dataset para Sprint 3

---

## Entregas Concluidas

### Notebooks (6/6)

| Notebook | Descricao | Status |
|----------|-----------|--------|
| 07_Recomendacoes_Sistema.ipynb | Sistema de regras por cluster | :white_check_mark: |
| 08_Recomendacoes_Economia.ipynb | Calculo de economia projetada | :white_check_mark: |
| 09_Anomalias_Treino.ipynb | Treinamento Isolation Forest | :white_check_mark: |
| 10_Anomalias_Validacao.ipynb | Validacao H6 | :white_check_mark: |
| 11_Pipeline_Integrado.ipynb | Pipeline end-to-end | :white_check_mark: |
| 12_Demonstracao.ipynb | Demonstracao do sistema | :white_check_mark: |

### Modelos e Artefatos

| Arquivo | Descricao | Status |
|---------|-----------|--------|
| `models/recomendacoes_regras.json` | 8 regras (2 por cluster) | :white_check_mark: |
| `models/isolation_forest.pkl` | Detector de anomalias | :white_check_mark: |
| `models/scaler_anomalias.pkl` | Scaler para features de anomalias | :white_check_mark: |
| `models/stats_categoria_anomalias.csv` | Estatisticas por categoria | :white_check_mark: |
| `models/config_anomalias.json` | Configuracao do modelo | :white_check_mark: |
| `models/pipeline_completo.pkl` | Pipeline integrado | :white_check_mark: |
| `models/config_pipeline.json` | Configuracao do pipeline | :white_check_mark: |

### Datasets Gerados

| Arquivo | Linhas | Descricao |
|---------|--------|-----------|
| `economia_projetada.csv` | 500 | Economia por usuario |
| `transacoes_com_anomalias_pred.csv` | 191.231 | Transacoes com predicoes |
| `pipeline_teste_resultados.csv` | 10 | Resultados de teste |

### Visualizacoes

- `outputs/economia_por_cluster.png`
- `outputs/distribuicao_economia_cluster.png`
- `outputs/poupanca_atual_vs_projetada.png`
- `outputs/economia_por_recomendacao.png`
- `outputs/anomalias_distribuicao.png`
- `outputs/matriz_confusao_anomalias.png`
- `outputs/validacao_h6_*.png` (3 arquivos)
- `outputs/pipeline_resultados_teste.png`
- `outputs/demo_cluster_*.png` (4 arquivos)
- `outputs/demo_comparativo_perfis.png`

### Documentacao

- `outputs/validacao_h1.md`
- `outputs/validacao_h6.md`
- `outputs/metricas_anomalias.csv`
- `outputs/Sprint2_Review.md` (este documento)
- `outputs/Sprint2_Resumo.md`

---

## Pipeline Integrado

### Funcao Principal

```python
resultado = pipeline.analisar_usuario(user_id, transacoes)
```

### Retorno

```python
{
    'user_id': str,
    'perfil': {
        'cluster': int,
        'cluster_nome': str,
        'prioridade': str,
        'confianca': float
    },
    'financeiro': {
        'renda_media': float,
        'gasto_medio': float,
        'taxa_poupanca': float,
        'pct_essenciais': float
    },
    'recomendacoes': [
        {'titulo': str, 'economia_potencial': float, 'dica': str},
        {'titulo': str, 'economia_potencial': float, 'dica': str}
    ],
    'economia': {
        'total_mensal': float,
        'pct_da_renda': float
    },
    'anomalias': {
        'total_anomalias': int,
        'transacoes_anomalas': list
    }
}
```

### Performance

- Tempo medio por usuario: ~0.05 segundos
- Throughput: ~20 usuarios/segundo
- Reproducibilidade: 100% (3 execucoes identicas)

---

## Impacto de Negocio

### Economia Projetada

| Metrica | Valor |
|---------|-------|
| Total Mensal | R$ 135.972,17 |
| Total Anual | R$ 1.631.666,04 |
| Media por Usuario | R$ 271,94/mes |

### Melhoria na Taxa de Poupanca

| Cluster | Taxa Atual | Taxa Projetada | Melhoria |
|---------|------------|----------------|----------|
| Endividados Severos | -88.6% | -81.7% | +6.9pp |
| Em Alerta | -14.8% | -9.4% | +5.4pp |
| Endividados Moderados | -57.7% | -48.3% | +9.4pp |
| Poupadores | 25.4% | 27.1% | +1.7pp |

---

## Licoes Aprendidas

### O que funcionou bem

1. **Pipeline modular:** Facilita manutencao e testes
2. **Regras por cluster:** Recomendacoes personalizadas e acionaveis
3. **Dashboard de demonstracao:** Visualizacao clara do valor entregue
4. **Documentacao continua:** Facilita handoff para Sprint 3

### Desafios enfrentados

1. **H1 parcialmente atingida:** Apenas Cluster 0 atingiu target
2. **H6 nao atingida:** Anomalias sinteticas aleatorias dificultam deteccao
3. **Ground truth sintetico:** Nao reflete padroes reais de anomalias

### Recomendacoes para Sprint 3

1. **Ajustar regras de economia:** Aumentar agressividade para clusters 1-3
2. **Revisar geracao de anomalias:** Criar padroes detectaveis (outliers reais)
3. **Dashboard interativo:** Permitir exploracao dos dados pelo usuario
4. **API REST:** Expor pipeline como servico web

---

## Criterios de Sucesso (Final)

| Criterio | Target | Resultado | Status |
|----------|--------|-----------|--------|
| H1 Validada | 15-20% economia | 8.11% (19.22% Cluster 0) | :yellow_circle: Parcial |
| H6 Validada | Precision >0.85 | 47.3% | :x: Nao atingido |
| H6 Validada | Recall >0.80 | 47.4% | :x: Nao atingido |
| Pipeline Funcional | Sim | Sim | :white_check_mark: Atingido |
| Notebooks Executaveis | 6 novos | 6 completos | :white_check_mark: Atingido |
| Modelos Salvos | 3+ novos | 7 novos | :white_check_mark: Atingido |
| Demonstracao | 4 perfis | 4 perfis | :white_check_mark: Atingido |

---

## Handoff para Sprint 3

### Artefatos Prontos

- Pipeline completo funcional (`pipeline_completo.pkl`)
- Sistema de recomendacoes (8 regras)
- Detector de anomalias (precisa refinamento)
- Dashboards de demonstracao

### Tarefas Prioritarias Sprint 3

1. **Dia 15-16:** Dashboard Streamlit
2. **Dia 17-18:** Refinamento H1 (ajustar regras)
3. **Dia 19-20:** Documentacao final + apresentacao
4. **Dia 21:** Review e entrega

### Dependencias

- Streamlit instalado
- Pipeline pkl carregavel
- Dados de teste disponiveis

---

## Conclusao

**Sprint 2 CONCLUIDO com sucesso parcial:**

- :white_check_mark: 6 notebooks desenvolvidos e executados
- :white_check_mark: Pipeline integrado funcional
- :white_check_mark: Sistema de recomendacoes implementado
- :yellow_circle: H1 parcialmente validada (Cluster 0 OK)
- :x: H6 nao validada (necessita revisao do dataset)

**Recomendacao:** Prosseguir para Sprint 3 focando no Dashboard e refinamento das hipoteses.

---

**Documento atualizado em:** 27 de Janeiro de 2026
**Versao:** 2.0 (Final)
**Status:** Aprovado
**Proximo:** Sprint 3 - Dashboard e Integracao
