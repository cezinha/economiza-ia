# Sprint 2 - Planejamento Reformulado
## Economiza+ MVP - Recomendacoes e Deteccao de Anomalias

**Periodo:** Janeiro 2026
**Duracao:** 7 dias
**Foco:** Validacao das hipoteses H1 e H6

---

## Objetivos do Sprint

| Hipotese | Descricao | Target | Entregavel |
|----------|-----------|--------|------------|
| H1 | Recomendacoes geram economia real | 15-20% reducao | Sistema de 2 regras por cluster |
| H6 | Isolation Forest detecta anomalias | Precision >0.85, Recall >0.80 | Detector global treinado |

---

## Restricoes (Pre-definidas)

- **Recomendacoes:** Exatamente 2 regras por cluster (total: 8 regras)
- **Anomalias:** Isolation Forest global (nao por categoria)
- **Ambiente:** Google Colab
- **Dados:** Dataset sintetico (LGPD)

---

## Backlog Sprint 2

### Dia 8: Sistema de Recomendacoes - Estrutura
**Notebook:** `07_Recomendacoes_Sistema.ipynb`

- [ ] Carregar `usuarios_clustered.csv` e `transacoes.csv`
- [ ] Definir 2 regras de recomendacao por cluster:
  - **Cluster 0 (Endividados Severos):**
    1. Cortar Alimentacao_Fora em 70% (economia: ~R$ 288/mes)
    2. Eliminar Vestuario nao essencial (economia: ~R$ 150/mes)
  - **Cluster 1 (Em Alerta):**
    1. Reduzir Alimentacao_Fora em 40% (economia: ~R$ 165/mes)
    2. Limitar Lazer a R$ 100/mes (economia: ~R$ 55/mes)
  - **Cluster 2 (Endividados Moderados):**
    1. Reduzir Alimentacao_Fora em 50% (economia: ~R$ 206/mes)
    2. Cortar Vestuario em 50% (economia: ~R$ 99/mes)
  - **Cluster 3 (Poupadores):**
    1. Otimizar gastos com Transporte (economia: ~R$ 50/mes)
    2. Revisar assinaturas em Telecomunicacoes (economia: ~R$ 30/mes)
- [ ] Criar funcao `gerar_recomendacoes(user_id, cluster)` -> lista de 2 recomendacoes
- [ ] Salvar regras em `models/recomendacoes_regras.json`

### Dia 9: Sistema de Recomendacoes - Calculo de Economia
**Notebook:** `08_Recomendacoes_Economia.ipynb`

- [ ] Calcular economia potencial por usuario aplicando as regras
- [ ] Criar DataFrame `economia_projetada.csv`:
  - user_id, cluster, recomendacao_1, economia_1, recomendacao_2, economia_2, total_economia
- [ ] Validar H1: % de economia media por cluster
- [ ] Gerar visualizacao: economia potencial por cluster
- [ ] Documentar resultado da validacao H1

### Dia 10: Deteccao de Anomalias - Treino
**Notebook:** `09_Anomalias_Treino.ipynb`

- [ ] Carregar `transacoes.csv`
- [ ] Filtrar apenas gastos (excluir Renda)
- [ ] Preparar features para Isolation Forest:
  - `valor` (principal)
  - `valor_normalizado_por_categoria` (valor / media_categoria)
- [ ] Treinar Isolation Forest global:
  - contamination=0.05 (5% anomalias conhecidas)
  - random_state=42
- [ ] Salvar modelo: `models/isolation_forest.pkl`
- [ ] Gerar predicoes para todo o dataset

### Dia 11: Deteccao de Anomalias - Validacao
**Notebook:** `10_Anomalias_Validacao.ipynb`

- [ ] Comparar predicoes com `is_anomalia` (ground truth)
- [ ] Calcular metricas H6:
  - Precision (target: >0.85)
  - Recall (target: >0.80)
  - F1-Score
  - Matriz de confusao
- [ ] Se metricas abaixo do target:
  - Ajustar contamination
  - Testar features adicionais
- [ ] Documentar resultado da validacao H6
- [ ] Salvar metricas: `outputs/metricas_anomalias.csv`

### Dia 12: Integracao - Pipeline Unificado
**Notebook:** `11_Pipeline_Integrado.ipynb`

- [ ] Criar pipeline end-to-end:
  1. Entrada: dados de um novo usuario
  2. Normalizar features (scaler.pkl)
  3. Classificar em cluster (kmeans_best.pkl)
  4. Gerar 2 recomendacoes (recomendacoes_regras.json)
  5. Detectar anomalias nas transacoes (isolation_forest.pkl)
  6. Saida: perfil + recomendacoes + alertas
- [ ] Criar funcao `analisar_usuario(user_id)` -> dict completo
- [ ] Testar com 10 usuarios de diferentes clusters
- [ ] Salvar pipeline: `models/pipeline_completo.pkl`

### Dia 13: Demonstracao e Testes
**Notebook:** `12_Demonstracao.ipynb`

- [ ] Criar notebook de demonstracao executavel
- [ ] Demonstrar fluxo completo para 1 usuario de cada cluster
- [ ] Gerar visualizacoes finais:
  - Perfil do usuario
  - Recomendacoes personalizadas
  - Alertas de anomalias
- [ ] Validar reproducibilidade (executar do zero)

### Dia 14: Documentacao e Review
**Entregas:**

- [ ] `outputs/Sprint2_Review.md` - Resumo executivo
- [ ] `outputs/Sprint2_Resumo.md` - Documentacao tecnica completa
- [ ] Atualizar `CLAUDE.md` com novos modelos e notebooks
- [ ] Checklist de validacao H1 e H6
- [ ] Preparar handoff para Sprint 3 (Dashboard)

---

## Artefatos Esperados

### Modelos
- `models/recomendacoes_regras.json`
- `models/isolation_forest.pkl`
- `models/pipeline_completo.pkl`

### Datasets
- `data/processed/economia_projetada.csv`
- `data/processed/transacoes_com_anomalias_pred.csv`

### Notebooks
- `07_Recomendacoes_Sistema.ipynb`
- `08_Recomendacoes_Economia.ipynb`
- `09_Anomalias_Treino.ipynb`
- `10_Anomalias_Validacao.ipynb`
- `11_Pipeline_Integrado.ipynb`
- `12_Demonstracao.ipynb`

### Documentacao
- `outputs/Sprint2_Review.md`
- `outputs/Sprint2_Resumo.md`
- `outputs/metricas_anomalias.csv`

---

## Criterios de Sucesso

| Criterio | Target | Como Medir |
|----------|--------|------------|
| H1 Validada | 15-20% economia | Media de economia_total / renda por cluster |
| H6 Validada | Precision >0.85 | Comparar predicoes vs is_anomalia |
| H6 Validada | Recall >0.80 | Comparar predicoes vs is_anomalia |
| Pipeline Funcional | Sim | Executar para usuarios de teste |
| Notebooks Executaveis | 6 novos | Todos rodam sem erro |
| Modelos Salvos | 3 novos | Arquivos .pkl e .json criados |

---

## Dependencias do Sprint 1

Artefatos necessarios (ja existem):
- [x] `data/processed/usuarios_clustered.csv`
- [x] `data/processed/features_clustering.csv`
- [x] `models/kmeans_best.pkl`
- [x] `models/scaler.pkl`
- [x] `outputs/transacoes.csv` (com is_anomalia)

---

## Riscos e Mitigacoes

| Risco | Probabilidade | Mitigacao |
|-------|---------------|-----------|
| H6 nao atingir Precision >0.85 | Media | Ajustar contamination, adicionar features |
| H1 economia < 15% | Baixa | Regras ja baseadas em analise do Sprint 1 |
| Tempo insuficiente para integracao | Baixa | Dia 12-13 tem buffer |

---

## Notas

- Manter simplicidade: 2 regras por cluster, nao mais
- Isolation Forest global para facilitar manutencao
- Documentar decisoes e justificativas
- Priorizar entrega funcional sobre otimizacao prematura

---

**Documento criado em:** 26 de Janeiro de 2026
**Versao:** 1.0
**Status:** Aprovado para execucao
