alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    notas = []
    for i in range(1, 4):
        nota = float(input(f"Nota {i}: "))
        notas.append(nota)

    media = sum(notas) / 3
    alunos[nome] = media
    print(f"{nome} cadastrado com média {media:.1f}")

print("\nAlunos Aprovados:")
for aluno, media in alunos.items():
    if media >= 7:
        print(f"{aluno} - Média: {media:.1f}")

print("\nAlunos Reprovados:")
for aluno, media in alunos.items():
    if media < 7:
        print(f"{aluno} - Média: {media:.1f}")
