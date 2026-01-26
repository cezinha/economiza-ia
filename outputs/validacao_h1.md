
# Validacao Hipotese H1
## Recomendacoes geram economia de 15-20%

**Data:** 2026-01-26
**Sprint:** 2 - Dia 9

---

## Resultado

| Metrica | Target | Resultado | Status |
|---------|--------|-----------|--------|
| Economia media (% renda) | 15-20% | 8.11% | NAO ATINGIDA |
| Economia mediana (% renda) | 15-20% | 6.72% | - |

---

## Economia por Cluster

| Cluster | Usuarios | Economia Media (R$) | Economia Media (% Renda) |
|---------|----------|---------------------|-------------------------|
| Endividados Severos | 59 | R$ 698.53 | 19.22% |
| Em Alerta | 196 | R$ 162.59 | 5.37% |
| Endividados Moderados | 167 | R$ 320.13 | 10.38% |
| Poupadores | 78 | R$ 120.90 | 1.72% |

---

## Impacto Total Projetado

- **Economia mensal total (500 usuarios):** R$ 135,972.17
- **Economia anual total:** R$ 1,631,666.04
- **Economia media por usuario:** R$ 271.94/mes

---

## Melhoria na Taxa de Poupanca

| Cluster | Taxa Atual | Taxa Projetada | Melhoria |
|---------|------------|----------------|----------|
| Endividados Severos | -88.6% | -81.7% | +6.9pp |
| Em Alerta | -14.8% | -9.4% | +5.4pp |
| Endividados Moderados | -57.7% | -48.3% | +9.4pp |
| Poupadores | 25.4% | 27.1% | +1.7pp |

---

## Conclusao

**Status H1: NAO ATINGIDA**

As recomendacoes nao atingem o target minimo de 15% de economia sobre a renda.

---

## Artefatos Gerados

- `data/processed/economia_projetada.csv`
- `outputs/economia_por_cluster.png`
- `outputs/distribuicao_economia_cluster.png`
- `outputs/poupanca_atual_vs_projetada.png`
- `outputs/economia_por_recomendacao.png`
