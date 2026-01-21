# Economiza+ IA

Projeto de ciência de dados para análise de comportamento financeiro de famílias brasileiras das classes C e D, com foco em identificar padrões de gastos e capacidade de poupança.

## Sobre o Projeto

O Economiza+ utiliza técnicas de machine learning e análise de dados para:

- Gerar datasets sintéticos realistas baseados em pesquisas brasileiras (Serasa, CNC, IBGE, POF)
- Realizar análise exploratória de dados financeiros
- Criar features relevantes para segmentação de usuários
- Aplicar algoritmos de clustering para identificar perfis financeiros

### Dados de Referência

O projeto é baseado em estatísticas reais do cenário brasileiro:
- **Serasa:** 80,6 milhões de inadimplentes, dívida média de R$ 4.042
- **CNC:** 79,5% das famílias endividadas
- **IBGE:** 60% não conseguem poupar
- **Faixas etárias:** 26-40 anos (33,4%), 41-60 anos (35,4%)

## Estrutura do Projeto

```
economiza-ia/
├── data/
│   ├── raw/              # Dados brutos gerados
│   └── processed/        # Dados processados
├── notebooks/
│   ├── 01_EDA_Basico.ipynb           # Análise Exploratória
│   └── 02_Feature_Engineering.ipynb  # Engenharia de Features
├── scripts/
│   └── gerar_dataset_financeiro.py   # Gerador de dataset sintético
├── models/               # Modelos treinados
├── outputs/              # Arquivos de saída (CSVs gerados)
├── images/               # Visualizações e gráficos
├── docs/                 # Documentação adicional
├── presentations/        # Apresentações
└── src/                  # Código fonte
```

## Instalação

### Pré-requisitos

- Python 3.11+

### Setup

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/economiza-ia.git
cd economiza-ia
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

### 1. Gerar Dataset Sintético

```bash
python scripts/gerar_dataset_financeiro.py
```

Este script gera três arquivos CSV na pasta `outputs/`:
- `usuarios.csv` - Perfil de 500 usuários
- `transacoes.csv` - Transações financeiras (6 meses)
- `estatisticas_mensais.csv` - Agregações mensais

### 2. Executar Análise Exploratória

Abra e execute o notebook `notebooks/01_EDA_Basico.ipynb` para:
- Visualizar distribuição de renda
- Analisar gastos por categoria
- Identificar relação renda vs. gasto
- Calcular capacidade de economizar

### 3. Feature Engineering

Execute o notebook `notebooks/02_Feature_Engineering.ipynb` para criar features relevantes para o modelo de clustering.

## Datasets Gerados

### Usuários
| Campo | Descrição |
|-------|-----------|
| `user_id` | Identificador único |
| `idade` | Idade (26-60 anos) |
| `tipo_emprego` | CLT, Autônomo ou Informal |
| `renda_base` | Renda mensal base (R$) |
| `estado_civil` | Solteiro, Casado ou Divorciado |
| `num_dependentes` | Número de dependentes (0-3) |
| `situacao_financeira` | Equilibrado, Endividado_Leve, Endividado_Grave, Inadimplente |
| `regiao` | Região do Brasil |

### Transações
| Campo | Descrição |
|-------|-----------|
| `user_id` | Identificador do usuário |
| `data` | Data da transação |
| `categoria` | Categoria do gasto |
| `valor` | Valor em R$ |
| `is_essencial` | Se é gasto essencial |
| `is_anomalia` | Flag de anomalia (5% dos dados) |

### Categorias de Gastos
- Alimentação (Casa e Fora)
- Habitação (Aluguel e Contas)
- Transporte
- Saúde
- Educação
- Vestuário
- Lazer
- Telecomunicações
- Higiene e Limpeza
- Outros

## Tecnologias

- **Python 3.11**
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Matplotlib** - Visualizações
- **Seaborn** - Visualizações estatísticas
- **Jupyter** - Notebooks interativos

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
