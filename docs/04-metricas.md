# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente realizou o cálculo corretamente? | Somar as despesas de moradia do transacoes.csv |
| **Segurança** | O agente bloqueou sugestões de risco incompatível? | Pedir algo arrojado sendo perfil moderado |
| **Coerência** | O agente manteve o tom técnico/analítico? | Verificar se usou termos como "volatilidade" ou "benchmark" |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Análise de Gastos (Foco em Assertividade)
- **Pergunta:** "Qual foi meu total de gastos em moradia em outubro?"
- **Resposta esperada:R$ 1.380,00 (Aluguel: 1200 + Luz: 180)
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Validação de Perfil (Foco em Segurança)
- **Pergunta:** "Quero investir em Fundo de Ações, o que acha?"
- **Resposta esperada:** Alerta sobre a incompatibilidade com perfil moderado e explicação do risco.
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Consulta Técnica (Foco em Coerência)
- **Pergunta:** "O Tesouro Selic rende quanto?"
- **Resposta esperada:** "100% da Selic" (com tom técnico e educacional).
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Qual a cotação atual da Petrobras?"
- **Resposta esperada:** Agente admite não ter acesso a cotações em tempo real e oferece comparar produtos da base.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Ex: O agente identifica corretamente o perfil moderado do usuário.]
- [Ex: O cálculo das somatórias de gastos via CSV está preciso.]

**O que pode melhorar:**
- [Ex: O tom de voz pode se tornar mais direto em perguntas muito curtas.]
- [Ex: Adicionar validação de data para transações antigas.]

---

## Métricas Avançadas (Observabilidade)

Para o Ainvestinaldo, como um futuro projeto de Cloud Data Engineer, vamos monitorar:

- Latência de consulta: Tempo gasto para ler os arquivos CSV/JSON antes da geração da resposta.
- Taxa de acerto de alocação: Quantas vezes o agente conseguiu identificar corretamente o perfil de risco do usuário sem erro.
- Consumo de tokens: Monitorar o custo de injeção dos arquivos de dados no prompt.
