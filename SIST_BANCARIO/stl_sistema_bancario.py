#utiliando a biblioteca streamlit
# Para instalar a biblioteca, use o comando: pip install streamlit
# Para executar o código, use o comando: streamlit run stl_sistema_bancario.py

import streamlit as st

st.set_page_config(page_title="Sistema Bancário", layout="centered")

st.title("🏦 Sistema Bancário")

# Inicialização de estados
if "saldo" not in st.session_state:
    st.session_state.saldo = 0.0
if "extrato" not in st.session_state:
    st.session_state.extrato = ""
if "numero_saques" not in st.session_state:
    st.session_state.numero_saques = 0

limite = 500
limite_saques = 3

st.subheader("Escolha uma operação:")

operacao = st.radio("Operação", ["Depositar", "Sacar", "Extrato"])

if operacao == "Depositar":
    valor = st.number_input("Informe o valor para depósito:", min_value=0.0, format="%.2f")
    if st.button("Depositar"):
        if valor > 0:
            st.session_state.saldo += valor
            st.session_state.extrato += f"Depósito: R$ {valor:.2f}\n"
            st.success(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            st.error("Valor inválido para depósito.")

elif operacao == "Sacar":
    valor = st.number_input("Informe o valor para saque:", min_value=0.0, format="%.2f")
    if st.button("Sacar"):
        if valor <= 0:
            st.error("Valor inválido para saque.")
        elif valor > st.session_state.saldo:
            st.error("Saldo insuficiente.")
        elif valor > limite:
            st.error("Valor do saque excede o limite permitido.")
        elif st.session_state.numero_saques >= limite_saques:
            st.error("Número de saques diários excedido.")
        else:
            st.session_state.saldo -= valor
            st.session_state.extrato += f"Saque: R$ {valor:.2f}\n"
            st.session_state.numero_saques += 1
            st.success(f"Saque de R$ {valor:.2f} realizado com sucesso.")

elif operacao == "Extrato":
    st.subheader("📄 Extrato")
    if st.session_state.extrato == "":
        st.info("Não foram realizadas movimentações.")
    else:
        st.text(st.session_state.extrato)
    st.write(f"**Saldo atual:** R$ {st.session_state.saldo:.2f}")
