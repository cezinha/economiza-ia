# Economiza+ MVP
## Apresentação Final - TCC Data Science

---

# 1. Apresentação

## Celina Uemura

**Formação:**
- Desenho Industrial - Programação Visual (Mackenzie)
- MBA Engenharia de Software (FIAP)
- Data Science (XP Educação) - em andamento

**Experiência:**
- +25 anos em desenvolvimento web/mobile
- Staff Software Engineer na McKinsey & Company
- Especialista em React, TypeScript, IA Generativa

---

# 2. Desafio

## O Problema
- **78%** das famílias brasileiras endividadas
- Classes C/D mais afetadas
- Falta de ferramentas personalizadas

## Hipóteses
| # | Hipótese |
|---|----------|
| H1 | Recomendações personalizadas geram 15-20% de economia |
| H2 | K-means identifica perfis distintos |
| H6 | Isolation Forest detecta anomalias |

---

# 3. Solução

## Economiza+ MVP

**Proposta:** Sistema que segmenta usuários em perfis e oferece recomendações personalizadas de economia.

**Funcionamento:** Analisa transações > Identifica perfil > Gera recomendações > Projeta economia

## Objetivo SMART
- **S:** Sistema de recomendações personalizadas
- **M:** Economia de 15-20% para usuários em risco
- **A:** K-means + regras baseadas em dados
- **R:** Impacto em famílias classes C/D
- **T:** 21 dias (3 sprints)

---

# 4. Diferencial

- **Segmentação por ML:** 4 perfis identificados automaticamente
- **Personalização real:** Recomendações específicas por perfil
- **Dados brasileiros:** Baseado em Serasa, IBGE, POF
- **Foco em C/D:** Público ignorado pelo mercado
- **Economia quantificada:** Valores exatos, não promessas
- **Detecção de anomalias:** Identifica gastos atípicos

---

# 5. Desenvolvimento

## Sprint 1: Segmentação (Dias 1-7)
- EDA: 500 usuários, 191K transações
- K-means K=4: 4 perfis identificados
- **Descoberta:** 85% gastam mais do que ganham

## Sprint 2: Recomendações (Dias 8-14)
- 9 regras de economia (2-3 por perfil)
- Top corte: Alimentação Fora (R$ 411/mês)
- Pipeline integrado: ~20 usuários/segundo

## Sprint 3: Dashboard (Dias 15-21)
- Streamlit: 5 páginas interativas
- Refinamento H1: economia 8.6% > 9.83%
- Documentação completa

---

# 6. Resultados

## Validação das Hipóteses
| Hipótese | Status | Resultado |
|----------|--------|-----------|
| H1 | Parcial | 2/3 clusters atingem 15%+ |
| H2 | Parcial | Silhouette 0.267, clusters interpretáveis |
| H6 | Não validada | Limitação do dataset |

## Métricas Finais
| Métrica | Valor |
|---------|-------|
| Usuários em risco | 85.2% (426/500) |
| Economia mensal | R$ 188.746 |
| Economia anual | R$ 2,26 milhões |

## Lições Aprendidas
- Interpretabilidade > métricas estatísticas
- Simplicidade funciona (5 features)
- Perfis críticos precisam de regras agressivas

## Próximos Passos
- Integração Open Finance (dados reais)
- Módulo de educação financeira
- Deploy em cloud

---

# Obrigada!

**Celina Uemura**
Staff Software Engineer | McKinsey & Company

*Economiza+ MVP - TCC Data Science - XP Educação*
*Orientador: Marcos Prochnow | Fevereiro 2026*
