import streamlit as st
from utils.calculator import add, subtract, multiply, divide, square  # Importando a função square

def main():
    st.title("Calculadora Simples")
    
    # Entrada do usuário para os números
    num1 = st.number_input("Digite o primeiro número", value=0.0)
    num2 = st.number_input("Digite o segundo número", value=0.0)
    
    # Entrada do usuário para a operação
    operation = st.selectbox("Selecione a operação", ["Somar", "Subtrair", "Multiplicar", "Dividir", "Elevar ao Quadrado"])
    
    # Calcular e exibir o resultado
    if st.button("Calcular"):
        if operation == "Somar":
            result = add(num1, num2)
        elif operation == "Subtrair":
            result = subtract(num1, num2)
        elif operation == "Multiplicar":
            result = multiply(num1, num2)
        elif operation == "Dividir":
            try:
                result = divide(num1, num2)
            except ValueError as e:
                result = str(e)  # Tratando erro de divisão por zero
        elif operation == "Elevar ao Quadrado":
            result = square(num1)  # Usando a função de elevar ao quadrado
        
        st.write(f"Resultado: {result}")

if __name__ == "__main__":
    main()
