estoque = {}

while True:
    print("\n==== MENU ====")
    print("1. Adicionar produto")
    print("2. Atualizar quantidade")
    print("3. Mostrar estoque")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        if produto in estoque:
            print("Produto já existe. Use a opção 2 para atualizar a quantidade.")
        else:
            estoque[produto] = quantidade
            print("Produto adicionado com sucesso!")

    elif opcao == "2":
        produto = input("Digite o nome do produto a atualizar: ")
        if produto in estoque:
            nova_quantidade = int(input("Digite a nova quantidade: "))
            estoque[produto] = nova_quantidade
            print("Quantidade atualizada com sucesso!")
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        if not estoque:
            print("Estoque vazio.")
        else:
            print("\nEstoque atual:")
            for produto, qtd in estoque.items():
                print(f"{produto}: {qtd} unidades")

    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
