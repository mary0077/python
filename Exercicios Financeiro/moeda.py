TAXAS_CONVERSAO = {
    "USD": 5.10,
    "EUR": 5.55,
    "GBP": 6.20,
    "JPY": 0.035
}

def converter_moeda(valor_brl, moeda_destino):
    taxa = TAXAS_CONVERSAO.get(moeda_destino.upper())
    if taxa:
        valor_convertido = valor_brl / taxa
        return round(valor_convertido, 2)
    else:
        return None

def main():
    print("=== Conversor de Moedas ===")

    try:
        valor_brl = float(input("Digite o valor em BRL: "))
    except ValueError:
        print("Valor inválido. Digite um número.")
        return

    moeda_destino = input("Digite a moeda de destino (USD, EUR, GBP, JPY): ").upper()

    if moeda_destino not in TAXAS_CONVERSAO:
        print("Moeda não suportada.")
        return

    resultado = converter_moeda(valor_brl, moeda_destino)
    print(f"{valor_brl:.2f} BRL = {resultado:.2f} {moeda_destino}")

if __name__ == "__main__":
    main()
