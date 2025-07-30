import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("🎯 Jogo de Adivinhação")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        try:
            chute = int(input("Seu palpite: "))
            tentativas += 1

            if chute < 1 or chute > 100:
                print("Digite um número entre 1 e 100.")
                continue

            if chute < numero_secreto:
                print("🔽 Muito baixo!")
            elif chute > numero_secreto:
                print("🔼 Muito alto!")
            else:
                print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break

        except ValueError:
            print("❌ Entrada inválida. Digite um número inteiro.")

if __name__ == "__main__":
    jogar()
