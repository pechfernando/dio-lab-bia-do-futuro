import pandas as pd
import json
import os

def carregar_dados():
    with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
        perfil = json.load(f)
    with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
        produtos = json.load(f)
    transacoes = pd.read_csv('data/transacoes.csv')
    return perfil, produtos, transacoes

def responder_pergunta(pergunta, perfil, produtos, transacoes):
    # Lógica simples do agente (pode ser substituída por chamada de LLM)
    pergunta = pergunta.lower()
    if "risco" in pergunta:
        return f"João, seu perfil é {perfil['perfil_investidor']}. Recomendo cautela com ativos de alto risco."
    return "Como seu analista, analisei seus dados e recomendo focar na reserva de emergência antes de diversificar."
