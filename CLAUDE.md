# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Economiza+ is a financial behavior analysis and segmentation system for Brazilian middle-to-lower-income families (classes C and D). The project uses machine learning to identify spending patterns, segment users into financial profiles, and provide personalized saving recommendations.

The project generates synthetic financial data based on Brazilian statistics (Serasa, CNC, IBGE, POF) and applies K-means clustering to identify 4 distinct user profiles ranging from "Endividados Severos" (-89% savings rate) to "Poupadores" (+25% savings rate).

## Academic Context

- **Course**: Data Science (XP Educação)
- **Advisor**: Marcos Prochnow
- **Duration**: 21 days (3 sprints × 7 days)

## Hypotheses and Validation Results

| Hypothesis | Description | Target | Result | Status |
|------------|-------------|--------|--------|--------|
| H1 | Economy recommendations generate real savings | 15-20% reduction | 8.11% (19.22% Cluster 0) | Partial |
| H2 | K-means clustering identifies distinct profiles | Silhouette Score > 0.5 | 0.52 | Validated |
| H6 | Isolation Forest detects anomalous transactions | Precision > 0.85, Recall > 0.80 | P=47.3%, R=47.4% | Not validated |

## Sprint Structure

- **Sprint 1** (Days 1-7): EDA, Feature Engineering, Clustering - COMPLETED
- **Sprint 2** (Days 8-14): Recommendation system, Anomaly detection - COMPLETED
- **Sprint 3** (Days 15-21): Dashboard (Streamlit), Integration, Documentation

## Constraints and Pre-defined Decisions

### Constraints
- No real user data (LGPD compliance) - synthetic data only
- Development environment: Google Colab
- 21-day deadline

### Technical Decisions (Non-negotiable)
- **Clustering**: K-means (not DBSCAN)
- **Normalization**: StandardScaler
- **Features**: Exactly 5 clustering features
- **Recommendations**: 2 rule-based recommendations per cluster
- **Anomaly Detection**: Global Isolation Forest (not per-category)

## Commands

### Setup
```bash
pip install -r requirements.txt
```

### Generate Synthetic Dataset
```bash
python scripts/gerar_dataset_financeiro.py
```
Outputs to `data/raw/`: `usuarios.csv`, `transacoes.csv`, `estatisticas_mensais.csv`

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
scripts/gerar_dataset_financeiro.py → data/raw/ → notebooks (processing) → data/processed/ → models/ → pipeline
```

### Key Directories
- `data/raw/` - Raw CSVs (usuarios, transacoes, estatisticas_mensais)
- `data/processed/` - Engineered features and predictions
- `models/` - Trained models and configurations
- `outputs/` - Visualizations and documentation

### Dataset Schema
- **usuarios.csv**: Demographics (user_id, idade, tipo_emprego, renda_base, estado_civil, num_dependentes, situacao_financeira, regiao)
- **transacoes.csv**: ~194K transactions with (user_id, data, categoria, valor, is_essencial, is_anomalia)
- **estatisticas_mensais.csv**: Monthly aggregations per user

### 5 Clustering Features
1. `media_renda` - Average monthly income
2. `media_gasto` - Average monthly spending
3. `taxa_poupanca` - Savings rate: (renda - gasto) / renda
4. `pct_gastos_essenciais` - % spent on essentials
5. `std_gasto` - Spending variability

### 4 Identified Clusters
- Cluster 0: Endividados Severos (11.8%, -89% savings rate)
- Cluster 1: Em Alerta (39.2%, -15% savings rate)
- Cluster 2: Endividados Moderados (33.4%, -58% savings rate)
- Cluster 3: Poupadores (15.6%, +25% savings rate)

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
- `data/processed/usuarios_clustered.csv` - Users with cluster assignment
- `data/processed/features_clustering.csv` - 5 features per user
- `data/processed/economia_projetada.csv` - Projected savings per user
- `data/processed/transacoes_com_anomalias_pred.csv` - Transactions with predictions

## Pipeline Usage

### Load and Use Pipeline
```python
import pickle
import pandas as pd

# Load pipeline
with open('models/pipeline_completo.pkl', 'rb') as f:
    pipeline_data = pickle.load(f)

# Load transactions
transacoes = pd.read_csv('data/raw/transacoes.csv')

# Analyze user (full analysis)
resultado = pipeline.analisar_usuario('user_0001', transacoes)

# Access results
print(resultado['perfil']['cluster_nome'])  # e.g., 'Poupadores'
print(resultado['economia']['total_mensal'])  # e.g., 103.50
print(resultado['anomalias']['total_anomalias'])  # e.g., 3
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

| Cluster | Rule 1 | Rule 2 |
|---------|--------|--------|
| 0 - Endividados Severos | Cut Alimentacao_Fora 70% | Eliminate Vestuario 90% |
| 1 - Em Alerta | Reduce Alimentacao_Fora 40% | Limit Lazer 35% |
| 2 - Endividados Moderados | Reduce Alimentacao_Fora 50% | Cut Vestuario 50% |
| 3 - Poupadores | Optimize Transporte 15% | Review Telecomunicacoes 20% |

## Data Conventions

- Always filter out "Renda" category when analyzing expenses: `transacoes[transacoes['categoria'] != 'Renda']`
- 5% of transactions are marked as anomalies (`is_anomalia=True`) for detector training
- Random seed 42 is used for reproducibility
- All monetary values are in Brazilian Reais (R$)

## Tech Stack

- Python 3.11+
- pandas, numpy, scipy - Data processing
- scikit-learn - Machine learning (K-means, StandardScaler, IsolationForest)
- matplotlib, seaborn - Visualization
- Jupyter notebooks - Development environment
- pickle/joblib - Model serialization
- Streamlit (Sprint 3) - Dashboard

## Documentation

- `outputs/Sprint1_Review.md` - Sprint 1 executive review
- `outputs/Sprint1_Resumo.md` - Sprint 1 technical documentation
- `outputs/Sprint2_Review.md` - Sprint 2 executive review
- `outputs/Sprint2_Resumo.md` - Sprint 2 technical documentation
- `outputs/Sprint2_Planejamento.md` - Sprint 2 planning
- `outputs/validacao_h1.md` - H1 validation details
- `outputs/validacao_h6.md` - H6 validation details
- `outputs/Perfis_Clusters.md` - Cluster profiles description
