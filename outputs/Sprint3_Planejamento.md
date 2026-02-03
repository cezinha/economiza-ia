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
| 18 | Otimização e Tratamento de Erros | ⏳ Próximo |
| 19 | Documentação - README e Apresentação | ⏳ Pendente |
| 20 | Documentação - Relatório Final | ⏳ Pendente |
| 21 | Review Final e Entrega | ⏳ Pendente |

**Progresso:** 3/7 dias (43%)

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

**Tarefas:**
- [ ] Adicionar tratamento de erros no dashboard:
  - Usuário não encontrado
  - Dados faltantes
  - Erros de carregamento
- [ ] Otimizar performance:
  - Cache de dados pesados
  - Lazy loading de gráficos
- [ ] Melhorar UX:
  - Mensagens de loading
  - Tooltips explicativos
  - Cores consistentes por cluster
- [ ] Testar em diferentes navegadores
- [ ] Documentar requisitos mínimos

**Entregáveis:**
- Dashboard robusto
- Tratamento de erros implementado

### Dia 19: Documentação - README e Apresentação
**Objetivo:** Preparar documentação para entrega acadêmica

**Tarefas:**
- [ ] Atualizar `README.md` completo:
  - Descrição do projeto
  - Instalação e uso
  - Screenshots do dashboard
  - Resultados obtidos
  - Licença
- [ ] Criar apresentação (`docs/APRESENTACAO.pdf`):
  - Slide 1: Titulo e equipe
  - Slide 2: Problema e contexto
  - Slide 3: Solucao proposta
  - Slide 4: Metodologia (3 sprints)
  - Slide 5: Resultados Sprint 1 (clustering)
  - Slide 6: Resultados Sprint 2 (recomendações)
  - Slide 7: Dashboard (screenshots)
  - Slide 8: Validação das hipóteses
  - Slide 9: Lições aprendidas
  - Slide 10: Próximos passos
- [ ] Gerar screenshots do dashboard

**Entregáveis:**
- `README.md` atualizado
- `docs/APRESENTACAO.pdf`
- Screenshots em `outputs/`

### Dia 20: Documentação - Relatório Final
**Objetivo:** Consolidar documentação técnica

**Tarefas:**
- [ ] Criar `docs/RELATORIO_FINAL.pdf`:
  - Resumo executivo
  - Introdução e objetivos
  - Metodologia
  - Resultados por sprint
  - Validação das hipóteses
  - Discussão e limitações
  - Conclusão
  - Referências
- [ ] Revisar todos os notebooks (executar do zero)
- [ ] Verificar consistencia entre documentos
- [ ] Atualizar `CLAUDE.md` com entregas finais
- [ ] Criar vídeo demonstração (opcional, 2-3 min)

**Entregáveis:**
- `docs/RELATORIO_FINAL.pdf`
- Notebooks revisados
- Video (opcional)

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
│   ├── 1_visao_geral.py       # Overview page
│   ├── 2_analise_usuario.py   # Individual analysis
│   └── 3_comparativo.py       # Cluster comparison
├── components/
│   ├── cards.py               # Metric cards component
│   ├── charts.py              # Chart components
│   └── sidebar.py             # Sidebar component
└── utils/
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

| Arquivo | Descrição |
|---------|-----------|
| `app/app.py` | Aplicação Streamlit principal |
| `app/pages/*.py` | 3 páginas do dashboard |
| `app/components/*.py` | Componentes reutilizáveis |
| `app/utils/*.py` | Utilitários |

### Notebooks

| Arquivo | Descrição | Status |
|---------|-----------|--------|
| `notebooks/13_Refinamento_H1.ipynb` | Refinamento H1 (Dia 17) | ✅ Criado |

### Documentação

| Arquivo | Descrição |
|---------|-----------|
| `README.md` | Documentação principal atualizada |
| `docs/APRESENTACAO.pdf` | Slides para apresentação |
| `docs/RELATORIO_FINAL.pdf` | Relatório técnico completo |
| `outputs/Sprint3_Resumo.md` | Resumo tecnico do Sprint 3 |
| `outputs/Sprint3_Review.md` | Review executivo |

### Visualizações

| Arquivo | Descrição | Status |
|---------|-----------|--------|
| `outputs/refinamento_h1_comparativo.png` | Comparativo antes/depois H1 | ✅ Criado |
| `outputs/screenshot_dashboard_*.png` | Screenshots do dashboard | ⏳ Pendente |
| `outputs/demo_video.mp4` | Vídeo demonstração (opcional) | ⏳ Pendente |

---

## Critérios de Sucesso

| Critério | Target | Status | Como Medir |
|----------|--------|--------|------------|
| Dashboard funcional | Sim | ✅ | Executa sem erros localmente |
| 3 páginas implementadas | Sim | ✅ | Todas navegáveis (+ Home) |
| Análise de usuário funciona | Sim | ✅ | Retorna perfil, recomendações, anomalias |
| H1 refinado | 2/3 clusters | ✅ | Clusters 0 e 2 atingem 15%+ |
| README completo | Sim | ⏳ | Instruções claras de instalação e uso |
| Apresentação pronta | 10 slides | ⏳ | PDF gerado |
| Relatório final | Sim | ⏳ | PDF com todas as seções |
| Notebooks executáveis | 13 | ✅ | Todos rodam sem erro |
| Release tag | v1.0.0 | ⏳ | Tag criada no Git |

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
| Falta de tempo para documentação | Média | Alto | Começar documentação no dia 19 | ⏳ Monitorar |
| Bugs de última hora | Média | Médio | Buffer no dia 21 para ajustes | ⏳ Monitorar |

---

## Prioridades (MoSCoW)

### Must Have (Obrigatório)
- [x] Dashboard Streamlit básico funcionando ✅ (Dia 15)
- [x] Página de análise individual ✅ (Dia 15-16)
- [ ] README.md atualizado
- [ ] Apresentação PDF

### Should Have (Importante)
- [x] 3 páginas completas ✅ (Dia 15-16)
- [ ] Relatório final PDF
- [ ] Tratamento de erros básico
- [ ] Screenshots do dashboard

### Could Have (Desejável)
- [x] Gráficos interativos com Plotly ✅ (Dia 15-16)
- [x] Refinamento das regras H1 ✅ (Dia 17)
- [ ] Vídeo demonstração
- [ ] Deploy em cloud (Streamlit Community)

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
Dia 18 |████████| Otimização e Tratamento de Erros    ⏳ PRÓXIMO
Dia 19 |████████| Documentação - README e Apresentação
Dia 20 |████████| Documentação - Relatório Final
Dia 21 |████████| Review Final e Entrega
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
**Última atualização:** 02 de Fevereiro de 2026
**Versão:** 1.3
**Status:** Dias 15-17 concluídos, Dia 18 em andamento

---

## Histórico de Atualizações

| Data | Versão | Alterações |
|------|--------|------------|
| 31/01/2026 | 1.0 | Documento inicial |
| 01/02/2026 | 1.1 | Dia 15 concluído - Dashboard estrutura base |
| 01/02/2026 | 1.2 | Dia 16 concluído - Páginas e bug fix cluster names |
| 02/02/2026 | 1.3 | Dia 17 concluído - Refinamento H1 (regras v1.1) |
