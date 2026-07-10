# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Analisar o histórico de dúvidas e problemas já resolvidos para evitar repetições. |
| `perfil_investidor.json` | JSON | Definir o limite de risco (tolerância à volatilidade) e objetivos de longo prazo. |
| `produtos_financeiros.json` | JSON | Base técnica para comparar rentabilidade, risco e aporte mínimo. |
| `transacoes.csv` | CSV | Identificar a saúde financeira atual (disponibilidade de caixa) para sugerir aportes realistas. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram mantidos como mocks (fictícios) para garantir a privacidade, mas estruturados para permitir que o Ainvestinaldo realize cálculos simples de comparação. Não houve necessidade de expansão externa, pois os dados fornecidos são suficientes para demonstrar a lógica de análise de perfil e comparação de ativos.
---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

O agente utiliza uma estratégia de RAG (Retrieval-Augmented Generation) simplificada: ao iniciar a sessão, o agente lê os arquivos locais (.csv e .json) via bibliotecas Python (como pandas), transformando o conteúdo em uma string formatada que é injetada no contexto do sistema.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são inseridos dinamicamente como "Contexto do Cliente" e "Base de Produtos". Sempre que o usuário faz uma pergunta, o Ainvestinaldo consulta o JSON de produtos para comparar e o perfil do usuário para validar a viabilidade do produto.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
### PERFIL DO CLIENTE
Nome: João Silva
Perfil de Risco: Moderado
Objetivo Principal: Construir reserva de emergência (R$ 15.000)
Patrimônio Atual: R$ 15.000

### PRODUTOS DISPONÍVEIS PARA ANÁLISE
1. Tesouro Selic (Renda Fixa, Risco: Baixo, Rent: 100% Selic)
2. CDB Liquidez Diária (Renda Fixa, Risco: Baixo, Rent: 102% CDI)
3. Fundo Multimercado (Fundo, Risco: Médio, Rent: CDI + 2%)

### ESTADO FINANCEIRO ATUAL
Renda Mensal: R$ 5.000
Última Transação: Combustível - R$ 250 (25/10)
...
```
