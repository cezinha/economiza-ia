## 3. Considerações

### 3.1 Resultados

O Economiza+ MVP atingiu os principais objetivos de entrega técnica dentro do prazo de 21 dias, com pipeline funcional, dashboard interativo e documentação consolidada. A solução analisou 500 usuários e 191.231 transações, identificando 4 perfis financeiros com alto nível de interpretabilidade para apoio à tomada de decisão.

Os resultados de impacto indicam cenário financeiro crítico para a maior parte da base analisada, com taxa média de poupança de -31,6% e elevada concentração de usuários em risco. Em contrapartida, o sistema de recomendações projetou economia mensal relevante (R$ 188.746 no conjunto analisado), com melhor desempenho após o refinamento das regras na Sprint 3.

Na validação das hipóteses, houve avanço consistente em H1 e resultado parcial em H2, enquanto H6 não foi validada por limitação de qualidade do ground truth sintético para anomalias. Ainda assim, o projeto entregou evidências robustas de viabilidade para segmentação comportamental e personalização de recomendações financeiras.

### 3.2 Contribuições

As principais contribuições do projeto foram:

- Estruturação de um dataset sintético realista e reproduzível, alinhado a referências nacionais (Serasa, CNC, IBGE e POF);
- Definição de uma abordagem prática de segmentação com K-means e 5 features de alta relevância para o contexto financeiro das classes C e D;
- Desenvolvimento de um sistema de recomendações interpretável, auditável e ajustável por perfil de risco;
- Implementação de pipeline integrado com artefatos versionados para facilitar manutenção, testes e reuso;
- Entrega de dashboard em Streamlit com foco em análise operacional, comparação entre perfis e diagnóstico do sistema;
- Consolidação de documentação técnica e executiva para facilitar continuidade, replicação e apresentação dos resultados.

### 3.3 Próximos passos

Para evolução do Economiza+ após a entrega do MVP, recomenda-se:

1. Reforçar a estratégia do perfil "Em Alerta" com trilhas de educação financeira e intervenções graduais, além de cortes de despesas;
2. Melhorar a geração de anomalias sintéticas com lógica estatística e comportamental para permitir validação mais realista de H6;
3. Testar modelos complementares de segmentação (mantendo K-means como baseline) para comparação de estabilidade e qualidade dos clusters;
4. Implementar monitoramento contínuo de performance do pipeline e drift de dados em ambiente de produção;
5. Adicionar mecanismos de mensuração de adesão às recomendações e economia efetivamente realizada (não apenas projetada);
6. Preparar estratégia de transição para dados reais com governança, segurança e conformidade com LGPD.

Em síntese, o MVP comprova valor técnico e potencial de impacto social, com base sólida para expansão incremental do produto.