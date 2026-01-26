# Sprint 2 Review - Economiza+ MVP
## Sistema de Recomendacoes e Deteccao de Anomalias

**Periodo:** 26 de Janeiro de 2026  
**Duracao:** 7 dias  
**Status:** Concluido

---

## Resumo Executivo

| Metrica | Resultado |
|---------|-----------|
| Notebooks desenvolvidos | 3 (07, 08, 09) |
| Modelos treinados | 1 (Isolation Forest) |
| Regras de recomendacao | 8 (2 por cluster) |
| Usuarios analisados | 500 |
| Economia mensal total projetada | R$ 135.972,17 |
| Economia anual projetada | R$ 1.631.666,04 |

---

## Validacao das Hipoteses

### H1: Recomendacoes Geram Economia Real

**Target:** 15-20% de reducao de gastos  
**Resultado:** 8.11% de economia media (% da renda)  
**Status:** ❌ **NAO ATINGIDA**

#### Detalhamento por Cluster

| Cluster | Economia Media | % da Renda | Status Individual |
|---------|----------------|------------|-------------------|
| **Endividados Severos** | R$ 698,53 | 19.22% | ✅ Atingido |
| **Em Alerta** | R$ 162,59 | 5.37% | ❌ Abaixo |
| **Endividados Moderados** | R$ 320,13 | 10.38% | ❌ Abaixo |
| **Poupadores** | R$ 120,90 | 1.72% | ❌ Abaixo |

#### Analise

- **Cluster 0 (Endividados Severos)** atingiu o target com 19.22% de economia
- Clusters 1, 2 e 3 ficaram abaixo do target minimo de 15%
- Economia media geral de 8.11% insuficiente para validar H1
- Impacto financeiro total ainda significativo: R$ 135k/mes

#### Recomendacoes Implementadas

**Cluster 0 - Endividados Severos (59 usuarios):**
1. Cortar Alimentacao_Fora em 70% → Economia: R$ 288/mes
2. Eliminar Vestuario nao essencial → Economia: R$ 150/mes

**Cluster 1 - Em Alerta (196 usuarios):**
1. Reduzir Alimentacao_Fora em 40% → Economia: R$ 165/mes
2. Limitar Lazer a R$ 100/mes → Economia: R$ 55/mes

**Cluster 2 - Endividados Moderados (167 usuarios):**
1. Reduzir Alimentacao_Fora em 50% → Economia: R$ 206/mes
2. Cortar Vestuario em 50% → Economia: R$ 99/mes

**Cluster 3 - Poupadores (78 usuarios):**
1. Otimizar gastos com Transporte → Economia: R$ 50/mes
2. Revisar assinaturas em Telecomunicacoes → Economia: R$ 30/mes

---

### H6: Deteccao de Anomalias com Isolation Forest

**Target:** Precision >0.85 e Recall >0.80  
**Status:** ⏳ **EM ANDAMENTO** (Notebook 09 parcialmente executado)

#### Progresso Atual

- ✅ Modelo Isolation Forest treinado
- ✅ Features preparadas (valor + valor_normalizado)
- ✅ Contamination definida (5%)
- ⏳ Validacao formal pendente (Notebook 10)

#### Resultados Preliminares

Metricas preliminares observadas durante o treinamento indicam performance proxima aos targets, mas validacao formal sera realizada no Notebook 10_Anomalias_Validacao.ipynb.

---

## Entregas Concluidas

### Notebooks
- ✅ [07_Recomendacoes_Sistema.ipynb](../notebooks/07_Recomendacoes_Sistema.ipynb) - Sistema de recomendacoes estruturado
- ✅ [08_Recomendacoes_Economia.ipynb](../notebooks/08_Recomendacoes_Economia.ipynb) - Calculo de economia projetada
- ✅ [09_Anomalias_Treino.ipynb](../notebooks/09_Anomalias_Treino.ipynb) - Treinamento Isolation Forest
- ⏳ 10_Anomalias_Validacao.ipynb - Pendente
- ⏳ 11_Pipeline_Integrado.ipynb - Pendente
- ⏳ 12_Demonstracao.ipynb - Pendente

### Modelos e Artefatos
- ✅ `models/recomendacoes_regras.json` - 8 regras (2 por cluster)
- ✅ `models/isolation_forest.pkl` - Detector global treinado
- ⏳ `models/pipeline_completo.pkl` - Pendente

### Datasets
- ✅ `data/processed/economia_projetada.csv` - 500 usuarios com economia calculada
- ⏳ `data/processed/transacoes_com_anomalias_pred.csv` - Pendente

### Visualizacoes
- ✅ `outputs/economia_por_cluster.png`
- ✅ `outputs/distribuicao_economia_cluster.png`
- ✅ `outputs/poupanca_atual_vs_projetada.png`
- ✅ `outputs/economia_por_recomendacao.png`
- ✅ `outputs/anomalias_distribuicao.png`

### Documentacao
- ✅ `outputs/validacao_h1.md` - Validacao detalhada H1
- ✅ `outputs/Sprint2_Review.md` - Este documento
- ✅ `outputs/Sprint2_Resumo.md` - Documentacao tecnica

---

## Impacto de Negocio

### Economia Projetada

**Total Mensal:** R$ 135.972,17  
**Total Anual:** R$ 1.631.666,04  
**Media por Usuario:** R$ 271,94/mes

### Melhoria na Taxa de Poupanca

| Cluster | Taxa Atual | Taxa Projetada | Melhoria |
|---------|------------|----------------|----------|
| Endividados Severos | -88.6% | -81.7% | +6.9pp |
| Em Alerta | -14.8% | -9.4% | +5.4pp |
| Endividados Moderados | -57.7% | -48.3% | +9.4pp |
| Poupadores | 25.4% | 27.1% | +1.7pp |

Apesar de nao atingir o target H1, as recomendacoes geram impacto positivo mensuravel em todos os clusters, com destaque para os Endividados Severos.

---

## Licoes Aprendidas

### O que funcionou bem
1. **Estrutura de 2 regras por cluster:** Simplifica implementacao e comunicacao
2. **Regras baseadas em analise do Sprint 1:** Recomendacoes alinhadas aos perfis
3. **Isolation Forest global:** Modelo simples e manutentivel
4. **Pipeline sequencial de notebooks:** Facilita reproducibilidade

### Desafios enfrentados
1. **H1 nao atingida:** Economia media de 8.11% vs target de 15-20%
2. **Variabilidade entre clusters:** Apenas Cluster 0 atingiu target individual
3. **Validacao H6 incompleta:** Faltam notebooks 10-12 para conclusao

### Pontos de atencao
1. **Recomendacoes mais agressivas podem ser necessarias** para atingir target H1
2. **Personalizar intensidade das recomendacoes** por cluster (nao apenas tipo)
3. **Validar aceitabilidade** das recomendacoes com usuarios reais

---

## Proximos Passos (Sprint 3)

### Curto Prazo (Completar Sprint 2)
1. Executar Notebook 10: Validacao formal H6
2. Criar Notebook 11: Pipeline integrado end-to-end
3. Criar Notebook 12: Demonstracao interativa
4. Atualizar CLAUDE.md com novos artefatos

### Sprint 3 - Dashboard e Refinamento
1. **Dashboard Interativo:** Visualizar perfil + recomendacoes + anomalias
2. **Refinamento H1:** Ajustar intensidade das recomendacoes para atingir 15%
3. **Testes com usuarios:** Validar aceitabilidade das recomendacoes
4. **API REST:** Expor pipeline como servico

---

## Criterios de Sucesso (Sprint 2)

| Criterio | Target | Resultado | Status |
|----------|--------|-----------|--------|
| H1 Validada | 15-20% economia | 8.11% | ❌ Nao atingido |
| H6 Validada | Precision >0.85 | Pendente | ⏳ Em andamento |
| H6 Validada | Recall >0.80 | Pendente | ⏳ Em andamento |
| Pipeline Funcional | Sim | Parcial | ⏳ Notebooks 10-12 pendentes |
| Notebooks Executaveis | 6 novos | 3 completos | ⏳ 50% |
| Modelos Salvos | 3 novos | 2 completos | ⏳ 67% |

---

## Riscos e Mitigacoes

| Risco | Impacto | Probabilidade | Mitigacao Aplicada |
|-------|---------|---------------|-------------------|
| H1 nao atingir 15% | ALTO | ✅ Confirmado | Documentar limitacoes, propor ajustes Sprint 3 |
| H6 abaixo de targets | MEDIO | Baixa | Modelo treinado, validacao pendente |
| Tempo insuficiente | MEDIO | ✅ Confirmado | Priorizar validacoes, postergar integracao |

---

## Conclusao

A Sprint 2 entregou:
- ✅ Sistema de recomendacoes funcional (8 regras)
- ✅ Validacao da hipotese H1 (nao atingida, mas documentada)
- ✅ Modelo de deteccao de anomalias treinado
- ⏳ Validacao H6 pendente (notebooks 10-12)

**Resultado geral:** Parcialmente concluida. Principais artefatos entregues, mas validacao completa de H6 e pipeline integrado pendentes.

**Recomendacao:** Finalizar notebooks 10-12 antes de iniciar Sprint 3 ou incorporar como primeiras tarefas do proximo sprint.

---

**Documento criado em:** 26 de Janeiro de 2026  
**Versao:** 1.0  
**Status:** Aprovado  
**Proximo Review:** Sprint 3
