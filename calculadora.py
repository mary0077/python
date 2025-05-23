# calculadora.py

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

def main():
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", adicionar(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtrair(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif escolha == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
x