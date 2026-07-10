import streamlit as st
import pandas as pd
import json

# Configuração da página
st.set_page_config(page_title="Ainvestinaldo", layout="centered")

st.title("🤖 Ainvestinaldo")
st.subheader("Seu Analista de Investimentos Inteligente")

# 1. Carregamento dos Dados (Simulado)
@st.cache_data
def load_data():
    # Carregar Perfil (JSON)
    with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
        perfil = json.load(f)
    
    # Carregar Produtos (JSON)
    with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
        produtos = json.load(f)
    
    # Carregar Transações (CSV)
    transacoes = pd.read_csv('data/transacoes.csv')
    
    # Carregar Atendimentos (CSV)
    atendimentos = pd.read_csv('data/historico_atendimento.csv')
    
    return perfil, produtos, transacoes, atendimentos

perfil, produtos, transacoes, atendimentos = load_data()

# 2. Interface Lateral (Resumo do João)
st.sidebar.header("Perfil do Cliente")
st.sidebar.write(f"**Nome:** {perfil['nome']}")
st.sidebar.write(f"**Perfil:** {perfil['perfil_investidor']}")
st.sidebar.write(f"**Patrimônio:** R$ {perfil['patrimonio_total']:.2f}")

# 3. Chatbot (Simulação)
st.write("Olá! Sou o Ainvestinaldo. Como posso ajudar com sua análise financeira hoje?")

user_input = st.text_input("Sua pergunta:")

if user_input:
    # Lógica simples de resposta baseada no contexto
    if "reserva" in user_input.lower():
        st.write(f"João, sua meta é chegar a R$ {perfil['metas'][0]['valor_necessario']:.2f}.")
        st.write("Sugestão de produto para você: **Tesouro Selic**, ideal para reserva de emergência.")
    
    elif "transações" in user_input.lower():
        st.write("Aqui estão suas últimas movimentações:")
        st.dataframe(transacoes.tail(5))
    
    else:
        st.write("Analisei seus dados. Com seu perfil moderado, recomendo evitar ativos de alto risco como 'Fundo de Ações' no momento.")

