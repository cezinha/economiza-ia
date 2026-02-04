# Economiza+ MVP

Sistema de Análise Financeira e Recomendações Personalizadas para famílias brasileiras das classes C e D.

## Sobre o Projeto

O **Economiza+** é um sistema de machine learning que analisa comportamentos financeiros, identifica perfis de usuários através de clustering, e gera recomendações personalizadas de economia. O projeto foi desenvolvido como trabalho de conclusão do curso de Data Science da XP Educação.

### Principais Funcionalidades

- **Segmentação de Usuários**: Identificação de 4 perfis financeiros distintos usando K-means
- **Recomendações Personalizadas**: Sugestões de economia baseadas no perfil do usuário
- **Detecção de Anomalias**: Identificação de transações suspeitas com Isolation Forest
- **Dashboard Interativo**: Interface web para visualização e análise (Streamlit)

### Métricas do Projeto

| Métrica | Valor |
|---------|-------|
| Usuários analisados | 500 |
| Transações processadas | 191.231 |
| Perfis identificados | 4 |
| Usuários em risco financeiro | 85,2% |
| Economia mensal projetada | R$ 188.746 |
| Economia anual projetada | R$ 2,26M |

## Perfis Financeiros Identificados

| Perfil | Usuários | Taxa Poupança | Prioridade |
|--------|----------|---------------|------------|
| Endividados Moderados | 17,2% | -36,8% | ALTA |
| Em Alerta | 45,6% | -24,6% | MODERADA |
| Endividados Severos | 22,4% | -79,7% | CRÍTICA |
| Poupadores | 14,8% | +26,0% | BAIXA |

## Instalação

### Pré-requisitos

- Python 3.11+
- pip ou conda

### Setup

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/economiza-ia.git
cd economiza-ia
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

### 1. Gerar Dataset Sintético

```bash
python scripts/gerar_dataset_financeiro.py
```

Gera dados sintéticos baseados em estatísticas brasileiras (Serasa, CNC, IBGE, POF).

### 2. Executar Dashboard

```bash
cd app/
streamlit run app.py
```

Acesse em: http://localhost:8501

### 3. Executar Notebooks

Os notebooks devem ser executados na ordem para reproduzir a análise completa:

**Sprint 1 - Segmentação:**
1. `01_EDA_Basico.ipynb` - Análise exploratória
2. `02_Feature_Engineering.ipynb` - Criação de features
3. `03_Clustering.ipynb` - Clustering K-means
4. `04_Clustering_Validacao.ipynb` - Validação do modelo
5. `05_Interpretacao_Clusters.ipynb` - Interpretação dos perfis
6. `06_Recomendacoes_Review.ipynb` - Revisão das recomendações

**Sprint 2 - Recomendações:**
7. `07_Recomendacoes_Sistema.ipynb` - Sistema de regras
8. `08_Recomendacoes_Economia.ipynb` - Cálculo de economia
9. `09_Anomalias_Treino.ipynb` - Treinamento Isolation Forest
10. `10_Anomalias_Validacao.ipynb` - Validação H6
11. `11_Pipeline_Integrado.ipynb` - Pipeline completo
12. `12_Demonstracao.ipynb` - Demonstração do sistema

**Sprint 3 - Refinamento:**
13. `13_Refinamento_H1.ipynb` - Refinamento das regras v1.1

## Estrutura do Projeto

```
economiza-ia/
├── app/                      # Dashboard Streamlit
│   ├── app.py               # Aplicação principal
│   ├── pages/               # Páginas do dashboard
│   │   ├── 0_Home.py
│   │   ├── 1_Visao_Geral.py
│   │   ├── 2_Analise_Usuario.py
│   │   ├── 3_Comparativo.py
│   │   └── 4_Diagnostico.py
│   ├── components/          # Componentes reutilizáveis
│   └── utils/               # Utilitários
├── data/
│   ├── raw/                 # Dados brutos
│   └── processed/           # Dados processados
├── models/                  # Modelos treinados
│   ├── kmeans_best.pkl
│   ├── isolation_forest.pkl
│   ├── pipeline_completo.pkl
│   └── recomendacoes_regras.json
├── notebooks/               # Jupyter notebooks (13)
├── outputs/                 # Visualizações e relatórios
├── scripts/                 # Scripts de geração de dados
├── docs/                    # Documentação
└── requirements.txt
```

## Dashboard

O dashboard oferece 5 páginas:

1. **Início**: Visão geral e métricas principais
2. **Visão Geral**: Distribuição dos perfis e economia por cluster
3. **Análise de Usuário**: Análise individual com recomendações
4. **Comparativo**: Comparação entre os 4 perfis
5. **Diagnóstico**: Verificação de saúde do sistema

### Screenshots

*Execute o dashboard localmente para visualizar a interface completa.*

## Validação das Hipóteses

### H1: Recomendações geram economia real
| Cluster | Target | Resultado | Status |
|---------|--------|-----------|--------|
| Moderados | 15-20% | 15,97% | ✅ |
| Em Alerta | 15-20% | 10,03% | ⚠️ |
| Severos | 15-20% | 17,56% | ✅ |

**Conclusão**: 2 de 3 clusters atingem o target. Cluster "Em Alerta" requer abordagem complementar (educação financeira).

### H2: K-means identifica perfis distintos
| Métrica | Target | Resultado |
|---------|--------|-----------|
| Silhouette Score | > 0,50 | 0,267 |
| PCA Variance (2D) | > 70% | 82,7% |
| Interpretabilidade | Alta | Alta |

**Conclusão**: Parcialmente validada. Métricas estatísticas abaixo do ideal, mas clusters são interpretáveis e acionáveis.

### H6: Isolation Forest detecta anomalias
| Métrica | Target | Resultado |
|---------|--------|-----------|
| Precision | > 0,85 | 47,3% |
| Recall | > 0,80 | 47,4% |

**Conclusão**: Não validada devido a limitação do dataset (anomalias geradas aleatoriamente).

## Tecnologias

- **Python 3.11+**
- **pandas, numpy** - Processamento de dados
- **scikit-learn** - Machine Learning (K-means, Isolation Forest)
- **matplotlib, seaborn** - Visualizações (notebooks)
- **Streamlit** - Dashboard web
- **Plotly** - Gráficos interativos
- **joblib** - Serialização de modelos

## Contexto Acadêmico

- **Curso**: Data Science (XP Educação)
- **Orientador**: Marcos Prochnow
- **Duração**: 21 dias (3 sprints × 7 dias)
- **Data de Conclusão**: Fevereiro 2026

## Dados de Referência

Dataset sintético baseado em estatísticas reais:
- **Serasa**: 80,6 milhões de inadimplentes
- **CNC**: 79,5% das famílias endividadas
- **IBGE**: 60% não conseguem poupar
- **POF**: Distribuição de gastos por categoria

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

Desenvolvido como projeto de conclusão de curso.

---

*Economiza+ MVP v1.1.0 - Fevereiro 2026*
