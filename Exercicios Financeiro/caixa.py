def simular_caixa(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    resultado = {}

    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            resultado[cedula] = quantidade
            valor %= cedula

    return resultado


def main():
    print("💵 Simulador de Caixa Eletrônico 💵")
    try:
        valor = int(input("Digite o valor do saque (em R$): "))
        if valor <= 0:
            print("Valor inválido. Digite um valor maior que zero.")
            return

        distribuicao = simular_caixa(valor)

        print("\nNotas entregues:")
        for cedula, quantidade in distribuicao.items():
            print(f"{quantidade} x R${cedula}")

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()
