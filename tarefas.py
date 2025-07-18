def mostrar_menu():
    print("\n===== MENU =====")
    print("1. Adicionar nova tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")


def adicionar_tarefa(lista):
    descricao = input("Digite a descrição da tarefa: ")
    lista.append({"descricao": descricao, "concluida": False})
    print("✅ Tarefa adicionada com sucesso!")


def listar_tarefas(lista):
    if not lista:
        print("📭 Nenhuma tarefa cadastrada.")
        return

    print("\n📋 Lista de Tarefas:")
    for i, tarefa in enumerate(lista):
        status = "✔️" if tarefa["concluida"] else "❌"
        print(f"{i+1}. {tarefa['descricao']} - {status}")


def concluir_tarefa(lista):
    listar_tarefas(lista)
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        lista[indice]["concluida"] = True
        print("✅ Tarefa marcada como concluída.")
    except (ValueError, IndexError):
        print("⚠️ Número inválido.")


def remover_tarefa(lista):
    listar_tarefas(lista)
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        removida = lista.pop(indice)
        print(f"🗑️ Tarefa '{removida['descricao']}' removida.")
    except (ValueError, IndexError):
        print("⚠️ Número inválido.")


def main():
    tarefas = []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            concluir_tarefa(tarefas)
        elif escolha == "4":
            remover_tarefa(tarefas)
        elif escolha == "5":
            print("👋 Encerrando o programa.")
            break
        else:
            print("⚠️ Opção inválida!")


if __name__ == "__main__":
    main()
