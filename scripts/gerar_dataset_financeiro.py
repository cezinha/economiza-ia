"""
Gerador de Dataset Sintético de Transações Financeiras
Projeto: Economiza+ (Classes C e D - Brasil)

Baseado em dados reais:
- Serasa: 80,6M inadimplentes, dívida média R$ 4.042
- CNC: 79,5% famílias endividadas
- IBGE: 60% não conseguem poupar
- Faixas etárias: 26-40 anos (33,4%), 41-60 anos (35,4%)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os
from pathlib import Path

# Configuração de seed para reprodutibilidade
np.random.seed(42)
random.seed(42)

# Configurar diretório de saída
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / 'outputs'
OUTPUT_DIR.mkdir(exist_ok=True)

# ============================================================================
# CONFIGURAÇÕES DO DATASET
# ============================================================================

NUM_USUARIOS = 500  # Número de usuários (ajuste conforme necessário)
NUM_MESES = 6       # Histórico de 6 meses
DATA_INICIAL = datetime(2025, 7, 1)  # Julho 2025

# ============================================================================
# PERFIS DE USUÁRIOS (baseado em personas)
# ============================================================================

def gerar_usuarios(n=NUM_USUARIOS):
    """Gera perfil de usuários com características realistas"""
    
    usuarios = []
    
    for i in range(n):
        user_id = f"user_{i+1:04d}"
        
        # Distribuição de idade (baseado em dados Serasa)
        idade_dist = np.random.choice(
            ['26-30', '31-35', '36-40', '41-50', '51-60'],
            p=[0.15, 0.18, 0.16, 0.28, 0.23]  # Maior concentração em 41-60
        )
        
        if idade_dist == '26-30':
            idade = random.randint(26, 30)
        elif idade_dist == '31-35':
            idade = random.randint(31, 35)
        elif idade_dist == '36-40':
            idade = random.randint(36, 40)
        elif idade_dist == '41-50':
            idade = random.randint(41, 50)
        else:
            idade = random.randint(51, 60)
        
        # Tipo de emprego
        tipo_emprego = np.random.choice(
            ['CLT', 'Autonomo', 'Informal'],
            p=[0.45, 0.35, 0.20]
        )
        
        # Renda base (classes C e D)
        if tipo_emprego == 'CLT':
            # Renda fixa entre R$ 2.000 - 4.000
            renda_base = np.random.uniform(2000, 4000)
            variabilidade_renda = 0.05  # 5% de variação
        else:  # Autônomo/Informal
            # Renda variável entre R$ 1.800 - 4.500
            renda_base = np.random.uniform(1800, 4500)
            variabilidade_renda = 0.35  # 35% de variação
        
        # Estado civil e dependentes
        estado_civil = np.random.choice(
            ['Solteiro', 'Casado', 'Divorciado'],
            p=[0.40, 0.45, 0.15]
        )
        
        if estado_civil == 'Solteiro':
            num_dependentes = np.random.choice([0, 1], p=[0.80, 0.20])
        elif estado_civil == 'Casado':
            num_dependentes = np.random.choice([0, 1, 2, 3], p=[0.20, 0.35, 0.30, 0.15])
        else:  # Divorciado
            num_dependentes = np.random.choice([0, 1, 2], p=[0.40, 0.40, 0.20])
        
        # Situação financeira (baseado em estatísticas)
        situacao = np.random.choice(
            ['Equilibrado', 'Endividado_Leve', 'Endividado_Grave', 'Inadimplente'],
            p=[0.205, 0.495, 0.195, 0.105]  # ~79,5% endividados
        )
        
        # Região (simplificado)
        regiao = np.random.choice(
            ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste', 'Norte'],
            p=[0.42, 0.15, 0.27, 0.08, 0.08]
        )
        
        usuarios.append({
            'user_id': user_id,
            'idade': idade,
            'tipo_emprego': tipo_emprego,
            'renda_base': round(renda_base, 2),
            'variabilidade_renda': variabilidade_renda,
            'estado_civil': estado_civil,
            'num_dependentes': num_dependentes,
            'situacao_financeira': situacao,
            'regiao': regiao
        })
    
    return pd.DataFrame(usuarios)


# ============================================================================
# CATEGORIAS DE GASTOS (baseado em POF-IBGE)
# ============================================================================

CATEGORIAS_GASTOS = {
    # Categoria: (peso_médio, é_essencial, variabilidade)
    'Alimentacao_Casa': (0.18, True, 0.15),
    'Alimentacao_Fora': (0.08, False, 0.30),
    'Habitacao_Aluguel': (0.25, True, 0.02),
    'Habitacao_Contas': (0.12, True, 0.25),  # Água, luz, gás
    'Transporte': (0.10, True, 0.20),
    'Saude': (0.07, True, 0.40),
    'Educacao': (0.05, True, 0.10),
    'Vestuario': (0.04, False, 0.35),
    'Lazer': (0.03, False, 0.50),
    'Telecomunicacoes': (0.03, True, 0.10),
    'Higiene_Limpeza': (0.03, True, 0.15),
    'Outros': (0.02, False, 0.60)
}


# ============================================================================
# GERAÇÃO DE TRANSAÇÕES
# ============================================================================

def gerar_transacoes(usuarios_df, num_meses=NUM_MESES):
    """Gera transações mensais para cada usuário"""
    
    transacoes = []
    
    for _, usuario in usuarios_df.iterrows():
        user_id = usuario['user_id']
        renda_base = usuario['renda_base']
        variabilidade = usuario['variabilidade_renda']
        situacao = usuario['situacao_financeira']
        num_dependentes = usuario['num_dependentes']
        
        # Ajuste de gastos baseado em situação financeira
        if situacao == 'Equilibrado':
            fator_gasto = np.random.uniform(0.70, 0.85)  # Gasta 70-85% da renda
        elif situacao == 'Endividado_Leve':
            fator_gasto = np.random.uniform(0.85, 1.05)  # Gasta 85-105%
        elif situacao == 'Endividado_Grave':
            fator_gasto = np.random.uniform(1.05, 1.25)  # Gasta 105-125%
        else:  # Inadimplente
            fator_gasto = np.random.uniform(1.20, 1.50)  # Gasta 120-150%
        
        # Ajuste por número de dependentes
        fator_dependentes = 1 + (num_dependentes * 0.15)
        
        # Gerar transações para cada mês
        for mes in range(num_meses):
            data_mes = DATA_INICIAL + timedelta(days=30 * mes)
            mes_num = data_mes.month
            
            # Renda do mês (com variabilidade)
            renda_mes = renda_base * (1 + np.random.uniform(-variabilidade, variabilidade))
            
            # Orçamento total baseado em renda e situação
            orcamento_mes = renda_mes * fator_gasto * fator_dependentes
            
            # Distribuir orçamento entre categorias
            for categoria, (peso, essencial, var_cat) in CATEGORIAS_GASTOS.items():
                
                # Pular aluguel se situação indica não paga
                if categoria == 'Habitacao_Aluguel':
                    paga_aluguel = np.random.choice([True, False], p=[0.70, 0.30])
                    if not paga_aluguel:
                        continue
                
                # Calcular gasto esperado
                gasto_esperado = orcamento_mes * peso
                
                # Adicionar variabilidade sazonal
                if mes_num == 12:  # Dezembro - gastos maiores
                    gasto_esperado *= 1.3
                elif mes_num == 1:  # Janeiro - IPTU, matrícula
                    if categoria in ['Habitacao_Contas', 'Educacao']:
                        gasto_esperado *= 1.5
                
                # Adicionar variabilidade da categoria
                gasto_real = gasto_esperado * (1 + np.random.uniform(-var_cat, var_cat))
                
                # Garantir valores positivos
                gasto_real = max(gasto_real, 0)
                
                # Número de transações no mês para esta categoria
                if essencial:
                    num_transacoes = np.random.randint(3, 12)  # Essenciais: mais frequentes
                else:
                    num_transacoes = np.random.randint(1, 5)   # Não essenciais: menos frequentes
                
                # Distribuir gasto em múltiplas transações
                valores_transacoes = np.random.dirichlet(np.ones(num_transacoes)) * gasto_real
                
                for i, valor in enumerate(valores_transacoes):
                    # Data aleatória no mês
                    dia = np.random.randint(1, 29)
                    data_transacao = data_mes.replace(day=dia)
                    
                    # Adicionar transação
                    transacoes.append({
                        'user_id': user_id,
                        'data': data_transacao,
                        'categoria': categoria,
                        'valor': round(valor, 2),
                        'mes': mes_num,
                        'ano': data_transacao.year,
                        'renda_mes': round(renda_mes, 2),
                        'is_essencial': essencial
                    })
            
            # Adicionar renda como "transação" positiva
            transacoes.append({
                'user_id': user_id,
                'data': data_mes.replace(day=5),  # Renda no dia 5
                'categoria': 'Renda',
                'valor': round(renda_mes, 2),
                'mes': mes_num,
                'ano': data_mes.year,
                'renda_mes': round(renda_mes, 2),
                'is_essencial': True
            })
    
    return pd.DataFrame(transacoes)


# ============================================================================
# ADICIONAR ANOMALIAS (para treinar detector)
# ============================================================================

def adicionar_anomalias(transacoes_df, taxa_anomalia=0.05):
    """Adiciona transações anômalas (gastos atípicos)"""
    
    n_anomalias = int(len(transacoes_df) * taxa_anomalia)
    indices_anomalias = np.random.choice(transacoes_df.index, n_anomalias, replace=False)
    
    for idx in indices_anomalias:
        # Multiplicar valor por 3-8x (gasto muito acima do normal)
        fator_anomalia = np.random.uniform(3, 8)
        transacoes_df.loc[idx, 'valor'] = transacoes_df.loc[idx, 'valor'] * fator_anomalia
        transacoes_df.loc[idx, 'is_anomalia'] = True
    
    # Marcar transações normais
    transacoes_df['is_anomalia'] = transacoes_df['is_anomalia'].fillna(False)
    
    return transacoes_df


# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def gerar_dataset_completo():
    """Gera dataset completo: usuários + transações"""
    
    print("="*70)
    print("GERADOR DE DATASET SINTÉTICO - ECONOMIZA+")
    print("="*70)
    
    # 1. Gerar usuários
    print("\n[1/5] Gerando perfis de usuários...")
    usuarios_df = gerar_usuarios(NUM_USUARIOS)
    print(f"✓ {len(usuarios_df)} usuários gerados")
    print(f"  - CLT: {(usuarios_df['tipo_emprego']=='CLT').sum()}")
    print(f"  - Autônomos: {(usuarios_df['tipo_emprego']=='Autonomo').sum()}")
    print(f"  - Informais: {(usuarios_df['tipo_emprego']=='Informal').sum()}")
    
    # 2. Gerar transações
    print("\n[2/5] Gerando transações financeiras...")
    transacoes_df = gerar_transacoes(usuarios_df, NUM_MESES)
    print(f"✓ {len(transacoes_df)} transações geradas")
    print(f"  - Período: {NUM_MESES} meses")
    print(f"  - Média transações/usuário/mês: {len(transacoes_df)/(NUM_USUARIOS*NUM_MESES):.1f}")
    
    # 3. Adicionar anomalias
    print("\n[3/5] Adicionando anomalias...")
    transacoes_df = adicionar_anomalias(transacoes_df, taxa_anomalia=0.05)
    n_anomalias = transacoes_df['is_anomalia'].sum()
    print(f"✓ {n_anomalias} anomalias adicionadas ({n_anomalias/len(transacoes_df)*100:.2f}%)")
    
    # 4. Calcular estatísticas agregadas
    print("\n[4/5] Calculando estatísticas agregadas...")
    
    # Agregar por usuário e mês
    stats_mensais = transacoes_df[transacoes_df['categoria'] != 'Renda'].groupby(
        ['user_id', 'ano', 'mes']
    ).agg({
        'valor': ['sum', 'mean', 'std', 'count'],
        'is_essencial': lambda x: (x == True).sum() / len(x),
        'is_anomalia': 'sum'
    }).reset_index()
    
    stats_mensais.columns = ['user_id', 'ano', 'mes', 'gasto_total', 'gasto_medio', 
                              'gasto_std', 'num_transacoes', 'pct_essencial', 'num_anomalias']
    
    # Adicionar renda do mês
    renda_mensal = transacoes_df[transacoes_df['categoria'] == 'Renda'].groupby(
        ['user_id', 'ano', 'mes']
    )['valor'].first().reset_index()
    renda_mensal.columns = ['user_id', 'ano', 'mes', 'renda_mes']
    
    stats_mensais = stats_mensais.merge(renda_mensal, on=['user_id', 'ano', 'mes'])
    
    # Calcular saldo mensal
    stats_mensais['saldo_mes'] = stats_mensais['renda_mes'] - stats_mensais['gasto_total']
    stats_mensais['pct_gasto'] = (stats_mensais['gasto_total'] / stats_mensais['renda_mes']) * 100
    
    print(f"✓ Estatísticas calculadas para {len(stats_mensais)} meses-usuário")
    
    # 5. Salvar arquivos
    print("\n[5/5] Salvando arquivos...")
    
    usuarios_df.to_csv(OUTPUT_DIR / 'usuarios.csv', index=False)
    print("✓ usuarios.csv salvo")
    
    transacoes_df.to_csv(OUTPUT_DIR / 'transacoes.csv', index=False)
    print("✓ transacoes.csv salvo")
    
    stats_mensais.to_csv(OUTPUT_DIR / 'estatisticas_mensais.csv', index=False)
    print("✓ estatisticas_mensais.csv salvo")
    
    # 6. Relatório final
    print("\n" + "="*70)
    print("RESUMO DO DATASET GERADO")
    print("="*70)
    
    print(f"\n📊 USUÁRIOS ({len(usuarios_df)} total):")
    print(f"  Idade média: {usuarios_df['idade'].mean():.1f} anos")
    print(f"  Renda média: R$ {usuarios_df['renda_base'].mean():.2f}")
    print(f"  Renda mediana: R$ {usuarios_df['renda_base'].median():.2f}")
    print(f"  Dependentes médios: {usuarios_df['num_dependentes'].mean():.2f}")
    
    print(f"\n💳 TRANSAÇÕES ({len(transacoes_df)} total):")
    transacoes_gastos = transacoes_df[transacoes_df['categoria'] != 'Renda']
    print(f"  Valor médio: R$ {transacoes_gastos['valor'].mean():.2f}")
    print(f"  Valor total: R$ {transacoes_gastos['valor'].sum():,.2f}")
    print(f"  Anomalias: {transacoes_gastos['is_anomalia'].sum()} ({transacoes_gastos['is_anomalia'].sum()/len(transacoes_gastos)*100:.2f}%)")
    
    print(f"\n📈 ESTATÍSTICAS MENSAIS:")
    print(f"  Gasto médio/mês: R$ {stats_mensais['gasto_total'].mean():.2f}")
    print(f"  % média gasto vs renda: {stats_mensais['pct_gasto'].mean():.1f}%")
    print(f"  Saldo médio/mês: R$ {stats_mensais['saldo_mes'].mean():.2f}")
    print(f"  Usuários com saldo negativo: {(stats_mensais['saldo_mes'] < 0).sum()} ({(stats_mensais['saldo_mes'] < 0).sum()/len(stats_mensais)*100:.1f}%)")
    
    print("\n" + "="*70)
    print("✅ DATASET GERADO COM SUCESSO!")
    print("="*70)
    print(f"\nArquivos salvos em: {OUTPUT_DIR}/")
    print("  1. usuarios.csv - Perfil dos usuários")
    print("  2. transacoes.csv - Todas as transações")
    print("  3. estatisticas_mensais.csv - Agregações mensais")
    print("\n💡 Próximos passos:")
    print("  - Carregar os CSVs no seu notebook")
    print("  - Fazer EDA (Análise Exploratória)")
    print("  - Treinar modelos de clustering")
    print("="*70)
    
    return usuarios_df, transacoes_df, stats_mensais


# ============================================================================
# EXECUTAR
# ============================================================================

if __name__ == "__main__":
    usuarios, transacoes, stats = gerar_dataset_completo()
