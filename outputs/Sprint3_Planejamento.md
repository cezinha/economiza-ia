# Sprint 3 - Planejamento
## Economiza+ MVP - Dashboard e Entrega Final

**Período:** Janeiro/Fevereiro 2026
**Duração:** 7 dias (Dias 15-21)
**Foco:** Dashboard Streamlit, Refinamento H1 e Documentação Final

---

## Progresso Atual

| Dia | Atividade | Status |
|-----|-----------|--------|
| 15 | Dashboard - Estrutura Base | ✅ Concluído |
| 16 | Dashboard - Páginas e Visualizações | ✅ Concluído |
| 17 | Refinamento H1 e Testes | ✅ Concluído |
| 18 | Otimização e Tratamento de Erros | ✅ Concluído |
| 19 | Documentação - README e Apresentação | ✅ Concluído |
| 20 | Documentação - Relatório Final | ✅ Concluído |
| 21 | Review Final e Entrega | ⏳ Próximo |

**Progresso:** 6/7 dias (86%)

---

## Objetivos do Sprint

| Objetivo | Descrição | Entregável |
|----------|-----------|------------|
| Dashboard | Interface web interativa com Streamlit | `app/app.py` funcional |
| Refinamento H1 | Ajustar regras para clusters 1-3 | Regras atualizadas |
| Documentação | Apresentação e relatório final | PDF/Slides |
| Entrega | Projeto completo e funcional | Tag release no Git |

---

## Estado Atual (Herança Sprint 2)

### Hipóteses

| Hipótese | Status Sprint 2 | Ação Sprint 3 | Status Atual |
|----------|-----------------|---------------|--------------|
| H1 | Parcial (8.60% global, **17.56% Cluster 2**) | Ajustar regras clusters 0, 1 | ✅ Refinado (9.83% global, 2/3 atingem target) |
| H2 | Parcial (Silhouette 0.267, interpretavel) | Manter | ✅ Mantido |
| H6 | Não validada (P=47.3%, R=47.4%) | Documentar limitação do dataset | ✅ Documentado |

### Artefatos Disponíveis

| Artefato | Status | Localização |
|----------|--------|-------------|
| Pipeline completo | Pronto | `models/pipeline_completo.pkl` |
| K-means K=4 | Pronto | `models/kmeans_best.pkl` |
| Isolation Forest | Pronto | `models/isolation_forest.pkl` |
| Regras de economia | Pronto | `models/recomendacoes_regras.json` |
| Usuários clusterizados | Pronto | `data/processed/usuarios_clustered.csv` |
| Economia projetada | Pronto | `data/processed/economia_projetada.csv` |
| Transações | Pronto | `data/raw/transacoes.csv` (194K) |

---

## Restrições (Pré-definidas)

- **Dashboard:** Streamlit (não Flask/Django)
- **Gráficos:** Matplotlib/Seaborn ou Plotly (opcional)
- **Ambiente:** Google Colab para notebooks, local para Streamlit
- **Deploy:** Local (não cloud obrigatório)
- **Dados:** Dataset sintético (LGPD)

---

## Backlog Sprint 3

### Dia 15: Dashboard Streamlit - Estrutura Base
**Objetivo:** Criar estrutura do app e página principal
**Status:** CONCLUÍDO

**Tarefas:**
- [x] Instalar dependências: `pip install streamlit plotly`
- [x] Criar estrutura de pastas:
  ```
  app/
  ├── app.py
  ├── pages/
  ├── components/
  └── utils/
  ```
- [x] Implementar `app.py` com layout base
- [x] Criar sidebar com seleção de usuário
- [x] Implementar carregamento do pipeline com `@st.cache_resource`
- [x] Testar execução local: `streamlit run app/app.py`

**Entregáveis:**
- [x] `app/app.py` - Aplicação base funcionando
- [x] `app/utils/pipeline.py` - Wrapper do pipeline
- [x] `app/utils/config.py` - Configurações
- [x] `app/utils/data_loader.py` - Carregamento de dados
- [x] `app/components/cards.py` - Componentes de cards
- [x] `app/components/charts.py` - Componentes de gráficos
- [x] `app/components/sidebar.py` - Componente de sidebar
- [x] `app/pages/1_Visao_Geral.py` - Página de visão geral
- [x] `app/pages/2_Analise_Usuario.py` - Página de análise individual
- [x] `app/pages/3_Comparativo.py` - Página comparativa

### Dia 16: Dashboard Streamlit - Páginas e Visualizações
**Objetivo:** Implementar páginas e componentes visuais
**Status:** CONCLUÍDO

**Tarefas:**
- [x] Página 1 - Visão Geral (`pages/1_Visao_Geral.py`):
  - Distribuição dos clusters (pie chart)
  - Métricas gerais (total usuários, economia projetada)
  - Estatísticas detalhadas por cluster
- [x] Página 2 - Análise Individual (`pages/2_Analise_Usuario.py`):
  - Seleção de usuário
  - Cards: perfil, renda, gasto, taxa poupança
  - Recomendações personalizadas com economia
  - Lista de anomalias detectadas
  - Gauge de saúde financeira
- [x] Página 3 - Comparativo (`pages/3_Comparativo.py`):
  - Comparação entre os 4 clusters
  - Gráficos de barras comparativos (renda vs gasto)
  - Radar chart por cluster
  - Tabela resumo
- [x] Componentes reutilizáveis criados:
  - `components/cards.py` - Cards de métricas
  - `components/charts.py` - Gráficos Plotly
- [x] Bug fix: Correção dos nomes dos clusters (0 e 2 estavam trocados)

**Entregáveis:**
- [x] 3 páginas funcionais + Home
- [x] Componentes reutilizáveis
- [x] Bug fix documentado

### Dia 17: Refinamento H1 e Testes
**Objetivo:** Ajustar regras de economia e testar sistema
**Status:** CONCLUÍDO

**Tarefas:**
- [x] Analisar gap por cluster:
  - Cluster 0: 10.98% (gap -4pp)
  - Cluster 1: 5.19% (gap -10pp)
  - Cluster 2: 17.56% (OK)
  - Cluster 3: N/A (controle)
- [x] Ajustes implementados nas regras (v1.0 → v1.1):
  - Cluster 0: Alimentacao_Fora 50%→70%, Vestuario 50%→70%
  - Cluster 1: Alimentacao_Fora 40%→60%, Lazer 35%→50%, **+Vestuario 40%**
- [x] Criado notebook `13_Refinamento_H1.ipynb`
- [x] Recalculada economia projetada com novas regras
- [x] Atualizado `pipeline_completo.pkl` com novas regras
- [x] Testado dashboard com usuários de todos os clusters
- [x] Validada reprodutibilidade (3 execuções idênticas)

**Resultados:**
| Cluster | Antes | Depois | Status |
|---------|-------|--------|--------|
| 0 | 10.98% | **15.97%** | ✅ ATINGE TARGET |
| 1 | 5.19% | 10.03% | ⚠️ Melhora significativa |
| 2 | 17.41% | 17.56% | ✅ ATINGE TARGET |
| Média | 8.60% | **9.83%** | +1.23pp |

**Entregáveis:**
- [x] `models/recomendacoes_regras.json` (v1.1, 9 regras)
- [x] `models/pipeline_completo.pkl` (atualizado)
- [x] `data/processed/economia_projetada.csv` (recalculado)
- [x] `notebooks/13_Refinamento_H1.ipynb`
- [x] Limitação Cluster 1 documentada (requer educação financeira)

### Dia 18: Otimização e Tratamento de Erros
**Objetivo:** Garantir robustez e performance
**Status:** CONCLUÍDO

**Tarefas:**
- [x] Adicionar tratamento de erros no dashboard:
  - Usuário não encontrado (com mensagem contextual)
  - Dados faltantes (com fallback para DataFrames vazios)
  - Erros de carregamento (com sugestões de correção)
- [x] Otimizar performance:
  - Cache de dados pesados (`@st.cache_data`, `@st.cache_resource`)
  - `show_spinner=False` para controle fino de loading
- [x] Melhorar UX:
  - Mensagens de loading com `st.spinner()`
  - Links para página de Diagnóstico em erros
  - Valores dinâmicos (corrigido hardcoded em Visão Geral)
- [x] Criar página de Diagnóstico do Sistema
- [x] Atualizar config.py com métricas v1.1

**Entregáveis:**
- [x] `app/utils/data_loader.py` - Error handling robusto
- [x] `app/utils/pipeline.py` - Validações e health check
- [x] `app/pages/4_Diagnostico.py` - Nova página de diagnóstico
- [x] Todas as páginas com tratamento de erro melhorado
- [x] Valores dinâmicos em vez de hardcoded

### Dia 19: Documentação - README e Apresentação
**Objetivo:** Preparar documentação para entrega acadêmica
**Status:** CONCLUÍDO

**Tarefas:**
- [x] Atualizar `README.md` completo:
  - Descrição do projeto com métricas
  - Instalação e uso (dashboard + notebooks)
  - Estrutura do projeto atualizada
  - Resultados e validação das hipóteses
  - Stack tecnológica completa
- [x] Criar apresentação em 3 formatos:
  - `docs/APRESENTACAO.md` - Markdown simples
  - `docs/APRESENTACAO_SLIDES.md` - Formato Marp (slides)
  - `docs/APRESENTACAO.html` - HTML (print to PDF)
- [x] Apresentação com 12 slides:
  - Slide 1: Título e equipe
  - Slide 2: Problema e contexto brasileiro
  - Slide 3: Solução Economiza+
  - Slide 4: Metodologia (3 sprints)
  - Slide 5: Sprint 1 - Segmentação (4 perfis)
  - Slide 6: Sprint 2 - Recomendações
  - Slide 7: Sprint 3 - Dashboard
  - Slide 8: Validação das hipóteses
  - Slide 9: Lições aprendidas
  - Slide 10: Próximos passos
  - Slide 11: Métricas finais
  - Slide 12: Obrigado
- [x] Documentação para geração de PDF (`docs/README.md`)

**Entregáveis:**
- [x] `README.md` - Documentação principal atualizada
- [x] `docs/APRESENTACAO.md` - Apresentação Markdown
- [x] `docs/APRESENTACAO_SLIDES.md` - Apresentação Marp
- [x] `docs/APRESENTACAO.html` - Apresentação HTML (print to PDF)
- [x] `docs/README.md` - Instruções de geração de PDF

### Dia 20: Documentação - Relatório Final
**Objetivo:** Consolidar documentação técnica
**Status:** CONCLUÍDO

**Tarefas:**
- [x] Criar relatório final em 2 formatos:
  - `docs/RELATORIO_FINAL.md` - Markdown completo (600+ linhas)
  - `docs/RELATORIO_FINAL.html` - HTML para impressão PDF
- [x] Conteúdo do relatório:
  - Resumo executivo com métricas
  - Introdução e contexto brasileiro
  - Objetivos e hipóteses
  - Metodologia (3 sprints, stack, dataset)
  - Resultados Sprint 1 (4 perfis identificados)
  - Resultados Sprint 2 (sistema de recomendações)
  - Resultados Sprint 3 (dashboard, refinamento)
  - Validação das 3 hipóteses
  - Discussão e limitações
  - Conclusão
  - Trabalhos futuros
  - Referências bibliográficas
  - Anexos (estrutura, notebooks, comandos)
- [x] Verificar consistência: 13 notebooks confirmados
- [x] Atualizar `docs/README.md` com instruções

**Entregáveis:**
- [x] `docs/RELATORIO_FINAL.md` - Relatório técnico Markdown
- [x] `docs/RELATORIO_FINAL.html` - Versão HTML (print to PDF)
- [x] `docs/README.md` - Instruções atualizadas
- [ ] Vídeo demonstração (opcional - não implementado)

### Dia 21: Review Final e Entrega
**Objetivo:** Finalizar e entregar projeto

**Tarefas:**
- [ ] Review final com orientador (se aplicável)
- [ ] Ajustes de última hora
- [ ] Verificar checklist de entrega
- [ ] Criar tag de release no Git: `v1.0.0`
- [ ] Fazer backup completo
- [ ] Entrega oficial

**Checklist de Entrega:**
- [ ] Dashboard funcionando localmente
- [ ] 12+ notebooks executáveis
- [ ] Modelos salvos e documentados
- [ ] README.md completo
- [ ] Apresentação PDF
- [ ] Relatório final PDF
- [ ] CLAUDE.md atualizado
- [ ] Tag de release criada

---

## Estrutura do Dashboard

### Arquitetura de Arquivos

```
app/
├── app.py                     # Streamlit main entry point
├── pages/
│   ├── 0_Home.py              # Home page (landing)
│   ├── 1_Visao_Geral.py       # Overview page
│   ├── 2_Analise_Usuario.py   # Individual analysis
│   ├── 3_Comparativo.py       # Cluster comparison
│   └── 4_Diagnostico.py       # System health check (Day 18)
├── components/
│   ├── __init__.py
│   ├── cards.py               # Metric cards component
│   ├── charts.py              # Chart components
│   └── sidebar.py             # Sidebar component
└── utils/
    ├── __init__.py
    ├── pipeline.py            # Pipeline wrapper
    ├── data_loader.py         # Data loading utilities
    └── config.py              # App configuration
```

### Wireframe das Páginas

**Página 1 - Visão Geral:**
```
+----------------------------------+
| ECONOMIZA+ MVP                   |
+----------------------------------+
| [Card: 500 usuários]             |
| [Card: R$ 189K economia/mês]     |
| [Card: 85.2% em risco]           |
+----------------------------------+
| [Pie Chart: Distribuição]        |
| [Bar Chart: Economia por cluster]|
+----------------------------------+
```

**Página 2 - Análise Individual:**
```
+----------------------------------+
| Selecione o usuário: [dropdown]  |
| [Botão: Analisar]                |
+----------------------------------+
| PERFIL: Endividados Severos      |
| Renda: R$ 4.148  | Gasto: R$ 7.084|
| Taxa Poupança: -70.76%           |
+----------------------------------+
| RECOMENDAÇÕES:                   |
| 1. Cortar Alimentação Fora 70%   |
|    Economia: R$ 450/mês          |
| 2. Eliminar Vestuário 90%        |
|    Economia: R$ 392/mês          |
+----------------------------------+
| ANOMALIAS DETECTADAS: 28         |
| [Lista de transações suspeitas]  |
+----------------------------------+
```

**Página 3 - Comparativo:**
```
+----------------------------------+
| COMPARATIVO ENTRE PERFIS         |
+----------------------------------+
| [Grouped Bar: Renda vs Gasto]    |
| [Bar: Taxa de Poupanca]          |
| [Bar: Economia Potencial]        |
+----------------------------------+
| [Tabela resumo dos 4 clusters]   |
+----------------------------------+
```

---

## Artefatos Esperados

### Código

| Arquivo | Descrição | Status |
|---------|-----------|--------|
| `app/app.py` | Aplicação Streamlit principal | ✅ |
| `app/pages/*.py` | 5 páginas do dashboard (Home, Visão Geral, Análise, Comparativo, Diagnóstico) | ✅ |
| `app/components/*.py` | Componentes reutilizáveis (cards, charts, sidebar) | ✅ |
| `app/utils/*.py` | Utilitários (pipeline, data_loader, config) | ✅ |

### Notebooks

| Arquivo | Descrição | Status |
|---------|-----------|--------|
| `notebooks/13_Refinamento_H1.ipynb` | Refinamento H1 (Dia 17) | ✅ Criado |

### Documentação

| Arquivo | Descrição | Status |
|---------|-----------|--------|
| `README.md` | Documentação principal atualizada | ✅ |
| `docs/APRESENTACAO.md` | Apresentação em Markdown | ✅ |
| `docs/APRESENTACAO_SLIDES.md` | Apresentação formato Marp | ✅ |
| `docs/APRESENTACAO.html` | Apresentação HTML (print to PDF) | ✅ |
| `docs/RELATORIO_FINAL.md` | Relatório técnico Markdown | ✅ |
| `docs/RELATORIO_FINAL.html` | Relatório HTML (print to PDF) | ✅ |
| `docs/README.md` | Instruções de geração de PDF | ✅ |
| `outputs/Sprint3_Resumo.md` | Resumo tecnico do Sprint 3 | ⏳ Dia 21 |
| `outputs/Sprint3_Review.md` | Review executivo | ⏳ Dia 21 |

### Visualizações

| Arquivo | Descrição | Status |
|---------|-----------|--------|
| `outputs/refinamento_h1_comparativo.png` | Comparativo antes/depois H1 | ✅ Criado (Dia 17) |
| `outputs/screenshot_dashboard_*.png` | Screenshots do dashboard | ⏳ Opcional |
| `outputs/demo_video.mp4` | Vídeo demonstração | ⏳ Opcional (não implementado) |

---

## Critérios de Sucesso

| Critério | Target | Status | Como Medir |
|----------|--------|--------|------------|
| Dashboard funcional | Sim | ✅ | Executa sem erros localmente |
| 3 páginas implementadas | Sim | ✅ | Todas navegáveis (+ Home + Diagnóstico) |
| Análise de usuário funciona | Sim | ✅ | Retorna perfil, recomendações, anomalias |
| H1 refinado | 2/3 clusters | ✅ | Clusters 0 e 2 atingem 15%+ |
| README completo | Sim | ✅ | Instruções claras de instalação e uso |
| Apresentação pronta | 12 slides | ✅ | 3 formatos (MD, Marp, HTML) |
| Relatório final | Sim | ✅ | MD + HTML (600+ linhas) |
| Notebooks executáveis | 13 | ✅ | Todos rodam sem erro |
| Release tag | v1.0.0 | ⏳ | Tag criada no Git (Dia 21) |

---

## Dependencias Sprint 2

Artefatos necessarios (ja existem):

- [x] `models/pipeline_completo.pkl` - Pipeline integrado
- [x] `models/kmeans_best.pkl` - Modelo de clustering
- [x] `models/scaler.pkl` - Normalizador
- [x] `models/isolation_forest.pkl` - Detector de anomalias
- [x] `models/recomendacoes_regras.json` - Regras de economia
- [x] `data/processed/usuarios_clustered.csv` - Usuários com clusters
- [x] `data/processed/economia_projetada.csv` - Economia por usuário
- [x] `data/raw/transacoes.csv` - Transações
- [x] `outputs/demo_cluster_*.png` - Dashboards de demonstracao

---

## Dependências Técnicas

### Instalação

```bash
# Dependências Sprint 3
pip install streamlit>=1.28.0
pip install plotly>=5.18.0

# Verificar instalação
streamlit --version
```

### Execução Local

```bash
# Navegar para pasta do app
cd app/

# Executar dashboard
streamlit run app.py

# Acessar em: http://localhost:8501
```

---

## Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação | Status |
|-------|---------------|---------|-----------|--------|
| Tempo insuficiente para dashboard completo | Média | Alto | Priorizar funcionalidades essenciais (MVP) | ✅ Mitigado |
| Problemas de compatibilidade Streamlit | Baixa | Médio | Testar versões, usar ambiente virtual | ✅ Sem problemas |
| H1 não atingir target global | Alta | Baixo | Documentar como limitação conhecida | ✅ Refinado (2/3 atingem) |
| Falta de tempo para documentação | Média | Alto | Começar documentação no dia 19 | ✅ Documentação completa |
| Bugs de última hora | Média | Médio | Buffer no dia 21 para ajustes | ✅ Sistema estável |

---

## Prioridades (MoSCoW)

### Must Have (Obrigatório)
- [x] Dashboard Streamlit básico funcionando ✅ (Dia 15)
- [x] Página de análise individual ✅ (Dia 15-16)
- [x] README.md atualizado ✅ (Dia 19)
- [x] Apresentação PDF ✅ (Dia 19 - 3 formatos)

### Should Have (Importante)
- [x] 3 páginas completas ✅ (Dia 15-16)
- [x] Relatório final PDF ✅ (Dia 20 - MD + HTML)
- [x] Tratamento de erros básico ✅ (Dia 18)
- [ ] Screenshots do dashboard (opcional)

### Could Have (Desejável)
- [x] Gráficos interativos com Plotly ✅ (Dia 15-16)
- [x] Refinamento das regras H1 ✅ (Dia 17)
- [ ] Vídeo demonstração (não implementado)
- [ ] Deploy em cloud (Streamlit Community) (não implementado)

### Won't Have (Fora do escopo)
- API REST (FastAPI)
- Autenticação de usuários
- Banco de dados em tempo real
- App mobile

---

## Código Base - Quick Start

### app/app.py

```python
import streamlit as st
import pickle
import pandas as pd
import sys
sys.path.append('..')

st.set_page_config(
    page_title="Economiza+ MVP",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_pipeline():
    with open('../models/pipeline_completo.pkl', 'rb') as f:
        return pickle.load(f)

@st.cache_data
def load_data():
    usuarios = pd.read_csv('../data/processed/usuarios_clustered.csv')
    transacoes = pd.read_csv('../data/raw/transacoes.csv')
    return usuarios, transacoes

# Carregar dados
pipeline_data = load_pipeline()
usuarios, transacoes = load_data()

# Título
st.title("💰 Economiza+ MVP")
st.subheader("Sistema de Análise Financeira e Recomendações Personalizadas")

# Métricas gerais
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Usuários", "500")
col2.metric("Economia Projetada/Mês", "R$ 188.746")
col3.metric("Usuários em Risco", "85.2%")
col4.metric("Clusters", "4")

st.markdown("---")
st.info("👈 Use o menu lateral para navegar entre as paginas")
```

---

## Cronograma Visual

```
Dia 15 |████████| Dashboard - Estrutura Base          ✅ CONCLUÍDO
Dia 16 |████████| Dashboard - Páginas e Visualizações ✅ CONCLUÍDO
Dia 17 |████████| Refinamento H1 e Testes             ✅ CONCLUÍDO
Dia 18 |████████| Otimização e Tratamento de Erros    ✅ CONCLUÍDO
Dia 19 |████████| Documentação - README e Apresentação ✅ CONCLUÍDO
Dia 20 |████████| Documentação - Relatório Final      ✅ CONCLUÍDO
Dia 21 |████████| Review Final e Entrega              ⏳ PRÓXIMO
```

---

## Notas Importantes

1. **Foco em MVP:** Entregar funcional antes de perfeito
2. **Documentação contínua:** Não deixar para o último dia
3. **Testes frequentes:** Validar dashboard a cada mudança
4. **Backup diário:** Commits frequentes no Git
5. **Reutilizar visualizações:** Usar outputs do Sprint 2 como referência
6. **Simplicidade:** Streamlit puro, sem frameworks adicionais

---

**Documento criado em:** 31 de Janeiro de 2026
**Última atualização:** 04 de Fevereiro de 2026
**Versão:** 1.8
**Status:** Dias 15-20 concluídos (86%), Dia 21 em andamento - ENTREGA FINAL

---

## Histórico de Atualizações

| Data | Versão | Alterações |
|------|--------|------------|
| 31/01/2026 | 1.0 | Documento inicial |
| 01/02/2026 | 1.1 | Dia 15 concluído - Dashboard estrutura base |
| 01/02/2026 | 1.2 | Dia 16 concluído - Páginas e bug fix cluster names |
| 02/02/2026 | 1.3 | Dia 17 concluído - Refinamento H1 (regras v1.1) |
| 03/02/2026 | 1.4 | Consolidação Day 17, preparação Day 18 |
| 03/02/2026 | 1.5 | Dia 18 concluído - Error handling, página diagnóstico |
| 03/02/2026 | 1.6 | Dia 19 concluído - README e apresentação (3 formatos) |
| 03/02/2026 | 1.7 | Dia 20 concluído - Relatório final (MD + HTML) |
| 04/02/2026 | 1.8 | Atualização critérios, cronograma visual, prioridades MoSCoW |
