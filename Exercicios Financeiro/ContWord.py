import string

def contar_palavras(frase):
    frase = frase.lower()
    frase = frase.translate(str.maketrans("", "", string.punctuation))
    palavras = frase.split()

    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    # Ordena por frequência
    for palavra, qtd in sorted(contagem.items(), key=lambda item: item[1], reverse=True):
        print(f"{palavra}: {qtd}")

# Programa principal
entrada = input("Digite uma frase: ")
contar_palavras(entrada)
