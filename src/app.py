import streamlit as st
from agente import carregar_dados, responder_pergunta

st.title("🤖 Ainvestinaldo")
perfil, produtos, transacoes = carregar_dados()

pergunta = st.text_input("Como posso te ajudar?")
if pergunta:
    resposta = responder_pergunta(pergunta, perfil, produtos, transacoes)
    st.write(resposta)
