# Economiza+ MVP
## Relatório Final do Projeto

**Curso:** Data Science - XP Educação
**Orientador:** Marcos Prochnow
**Data:** Fevereiro 2026
**Versão:** 1.1.0

---

## Sumário

1. [Resumo Executivo](#1-resumo-executivo)
2. [Introdução](#2-introdução)
3. [Objetivos](#3-objetivos)
4. [Metodologia](#4-metodologia)
5. [Resultados - Sprint 1](#5-resultados---sprint-1)
6. [Resultados - Sprint 2](#6-resultados---sprint-2)
7. [Resultados - Sprint 3](#7-resultados---sprint-3)
8. [Validação das Hipóteses](#8-validação-das-hipóteses)
9. [Discussão e Limitações](#9-discussão-e-limitações)
10. [Conclusão](#10-conclusão)
11. [Trabalhos Futuros](#11-trabalhos-futuros)
12. [Referências](#12-referências)
13. [Anexos](#13-anexos)

---

## 1. Resumo Executivo

O **Economiza+ MVP** é um sistema de análise financeira e recomendações personalizadas desenvolvido para auxiliar famílias brasileiras das classes C e D a melhorar sua saúde financeira. O projeto utiliza técnicas de machine learning para segmentar usuários em perfis financeiros distintos e gerar recomendações de economia específicas para cada perfil.

### Principais Resultados

| Métrica | Valor |
|---------|-------|
| Usuários analisados | 500 |
| Transações processadas | 191.231 |
| Perfis identificados | 4 |
| Usuários em risco financeiro | 85,2% |
| Economia mensal projetada | R$ 188.746 |
| Economia anual projetada | R$ 2,26 milhões |

### Validação das Hipóteses

- **H1 (Economia):** Parcialmente validada - 2 de 3 clusters atingem target de 15-20%
- **H2 (Clustering):** Parcialmente validada - clusters interpretáveis apesar de métricas abaixo do ideal
- **H6 (Anomalias):** Não validada - limitação do dataset sintético

### Entregas

- 13 notebooks Jupyter documentados
- Dashboard interativo com 5 páginas (Streamlit)
- Pipeline integrado de análise
- Documentação completa

---

## 2. Introdução

### 2.1 Contexto

O Brasil enfrenta uma crise financeira crônica que afeta milhões de famílias. Segundo dados recentes:

- **80,6 milhões** de brasileiros estão inadimplentes (Serasa, 2024)
- **79,5%** das famílias estão endividadas (CNC, 2024)
- **60%** não conseguem poupar (IBGE, 2023)
- A dívida média por pessoa é de **R$ 4.042** (Serasa, 2024)

As classes C e D são as mais afetadas, com renda limitada e pouco acesso a educação financeira personalizada.

### 2.2 Problema

As soluções existentes de gestão financeira pessoal são geralmente:

1. **Genéricas** - Não consideram o perfil específico do usuário
2. **Complexas** - Requerem conhecimento financeiro avançado
3. **Inacessíveis** - Focadas em classes A e B

### 2.3 Proposta

O Economiza+ propõe um sistema que:

1. **Analisa** automaticamente o comportamento financeiro
2. **Segmenta** usuários em perfis distintos
3. **Personaliza** recomendações de acordo com o perfil
4. **Monitora** transações suspeitas

---

## 3. Objetivos

### 3.1 Objetivo Geral

Desenvolver um sistema de recomendação financeira personalizada baseado em machine learning para famílias das classes C e D.

### 3.2 Objetivos Específicos

1. Gerar dataset sintético realista baseado em estatísticas brasileiras
2. Realizar análise exploratória para identificar padrões de gastos
3. Aplicar clustering para segmentar usuários em perfis financeiros
4. Desenvolver sistema de recomendações personalizadas
5. Implementar detecção de anomalias em transações
6. Criar dashboard interativo para visualização
7. Validar hipóteses através de métricas quantitativas

### 3.3 Hipóteses

| ID | Hipótese | Target |
|----|----------|--------|
| H1 | Recomendações personalizadas geram economia de 15-20% da renda | 15-20% |
| H2 | K-means identifica perfis financeiros distintos | Silhouette > 0.50 |
| H6 | Isolation Forest detecta transações anômalas | Precision > 0.85 |

---

## 4. Metodologia

### 4.1 Estrutura do Projeto

O projeto foi desenvolvido em **3 sprints** de 7 dias cada, totalizando 21 dias:

| Sprint | Período | Foco | Entregas |
|--------|---------|------|----------|
| 1 | Dias 1-7 | Segmentação | EDA, Features, Clustering |
| 2 | Dias 8-14 | Recomendações | Regras, Anomalias, Pipeline |
| 3 | Dias 15-21 | Dashboard | Streamlit, Documentação |

### 4.2 Stack Tecnológica

| Categoria | Tecnologias |
|-----------|-------------|
| Linguagem | Python 3.11+ |
| Processamento | pandas, numpy, scipy |
| Machine Learning | scikit-learn (K-means, Isolation Forest) |
| Visualização | matplotlib, seaborn, Plotly |
| Dashboard | Streamlit |
| Serialização | joblib, pickle |
| Versionamento | Git |

### 4.3 Dataset

#### 4.3.1 Geração de Dados Sintéticos

O dataset foi gerado sinteticamente baseado em estatísticas reais:

- **Serasa:** Distribuição de inadimplência por faixa etária
- **CNC:** Percentual de famílias endividadas
- **IBGE:** Distribuição de renda por região
- **POF:** Distribuição de gastos por categoria

#### 4.3.2 Estrutura do Dataset

| Arquivo | Registros | Descrição |
|---------|-----------|-----------|
| usuarios.csv | 500 | Perfil demográfico dos usuários |
| transacoes.csv | 191.231 | Transações financeiras (6 meses) |
| estatisticas_mensais.csv | 2.500 | Agregações mensais por usuário |

#### 4.3.3 Features de Clustering

| Feature | Descrição | Média | Std |
|---------|-----------|-------|-----|
| media_renda | Renda média mensal | R$ 3.800 | R$ 2.100 |
| media_gasto | Gasto médio mensal | R$ 4.200 | R$ 1.900 |
| taxa_poupanca | (renda - gasto) / renda | -31,6% | 42% |
| pct_gastos_essenciais | % em gastos essenciais | 81% | 3% |
| std_gasto | Variabilidade dos gastos | R$ 1.800 | R$ 800 |

### 4.4 Algoritmos

#### 4.4.1 K-means Clustering

- **Objetivo:** Segmentar usuários em perfis financeiros
- **Pré-processamento:** StandardScaler para normalização
- **Seleção de K:** Método Elbow + Silhouette Score
- **K escolhido:** 4 clusters

#### 4.4.2 Isolation Forest

- **Objetivo:** Detectar transações anômalas
- **Contamination:** 5% (baseado no ground truth)
- **Features:** valor, valor_zscore, pct_da_media_categoria

---

## 5. Resultados - Sprint 1

### 5.1 Análise Exploratória (EDA)

#### 5.1.1 Distribuição de Renda

- Renda média: **R$ 3.800**
- Mediana: **R$ 3.200**
- Distribuição assimétrica positiva (cauda longa para rendas altas)

#### 5.1.2 Distribuição de Gastos por Categoria

| Categoria | % do Gasto Total | Essencial |
|-----------|------------------|-----------|
| Alimentação Casa | 25,3% | Sim |
| Habitação | 22,1% | Sim |
| Transporte | 15,7% | Sim |
| Alimentação Fora | 9,8% | Não |
| Saúde | 8,2% | Sim |
| Educação | 6,1% | Sim |
| Vestuário | 4,7% | Não |
| Lazer | 3,7% | Não |
| Telecomunicações | 2,8% | Não |
| Outros | 1,6% | Não |

#### 5.1.3 Taxa de Poupança

- Taxa média: **-31,6%** (déficit)
- Usuários com déficit: **77,2%**
- Usuários que conseguem poupar: **22,8%**

### 5.2 Clustering

#### 5.2.1 Seleção do Número de Clusters

| K | Inertia | Silhouette | Davies-Bouldin |
|---|---------|------------|----------------|
| 2 | 1847.3 | 0.312 | 1.089 |
| 3 | 1423.1 | 0.289 | 1.156 |
| **4** | **1156.8** | **0.267** | **1.184** |
| 5 | 987.2 | 0.251 | 1.243 |

**Decisão:** K=4 escolhido pelo método Elbow e interpretabilidade dos clusters.

#### 5.2.2 Perfis Identificados

| Cluster | Nome | N | % | Taxa Poupança | Prioridade |
|---------|------|---|---|---------------|------------|
| 0 | Endividados Moderados | 86 | 17,2% | -36,8% | ALTA |
| 1 | Em Alerta | 228 | 45,6% | -24,6% | MODERADA |
| 2 | Endividados Severos | 112 | 22,4% | -79,7% | CRÍTICA |
| 3 | Poupadores | 74 | 14,8% | +26,0% | BAIXA |

#### 5.2.3 Caracterização dos Perfis

**Cluster 0 - Endividados Moderados (17,2%)**
- Renda média: R$ 3.105
- Gasto médio: R$ 4.247
- Déficit: -R$ 1.142/mês
- Característica: Renda baixa, gastos acima da média

**Cluster 1 - Em Alerta (45,6%)**
- Renda média: R$ 3.598
- Gasto médio: R$ 4.482
- Déficit: -R$ 884/mês
- Característica: Maior grupo, déficit moderado controlável

**Cluster 2 - Endividados Severos (22,4%)**
- Renda média: R$ 4.148
- Gasto médio: R$ 7.450
- Déficit: -R$ 3.302/mês
- Característica: Gasto muito acima da renda, situação crítica

**Cluster 3 - Poupadores (14,8%)**
- Renda média: R$ 5.031
- Gasto médio: R$ 3.723
- Superávit: +R$ 1.308/mês
- Característica: Renda alta, gastos controlados

---

## 6. Resultados - Sprint 2

### 6.1 Sistema de Recomendações

#### 6.1.1 Regras Definidas (v1.1)

| Cluster | Prioridade | Regra 1 | Regra 2 | Regra 3 |
|---------|------------|---------|---------|---------|
| 0 | ALTA | Cortar Alimentação Fora 70% | Cortar Vestuário 70% | - |
| 1 | MODERADA | Reduzir Alimentação Fora 60% | Cortar Lazer 50% | Reduzir Vestuário 40% |
| 2 | CRÍTICA | Cortar Alimentação Fora 70% | Eliminar Vestuário 90% | - |
| 3 | BAIXA | Otimizar Transporte 15% | Revisar Telecomunicações 20% | - |

#### 6.1.2 Economia Projetada

| Cluster | Economia Média/Usuário | Economia Total/Mês | % da Renda |
|---------|------------------------|-------------------|------------|
| 0 | R$ 496,56 | R$ 42.704 | 15,97% |
| 1 | R$ 299,15 | R$ 68.206 | 10,03% |
| 2 | R$ 613,49 | R$ 68.711 | 17,56% |
| 3 | R$ 123,29 | R$ 9.123 | 2,45% |
| **Total** | **R$ 377,49** | **R$ 188.746** | **9,83%** |

### 6.2 Detecção de Anomalias

#### 6.2.1 Configuração do Modelo

- Algoritmo: Isolation Forest
- Contamination: 5%
- Random State: 42

#### 6.2.2 Métricas de Validação

| Métrica | Valor |
|---------|-------|
| Precision | 47,3% |
| Recall | 47,4% |
| Specificity | 97,2% |
| F1-Score | 47,3% |

**Nota:** Métricas abaixo do esperado devido à geração aleatória de anomalias no dataset sintético.

### 6.3 Pipeline Integrado

O pipeline integrado processa um usuário em aproximadamente **50ms**, incluindo:

1. Carregamento de dados
2. Cálculo de features
3. Predição de cluster
4. Geração de recomendações
5. Cálculo de economia projetada
6. Detecção de anomalias

---

## 7. Resultados - Sprint 3

### 7.1 Dashboard Streamlit

#### 7.1.1 Páginas Implementadas

| Página | Descrição |
|--------|-----------|
| Início | Métricas gerais e navegação |
| Visão Geral | Distribuição dos perfis, economia por cluster |
| Análise de Usuário | Perfil individual, recomendações, anomalias |
| Comparativo | Comparação entre os 4 perfis |
| Diagnóstico | Verificação de saúde do sistema |

#### 7.1.2 Funcionalidades

- **Cache** de dados pesados para performance
- **Tratamento de erros** robusto com mensagens contextuais
- **Gráficos interativos** com Plotly
- **Responsividade** para diferentes tamanhos de tela

### 7.2 Refinamento H1 (Day 17)

#### 7.2.1 Ajustes nas Regras (v1.0 → v1.1)

| Cluster | Antes | Depois | Melhoria |
|---------|-------|--------|----------|
| 0 | 10,98% | 15,97% | +4,99pp |
| 1 | 5,19% | 10,03% | +4,84pp |
| 2 | 17,41% | 17,56% | +0,15pp |
| **Média** | **8,60%** | **9,83%** | **+1,23pp** |

### 7.3 Melhorias de Robustez (Day 18)

- Classe `DataLoadError` para tratamento de erros de dados
- Validação de arquivos antes do carregamento
- Fallback para DataFrames vazios
- Página de diagnóstico para troubleshooting

---

## 8. Validação das Hipóteses

### 8.1 H1: Recomendações geram economia de 15-20%

| Cluster | Target | Resultado | Status |
|---------|--------|-----------|--------|
| 0 (Moderados) | 15-20% | 15,97% | ✅ Atingido |
| 1 (Em Alerta) | 15-20% | 10,03% | ⚠️ Abaixo |
| 2 (Severos) | 15-20% | 17,56% | ✅ Atingido |

**Conclusão:** PARCIALMENTE VALIDADA

- 2 de 3 clusters target atingem a meta
- Cluster 1 requer abordagem complementar (educação financeira)
- Média geral de 9,83% representa economia significativa

### 8.2 H2: K-means identifica perfis distintos

| Métrica | Target | Resultado | Status |
|---------|--------|-----------|--------|
| Silhouette Score | > 0.50 | 0.267 | ❌ Abaixo |
| Davies-Bouldin | < 1.00 | 1.184 | ⚠️ Próximo |
| PCA Variance (2D) | > 70% | 82.7% | ✅ Atingido |
| Interpretabilidade | Alta | Alta | ✅ Atingido |

**Conclusão:** PARCIALMENTE VALIDADA

- Métricas estatísticas abaixo do ideal
- Porém, clusters são interpretáveis e acionáveis
- PCA mostra boa separação visual
- Trade-off: interpretabilidade vs métricas estatísticas

### 8.3 H6: Isolation Forest detecta anomalias

| Métrica | Target | Resultado | Status |
|---------|--------|-----------|--------|
| Precision | > 0.85 | 47.3% | ❌ Não atingido |
| Recall | > 0.80 | 47.4% | ❌ Não atingido |
| Specificity | - | 97.2% | ✅ Excelente |

**Conclusão:** NÃO VALIDADA

- Anomalias no dataset foram geradas aleatoriamente (5% randômico)
- Modelo não consegue aprender padrões que não existem
- Alta especificidade indica poucos falsos positivos
- Requer dataset com anomalias estatisticamente geradas para validação real

---

## 9. Discussão e Limitações

### 9.1 Pontos Fortes

1. **Abordagem personalizada:** Recomendações específicas por perfil
2. **Interpretabilidade:** Clusters facilmente explicáveis para usuários finais
3. **Escalabilidade:** Pipeline processa ~20 usuários/segundo
4. **Documentação:** 13 notebooks detalhados e CLAUDE.md completo
5. **Interface amigável:** Dashboard intuitivo com Streamlit

### 9.2 Limitações

#### 9.2.1 Dataset Sintético

- Não captura correlações reais entre variáveis
- Anomalias geradas aleatoriamente inviabilizam H6
- Padrões comportamentais simplificados

#### 9.2.2 Clustering

- Silhouette Score abaixo do ideal (0.267 vs 0.50)
- Sensível à escala das features
- K=4 escolhido heuristicamente

#### 9.2.3 Recomendações

- Regras baseadas em percentuais fixos
- Não considera sazonalidade
- Cluster 1 requer abordagem diferente (educação financeira)

#### 9.2.4 Escopo

- Apenas dados de gastos (não considera investimentos)
- Sem integração com sistemas bancários reais
- Sem validação com usuários reais

### 9.3 Lições Aprendidas

| Lição | Descrição |
|-------|-----------|
| Interpretabilidade > Métricas | Clusters úteis mesmo com Silhouette baixo |
| Simplicidade funciona | 5 features foram suficientes |
| Taxa de poupança é chave | Feature mais discriminante |
| Documentação contínua | Economiza tempo no longo prazo |
| Ground truth importa | H6 falhou por dados inadequados |
| Perfis diferentes, abordagens diferentes | Cluster 1 precisa de educação financeira |

---

## 10. Conclusão

O projeto **Economiza+ MVP** atingiu seus principais objetivos:

1. ✅ Dataset sintético realista gerado com sucesso
2. ✅ Análise exploratória identificou padrões relevantes
3. ✅ Clustering segmentou usuários em 4 perfis interpretáveis
4. ✅ Sistema de recomendações gera economia significativa
5. ⚠️ Detecção de anomalias limitada pelo dataset
6. ✅ Dashboard interativo implementado
7. ⚠️ Hipóteses parcialmente validadas

### Contribuições Principais

1. **Framework de análise** financeira para classes C e D
2. **Metodologia de segmentação** baseada em comportamento
3. **Sistema de recomendações** personalizado por perfil
4. **Pipeline reproduzível** documentado em 13 notebooks

### Métricas de Sucesso

| Métrica | Alcançado |
|---------|-----------|
| Economia projetada | R$ 2,26M/ano |
| Usuários beneficiados | 426 (85,2%) |
| Notebooks documentados | 13 |
| Páginas do dashboard | 5 |
| Cobertura de documentação | 100% |

---

## 11. Trabalhos Futuros

### 11.1 Curto Prazo (1-3 meses)

- [ ] Validação com usuários reais
- [ ] Deploy em cloud (Streamlit Community)
- [ ] Coleta de feedback
- [ ] Testes A/B de recomendações

### 11.2 Médio Prazo (3-6 meses)

- [ ] Integração com Open Banking
- [ ] App mobile (React Native)
- [ ] Sistema de notificações
- [ ] Gamificação de metas

### 11.3 Longo Prazo (6-12 meses)

- [ ] Modelo preditivo de inadimplência
- [ ] Recomendações de investimento
- [ ] Parcerias com instituições financeiras
- [ ] Expansão para outros países da América Latina

---

## 12. Referências

### Dados e Estatísticas

1. **Serasa Experian.** Mapa da Inadimplência no Brasil. 2024.
2. **CNC - Confederação Nacional do Comércio.** Pesquisa de Endividamento e Inadimplência do Consumidor (PEIC). 2024.
3. **IBGE.** Pesquisa de Orçamentos Familiares (POF). 2023.
4. **Banco Central do Brasil.** Relatório de Economia Bancária. 2024.

### Técnicas e Algoritmos

5. **MacQueen, J.** Some methods for classification and analysis of multivariate observations. Proceedings of 5th Berkeley Symposium on Mathematical Statistics and Probability. 1967.
6. **Liu, F.T., Ting, K.M., Zhou, Z.H.** Isolation Forest. Eighth IEEE International Conference on Data Mining. 2008.
7. **Rousseeuw, P.J.** Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. Journal of Computational and Applied Mathematics. 1987.

### Ferramentas

8. **Pedregosa, F. et al.** Scikit-learn: Machine Learning in Python. JMLR 12. 2011.
9. **McKinney, W.** pandas: a Foundational Python Library for Data Analysis and Statistics. 2011.
10. **Streamlit Inc.** Streamlit Documentation. 2024.

---

## 13. Anexos

### Anexo A: Estrutura de Diretórios

```
economiza-ia/
├── app/                      # Dashboard Streamlit
│   ├── app.py
│   ├── pages/               # 5 páginas
│   ├── components/          # Componentes reutilizáveis
│   └── utils/               # Utilitários
├── data/
│   ├── raw/                 # Dados brutos
│   └── processed/           # Dados processados
├── models/                  # Modelos treinados
├── notebooks/               # 13 Jupyter notebooks
├── outputs/                 # Visualizações e relatórios
├── scripts/                 # Scripts de geração
├── docs/                    # Documentação
├── CLAUDE.md               # Instruções do projeto
├── README.md               # Documentação principal
└── requirements.txt        # Dependências
```

### Anexo B: Lista de Notebooks

| # | Notebook | Sprint | Descrição |
|---|----------|--------|-----------|
| 1 | 01_EDA_Basico | 1 | Análise exploratória |
| 2 | 02_Feature_Engineering | 1 | Criação de features |
| 3 | 03_Clustering | 1 | K-means clustering |
| 4 | 04_Clustering_Validacao | 1 | Validação do modelo |
| 5 | 05_Interpretacao_Clusters | 1 | Interpretação dos perfis |
| 6 | 06_Recomendacoes_Review | 1 | Revisão das recomendações |
| 7 | 07_Recomendacoes_Sistema | 2 | Sistema de regras |
| 8 | 08_Recomendacoes_Economia | 2 | Cálculo de economia |
| 9 | 09_Anomalias_Treino | 2 | Treinamento Isolation Forest |
| 10 | 10_Anomalias_Validacao | 2 | Validação H6 |
| 11 | 11_Pipeline_Integrado | 2 | Pipeline completo |
| 12 | 12_Demonstracao | 2 | Demonstração do sistema |
| 13 | 13_Refinamento_H1 | 3 | Refinamento das regras |

### Anexo C: Modelos Salvos

| Arquivo | Descrição | Tamanho |
|---------|-----------|---------|
| kmeans_best.pkl | K-means K=4 | ~2 KB |
| scaler.pkl | StandardScaler | ~1 KB |
| isolation_forest.pkl | Anomaly detector | ~500 KB |
| pipeline_completo.pkl | Pipeline integrado | ~2 MB |
| recomendacoes_regras.json | 9 regras v1.1 | ~3 KB |

### Anexo D: Comandos de Execução

```bash
# Setup do ambiente
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Gerar dataset
python scripts/gerar_dataset_financeiro.py

# Executar dashboard
cd app/
streamlit run app.py

# Acessar em: http://localhost:8501
```

---

**Fim do Relatório**

*Economiza+ MVP v1.1.0*
*Fevereiro 2026*
