# GUIA DO DATASET SINTÉTICO - ECONOMIZA+

## 📊 RESUMO DO DATASET GERADO

### Estatísticas Principais:
- **500 usuários** (classes C e D)
- **194.231 transações** (6 meses de histórico)
- **2.500 registros mensais** agregados
- **~74% dos usuários** com saldo negativo (realista!)
- **5% de anomalias** injetadas para treino do detector

---

## 📁 ARQUIVOS GERADOS

### 1. `usuarios.csv` (500 linhas)
Perfil demográfico e financeiro de cada usuário.

**Colunas:**
- `user_id`: Identificador único (user_0001 a user_0500)
- `idade`: 26-60 anos (distribuição baseada em dados Serasa)
- `tipo_emprego`: CLT (45%), Autônomo (35%), Informal (20%)
- `renda_base`: R$ 2.000 - 4.500 (média R$ 3.080)
- `variabilidade_renda`: 0.05 (CLT) ou 0.35 (Autônomos)
- `estado_civil`: Solteiro, Casado, Divorciado
- `num_dependentes`: 0-3 filhos/dependentes
- `situacao_financeira`: Equilibrado, Endividado_Leve, Endividado_Grave, Inadimplente
- `regiao`: Sudeste, Sul, Nordeste, Centro-Oeste, Norte

**Exemplo de uso:**
```python
import pandas as pd

# Carregar usuários
usuarios = pd.read_csv('usuarios.csv')

# Ver distribuição de renda por tipo de emprego
usuarios.groupby('tipo_emprego')['renda_base'].describe()

# Filtrar apenas usuários equilibrados
equilibrados = usuarios[usuarios['situacao_financeira'] == 'Equilibrado']
```

---

### 2. `transacoes.csv` (194.231 linhas)
Todas as transações de todos os usuários em 6 meses.

**Colunas:**
- `user_id`: ID do usuário
- `data`: Data da transação (jul/2025 a dez/2025)
- `categoria`: 12 categorias + Renda
  - **Essenciais**: Alimentacao_Casa, Habitacao_Aluguel, Habitacao_Contas, Transporte, Saude, Educacao, Telecomunicacoes, Higiene_Limpeza
  - **Não essenciais**: Alimentacao_Fora, Vestuario, Lazer, Outros
  - **Renda**: Entrada de dinheiro (positivo)
- `valor`: Valor em reais (R$)
- `mes`: Mês da transação (1-12)
- `ano`: Ano (2025)
- `renda_mes`: Renda do usuário naquele mês
- `is_essencial`: True/False
- `is_anomalia`: True/False (5% das transações são anomalias)

**Características especiais:**
- **Sazonalidade**: Dezembro tem gastos 30% maiores (festas)
- **Variabilidade realista**: Categorias não essenciais variam até 60%
- **Anomalias injetadas**: 5% das transações têm valores 3-8x maiores que o normal

**Exemplo de uso:**
```python
# Carregar transações
transacoes = pd.read_csv('transacoes.csv')
transacoes['data'] = pd.to_datetime(transacoes['data'])

# Filtrar apenas gastos (remover renda)
gastos = transacoes[transacoes['categoria'] != 'Renda']

# Ver anomalias
anomalias = gastos[gastos['is_anomalia'] == True]
print(f"Total de anomalias: {len(anomalias)}")

# Gastos por categoria
gastos.groupby('categoria')['valor'].agg(['sum', 'mean', 'count'])

# Séries temporais de um usuário
user_001 = transacoes[transacoes['user_id'] == 'user_0001']
user_001.groupby('data')['valor'].sum().plot()
```

---

### 3. `estatisticas_mensais.csv` (2.500 linhas)
Agregações mensais por usuário (500 usuários × 5 meses).

**Colunas:**
- `user_id`: ID do usuário
- `ano`, `mes`: Referência temporal
- `gasto_total`: Soma de todos os gastos do mês
- `gasto_medio`: Média dos valores das transações
- `gasto_std`: Desvio padrão dos gastos
- `num_transacoes`: Quantidade de transações no mês
- `pct_essencial`: % de transações essenciais
- `num_anomalias`: Quantidade de anomalias detectadas
- `renda_mes`: Renda do usuário no mês
- `saldo_mes`: renda_mes - gasto_total (pode ser negativo!)
- `pct_gasto`: (gasto_total / renda_mes) × 100

**Exemplo de uso:**
```python
# Carregar estatísticas
stats = pd.read_csv('estatisticas_mensais.csv')

# Usuários com gasto > renda
endividados = stats[stats['pct_gasto'] > 100]
print(f"{len(endividados)/len(stats)*100:.1f}% dos meses com gasto > renda")

# Evolução temporal de um usuário
import matplotlib.pyplot as plt

user_stats = stats[stats['user_id'] == 'user_0001']
plt.plot(user_stats['mes'], user_stats['saldo_mes'])
plt.title('Saldo Mensal - User 0001')
plt.show()
```

---

## 🎯 COMO USAR NO SEU PROJETO

### SPRINT 1: EDA e Clustering

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CARREGAR DADOS
usuarios = pd.read_csv('usuarios.csv')
transacoes = pd.read_csv('transacoes.csv')
stats = pd.read_csv('estatisticas_mensais.csv')

# 2. CRIAR FEATURES PARA CLUSTERING
# Agregar por usuário
features_clustering = stats.groupby('user_id').agg({
    'renda_mes': 'mean',
    'gasto_total': 'mean',
    'gasto_std': 'mean',
    'pct_gasto': 'mean',
    'num_transacoes': 'mean',
    'pct_essencial': 'mean',
    'num_anomalias': 'sum'
}).reset_index()

# Merge com dados demográficos
features_clustering = features_clustering.merge(
    usuarios[['user_id', 'idade', 'num_dependentes', 'variabilidade_renda']], 
    on='user_id'
)

# 3. NORMALIZAR
scaler = StandardScaler()
X = scaler.fit_transform(features_clustering.drop('user_id', axis=1))

# 4. APLICAR K-MEANS
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(X)
features_clustering['cluster'] = clusters

# 5. ANALISAR CLUSTERS
print(features_clustering.groupby('cluster').mean())
```

### SPRINT 2: Sistema de Recomendação

```python
# Identificar oportunidades de economia por cluster
def recomendar_economia(user_id, cluster_id):
    # Pegar gastos do usuário
    user_gastos = transacoes[
        (transacoes['user_id'] == user_id) & 
        (transacoes['categoria'] != 'Renda')
    ]
    
    # Média do cluster
    cluster_users = features_clustering[
        features_clustering['cluster'] == cluster_id
    ]['user_id']
    
    cluster_gastos = transacoes[
        (transacoes['user_id'].isin(cluster_users)) &
        (transacoes['categoria'] != 'Renda')
    ]
    
    # Comparar por categoria
    user_por_cat = user_gastos.groupby('categoria')['valor'].sum()
    cluster_por_cat = cluster_gastos.groupby('categoria')['valor'].mean()
    
    # Identificar onde usuário gasta mais que a média
    oportunidades = (user_por_cat - cluster_por_cat).sort_values(ascending=False)
    
    return oportunidades[oportunidades > 0]
```

### SPRINT 2: Detecção de Anomalias

```python
from sklearn.ensemble import IsolationForest

# Treinar detector por categoria
def treinar_detector_anomalias(categoria):
    gastos_cat = transacoes[transacoes['categoria'] == categoria]
    
    # Features
    X = gastos_cat[['valor']].values
    
    # Treinar
    detector = IsolationForest(contamination=0.05, random_state=42)
    detector.fit(X)
    
    return detector

# Aplicar
detectors = {}
for cat in transacoes['categoria'].unique():
    if cat != 'Renda':
        detectors[cat] = treinar_detector_anomalias(cat)
```

---

## 🔍 VALIDAÇÃO DO DATASET

### Checklist de Qualidade:

✅ **Distribuição de renda realista**: Média R$ 3.080 (compatível com classes C/D)
✅ **Taxa de endividamento**: ~74% com saldo negativo (próximo aos 79,5% da CNC)
✅ **Variabilidade de renda**: CLT estável, autônomos variáveis
✅ **Categorias baseadas em POF-IBGE**: Pesos realistas
✅ **Sazonalidade**: Dezembro com gastos maiores
✅ **Anomalias controladas**: 5% para treino do detector

---

## 💡 DICAS E BOAS PRÁTICAS

### 1. **Sempre filtrar a categoria "Renda"**
```python
# Correto: apenas gastos
gastos = transacoes[transacoes['categoria'] != 'Renda']
```

### 2. **Usar `estatisticas_mensais.csv` para clustering**
É mais eficiente que agregar `transacoes.csv` toda vez.

### 3. **Validar com dados reais posteriormente**
Este dataset é sintético. Compare padrões com POF-IBGE quando possível.

### 4. **Ajustar parâmetros se necessário**
Edite o script `gerar_dataset_financeiro.py` e rode novamente:
```python
NUM_USUARIOS = 1000  # Aumentar para 1000
NUM_MESES = 12       # Aumentar histórico
```

### 5. **Documentar premissas**
No seu notebook, sempre documente:
- Quais features usou para clustering
- Por que escolheu determinado threshold
- Como tratou valores negativos

---

## 📚 REFERÊNCIAS DOS DADOS

### Dados Reais Usados como Base:
- **Serasa** (Nov/2025): 80,6M inadimplentes, dívida média R$ 4.042
- **CNC** (Out/2025): 79,5% famílias endividadas, 30,5% inadimplentes
- **IBGE**: 60% não conseguem poupar, POF (Pesquisa de Orçamentos Familiares)

### Categorias baseadas em:
- **POF-IBGE 2017-2018**: Pesos das categorias de despesa
- **Distribuição de renda**: Faixas salariais classes C e D

---

## 🚀 PRÓXIMOS PASSOS

1. **Sprint 1 (Dias 1-7)**:
   - Carregar datasets
   - EDA completo (estatísticas, visualizações)
   - Feature Engineering
   - Clustering (K-means)

2. **Sprint 2 (Dias 8-14)**:
   - Sistema de recomendação
   - Detecção de anomalias (Isolation Forest)

3. **Sprint 3 (Dias 15-21)**:
   - Integração dos modelos
   - Dashboard Streamlit
   - Documentação final

---

## ❓ FAQ

**P: Posso usar dados reais?**
R: Não para o MVP. LGPD impede o uso de dados reais sem consentimento. Use este dataset sintético.

**P: Como validar se os modelos funcionam?**
R: Use as métricas definidas no projeto (Silhouette > 0.5, Precision > 0.85, etc.)

**P: E se eu quiser mais usuários?**
R: Edite `NUM_USUARIOS = 1000` no script e rode novamente.

**P: As anomalias estão marcadas?**
R: Sim! Coluna `is_anomalia = True`. Use para validar seu detector.

**P: Por que 74% têm saldo negativo?**
R: É realista! 79,5% das famílias brasileiras estão endividadas (CNC).

---

**Boa sorte no seu projeto!** 🚀
