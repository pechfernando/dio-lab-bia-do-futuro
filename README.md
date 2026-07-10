# 🤖 Ainvestinaldo: Seu Analista de Investimentos com IA

O **Ainvestinaldo** é um agente de análise financeira desenvolvido para transformar dados brutos em decisões informadas. Ele atua como um mentor técnico, auxiliando investidores a entenderem a relação entre risco, rentabilidade e adequação ao seu perfil financeiro, evitando escolhas baseadas em dicas superficiais.

## 🎯 Objetivo
Prover uma análise comparativa de produtos financeiros, validando a compatibilidade de cada ativo com o perfil do investidor (moderado, arrojado, etc.) e garantindo segurança através de uma base de conhecimento estruturada.

---

## 📑 Documentação do Projeto

| Etapa | Descrição | Link |
| :--- | :--- | :--- |
| **01. Documentação** | Caso de uso, persona e arquitetura do Ainvestinaldo | [Acessar](./docs/01-documentacao-agente.md) |
| **02. Base de Conhecimento** | Estrutura dos dados (`.json` e `.csv`) | [Acessar](./docs/02-base-conhecimento.md) |
| **03. Prompts** | System prompt e estratégias de anti-alucinação | [Acessar](./docs/03-prompts.md) |
| **04. Métricas** | Testes de assertividade e qualidade | [Acessar](./docs/04-metricas.md) |
| **05. Pitch** | Roteiro de apresentação técnica | [Acessar](./docs/05-pitch.md) |

---
## Estrutura do Repositório

```
📁 lab-agente-financeiro/
├── 📁 data/        # Dados estruturados (Perfil, Transações, Produtos)
├── 📁 docs/        # Documentação completa do projeto
├── 📁 src/         # Código fonte da aplicação
└── 📄 README.md    # Este arquivo
```
---

🛠️ Tecnologias Utilizadas

- Linguagem: Python
- Interface: Streamlit
- LLM: [Insira aqui o modelo utilizado, ex: OpenAI GPT-4 / Google Gemini]
- Processamento de Dados: Pandas

---

💡 Dicas de Uso
- Validação: Sempre consulte o Ainvestinaldo sobre a compatibilidade de um produto com seu perfil antes de tomar decisões.
- Segurança: O agente foi treinado para emitir alertas de risco em produtos incompatíveis com seu perfil.
- Transparência: O Ainvestinaldo baseia-se exclusivamente na base de dados fornecida, priorizando a precisão técnica.
