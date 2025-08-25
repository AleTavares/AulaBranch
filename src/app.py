def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def main():
    print("Calculadora Simples")
    print("Operações disponíveis: +, -, *, /")
    a = float(input("Digite o primeiro número: "))
    op = input("Digite a operação (+, -, *, /): ")
    b = float(input("Digite o segundo número: "))

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        result = divide(a, b)
    else:
        result = "Operação inválida"

    print("Resultado:", result)

if __name__ == "__main__":
    main()