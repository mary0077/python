def coletar_numeros():
    numeros = []
    print("🔢 Digite números (digite 'sair' para encerrar):")

    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("⚠️ Entrada inválida. Digite um número ou 'sair'.")

    return numeros


def analisar(numeros):
    if not numeros:
        print("⚠️ Nenhum número foi inserido.")
        return

    total = len(numeros)
    media = sum(numeros) / total
    maior = max(numeros)
    menor = min(numeros)
    ordenados = sorted(numeros)

    print("\n📊 Análise dos Números:")
    print(f"- Total de números: {total}")
    print(f"- Média: {media:.2f}")
    print(f"- Maior número: {maior}")
    print(f"- Menor número: {menor}")
    print(f"- Números em ordem crescente: {ordenados}")


def main():
    numeros = coletar_numeros()
    analisar(numeros)


if __name__ == "__main__":
    main()
