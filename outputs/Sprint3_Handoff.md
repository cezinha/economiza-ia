# Sprint 3 - Documento de Handoff
## Economiza+ MVP - Dashboard e Integracao Final

**Data:** 27 de Janeiro de 2026
**De:** Sprint 2
**Para:** Sprint 3
**Periodo:** Dias 15-21

---

## Resumo do Estado Atual

### Sprints Anteriores

| Sprint | Status | Entregas |
|--------|--------|----------|
| Sprint 1 | Concluido | EDA, Features, Clustering (H2 validada) |
| Sprint 2 | Concluido | Recomendacoes, Anomalias, Pipeline |

### Hipoteses

| Hipotese | Status | Acao Sprint 3 |
|----------|--------|---------------|
| H1 | Parcial (8.11%, Cluster 0 OK) | Ajustar regras |
| H2 | Validada (Silhouette 0.52) | Manter |
| H6 | Nao validada (P=47%, R=47%) | Revisar dataset ou aceitar limitacao |

---

## Artefatos Disponiveis

### Pipeline Pronto para Uso

```python
# Carregar pipeline
with open('models/pipeline_completo.pkl', 'rb') as f:
    pipeline_data = pickle.load(f)

# Usar
resultado = pipeline.analisar_usuario(user_id, transacoes)
```

### Modelos

| Arquivo | Descricao | Pronto |
|---------|-----------|--------|
| pipeline_completo.pkl | Pipeline integrado | Sim |
| kmeans_best.pkl | Classificador de clusters | Sim |
| isolation_forest.pkl | Detector de anomalias | Sim |
| recomendacoes_regras.json | Regras de economia | Sim |

### Dados

| Arquivo | Registros | Pronto |
|---------|-----------|--------|
| usuarios.csv | 500 | Sim |
| transacoes.csv | 194K | Sim |
| usuarios_clustered.csv | 500 | Sim |
| economia_projetada.csv | 500 | Sim |

---

## Planejamento Sprint 3

### Dia 15-16: Dashboard Streamlit

**Objetivo:** Interface web interativa

**Tarefas:**
- [ ] Instalar Streamlit
- [ ] Criar estrutura do app
- [ ] Pagina 1: Visao geral (distribuicao clusters)
- [ ] Pagina 2: Analise individual (selecionar usuario)
- [ ] Pagina 3: Comparativo entre perfis
- [ ] Deploy local funcionando

**Componentes do Dashboard:**
1. Sidebar com selecao de usuario
2. Cards com metricas principais
3. Grafico de perfil financeiro
4. Lista de recomendacoes
5. Alertas de anomalias

### Dia 17-18: Refinamento e Testes

**Objetivo:** Ajustar hipoteses e garantir qualidade

**Tarefas:**
- [ ] Revisar regras H1 para clusters 1-3
- [ ] Testar dashboard com diferentes usuarios
- [ ] Corrigir bugs encontrados
- [ ] Otimizar performance
- [ ] Adicionar tratamento de erros

**Opcional (se tempo permitir):**
- [ ] API REST com FastAPI
- [ ] Revisar geracao de anomalias no dataset

### Dia 19-20: Documentacao Final

**Objetivo:** Preparar entrega academica

**Tarefas:**
- [ ] README.md completo
- [ ] Apresentacao (slides)
- [ ] Video demonstracao (opcional)
- [ ] Relatorio final do projeto
- [ ] Revisao de todos os notebooks

**Entregas:**
- README.md
- docs/APRESENTACAO.pdf
- docs/RELATORIO_FINAL.pdf

### Dia 21: Review e Entrega

**Objetivo:** Finalizar e entregar

**Tarefas:**
- [ ] Review final com orientador
- [ ] Ajustes de ultima hora
- [ ] Tag de release no Git
- [ ] Entrega oficial

---

## Estrutura Sugerida do Dashboard

```
app/
├── app.py                 # Streamlit main
├── pages/
│   ├── 1_visao_geral.py   # Overview
│   ├── 2_analise_usuario.py # Individual
│   └── 3_comparativo.py   # Comparison
├── components/
│   ├── cards.py           # Metric cards
│   ├── charts.py          # Visualizations
│   └── sidebar.py         # Navigation
└── utils/
    └── pipeline.py        # Pipeline wrapper
```

### Codigo Base do App

```python
# app.py
import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Economiza+ MVP", layout="wide")

@st.cache_resource
def load_pipeline():
    with open('models/pipeline_completo.pkl', 'rb') as f:
        return pickle.load(f)

@st.cache_data
def load_data():
    return pd.read_csv('data/raw/transacoes.csv')

pipeline_data = load_pipeline()
transacoes = load_data()

st.title("Economiza+ MVP")
st.subheader("Sistema de Analise Financeira e Recomendacoes")

# Sidebar
user_id = st.sidebar.selectbox("Selecione o usuario", usuarios['user_id'].tolist())

# Analise
if st.sidebar.button("Analisar"):
    resultado = pipeline.analisar_usuario(user_id, transacoes)

    col1, col2, col3 = st.columns(3)
    col1.metric("Perfil", resultado['perfil']['cluster_nome'])
    col2.metric("Economia Potencial", f"R$ {resultado['economia']['total_mensal']:.2f}")
    col3.metric("Anomalias", resultado['anomalias']['total_anomalias'])
```

---

## Riscos e Mitigacoes

| Risco | Probabilidade | Mitigacao |
|-------|---------------|-----------|
| Tempo insuficiente para dashboard completo | Media | Priorizar funcionalidades essenciais |
| Problemas de deploy Streamlit | Baixa | Testar localmente primeiro |
| H1 nao atingir target global | Alta | Documentar como limitacao conhecida |

---

## Dependencias Tecnicas

### Novas Bibliotecas (Sprint 3)

```bash
pip install streamlit
pip install plotly  # opcional, para graficos interativos
```

### Versoes Testadas

- streamlit >= 1.28.0
- plotly >= 5.18.0

---

## Contatos e Referencias

- **Documentacao Sprint 1:** outputs/Sprint1_Resumo.md
- **Documentacao Sprint 2:** outputs/Sprint2_Resumo.md
- **Planejamento Original:** outputs/Sprint2_Planejamento.md
- **CLAUDE.md:** Guia completo do projeto

---

## Checklist Pre-Sprint 3

- [x] Pipeline funcionando
- [x] Dados disponiveis
- [x] Modelos salvos
- [x] Documentacao atualizada
- [x] CLAUDE.md atualizado
- [ ] Streamlit instalado
- [ ] Estrutura do app criada

---

**Documento criado em:** 27 de Janeiro de 2026
**Versao:** 1.0
**Status:** Pronto para Sprint 3
