import random

personagens = ["um dragão", "uma princesa", "um robô", "um gato falante", "um pirata"]
cenarios = ["na floresta encantada", "no fundo do mar", "em Marte", "num castelo abandonado", "num parque de diversões"]
objetos = ["um celular mágico", "um mapa do tesouro", "um skate voador", "um livro secreto", "um chapéu invisível"]
situacoes = ["decidiu pedir uma pizza voadora", "achou um portal para outra dimensão", "ganhou superpoderes", "resolveu montar uma banda de rock", "foi desafiado a uma corrida intergaláctica"]

def gerar_historia():
    personagem = random.choice(personagens)
    cenario = random.choice(cenarios)
    objeto = random.choice(objetos)
    situacao = random.choice(situacoes)

    historia = f"Era uma vez {personagem} que encontrou {objeto} {cenario}. Ele {situacao}!"
    return historia

def main():
    print("=== GERADOR DE HISTÓRIAS ===")
    while True:
        print("\n" + gerar_historia())
        continuar = input("\nGerar outra história? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando o gerador de histórias. Até mais!")
            break

if __name__ == "__main__":
    main()
