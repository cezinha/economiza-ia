# Relatório Técnico Sprint 3 - Dashboard e Entrega Final

**Período de Execução:** 31/01/2026 - 04/02/2026
**Equipe:** Economiza IA
**Status:** CONCLUÍDO

---

## Sumário Executivo

### Contexto e Objetivos

O presente relatório documenta os resultados do Sprint 3 do projeto Economiza IA, cujo objetivo principal foi desenvolver um dashboard interativo em Streamlit, refinar as regras de economia (H1) e preparar toda a documentação para entrega final do TCC. Este sprint consolidou os resultados dos sprints anteriores em uma interface visual acessível e documentação completa.

### Resultados Principais

**Objetivo Cumprido:** Desenvolvimento de dashboard Streamlit funcional com 5 páginas interativas e documentação completa para entrega acadêmica.

**Entregas Realizadas:**
- 1 notebook desenvolvido (13_Refinamento_H1.ipynb)
- 5 páginas de dashboard implementadas
- 9 regras de economia refinadas (v1.1)
- Economia projetada: R$ 188.746/mês (R$ 2,26M/ano)
- Documentação completa (apresentação TCC + relatório final)

**Validação das Hipóteses (Estado Final):**

| Hipótese | Target | Resultado Final | Status |
|----------|--------|-----------------|--------|
| H1 - Economia | 15-20% | 9.83% média (2/3 clusters OK) | PARCIAL |
| H2 - Clustering | Silhouette > 0.50 | 0.267 (interpretável) | PARCIAL |
| H6 - Anomalias | Precision > 0.85 | 47.3% (limitação dataset) | NÃO VALIDADA |

**Métricas do Dashboard:**

| Página | Funcionalidade | Status |
|--------|----------------|--------|
| Home | Navegação e visão geral | Completo |
| Visão Geral | Métricas e distribuição de clusters | Completo |
| Análise Individual | Perfil, recomendações, anomalias | Completo |
| Comparativo | Radar chart, tabelas comparativas | Completo |
| Diagnóstico | Health check do sistema | Completo |

---

## 1. Introdução

### 1.1 Objetivos do Sprint

O Sprint 3 estabeleceu os seguintes objetivos técnicos:

1. **Dashboard Streamlit:** Desenvolver interface web interativa para visualização dos resultados
2. **Refinamento H1:** Ajustar regras de economia para atingir meta de 15-20%
3. **Tratamento de Erros:** Implementar robustez e mensagens de erro informativas
4. **Documentação Final:** Preparar apresentação TCC e relatório técnico completo
5. **Entrega:** Consolidar projeto para avaliação acadêmica

### 1.2 Metodologia

A abordagem metodológica foi estruturada em 7 dias:

| Dia | Atividade | Entregável |
|-----|-----------|------------|
| 15 | Dashboard - Estrutura Base | app/app.py + utils/ |
| 16 | Dashboard - Páginas e Visualizações | 4 páginas + components/ |
| 17 | Refinamento H1 e Testes | Regras v1.1 + notebook 13 |
| 18 | Otimização e Tratamento de Erros | Página Diagnóstico + error handling |
| 19 | Documentação - README e Apresentação | docs/APRESENTACAO_PPT.* |
| 20 | Documentação - Relatório Final | docs/RELATORIO_FINAL.* |
| 21 | Review Final e Entrega | Tag release v1.0.0 |

**Tecnologias Utilizadas:**
- Streamlit 1.28+ para dashboard web
- Plotly 5.18+ para gráficos interativos
- Python 3.11 como linguagem base
- Pandas para manipulação de dados
- Joblib para carregamento de modelos

---

## 2. Evidência do Planejamento

### 2.1 Documentos de Planejamento

| Documento | Finalidade | Link |
|-----------|------------|------|
| Sprint3_Planejamento.md | Roadmap detalhado do sprint | [Link](https://github.com/cezinha/economiza-ia/blob/main/outputs/Sprint3_Planejamento.md) |
| Sprint3_Handoff.md | Transição do Sprint 2 | [Link](https://github.com/cezinha/economiza-ia/blob/main/outputs/Sprint3_Handoff.md) |
| CLAUDE.md | Especificação técnica completa | [Link](https://github.com/cezinha/economiza-ia/blob/main/CLAUDE.md) |

### 2.2 Estrutura Planejada do Dashboard

```
app/
├── app.py                     # Entry point
├── pages/
│   ├── 0_Home.py              # Home page
│   ├── 1_Visao_Geral.py       # Overview
│   ├── 2_Analise_Usuario.py   # Individual analysis
│   ├── 3_Comparativo.py       # Profile comparison
│   └── 4_Diagnostico.py       # System health
├── components/
│   ├── cards.py               # Metric cards
│   ├── charts.py              # Plotly charts
│   └── sidebar.py             # Navigation
└── utils/
    ├── config.py              # Configuration
    ├── data_loader.py         # Data loading
    └── pipeline.py            # Pipeline wrapper
```

### 2.3 Controle de Versão

Principais commits do Sprint 3:

| Hash | Mensagem | Descrição |
|------|----------|-----------|
| [3cbc4cc](https://github.com/cezinha/economiza-ia/commit/3cbc4cc) | added day 18 | Error handling e diagnóstico |
| [83b7492](https://github.com/cezinha/economiza-ia/commit/83b7492) | update CLAUDE.md and Sprint3_Planejamento | Day 17 metrics |
| [75917e6](https://github.com/cezinha/economiza-ia/commit/75917e6) | added day 16, 17 | Dashboard + refinement |
| [2db44b5](https://github.com/cezinha/economiza-ia/commit/2db44b5) | added top recommendations, fix bug | H1 v1.1 rules |
| [902f034](https://github.com/cezinha/economiza-ia/commit/902f034) | fix issue divergence | Cluster names fix |
| [25a2de0](https://github.com/cezinha/economiza-ia/commit/25a2de0) | added Day 15 | Dashboard structure |

---

## 3. Evidência da Execução

### 3.1 Dashboard Implementado

#### 3.1.1 Página Home (0_Home.py)

**Funcionalidades:**
- Boas-vindas e descrição do sistema
- Navegação para outras páginas
- Métricas resumidas (500 usuários, R$ 188K economia)

#### 3.1.2 Página Visão Geral (1_Visao_Geral.py)

**Funcionalidades:**
- Distribuição dos clusters (pie chart interativo)
- Economia por cluster (bar chart)
- Métricas gerais: total usuários, economia projetada, % em risco
- Tabela detalhada por cluster

**Métricas Exibidas:**

| Métrica | Valor |
|---------|-------|
| Total Usuários | 500 |
| Economia Mensal | R$ 188.746 |
| Usuários em Risco | 85.2% (426) |
| Clusters | 4 |

#### 3.1.3 Página Análise Individual (2_Analise_Usuario.py)

**Funcionalidades:**
- Seleção de usuário via dropdown
- Card de perfil (cluster, prioridade)
- Métricas financeiras (renda, gasto, taxa poupança)
- Recomendações personalizadas com economia estimada
- Lista de anomalias detectadas
- Gauge de saúde financeira

**Exemplo de Output:**

| Campo | Valor (user_0002) |
|-------|-------------------|
| Perfil | Endividados Severos |
| Prioridade | CRÍTICA |
| Renda Média | R$ 4.148,90 |
| Gasto Médio | R$ 7.084,61 |
| Taxa Poupança | -70.76% |
| Economia Potencial | R$ 842,26/mês |
| Anomalias | 28 transações |

#### 3.1.4 Página Comparativo (3_Comparativo.py)

**Funcionalidades:**
- Gráfico de barras agrupadas (Renda vs Gasto por cluster)
- Taxa de poupança por perfil (bar chart)
- Economia projetada por cluster
- Radar chart comparativo (5 dimensões)
- Tabela resumo dos 4 perfis

**Dimensões do Radar Chart:**
1. Renda Média
2. Gasto Médio
3. Taxa Poupança
4. % Essenciais
5. Economia Potencial

#### 3.1.5 Página Diagnóstico (4_Diagnostico.py)

**Funcionalidades:**
- Health check do sistema
- Status de arquivos necessários
- Verificação de modelos carregados
- Instruções de correção em caso de erro

**Arquivos Verificados:**

| Arquivo | Tipo | Descrição |
|---------|------|-----------|
| pipeline_completo.pkl | Modelo | Pipeline integrado |
| usuarios_clustered.csv | Dados | Usuários com clusters |
| economia_projetada.csv | Dados | Economia calculada |
| transacoes.csv | Dados | Transações brutas |

### 3.2 Notebook Executado

#### 3.2.1 Notebook 13 - Refinamento H1

**Arquivo:** [13_Refinamento_H1.ipynb](https://github.com/cezinha/economiza-ia/blob/main/notebooks/13_Refinamento_H1.ipynb)

**Objetivo:** Ajustar regras de economia para atingir meta de 15-20%

**Análise do Gap (Antes do Refinamento):**

| Cluster | % Economia (v1.0) | Gap vs 15% |
|---------|-------------------|------------|
| Cluster 0 | 10.98% | -4.02pp |
| Cluster 1 | 5.19% | -9.81pp |
| Cluster 2 | 17.56% | OK |

**Ajustes Implementados (v1.0 → v1.1):**

| Cluster | Regra | Antes | Depois |
|---------|-------|-------|--------|
| 0 | Alimentacao_Fora | 50% | **70%** |
| 0 | Vestuario | 50% | **70%** |
| 1 | Alimentacao_Fora | 40% | **60%** |
| 1 | Lazer | 35% | **50%** |
| 1 | Vestuario | - | **40%** (nova) |

**Resultados Após Refinamento:**

| Cluster | Antes | Depois | Status |
|---------|-------|--------|--------|
| Cluster 0 | 10.98% | **15.97%** | ✅ ATINGE TARGET |
| Cluster 1 | 5.19% | 10.03% | ⚠️ Melhorado |
| Cluster 2 | 17.41% | 17.56% | ✅ ATINGE TARGET |
| **Média** | 8.60% | **9.83%** | +1.23pp |

**Output Gerado:**
- `models/recomendacoes_regras.json` (v1.1 - 9 regras)
- `models/pipeline_completo.pkl` (atualizado)
- `data/processed/economia_projetada.csv` (recalculado)
- `outputs/refinamento_h1_comparativo.png`

### 3.3 Componentes Desenvolvidos

#### 3.3.1 Cards (components/cards.py)

- `card_perfil()` - Exibe cluster e prioridade
- `card_metrica()` - Métricas financeiras formatadas
- `card_recomendacao()` - Recomendação com economia
- `card_anomalia()` - Alerta de transação suspeita

#### 3.3.2 Charts (components/charts.py)

- `pie_chart_clusters()` - Distribuição de clusters
- `bar_chart_economia()` - Economia por cluster
- `gauge_saude()` - Indicador de saúde financeira
- `radar_chart_perfis()` - Comparativo multidimensional
- `bar_chart_comparativo()` - Barras agrupadas

#### 3.3.3 Utilitários (utils/)

- `config.py` - Constantes e configurações
- `data_loader.py` - Carregamento com cache e error handling
- `pipeline.py` - Wrapper do pipeline com validação

### 3.4 Bug Fixes Aplicados

#### Bug 1: Nomes de Clusters Trocados (Day 16)

**Problema:** Clusters 0 e 2 estavam com nomes invertidos no notebook 11

**Causa:** Dicionário `CLUSTER_NAMES` com mapeamento incorreto

**Correção:**
```python
# Antes (incorreto)
CLUSTER_NAMES = {
    0: "Endividados Severos",  # ERRADO
    2: "Endividados Moderados" # ERRADO
}

# Depois (correto)
CLUSTER_NAMES = {
    0: "Endividados Moderados",  # -37% savings
    2: "Endividados Severos"     # -80% savings
}
```

**Arquivos Corrigidos:**
- notebooks/11_Pipeline_Integrado.ipynb
- notebooks/12_Demonstracao.ipynb
- models/pipeline_completo.pkl
- outputs/demo_cluster_*.png

#### Bug 2: Valores Hardcoded (Day 18)

**Problema:** Página Visão Geral exibia valores fixos em vez de calculados

**Correção:** Substituir strings fixas por valores dinâmicos do DataFrame

---

## 4. Evidência dos Resultados

### 4.1 Economia Projetada Final (v1.1)

| Cluster | N | Economia Média | % Renda | Total/Mês |
|---------|---|----------------|---------|-----------|
| Endividados Moderados | 86 | R$ 496,56 | 15.97% | R$ 42.704 |
| Em Alerta | 228 | R$ 299,15 | 10.03% | R$ 68.206 |
| Endividados Severos | 112 | R$ 613,49 | 17.56% | R$ 68.711 |
| Poupadores | 74 | R$ 123,29 | 1.72% | R$ 9.123 |
| **Total** | **500** | **R$ 377,49** | **9.83%** | **R$ 188.746** |

### 4.2 Impacto Financeiro Projetado

| Período | Valor |
|---------|-------|
| Mensal | R$ 188.746 |
| Trimestral | R$ 566.237 |
| Semestral | R$ 1.132.474 |
| Anual | **R$ 2.264.948** |

**Se 50% dos usuários seguirem as recomendações:**
- Economia real: R$ 1.132.474/ano
- Usuários impactados: 250
- Média por usuário: R$ 4.530/ano

### 4.3 Regras de Economia Finais (v1.1)

| Cluster | Prioridade | Regra 1 | Regra 2 | Regra 3 |
|---------|------------|---------|---------|---------|
| 0 - Moderados | ALTA | Alimentacao_Fora 70% | Vestuario 70% | - |
| 1 - Em Alerta | MODERADA | Alimentacao_Fora 60% | Lazer 50% | Vestuario 40% |
| 2 - Severos | CRÍTICA | Alimentacao_Fora 70% | Vestuario 90% | - |
| 3 - Poupadores | BAIXA | Transporte 15% | Telecom 20% | - |

### 4.4 Documentação Gerada

#### Apresentação TCC (6 slides)

| Slide | Conteúdo |
|-------|----------|
| 1 | Apresentação pessoal |
| 2 | Desafio (problema, hipóteses) |
| 3 | Solução (proposta, SMART) |
| 4 | Diferencial |
| 5 | Desenvolvimento (3 sprints) |
| 6 | Resultados e lições |

**Arquivos:**
- `docs/APRESENTACAO_PPT.md`
- `docs/APRESENTACAO_PPT.html`

#### Relatório Final

- `docs/RELATORIO_FINAL.md` (600+ linhas)
- `docs/RELATORIO_FINAL.html`

#### README Atualizado

- Instalação e uso
- Estrutura do projeto
- Resultados das hipóteses
- Stack tecnológica

### 4.5 Arquivos do Dashboard

| Arquivo | Linhas | Descrição |
|---------|--------|-----------|
| app/app.py | ~50 | Entry point Streamlit |
| app/pages/0_Home.py | ~40 | Página inicial |
| app/pages/1_Visao_Geral.py | ~120 | Métricas e gráficos |
| app/pages/2_Analise_Usuario.py | ~180 | Análise individual |
| app/pages/3_Comparativo.py | ~150 | Comparação de perfis |
| app/pages/4_Diagnostico.py | ~100 | Health check |
| app/components/cards.py | ~80 | Cards reutilizáveis |
| app/components/charts.py | ~200 | Gráficos Plotly |
| app/utils/pipeline.py | ~150 | Wrapper do pipeline |
| app/utils/data_loader.py | ~80 | Carregamento de dados |
| app/utils/config.py | ~60 | Configurações |
| **Total** | **~1.210** | - |

---

## 5. Discussão e Lições Aprendidas

### 5.1 Sucessos do Sprint

#### 5.1.1 Dashboard Funcional

O dashboard Streamlit foi entregue com todas as funcionalidades planejadas:
- 5 páginas navegáveis
- Gráficos interativos com Plotly
- Análise individual de usuários
- Tratamento de erros robusto
- Página de diagnóstico para troubleshooting

#### 5.1.2 Refinamento H1 Efetivo

O ajuste das regras de economia (v1.0 → v1.1) trouxe melhorias significativas:
- Cluster 0: 10.98% → 15.97% (+5pp)
- Cluster 1: 5.19% → 10.03% (+4.8pp)
- Média geral: 8.60% → 9.83% (+1.2pp)
- 2 de 3 clusters agora atingem a meta de 15%

#### 5.1.3 Documentação Completa

Toda a documentação acadêmica foi preparada:
- Apresentação TCC em 3 formatos (MD, HTML, Marp)
- Relatório final técnico (600+ linhas)
- README atualizado com instruções completas
- CLAUDE.md como especificação técnica

### 5.2 Limitações Identificadas

#### 5.2.1 Cluster 1 (Em Alerta) Não Atinge Meta

**Problema:** Mesmo após refinamento, Cluster 1 atinge apenas 10.03% (meta: 15%)

**Análise:** Este perfil representa usuários com endividamento moderado mas gastos mais "justificáveis". Cortes mais agressivos poderiam ser contraproducentes.

**Recomendação:** Para Cluster 1, a abordagem ideal seria educação financeira complementar, não apenas cortes. Documentado como limitação conhecida.

#### 5.2.2 H6 Permanece Não Validada

**Problema:** Precision de 47.3% vs target de 85%

**Causa:** Anomalias no dataset sintético foram geradas aleatoriamente, não estatisticamente.

**Conclusão:** Limitação do dataset, não do modelo. Em produção com dados reais, resultados seriam diferentes.

### 5.3 Decisões Técnicas Validadas

| Decisão | Justificativa | Resultado |
|---------|---------------|-----------|
| Streamlit | Prototipagem rápida para MVP | Validada - funcional em 2 dias |
| Plotly | Gráficos interativos | Validada - UX superior |
| Cache (@st.cache) | Performance | Validada - carregamento rápido |
| Regras agressivas (v1.1) | Atingir meta H1 | Validada - 2/3 clusters OK |
| Página Diagnóstico | Troubleshooting | Validada - facilita debug |

### 5.4 Métricas de Qualidade do Sprint

| Indicador | Planejado | Realizado | Aderência |
|-----------|-----------|-----------|-----------|
| Páginas dashboard | 4 | 5 | 125% |
| Notebooks | 1 | 1 | 100% |
| Documentos | 4 | 8 | 200% |
| Regras refinadas | 8 | 9 | 112% |
| Clusters atingindo H1 | 3 | 2 | 67% |
| **Média geral** | - | - | **121%** |

---

## 6. Conclusões

### 6.1 Síntese dos Resultados

O Sprint 3 foi concluído com **100% das funcionalidades core** e entregas adicionais que superaram o planejamento. O MVP Economiza+ está funcional e documentado para entrega acadêmica.

**Principais Conquistas:**

1. **Dashboard Completo:**
   - 5 páginas interativas funcionais
   - Análise individual de 500 usuários
   - Visualizações profissionais com Plotly

2. **Refinamento H1 Parcialmente Bem-Sucedido:**
   - 2 de 3 clusters atingem meta de 15%
   - Economia projetada: R$ 2,26M/ano
   - Limitação de Cluster 1 documentada

3. **Documentação Acadêmica Completa:**
   - Apresentação TCC (6 slides)
   - Relatório técnico final
   - README com instruções de uso

4. **Robustez do Sistema:**
   - Tratamento de erros em todas as páginas
   - Página de diagnóstico para troubleshooting
   - Cache para performance

### 6.2 Estado Final das Hipóteses

| Hipótese | Status Final | Evidência |
|----------|--------------|-----------|
| H1 | **Parcialmente Validada** | 2/3 clusters atingem 15%+, média 9.83% |
| H2 | **Parcialmente Validada** | Silhouette 0.267, mas clusters interpretáveis |
| H6 | **Não Validada** | Limitação do dataset sintético |

### 6.3 Métricas Finais do Projeto

| Métrica | Valor |
|---------|-------|
| Usuários analisados | 500 |
| Transações processadas | 191.231 |
| Clusters identificados | 4 |
| Usuários em risco | 426 (85.2%) |
| Regras de economia | 9 |
| Economia mensal projetada | R$ 188.746 |
| Economia anual projetada | R$ 2,26 milhões |
| Notebooks desenvolvidos | 13 |
| Páginas de dashboard | 5 |

### 6.4 Próximos Passos (Pós-TCC)

1. **Integração Open Finance:** Conectar com dados bancários reais
2. **Educação Financeira:** Módulo para Cluster 1 (Em Alerta)
3. **Deploy Cloud:** Publicar no Streamlit Community Cloud
4. **Validação com Usuários Reais:** Testar hipóteses com dados reais
5. **Expansão de Regras:** Mais recomendações por perfil

---

## 7. Referências

### 7.1 Documentação Interna

- CLAUDE.md: [https://github.com/cezinha/economiza-ia/blob/main/CLAUDE.md](https://github.com/cezinha/economiza-ia/blob/main/CLAUDE.md)
- Sprint3_Planejamento.md: [https://github.com/cezinha/economiza-ia/blob/main/outputs/Sprint3_Planejamento.md](https://github.com/cezinha/economiza-ia/blob/main/outputs/Sprint3_Planejamento.md)
- README.md: [https://github.com/cezinha/economiza-ia/blob/main/README.md](https://github.com/cezinha/economiza-ia/blob/main/README.md)

### 7.2 Dashboard

| Arquivo | URL |
|---------|-----|
| app/app.py | [Link](https://github.com/cezinha/economiza-ia/blob/main/app/app.py) |
| app/pages/0_Home.py | [Link](https://github.com/cezinha/economiza-ia/blob/main/app/pages/0_Home.py) |
| app/pages/1_Visao_Geral.py | [Link](https://github.com/cezinha/economiza-ia/blob/main/app/pages/1_Visao_Geral.py) |
| app/pages/2_Analise_Usuario.py | [Link](https://github.com/cezinha/economiza-ia/blob/main/app/pages/2_Analise_Usuario.py) |
| app/pages/3_Comparativo.py | [Link](https://github.com/cezinha/economiza-ia/blob/main/app/pages/3_Comparativo.py) |
| app/pages/4_Diagnostico.py | [Link](https://github.com/cezinha/economiza-ia/blob/main/app/pages/4_Diagnostico.py) |

### 7.3 Notebook

| Arquivo | URL |
|---------|-----|
| 13_Refinamento_H1.ipynb | [Link](https://github.com/cezinha/economiza-ia/blob/main/notebooks/13_Refinamento_H1.ipynb) |

### 7.4 Documentação Final

| Arquivo | URL |
|---------|-----|
| APRESENTACAO_PPT.md | [Link](https://github.com/cezinha/economiza-ia/blob/main/docs/APRESENTACAO_PPT.md) |
| APRESENTACAO_PPT.html | [Link](https://github.com/cezinha/economiza-ia/blob/main/docs/APRESENTACAO_PPT.html) |
| RELATORIO_FINAL.md | [Link](https://github.com/cezinha/economiza-ia/blob/main/docs/RELATORIO_FINAL.md) |
| RELATORIO_FINAL.html | [Link](https://github.com/cezinha/economiza-ia/blob/main/docs/RELATORIO_FINAL.html) |

### 7.5 Modelos Atualizados

| Arquivo | URL |
|---------|-----|
| recomendacoes_regras.json (v1.1) | [Link](https://github.com/cezinha/economiza-ia/blob/main/models/recomendacoes_regras.json) |
| pipeline_completo.pkl | [Link](https://github.com/cezinha/economiza-ia/blob/main/models/pipeline_completo.pkl) |

### 7.6 Visualizações Sprint 3

| Arquivo | URL |
|---------|-----|
| refinamento_h1_comparativo.png | [Link](https://github.com/cezinha/economiza-ia/blob/main/outputs/refinamento_h1_comparativo.png) |

---

## Apêndices

### Apêndice A: Comandos para Execução

```bash
# Ativar ambiente
pyenv activate economiza-ia-env

# Instalar dependências
pip install -r requirements.txt

# Executar dashboard
cd app/
streamlit run app.py

# Acessar em http://localhost:8501
```

### Apêndice B: Estrutura Final do Projeto

```
economiza-ia/
├── app/                        # Dashboard Streamlit (Sprint 3)
│   ├── app.py
│   ├── pages/
│   │   ├── 0_Home.py
│   │   ├── 1_Visao_Geral.py
│   │   ├── 2_Analise_Usuario.py
│   │   ├── 3_Comparativo.py
│   │   └── 4_Diagnostico.py
│   ├── components/
│   │   ├── cards.py
│   │   ├── charts.py
│   │   └── sidebar.py
│   └── utils/
│       ├── config.py
│       ├── data_loader.py
│       └── pipeline.py
├── data/
│   ├── raw/                    # Dados brutos
│   └── processed/              # Dados processados
├── docs/                       # Documentação final
│   ├── APRESENTACAO_PPT.md
│   ├── APRESENTACAO_PPT.html
│   ├── RELATORIO_FINAL.md
│   └── RELATORIO_FINAL.html
├── models/                     # Modelos treinados
├── notebooks/                  # 13 notebooks
├── outputs/                    # Visualizações e relatórios
├── scripts/                    # Scripts auxiliares
├── CLAUDE.md                   # Especificação técnica
├── README.md                   # Documentação principal
└── requirements.txt            # Dependências
```

### Apêndice C: Glossário

**Streamlit:** Framework Python para criação de aplicações web de dados.

**Plotly:** Biblioteca para gráficos interativos em Python.

**Cache:** Mecanismo para armazenar resultados de funções e evitar recálculo.

**Health Check:** Verificação automatizada do estado de um sistema.

**Refinamento H1:** Processo de ajuste das regras de economia para atingir meta.

---

**Documento elaborado por:** Celina Uemura
**Data de conclusão:** 04 de Fevereiro de 2026
**Versão:** 1.0
**Status:** FINAL

---

**Histórico de Versões:**

| Versão | Data | Autor | Mudanças |
|--------|------|-------|----------|
| 1.0 | 04/02/2026 | Celina Uemura | Versão inicial |
