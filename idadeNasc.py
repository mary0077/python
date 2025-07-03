from datetime import datetime

data_nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")

try:
    nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
    hoje = datetime.now()
    idade = hoje.year - nascimento.year

    # Ajuste se ainda não fez aniversário este ano
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    print(f"Você tem {idade} anos.")
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

except ValueError:
    print("Formato inválido. Use dd/mm/aaaa.")

