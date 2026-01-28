# Sprint 2 - Documentacao Tecnica Completa
## Economiza+ MVP - Sistema de Recomendacoes e Deteccao de Anomalias

**Periodo:** 26-27 de Janeiro de 2026
**Duracao:** 7 dias (Dias 8-14)
**Status:** CONCLUIDO

---

## Indice

1. [Visao Geral](#visao-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Sistema de Recomendacoes](#sistema-de-recomendacoes)
4. [Deteccao de Anomalias](#deteccao-de-anomalias)
5. [Pipeline Integrado](#pipeline-integrado)
6. [Validacao das Hipoteses](#validacao-das-hipoteses)
7. [Artefatos Gerados](#artefatos-gerados)
8. [Guia de Uso](#guia-de-uso)
9. [Proximos Passos](#proximos-passos)

---

## Visao Geral

### Objetivos do Sprint

| Hipotese | Descricao | Target | Resultado | Status |
|----------|-----------|--------|-----------|--------|
| H1 | Recomendacoes geram economia | 15-20% | 8.11% (19.22% Cluster 0) | Parcial |
| H6 | Isolation Forest detecta anomalias | P>0.85, R>0.80 | P=47.3%, R=47.4% | Nao validada |

### Escopo Entregue

- **Recomendacoes:** 8 regras (2 por cluster) com calculo de economia
- **Anomalias:** Isolation Forest global treinado e validado
- **Pipeline:** Sistema end-to-end funcional
- **Demonstracao:** Dashboards para todos os perfis

---

## Arquitetura do Sistema

### Estrutura de Arquivos (Sprint 2)

```
economiza-ia/
├── notebooks/
│   ├── 07_Recomendacoes_Sistema.ipynb     # Sistema de regras
│   ├── 08_Recomendacoes_Economia.ipynb    # Calculo de economia
│   ├── 09_Anomalias_Treino.ipynb          # Treino Isolation Forest
│   ├── 10_Anomalias_Validacao.ipynb       # Validacao H6
│   ├── 11_Pipeline_Integrado.ipynb        # Pipeline end-to-end
│   └── 12_Demonstracao.ipynb              # Demonstracao visual
│
├── models/
│   ├── kmeans_best.pkl                    # [Sprint 1] K-means K=4
│   ├── scaler.pkl                         # [Sprint 1] StandardScaler
│   ├── recomendacoes_regras.json          # [Novo] 8 regras
│   ├── isolation_forest.pkl               # [Novo] Detector anomalias
│   ├── scaler_anomalias.pkl               # [Novo] Scaler anomalias
│   ├── stats_categoria_anomalias.csv      # [Novo] Stats por categoria
│   ├── config_anomalias.json              # [Novo] Config modelo
│   ├── pipeline_completo.pkl              # [Novo] Pipeline integrado
│   └── config_pipeline.json               # [Novo] Config pipeline
│
├── data/processed/
│   ├── usuarios_clustered.csv             # [Sprint 1] 500 usuarios
│   ├── features_clustering.csv            # [Sprint 1] 5 features
│   ├── economia_projetada.csv             # [Novo] Economia por usuario
│   └── transacoes_com_anomalias_pred.csv  # [Novo] Predicoes anomalias
│
└── outputs/
    ├── validacao_h1.md                    # Validacao H1
    ├── validacao_h6.md                    # Validacao H6
    ├── metricas_anomalias.csv             # Metricas H6
    ├── Sprint2_Review.md                  # Review executivo
    ├── Sprint2_Resumo.md                  # Este documento
    ├── demo_cluster_*.png                 # Dashboards por cluster
    └── demo_comparativo_perfis.png        # Comparativo
```

### Fluxo de Dados

```
[Transacoes] ──> [Features] ──> [K-means] ──> [Cluster]
                                    │
                                    v
                            [Recomendacoes] ──> [Economia]
                                    │
                                    v
                            [Isolation Forest] ──> [Anomalias]
                                    │
                                    v
                              [Pipeline Output]
```

---

## Sistema de Recomendacoes

### Regras por Cluster

#### Cluster 0: Endividados Severos (Prioridade CRITICA)

| ID | Categoria | Acao | Reducao | Economia Media |
|----|-----------|------|---------|----------------|
| R0_1 | Alimentacao_Fora | Cortar | 70% | R$ 288/mes |
| R0_2 | Vestuario | Eliminar nao essencial | 90% | R$ 150/mes |

#### Cluster 1: Em Alerta (Prioridade MODERADA)

| ID | Categoria | Acao | Reducao | Economia Media |
|----|-----------|------|---------|----------------|
| R1_1 | Alimentacao_Fora | Reduzir | 40% | R$ 165/mes |
| R1_2 | Lazer | Limitar | 35% | R$ 55/mes |

#### Cluster 2: Endividados Moderados (Prioridade ALTA)

| ID | Categoria | Acao | Reducao | Economia Media |
|----|-----------|------|---------|----------------|
| R2_1 | Alimentacao_Fora | Reduzir | 50% | R$ 206/mes |
| R2_2 | Vestuario | Cortar | 50% | R$ 99/mes |

#### Cluster 3: Poupadores (Prioridade BAIXA)

| ID | Categoria | Acao | Reducao | Economia Media |
|----|-----------|------|---------|----------------|
| R3_1 | Transporte | Otimizar | 15% | R$ 50/mes |
| R3_2 | Telecomunicacoes | Revisar | 20% | R$ 30/mes |

### Calculo de Economia

```python
# Para cada usuario
gasto_categoria = transacoes[categoria].sum() / n_meses
economia_regra = gasto_categoria * percentual_reducao
economia_total = economia_regra_1 + economia_regra_2
pct_economia = economia_total / renda_media * 100
```

### Resultados por Cluster

| Cluster | N | Economia Media | % Renda | Target |
|---------|---|----------------|---------|--------|
| Endividados Severos | 59 | R$ 698,53 | 19.22% | OK |
| Em Alerta | 196 | R$ 162,59 | 5.37% | Abaixo |
| Endividados Moderados | 167 | R$ 320,13 | 10.38% | Abaixo |
| Poupadores | 78 | R$ 120,90 | 1.72% | Abaixo |
| **TOTAL** | **500** | **R$ 271,94** | **8.11%** | **Parcial** |

---

## Deteccao de Anomalias

### Modelo: Isolation Forest

**Parametros:**

| Parametro | Valor | Justificativa |
|-----------|-------|---------------|
| contamination | 0.05 | 5% anomalias no dataset |
| n_estimators | 100 | Balanco performance/precisao |
| random_state | 42 | Reproducibilidade |

**Features:**

| Feature | Descricao | Formula |
|---------|-----------|---------|
| feat_valor_norm | Z-score por categoria | (valor - media_cat) / std_cat |
| feat_ratio_mediana | Ratio vs mediana | valor / mediana_cat |

### Resultados da Validacao

| Metrica | Valor | Target | Status |
|---------|-------|--------|--------|
| Precision | 0.4732 | > 0.85 | Nao atingido |
| Recall | 0.4736 | > 0.80 | Nao atingido |
| F1-Score | 0.4734 | - | - |
| Specificity | 0.9723 | - | - |

### Matriz de Confusao

```
                    Pred Normal    Pred Anomalia
Real Normal         176.645        5.036
Real Anomalia       5.027          4.523

True Positives:  4.523 (anomalias corretamente detectadas)
False Positives: 5.036 (normais marcadas como anomalia)
False Negatives: 5.027 (anomalias nao detectadas)
True Negatives:  176.645 (normais corretamente identificadas)
```

### Analise do Resultado

O modelo nao atingiu os targets por uma razao fundamental: **as anomalias no dataset sintetico sao marcadas aleatoriamente (5% de cada categoria)**, sem padroes reais de valores atipicos.

O Isolation Forest detecta **outliers estatisticos**, mas o ground truth foi gerado aleatoriamente, nao baseado em valores extremos. Isso explica a performance proxima a aleatorio (~47%).

**Recomendacao:** Revisar a geracao de anomalias no dataset para criar outliers detectaveis (ex: valores > 3 std da media).

---

## Pipeline Integrado

### Classe EconomizaPipeline

```python
class EconomizaPipeline:
    def __init__(self, kmeans_model, scaler_clustering, regras_recomendacao,
                 isolation_forest, scaler_anomalias, stats_categoria):
        # Inicializa todos os componentes

    def calcular_features_usuario(self, transacoes_usuario) -> Dict:
        # Calcula 5 features de clustering

    def classificar_cluster(self, features) -> Dict:
        # Classifica usuario em cluster

    def gerar_recomendacoes(self, cluster, transacoes_usuario) -> List[Dict]:
        # Gera 2 recomendacoes personalizadas

    def detectar_anomalias(self, transacoes_usuario, top_n=5) -> Dict:
        # Detecta transacoes atipicas

    def analisar_usuario(self, user_id, transacoes_df) -> Dict:
        # Analise completa (funcao principal)
```

### Funcao Principal

```python
# Uso
resultado = pipeline.analisar_usuario('user_0001', transacoes)

# Retorno
{
    'user_id': 'user_0001',
    'data_analise': '2026-01-27 15:30:00',
    'perfil': {
        'cluster': 3,
        'cluster_nome': 'Poupadores',
        'prioridade': 'BAIXA',
        'confianca': 0.8523
    },
    'financeiro': {
        'renda_media': 6500.00,
        'gasto_medio': 4800.00,
        'taxa_poupanca': 26.15,
        'pct_essenciais': 45.2,
        'variabilidade': 1250.00
    },
    'recomendacoes': [
        {
            'titulo': 'Otimizar gastos com transporte',
            'categoria': 'Transporte',
            'gasto_atual': 450.00,
            'economia_potencial': 67.50,
            'dica': 'Considere caronas ou transporte publico'
        },
        {
            'titulo': 'Revisar planos e assinaturas',
            'categoria': 'Telecomunicacoes',
            'gasto_atual': 180.00,
            'economia_potencial': 36.00,
            'dica': 'Cancele assinaturas nao utilizadas'
        }
    ],
    'economia': {
        'total_mensal': 103.50,
        'pct_da_renda': 1.59
    },
    'anomalias': {
        'total_anomalias': 3,
        'total_transacoes': 156,
        'pct_anomalias': 1.92,
        'transacoes_anomalas': [...]
    }
}
```

### Performance

| Metrica | Valor |
|---------|-------|
| Tempo por usuario | ~0.05s |
| Throughput | ~20 usuarios/s |
| Reproducibilidade | 100% |

---

## Validacao das Hipoteses

### H1: Recomendacoes Geram Economia Real

**Status: PARCIALMENTE VALIDADA**

| Aspecto | Resultado |
|---------|-----------|
| Media geral | 8.11% (abaixo do target 15-20%) |
| Cluster 0 | 19.22% (ATINGIU target) |
| Clusters 1-3 | 1.7% - 10.4% (abaixo do target) |
| Impacto total | R$ 135.972/mes (500 usuarios) |

**Conclusao:** A hipotese foi parcialmente validada. O sistema funciona e gera economia mensuravel, mas apenas o Cluster 0 (Endividados Severos) atingiu o target de 15-20%.

### H6: Isolation Forest Detecta Anomalias

**Status: NAO VALIDADA**

| Metrica | Target | Resultado |
|---------|--------|-----------|
| Precision | > 0.85 | 0.4732 |
| Recall | > 0.80 | 0.4736 |

**Conclusao:** A hipotese nao foi validada. A causa raiz e a geracao aleatoria de anomalias no dataset sintetico, que nao cria padroes estatisticos detectaveis.

---

## Artefatos Gerados

### Modelos (.pkl e .json)

| Arquivo | Tamanho | Descricao |
|---------|---------|-----------|
| recomendacoes_regras.json | 3 KB | 8 regras de economia |
| isolation_forest.pkl | 1.2 MB | Detector de anomalias |
| scaler_anomalias.pkl | 1 KB | Normalizador |
| pipeline_completo.pkl | 1.5 MB | Pipeline integrado |
| config_*.json | 1 KB | Configuracoes |

### Datasets (.csv)

| Arquivo | Linhas | Colunas | Descricao |
|---------|--------|---------|-----------|
| economia_projetada.csv | 500 | 19 | Economia por usuario |
| transacoes_com_anomalias_pred.csv | 191.231 | 10 | Predicoes |
| pipeline_teste_resultados.csv | 10 | 10 | Testes |

### Visualizacoes (.png)

| Arquivo | Tipo |
|---------|------|
| economia_por_cluster.png | Barplot |
| distribuicao_economia_cluster.png | Boxplot |
| poupanca_atual_vs_projetada.png | Comparativo |
| matriz_confusao_anomalias.png | Heatmap |
| validacao_h6_*.png | Analises H6 |
| demo_cluster_*.png | Dashboards |
| demo_comparativo_perfis.png | Comparativo |

---

## Guia de Uso

### Carregar Pipeline

```python
import pickle
import pandas as pd

# Carregar pipeline
with open('models/pipeline_completo.pkl', 'rb') as f:
    pipeline_data = pickle.load(f)

# Carregar dados
transacoes = pd.read_csv('data/raw/transacoes.csv')

# Instanciar pipeline
from economiza_pipeline import EconomizaPipeline
pipeline = EconomizaPipeline(**pipeline_data['componentes'])
```

### Analisar Usuario

```python
# Analise completa
resultado = pipeline.analisar_usuario('user_0001', transacoes)

# Acessar componentes
print(f"Perfil: {resultado['perfil']['cluster_nome']}")
print(f"Economia: R$ {resultado['economia']['total_mensal']:.2f}/mes")
print(f"Anomalias: {resultado['anomalias']['total_anomalias']}")
```

### Executar em Lote

```python
usuarios = ['user_0001', 'user_0002', 'user_0003']
resultados = [pipeline.analisar_usuario(u, transacoes) for u in usuarios]
```

---

## Proximos Passos

### Sprint 3 (Dias 15-21)

| Dia | Tarefa | Entregavel |
|-----|--------|------------|
| 15-16 | Dashboard Streamlit | App interativo |
| 17-18 | Refinamento H1 | Regras ajustadas |
| 19-20 | Documentacao final | README, apresentacao |
| 21 | Review e entrega | Projeto completo |

### Melhorias Sugeridas

1. **H1:** Aumentar agressividade das regras para clusters 1-3
2. **H6:** Gerar anomalias baseadas em outliers estatisticos
3. **Dashboard:** Interface web com Streamlit
4. **API:** Expor pipeline como servico REST

---

## Referencias

- [Sprint 1 Review](Sprint1_Review.md)
- [Sprint 1 Resumo](Sprint1_Resumo.md)
- [Validacao H1](validacao_h1.md)
- [Validacao H6](validacao_h6.md)
- [Planejamento Sprint 2](Sprint2_Planejamento.md)

---

**Documento atualizado em:** 27 de Janeiro de 2026
**Versao:** 2.0 (Final)
**Status:** Publicado
