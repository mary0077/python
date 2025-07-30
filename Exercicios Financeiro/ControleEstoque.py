def mostrar_menu():
    print("\n=== Controle de Estoque ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Consultar estoque")
    print("4 - Sair")

def adicionar_produto(estoque):
    produto = input("Digite o nome do produto: ").strip().title()
    try:
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Quantidade inválida. Use apenas números inteiros.")
        return

    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade

    print(f"✅ Produto '{produto}' atualizado. Quantidade atual: {estoque[produto]}")

def remover_produto(estoque):
    produto = input("Digite o nome do produto a remover: ").strip().title()
    if produto in estoque:
        del estoque[produto]
        print(f"🗑️ Produto '{produto}' removido do estoque.")
    else:
        print("Produto não encontrado no estoque.")

def consultar_estoque(estoque):
    if not estoque:
        print("📭 Estoque vazio.")
        return

    print("\n📦 Estoque Atual:")
    for produto, quantidade in estoque.items():
        print(f"- {produto}: {quantidade}")

def main():
    estoque = {}

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            remover_produto(estoque)
        elif opcao == "3":
            consultar_estoque(estoque)
        elif opcao == "4":
            print("👋 Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
