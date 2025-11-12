import streamlit as st
from utils.calculator import add, subtract, multiply, divide

def main():
    st.title("Calculadora Simples")
    
    # Entrada do usuário para os números
    num1 = st.number_input("Digite o primeiro número", value=0.0)
    num2 = st.number_input("Digite o segundo número", value=0.0)
    
   ":
    main()