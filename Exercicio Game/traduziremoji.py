# tradutor_emoji.py

emoji_dicionario = {
    "feliz": "😄",
    "triste": "😢",
    "pizza": "🍕",
    "cachorro": "🐶",
    "gato": "🐱",
    "amor": "❤️",
    "fogo": "🔥",
    "sol": "☀️",
    "chuva": "🌧️"
}

def traduzir_para_emoji(frase):
    palavras = frase.lower().split()
    traducao = []
    for palavra in palavras:
        if palavra in emoji_dicionario:
            traducao.append(emoji_dicionario[palavra])
        else:
            traducao.append(palavra)
    return ' '.join(traducao)

def main():
    print("=== Tradutor de Emojis ===")
    frase = input("Digite uma frase: ")
    resultado = traduzir_para_emoji(frase)
    print("Tradução:", resultado)

if __name__ == "__main__":
    main()
