# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Economiza+ is a financial behavior analysis and segmentation system for Brazilian middle-to-lower-income families (classes C and D). The project uses machine learning to identify spending patterns, segment users into financial profiles, and provide personalized saving recommendations.

The project generates synthetic financial data based on Brazilian statistics (Serasa, CNC, IBGE, POF) and applies K-means clustering to identify 4 distinct user profiles ranging from "Endividados Severos" (-89% savings rate) to "Poupadores" (+25% savings rate).

## Academic Context

- **Course**: Data Science (XP Educação)
- **Advisor**: Marcos Prochnow
- **Duration**: 21 days (3 sprints × 7 days)

## Hypotheses and Target Metrics

Three hypotheses being validated:

| Hypothesis | Description | Target |
|------------|-------------|--------|
| H1 | Economy recommendations generate real savings | 15-20% reduction |
| H2 | K-means clustering identifies distinct profiles | Silhouette Score > 0.5 |
| H6 | Isolation Forest detects anomalous transactions | Precision > 0.85, Recall > 0.80 |

## Sprint Structure

- **Sprint 1** (Days 1-7): EDA, Feature Engineering, Clustering
- **Sprint 2** (Days 8-14): Recommendation system, Anomaly detection
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
Outputs to `outputs/`: `usuarios.csv`, `transacoes.csv`, `estatisticas_mensais.csv`

### Run Notebooks
Execute notebooks sequentially in Jupyter:
1. `notebooks/01_EDA_Basico.ipynb` - Exploratory data analysis
2. `notebooks/02_Feature_Engineering.ipynb` - Feature creation
3. `notebooks/03_Clustering.ipynb` - K-means clustering
4. `notebooks/04_Clustering_Validacao.ipynb` - Validation metrics
5. `notebooks/05_Interpretacao_Clusters.ipynb` - Cluster profiling
6. `notebooks/06_Recomendacoes_Review.ipynb` - Recommendations

## Architecture

### Data Flow
```
scripts/gerar_dataset_financeiro.py → data/raw/ → notebooks (processing) → data/processed/ → models/
```

### Key Directories
- `data/raw/` - Raw CSVs (usuarios, transacoes, estatisticas_mensais)
- `data/processed/` - Engineered features (`features_clustering.csv`, `usuarios_clustered.csv`)
- `models/` - Trained models (`kmeans_best.pkl`, `scaler.pkl`)
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

## Data Conventions

- Always filter out "Renda" category when analyzing expenses: `transacoes[transacoes['categoria'] != 'Renda']`
- 5% of transactions are marked as anomalies (`is_anomalia=True`) for detector training
- Random seed 42 is used for reproducibility
- All monetary values are in Brazilian Reais (R$)

## Tech Stack

- Python 3.11+
- pandas, numpy, scipy - Data processing
- scikit-learn - Machine learning (K-means, StandardScaler)
- matplotlib, seaborn - Visualization
- Jupyter notebooks - Development environment
- pickle/joblib - Model serialization
