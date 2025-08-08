# Calculadora de Média de Notas (MNDA)

# Entrada das 4 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calculando a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verificando a situação
if media >= 7.0:
    situacao = "Aprovado"
elif media >= 5.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Exibindo o resultado
print(f"\nA média do aluno foi: {round(media, 2)}")
print(f"Situação: {situacao}")
