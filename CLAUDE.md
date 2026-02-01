# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Economiza+ is a financial behavior analysis and segmentation system for Brazilian middle-to-lower-income families (classes C and D). The project uses machine learning to identify spending patterns, segment users into financial profiles, and provide personalized saving recommendations.

The project generates synthetic financial data based on Brazilian statistics (Serasa, CNC, IBGE, POF) and applies K-means clustering to identify 4 distinct user profiles ranging from "Endividados Severos" (-80% savings rate) to "Poupadores" (+26% savings rate).

## Academic Context

- **Course**: Data Science (XP Educação)
- **Advisor**: Marcos Prochnow
- **Duration**: 21 days (3 sprints × 7 days)

## Key Metrics Summary

| Metric | Value |
|--------|-------|
| Users analyzed | 500 |
| Transactions processed | 191,231 |
| Clusters identified | 4 |
| Users in financial risk | 386 (77.2%) |
| Average savings rate | -31.6% |
| Projected monthly savings | R$ 144,912 |
| Projected annual savings | R$ 1.74M |
| Pipeline throughput | ~20 users/second |

## Hypotheses and Validation Results

### H1: Economy Recommendations Generate Real Savings
| Metric | Target | Result | Status |
|--------|--------|--------|--------|
| Average economy (% income) | 15-20% | 8.60% | Below target |
| Cluster 2 (critical) economy | 15-20% | **17.56%** | Achieved |
| Median economy | 15-20% | 6.20% | Below target |

**Conclusion**: Partially validated. Aggressive rules work effectively for critical profiles (Cluster 2 - Endividados Severos).

### H2: K-means Clustering Identifies Distinct Profiles
| Metric | Target | Result | Status |
|--------|--------|--------|--------|
| Silhouette Score | > 0.50 | 0.267 | Below target |
| Davies-Bouldin Index | < 1.00 | 1.184 | Near target |
| PCA Variance (2D) | > 70% | 82.7% | Exceeded |
| Interpretability | High | High | Achieved |

**Conclusion**: Partially validated. Statistical metrics below ideal, but clusters are interpretable and actionable.

### H6: Isolation Forest Detects Anomalous Transactions
| Metric | Target | Result | Status |
|--------|--------|--------|--------|
| Precision | > 0.85 | 47.3% | Not achieved |
| Recall | > 0.80 | 47.4% | Not achieved |
| Specificity | - | 97.2% | Excellent |
| F1-Score | - | 47.3% | - |

**Conclusion**: Not validated due to dataset limitation (anomalies were generated randomly, not statistically).

## Sprint Structure

- **Sprint 1** (Days 1-7): EDA, Feature Engineering, Clustering - COMPLETED
- **Sprint 2** (Days 8-14): Recommendation system, Anomaly detection - COMPLETED
- **Sprint 3** (Days 15-21): Dashboard (Streamlit), Integration, Documentation - IN PROGRESS
  - Day 15: Dashboard structure and pages - COMPLETED
  - Day 16: Dashboard enhancements - IN PROGRESS

### Sprint 3 Roadmap

| Days | Task | Deliverable |
|------|------|-------------|
| 15-16 | Streamlit Dashboard | Interactive app |
| 17-18 | H1 Refinement | Adjusted rules |
| 19-20 | Final Documentation | Presentation |
| 21 | Review and Delivery | Complete project |

### Sprint 3 Risks and Mitigations

| Risk | Probability | Mitigation |
|------|-------------|------------|
| Insufficient time for full dashboard | Medium | Prioritize essential features |
| Streamlit deploy issues | Low | Test locally first |
| H1 not reaching global target | High | Document as known limitation |

### Key Commits (Evidence)

| Hash | Message | Description |
|------|---------|-------------|
| `25a2de0` | added Day 15 | Sprint 3 Dashboard implementation |
| `a352a7a` | updated version with fixes | Bug fixes (cluster names) |
| `a7db2d9` | Sprint 2 | Sprint 2 finalization |
| `286ef55` | sprint 2 dias 8, 9, 10 | Days 8-10 development |
| `34d976e` | updated clusters names | Fixed cluster naming bug |
| `7f62a10` | sprint days 5-7 | Sprint 1 interpretation and documentation |

## Constraints and Pre-defined Decisions

### Constraints
- No real user data (LGPD compliance) - synthetic data only
- Development environment: Google Colab (notebooks) / Local with pyenv (dashboard)
- 21-day deadline
- Python environment: `pyenv activate economiza-ia-env`

### Technical Decisions (Non-negotiable)
- **Clustering**: K-means (not DBSCAN)
- **Normalization**: StandardScaler
- **Features**: Exactly 5 clustering features
- **Recommendations**: 2 rule-based recommendations per cluster
- **Anomaly Detection**: Global Isolation Forest (not per-category)

## Commands

### Setup
```bash
pyenv activate economiza-ia-env
pip install -r requirements.txt
```

### Generate Synthetic Dataset
```bash
python scripts/gerar_dataset_financeiro.py
```
Outputs to `data/raw/`: `usuarios.csv`, `transacoes.csv`, `estatisticas_mensais.csv`

### Run Dashboard (Sprint 3)
```bash
cd app/
streamlit run app.py
# Access at http://localhost:8501
```

### Run Notebooks
Execute notebooks sequentially in Jupyter:

**Sprint 1:**
1. `notebooks/01_EDA_Basico.ipynb` - Exploratory data analysis
2. `notebooks/02_Feature_Engineering.ipynb` - Feature creation
3. `notebooks/03_Clustering.ipynb` - K-means clustering
4. `notebooks/04_Clustering_Validacao.ipynb` - Validation metrics
5. `notebooks/05_Interpretacao_Clusters.ipynb` - Cluster profiling
6. `notebooks/06_Recomendacoes_Review.ipynb` - Recommendations review

**Sprint 2:**
7. `notebooks/07_Recomendacoes_Sistema.ipynb` - Recommendation rules system
8. `notebooks/08_Recomendacoes_Economia.ipynb` - Economy calculation
9. `notebooks/09_Anomalias_Treino.ipynb` - Isolation Forest training
10. `notebooks/10_Anomalias_Validacao.ipynb` - H6 validation
11. `notebooks/11_Pipeline_Integrado.ipynb` - End-to-end pipeline
12. `notebooks/12_Demonstracao.ipynb` - System demonstration

## Architecture

### Data Flow
```
scripts/gerar_dataset_financeiro.py → data/raw/ → notebooks (processing) → data/processed/ → models/ → app/ (dashboard)
```

### Key Directories
- `data/raw/` - Raw CSVs (usuarios, transacoes, estatisticas_mensais)
- `data/processed/` - Engineered features and predictions
- `models/` - Trained models and configurations
- `outputs/` - Visualizations and documentation
- `app/` - Streamlit dashboard application (Sprint 3)
- `notebooks/` - Jupyter notebooks (12 total)
- `scripts/` - Data generation scripts

### Dataset Schema
- **usuarios.csv**: Demographics (user_id, idade, tipo_emprego, renda_base, estado_civil, num_dependentes, situacao_financeira, regiao)
- **transacoes.csv**: ~194K transactions with (user_id, data, categoria, valor, is_essencial, is_anomalia)
- **estatisticas_mensais.csv**: Monthly aggregations per user

### 5 Clustering Features

| Feature | Description | Min | Mean | Max | Std |
|---------|-------------|-----|------|-----|-----|
| `media_renda` | Average monthly income | R$ 1,500 | R$ 3,800 | R$ 12,000 | R$ 2,100 |
| `media_gasto` | Average monthly spending | R$ 1,800 | R$ 4,200 | R$ 9,500 | R$ 1,900 |
| `taxa_poupanca` | Savings rate: (renda - gasto) / renda | -96% | -31.6% | +67% | 42% |
| `pct_gastos_essenciais` | % spent on essentials | 70% | 81% | 88% | 3% |
| `std_gasto` | Spending variability | R$ 500 | R$ 1,800 | R$ 4,500 | R$ 800 |

**Feature Correlation Matrix:**
| | media_renda | media_gasto | taxa_poupanca |
|--|-------------|-------------|---------------|
| **media_renda** | 1.00 | 0.72 | 0.58 |
| **media_gasto** | 0.72 | 1.00 | -0.45 |
| **taxa_poupanca** | 0.58 | -0.45 | 1.00 |

### 4 Identified Clusters

| Cluster | Name | N | % | Savings Rate | Risk Level | Monthly Economy |
|---------|------|---|---|--------------|------------|-----------------|
| 0 | Endividados Moderados | 86 | 17.2% | -36.8% | HIGH | R$ 354.69 |
| 1 | Em Alerta | 228 | 45.6% | -24.6% | MODERATE | R$ 160.42 |
| 2 | Endividados Severos | 112 | 22.4% | -79.7% | CRITICAL | R$ 613.49 |
| 3 | Poupadores | 74 | 14.8% | +26.0% | LOW | R$ 123.29 |

**Risk Distribution:**
- 77.2% of users in financial risk (386 of 500)
- 39.6% in critical situation (Clusters 0 and 2: 198 users)
- 45.6% in alert state (Cluster 1: 228 users)
- 14.8% with adequate financial health (Cluster 3: 74 users)

## Models and Artifacts

### Sprint 1 Models
- `models/kmeans_best.pkl` - K-means K=4 (best model)
- `models/scaler.pkl` - StandardScaler for clustering features

### Sprint 2 Models
- `models/recomendacoes_regras.json` - 8 recommendation rules (2 per cluster)
- `models/isolation_forest.pkl` - Anomaly detector
- `models/scaler_anomalias.pkl` - Scaler for anomaly features
- `models/stats_categoria_anomalias.csv` - Category statistics
- `models/config_anomalias.json` - Anomaly model configuration
- `models/pipeline_completo.pkl` - Integrated pipeline with all components
- `models/config_pipeline.json` - Pipeline configuration

### Processed Data

| File | Records | Columns | Description |
|------|---------|---------|-------------|
| `usuarios_clustered.csv` | 500 | 8 | Users with cluster assignment |
| `features_clustering.csv` | 500 | 6 | 5 features + user_id |
| `dataset_clusters_validado.csv` | 500 | 12 | Complete validated dataset |
| `economia_projetada.csv` | 500 | 19 | Projected savings per user |
| `transacoes_com_anomalias_pred.csv` | 191,231 | 10 | Transactions with predictions |
| `pipeline_teste_resultados.csv` | 10 | 10 | Pipeline test results |
| `metricas_anomalias.csv` | 9 | 4 | H6 validation metrics |

## Sprint Execution Summary

### Sprint 1 Notebooks (6 executed - 100%)

| # | Notebook | Lines | Objective |
|---|----------|-------|-----------|
| 1 | 01_EDA_Basico.ipynb | 484 KB | Exploratory data analysis |
| 2 | 02_Feature_Engineering.ipynb | 273 KB | Feature creation |
| 3 | 03_Clustering.ipynb | 243 KB | K-means clustering |
| 4 | 04_Clustering_Validacao.ipynb | 657 KB | Validation metrics |
| 5 | 05_Interpretacao_Clusters.ipynb | 88 KB | Cluster profiling |
| 6 | 06_Recomendacoes_Review.ipynb | 25 KB | Recommendations review |

### Sprint 2 Notebooks (6 executed - 100%)

| # | Notebook | Lines | Objective |
|---|----------|-------|-----------|
| 7 | 07_Recomendacoes_Sistema.ipynb | 924 | Recommendation rules system |
| 8 | 08_Recomendacoes_Economia.ipynb | 1,548 | Economy calculation |
| 9 | 09_Anomalias_Treino.ipynb | 1,323 | Isolation Forest training |
| 10 | 10_Anomalias_Validacao.ipynb | 1,216 | H6 validation |
| 11 | 11_Pipeline_Integrado.ipynb | 1,237 | End-to-end pipeline |
| 12 | 12_Demonstracao.ipynb | 1,399 | System demonstration |

**Total Sprint 2:** 7,647 lines of code

## Pipeline Usage

### Load and Use Pipeline
```python
import joblib
import pandas as pd

# Load pipeline
pipeline_data = joblib.load('models/pipeline_completo.pkl')

# Load transactions
transacoes = pd.read_csv('data/raw/transacoes.csv')

# Extract components
kmeans = pipeline_data['componentes']['kmeans']
scaler = pipeline_data['componentes']['scaler_clustering']
regras = pipeline_data['regras_recomendacao']
cluster_names = pipeline_data['configuracoes']['cluster_names']

# Or use the EconomizaPipeline class from notebook 12
```

### Pipeline Output Structure
```python
{
    'user_id': str,
    'perfil': {'cluster': int, 'cluster_nome': str, 'prioridade': str},
    'financeiro': {'renda_media': float, 'gasto_medio': float, 'taxa_poupanca': float},
    'recomendacoes': [{'titulo': str, 'economia_potencial': float, 'dica': str}, ...],
    'economia': {'total_mensal': float, 'pct_da_renda': float},
    'anomalias': {'total_anomalias': int, 'transacoes_anomalas': list}
}
```

## Recommendation Rules Summary

| Cluster | Priority | Rule 1 | Rule 2 |
|---------|----------|--------|--------|
| 0 - Endividados Moderados | HIGH | Reduce Alimentacao_Fora 50% | Cut Vestuario 50% |
| 1 - Em Alerta | MODERATE | Reduce Alimentacao_Fora 40% | Limit Lazer 35% |
| 2 - Endividados Severos | CRITICAL | Cut Alimentacao_Fora 70% | Eliminate Vestuario 90% |
| 3 - Poupadores | LOW | Optimize Transporte 15% | Review Telecomunicacoes 20% |

### Top 3 Categories for Economy (Non-Essential)

| Ranking | Category | Avg Monthly | Potential Cut | Est. Savings |
|---------|----------|-------------|---------------|--------------|
| 1 | Alimentacao Fora | R$ 411.64 | 50-70% | R$ 206-288/month |
| 2 | Vestuario | R$ 197.60 | 40-60% | R$ 79-119/month |
| 3 | Lazer | R$ 154.78 | 30-50% | R$ 46-77/month |

### Projected Savings Impact

| Period | Amount |
|--------|--------|
| Monthly (500 users) | R$ 144,912.93 |
| Quarterly | R$ 434,739 |
| Annual | R$ 1,738,955 |

If 50% of users follow recommendations:
- Real annual savings: R$ 869,478
- Users impacted: 250
- Average per user: R$ 3,478/year

## Data Conventions

- Always filter out "Renda" category when analyzing expenses: `transacoes[transacoes['categoria'] != 'Renda']`
- 5% of transactions are marked as anomalies (`is_anomalia=True`) for detector training
- Random seed 42 is used for reproducibility
- All monetary values are in Brazilian Reais (R$)

## Tech Stack

- Python 3.11+
- pandas, numpy, scipy - Data processing
- scikit-learn - Machine learning (K-means, StandardScaler, IsolationForest)
- matplotlib, seaborn - Visualization (notebooks)
- Jupyter notebooks - Development environment
- joblib - Model serialization
- Streamlit - Dashboard (Sprint 3)
- Plotly - Interactive charts (Sprint 3 dashboard)

### Sprint 3 Dependencies (included in requirements.txt)
```bash
streamlit>=1.28.0
plotly>=5.18.0
```

## Sprint 3 Dashboard Structure (Implemented)

```
app/
├── app.py                    # Streamlit main entry point
├── pages/
│   ├── 0_Home.py             # Home page
│   ├── 1_Visao_Geral.py      # Overview (cluster distribution, metrics)
│   ├── 2_Analise_Usuario.py  # Individual user analysis
│   └── 3_Comparativo.py      # Profile comparison (radar, tables)
├── components/
│   ├── __init__.py
│   ├── cards.py              # Metric cards (profile, recommendation, anomaly)
│   ├── charts.py             # Visualizations (pie, bar, gauge, radar)
│   └── sidebar.py            # Navigation component
└── utils/
    ├── __init__.py
    ├── config.py             # App configuration and constants
    ├── data_loader.py        # Data loading utilities
    └── pipeline.py           # Pipeline wrapper for Streamlit
```

### Run Dashboard
```bash
cd app/
streamlit run app.py
# Access at http://localhost:8501
```

### Dashboard Features (Implemented)
1. **Home Page**: Welcome and navigation
2. **Visão Geral**: Cluster distribution (pie), economy by cluster (bar), detailed stats per cluster
3. **Análise de Usuário**: User selection, profile card, financial metrics, recommendations with economy, anomaly alerts, financial health gauge
4. **Comparativo**: Renda vs Gasto (grouped bar), savings rate by profile, economy projection, radar chart, comparison table

### Using the Dashboard
```python
# The dashboard uses a PipelineWrapper class (app/utils/pipeline.py)
# that loads all models and provides easy access to analysis functions

from utils.pipeline import get_pipeline

pipeline = get_pipeline()

# Analyze a user
resultado = pipeline.analisar_usuario('user_0001')

# Get general summary
resumo = pipeline.get_resumo_geral()
```

## Key Insights from Sprints

### Critical Discoveries
1. **77% of users spend more than they earn** - 386 of 500 users at financial risk
2. **Eating out is the main villain** - R$ 411/month average, 50-70% reduction potential
3. **Only 14.8% manage to save** - Majority needs basic financial education
4. **Savings rate varies drastically** - From -80% (Cluster 2) to +26% (Cluster 3)
5. **High income-expense correlation (0.72)** - Higher earners spend more (behavioral issue)

### Lessons Learned

| Lesson | Description |
|--------|-------------|
| Interpretability > Metrics | Useful profiles even with low Silhouette score |
| Simplicity works | 5 features were sufficient |
| Savings rate is key | Most discriminating feature |
| Continuous documentation | Saves time long-term |
| Modular pipeline | Facilitates iteration and debugging |
| Aggressive rules for critical profiles | Cluster 2 achieved 17.56% (within target) |
| Ground truth matters | H6 failed due to random anomaly generation, not model |

### Technical Decisions Validated

| Decision | Alternative Considered | Result |
|----------|------------------------|--------|
| K-means | DBSCAN, Hierarchical | Validated - useful clusters |
| StandardScaler | MinMaxScaler, RobustScaler | Validated - adequate scale |
| 5 features | 10+ features | Validated - sufficient |
| K=4 | K=3 or K=5 | Validated - ideal balance |
| 2 rules per cluster | More rules | Validated - focus and simplicity |
| Rule-based recommendations | ML-based | Validated - interpretable and auditable |
| Global Isolation Forest | Per-category models | Partial - dataset issue |

## Documentation

### Sprint 1 Documentation
- `outputs/Sprint1_Resumo_Executivo.md` - Sprint 1 executive summary with key metrics and visualizations
- `outputs/Sprint1_Relatorio.md` - Sprint 1 comprehensive technical report (900+ lines)
- `outputs/Sprint1_Review.md` - Sprint 1 executive review
- `outputs/Sprint1_Resumo.md` - Sprint 1 technical documentation
- `outputs/Perfis_Clusters.md` - Cluster profiles description

### Sprint 2 Documentation
- `outputs/Sprint2_Resumo_Executivo.md` - Sprint 2 executive summary with validation results
- `outputs/Sprint2_Relatorio.md` - Sprint 2 comprehensive technical report
- `outputs/Sprint2_Review.md` - Sprint 2 executive review
- `outputs/Sprint2_Resumo.md` - Sprint 2 technical documentation
- `outputs/Sprint2_Planejamento.md` - Sprint 2 planning document
- `outputs/validacao_h1.md` - H1 validation details (economy recommendations)
- `outputs/validacao_h6.md` - H6 validation details (anomaly detection)
- `outputs/Sprint3_Handoff.md` - Sprint 3 handoff document with dashboard structure and roadmap
- `outputs/Sprint3_Planejamento.md` - Sprint 3 detailed planning with daily tasks and deliverables

### Sprint 3 Code (Dashboard)
- `app/app.py` - Main Streamlit application
- `app/pages/0_Home.py` - Home page
- `app/pages/1_Visao_Geral.py` - Overview page with metrics and charts
- `app/pages/2_Analise_Usuario.py` - Individual user analysis page
- `app/pages/3_Comparativo.py` - Cluster comparison page
- `app/components/cards.py` - Reusable card components
- `app/components/charts.py` - Reusable chart components (Plotly)
- `app/utils/pipeline.py` - Pipeline wrapper for Streamlit
- `app/utils/data_loader.py` - Data loading utilities
- `app/utils/config.py` - Configuration constants

### Visualizations Generated

**Sprint 1 (7 visualizations):**
- `outputs/elbow_curve.png` - K selection via Elbow method
- `outputs/cluster_visualization.png` - 2D scatter plot of clusters
- `outputs/silhouette_plot.png` - Silhouette analysis per cluster
- `outputs/pca_2d_clusters.png` - PCA 2D visualization
- `outputs/pca_clusters_individuais.png` - Individual PCA per cluster
- `outputs/distribuicao_clusters.png` - Cluster distribution (pie/bar)
- `outputs/boxplots_clusters.png` - Feature boxplots per cluster

**Sprint 2 - Economy (4 visualizations):**
- `outputs/economia_por_cluster.png` - Savings by cluster
- `outputs/distribuicao_economia_cluster.png` - Savings distribution
- `outputs/poupanca_atual_vs_projetada.png` - Current vs projected savings
- `outputs/economia_por_recomendacao.png` - Savings by recommendation

**Sprint 2 - Anomalies (6 visualizations):**
- `outputs/anomalias_distribuicao.png` - Anomaly distribution
- `outputs/matriz_confusao_anomalias.png` - Confusion matrix
- `outputs/distribuicao_scores_anomalia.png` - Anomaly score distribution
- `outputs/validacao_h6_matriz_confusao.png` - H6 validation matrix
- `outputs/validacao_h6_scores.png` - H6 scores visualization
- `outputs/validacao_h6_por_categoria.png` - H6 by category

**Sprint 2 - Demonstration (5 visualizations):**
- `outputs/demo_cluster_0.png` - Dashboard Endividados Moderados
- `outputs/demo_cluster_1.png` - Dashboard Em Alerta
- `outputs/demo_cluster_2.png` - Dashboard Endividados Severos
- `outputs/demo_cluster_3.png` - Dashboard Poupadores
- `outputs/demo_comparativo_perfis.png` - Profile comparison
