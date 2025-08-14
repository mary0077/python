def gerar_ascii(palavra):
    palavra = palavra.upper()
    arte = ""
    for letra in palavra:
        if letra == "A":
            arte += "  #  \n # # \n#####\n#   #\n#   #\n\n"
        elif letra == "B":
            arte += "#### \n#   #\n#### \n#   #\n#### \n\n"
        elif letra == "C":
            arte += " ####\n#    \n#    \n#    \n ####\n\n"
        elif letra == " ":
            arte += "\n"
        else:
            arte += letra + "\n\n"
    return arte

def main():
    print("=== GERADOR DE ARTE ASCII ===")
    frase = input("Digite uma palavra ou frase: ")
    print("\n" + gerar_ascii(frase))

if __name__ == "__main__":
    main()
