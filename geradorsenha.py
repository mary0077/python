import random

personagens = ["Gato", "Cachorro", "Dragão", "Princesa", "Robô"]
acoes = ["comeu", "achou", "pegou", "encontrou", "ganhou"]
objetos = ["Pizza", "Chave", "Livro", "Celular", "Tesouro"]
emocao = ["Feliz", "Triste", "Animado", "Assustado", "Surpreso"]
simbolos = ["!", "@", "#", "$", "%"]

def gerar_senha():
    p1 = random.choice(personagens)
    a1 = random.choice(acoes)
    o1 = random.choice(objetos)
    e1 = random.choice(emocao)
    numero = random.randint(0, 99)
    simbolo = random.choice(simbolos)
    
    senha = f"{p1}{numero}{simbolo}{o1}{e1}"
    historia = f"O {p1} {a1} {numero} {o1}s e ficou {e1}!"
    
    return senha, historia

def main():
    print("=== GERADOR DE SENHAS COM HISTÓRIA ===")
    while True:
        senha, historia = gerar_senha()
        print("\nSenha gerada:", senha)
        print("História para memorizar:", historia)
        
        continuar = input("\nGerar outra senha? (s/n): ").lower()
        if continuar != "s":
            print("Encerrando o gerador de senhas.")
            break

if __name__ == "__main__":
    main()
