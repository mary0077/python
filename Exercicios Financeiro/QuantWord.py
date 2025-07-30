import string

texto = input("Digite um texto: ")

# Normaliza o texto: minúsculas + remove pontuação
texto = texto.lower()
for pontuacao in string.punctuation:
    texto = texto.replace(pontuacao, "")

palavras = texto.split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print("\nContagem de palavras:")
for palavra in sorted(contagem):
    print(f"Palavra: {palavra} - {contagem[palavra]} vez(es)")
