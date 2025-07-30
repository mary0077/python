from collections import Counter
import string

# Entrada do usuário
texto = input("Digite o texto: ")
palavra_oculta = input("Digite a palavra oculta: ").lower()

# Limpeza
texto_limpo = texto.translate(str.maketrans('', '', string.punctuation)).lower()
palavras = texto_limpo.split()

# Frequência
contador = Counter(palavras)
mais_comuns = contador.most_common(5)

# Busca por palavras que contêm a palavra oculta
palavras_ocultas = [p for p in palavras if palavra_oculta in p]

# Resultado
print("\nTop 5 palavras mais frequentes:")
for i, (palavra, freq) in enumerate(mais_comuns, 1):
    print(f"{i}. {palavra} - {freq}x")

print(f"\nPalavras que contêm '{palavra_oculta}':")
for palavra in palavras_ocultas:
    print(f"- {palavra}")
