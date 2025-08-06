import unicodedata

def remover_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    return ''.join([c for c in nfkd if not unicodedata.combining(c)])

def eh_palindromo(frase):
    frase = remover_acentos(frase.lower())
    frase = ''.join(c for c in frase if c.isalnum())
    return frase == frase[::-1]

def main():
    print("=== DETECTOR DE PALÍNDROMOS ===")
    while True:
        frase = input("\nDigite uma palavra ou frase: ")
        if eh_palindromo(frase):
            print("✅ É um palíndromo!")
        else:
            print("❌ Não é um palíndromo.")

        continuar = input("\nQuer testar outra? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando o programa.")
            break

if __name__ == "__main__":
    main()
