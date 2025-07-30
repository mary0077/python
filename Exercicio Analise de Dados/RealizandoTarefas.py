import json
import os

ARQUIVO_TAREFAS = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append({"descricao": descricao})
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso.")


def listar_tarefas(tarefas):
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
        return
    print("\n📋 Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['descricao']}")
    print()


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        num = int(input("Digite o número da tarefa a remover: "))
        if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            salvar_tarefas(tarefas)
            print(f"🗑️ Tarefa '{removida['descricao']}' removida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")


def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "0":
            print("👋 Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
