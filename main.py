tarefas = []

def adicionar_tarefa(nome, descricao, prioridade='Normal', categoria='Geral'):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }
    tarefas.append(tarefa)

def listar_tarefas():
    for tarefa in tarefas:
        status = 'Concluída' if tarefa['concluida'] else 'Pendente'
        print(f"[{status}] {tarefa['nome']} (Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}) - {tarefa['descricao']}")

def marcar_concluida(nome):
    for tarefa in tarefas:
        if tarefa['nome'] == nome:
            tarefa['concluida'] = True
            break

def exibir_por_prioridade(prioridade):
    for tarefa in tarefas:
        if tarefa['prioridade'] == prioridade:
            status = 'Concluída' if tarefa['concluida'] else 'Pendente'
            print(f"[{status}] {tarefa['nome']} (Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}) - {tarefa['descricao']}")

def exibir_por_categoria(categoria):
    for tarefa in tarefas:
        if tarefa['categoria'] == categoria:
            status = 'Concluída' if tarefa['concluida'] else 'Pendente'
            print(f"[{status}] {tarefa['nome']} (Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}) - {tarefa['descricao']}")

def exibir_menu():
    print("\nMenu de Comandos:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Exibir Tarefas por Prioridade")
    print("5. Exibir Tarefas por Categoria")
    print("6. Sair")

def menu_de_comandos():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome da Tarefa: ")
            descricao = input("Descrição da Tarefa: ")
            prioridade = input("Prioridade da Tarefa (Baixa, Normal, Alta): ")
            categoria = input("Categoria da Tarefa: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            nome = input("Nome da Tarefa a ser marcada como concluída: ")
            marcar_concluida(nome)
        elif escolha == '4':
            prioridade = input("Prioridade das Tarefas a exibir (Baixa, Normal, Alta): ")
            exibir_por_prioridade(prioridade)
        elif escolha == '5':
            categoria = input("Categoria das Tarefas a exibir: ")
            exibir_por_categoria(categoria)
        elif escolha == '6':
            break
        else:
            print("Opção inválida! Tente novamente.")

menu_de_comandos()
