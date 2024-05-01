'''
Nome: Valdionice Jorge da Silva Neto
Curso: Inteligência Artificial Aplicada
'''
import json

# Função do menu principal
def menu_principal():
    opcao = ''
    while opcao != '9':
        print("---- MENU PRINCIPAL ----\n"
        "------------------------")
        print("(1)  Gerenciar estudantes.\n"
            "(2)  Gerenciar professores.\n"
            "(3)  Gerenciar disciplinas\n"
            "(4)  Gerenciar turmas.\n"
            "(5)  Gerenciar matrículas.\n"
            "(9)  Sair.\n"
            " \n")
        
        opcao = input("informe a opção desejada: ")
        # Validação das opções do menu para seguir às operações de cada opção
        if opcao == "1":
            menu_operacoes_1()
        elif opcao == "2":
            menu_operacoes_2()
        elif opcao == "3":
            menu_operacoes_3()
        elif opcao == "4":
            menu_operacoes_4()
        elif opcao == "5":
            menu_operacoes_5()
        elif opcao == "9":
            print("Finalizando aplicação...")
        else:
            print("Informe uma opção válida!")
            menu_principal()

# Função para carregar os dados do arquivo JSON
def carregar_dados_estudantes():
    try:
        with open('estudantes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_dados_estudantes(estudantes):
    with open('estudantes.json', 'w',encoding="utf-8") as file:
        json.dump(estudantes, file, indent=4,ensure_ascii=False)

def carregar_dados_professores():
    try:
        with open('professores.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_dados_professores(professores):
    with open('professores.json', 'w',encoding="utf-8") as file:
        json.dump(professores, file, indent=4,ensure_ascii=False)

def carregar_dados_disciplinas():
    try:
        with open('disciplinas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_dados_disciplinas(disciplinas):
    with open('disciplinas.json', 'w',encoding="utf-8") as file:
        json.dump(disciplinas, file, indent=4,ensure_ascii=False)

def carregar_dados_matriculas():
    try:
        with open('matriculas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_dados_matriculas(matriculas):
    with open('matriculas.json', 'w',encoding="utf-8") as file:
        json.dump(matriculas, file, indent=4,ensure_ascii=False)

def carregar_dados_turmas():
    try:
        with open('turmas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_dados_turmas(turmas):
    with open('turmas.json', 'w',encoding="utf-8") as file:
        json.dump(turmas, file, indent=4,ensure_ascii=False)

# Funções CRUD estudantes
def cadastrar_estudantes():
    print("Inclusão de estudantes")
    while True:
        codigo_estudante = int(input("Digite o código do estudante: "))
        nome_estudante = input("Digite o nome do estudante: ")
        cpf_estudante = int(input("Digite o CPF do estudante (sem ponto): "))
    
        novo_cadastro = {'Código': codigo_estudante, 'Nome': nome_estudante, 'CPF':cpf_estudante}
        estudantes.append(novo_cadastro)
        
        if input("Deseja cadastrar um novo estudante (s/n): ") == "n":
            salvar_dados_estudantes(estudantes)
            break

def listar_estudantes():
    print("Os estudantes cadastrados são:\n")   
    for estudante in estudantes:
        print("Código:", estudante['Código'])
        print("Nome:", estudante['Nome'])
        print("CPF:", estudante['CPF'])
        print()

def remover_estudantes():
    print("Remoção de estudantes\n")
    codigo = input("Informe o código do estudante que deseja remover: ")
    for estudante in estudantes:
        if estudante['Código'] == codigo:
            estudantes.remove(estudante)
            salvar_dados_estudantes(estudantes)
            print("Estudante removido com sucesso!")
            return
    else:
        print("Estudante não encontrado.")

def editar_estudantes():
    print("Edição de estudantes")
    codigo = input("Informe o código do estudante que deseja editar: ")
    for estudante in estudantes:
        if estudante['Código'] == codigo:
            print("Estudante encontrado. Preencha os novos dados:")
            estudante['Nome'] = input("Novo nome: ")
            estudante['CPF'] = input("Novo CPF para cadastro: ")
            salvar_dados_estudantes(estudantes)
            print("Estudante editado com sucesso!")
            return
    else:
        print("Estudante não encontrado.")

# Carregar dados dos estudantes
estudantes = carregar_dados_estudantes()

# Funções CRUD professores
def cadastrar_professores():
    print("Inclusão de professores")
    while True:
        codigo_professor = input("Digite o código do professor: ")
        nome_professor = input("Digite o nome do professor: ")
        disciplina_ministrada = input("Digite a disciplina ministrada pelo professor: ")
    
        novo_cadastro = {'Código': codigo_professor, 'Nome': nome_professor, 'Disciplina': disciplina_ministrada}
        professores.append(novo_cadastro)
        
        if input("Deseja cadastrar outro professor (s/n): ").lower() != "s":
            salvar_dados_professores(professores)
            break

def listar_professores():
    print("Os professores cadastrados são:")
    for professor in professores:
        print("Código:", professor['Código'])
        print("Nome:", professor['Nome'])
        print("Disciplina:", professor['Disciplina'])
        print()

def remover_professores():
    print("Remoção de professores")
    codigo = input("Informe o código do professor que deseja remover: ")
    for professor in professores:
        if professor['Código'] == codigo:
            professores.remove(professor)
            salvar_dados_professores(professores)
            print("Professor removido com sucesso!")
            return
    else:
        print("Professor não encontrado.")

def editar_professores():
    print("Edição de professores")
    codigo = input("Informe o código do professor que deseja editar: ")
    for professor in professores:
        if professor['Código'] == codigo:
            print("Professor encontrado. Preencha os novos dados:")
            professor['Nome'] = input("Novo nome: ")
            professor['Disciplina'] = input("Nova disciplina ministrada: ")
            salvar_dados_professores(professores)
            print("Professor editado com sucesso!")
            return
    else:
        print("Professor não encontrado.")

# Carregar dados dos professores
professores = carregar_dados_professores()

# Funções CRUD disciplinas
def cadastrar_disciplinas():
    print("Inclusão de disciplinas")
    while True:
        codigo_disciplina = input("Digite o código da disciplina: ")
        nome_disciplina = input("Digite o nome da disciplina: ")
    
        novo_cadastro = {'Código': codigo_disciplina, 'Nome': nome_disciplina}
        disciplinas.append(novo_cadastro)

        if input("Deseja cadastrar outra disciplina (s/n): ").lower() != "s":
            salvar_dados_disciplinas(disciplinas)
            break

def listar_disciplinas():
    print("As disciplinas cadastradas são:")
    for disciplina in disciplinas:
        print("Código:", disciplina['Código'])
        print("Nome:", disciplina['Nome'])
        print()

def remover_disciplinas():
    print("Remoção de disciplinas")
    codigo = input("Informe o código da disciplina que deseja remover: ")
    for disciplina in disciplinas:
        if disciplina['Código'] == codigo:
            disciplinas.remove(disciplina)
            salvar_dados_disciplinas(disciplinas)
            print("Disciplina removida com sucesso!")
            return
    else:
        print("Disciplina não encontrada.")

def editar_disciplinas():
    print("Edição de disciplinas")
    codigo = input("Informe o código da disciplina que deseja editar: ")
    for disciplina in disciplinas:
        if disciplina['Código'] == codigo:
            print("Disciplina encontrada. Preencha os novos dados:")
            disciplina['Nome'] = input("Novo nome: ")
            salvar_dados_disciplinas(disciplinas)
            print("Disciplina editada com sucesso!")
            return
    else:
        print("Disciplina não encontrada.")

# Carregar dados das disciplinas
disciplinas = carregar_dados_disciplinas()

# Funções CRUD turmas
def cadastrar_turmas():
    print("Inclusão de turmas")
    while True:
        codigo_turma = input("Digite o código da turma: ")
        disciplina_turma = input("Digite a disciplina da turma: ")
        periodo_turma = input("Digite o período da turma: ")
    
        nova_turma = {'Código': codigo_turma, 'Disciplina': disciplina_turma, 'Período': periodo_turma}
        turmas.append(nova_turma)

        if input("Deseja cadastrar outra turma (s/n): ").lower() != "s":
            salvar_dados_turmas(turmas)
            break

def listar_turmas():
    print("As turmas cadastradas são:")
    for turma in turmas:
        print("Código:", turma['Código'])
        print("Disciplina:", turma['Disciplina'])
        print("Período:", turma['Período'])
        print()

def remover_turmas():
    print("Remoção de turmas")
    codigo = input("Informe o código da turma que deseja remover: ")
    for turma in turmas:
        if turma['Código'] == codigo:
            turmas.remove(turma)
            salvar_dados_turmas(turmas)
            print("Turma removida com sucesso!")
            return
    else:
        print("Turma não encontrada.")

def editar_turmas():
    print("Edição de turmas")
    codigo = input("Informe o código da turma que deseja editar: ")
    for turma in turmas:
        if turma['Código'] == codigo:
            print("Turma encontrada. Preencha os novos dados:")
            turma['Disciplina'] = input("Nova disciplina: ")
            turma['Período'] = input("Novo período: ")
            salvar_dados_turmas(turmas)
            print("Turma editada com sucesso!")
            return
    else:
        print("Turma não encontrada.")

# Carregar dados das turmas
turmas = carregar_dados_turmas()

# Funções CRUD matrículas
def cadastrar_matriculas():
    print("Inclusão de matrículas")
    while True:
        codigo_matricula = input("Digite o código da matrícula: ")
        aluno_matricula = input("Digite o nome do aluno: ")
        turma_matricula = input("Digite o código da turma: ")
    
        nova_matricula = {'Código': codigo_matricula, 'Aluno': aluno_matricula, 'Turma': turma_matricula}
        matriculas.append(nova_matricula)

        if input("Deseja cadastrar outra matrícula (s/n): ").lower() != "s":
            salvar_dados_matriculas(matriculas)
            break

def listar_matriculas():
    print("As matrículas cadastradas são:")
    for matricula in matriculas:
        print("Código:", matricula['Código'])
        print("Aluno:", matricula['Aluno'])
        print("Turma:", matricula['Turma'])
        print()

def remover_matriculas():
    print("Remoção de matriculas")
    codigo = input("Informe o código da matricula que deseja remover: ")
    for matricula in matriculas:
        if matricula['Código'] == codigo:
            matriculas.remove(matricula)
            salvar_dados_matriculas(matriculas)
            print("Matricula removida com sucesso!")
            return
    else:
        print("Matricula não encontrada.")

def editar_matriculas():
    print("Edição de matriculas")
    codigo = input("Informe o código da matricula que deseja editar: ")
    for matricula in matriculas:
        if matricula['Código'] == codigo:
            print("Matricula encontrada. Preencha os novos dados:")
            matricula['Aluno'] = input("Novo aluno: ")
            matricula['Turma'] = input("Nova turma: ")
            salvar_dados_matriculas(matriculas)
            print("Matricula editada com sucesso!")
            return
    else:
        print("Matricula não encontrada.")   

# Carregar dados das matriculas
matriculas = carregar_dados_matriculas()

# Menu de operações para estudantes
def menu_operacoes_1():
    print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n"
          "******************************************\n"
          "(1)  Incluir.\n"
          "(2)  Listar.\n"
          "(3)  Atualizar.\n"
          "(4)  Excluir.\n"
          "(9)  Voltar ao menu pirncipal.\n"
          " \n")
    
    opcao = input("informe a ação desejada: ")

    if opcao == "1":
        cadastrar_estudantes()
        print("\n===== Voltando ao menu anterior =====\n")    
        menu_operacoes_1()
        
    elif opcao == "2":
        listar_estudantes()
        print("\n===== Voltando ao menu anterior =====\n")    
        menu_operacoes_1()

    elif opcao == "3":
        editar_estudantes()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_1()

    elif opcao == "4":
        remover_estudantes()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_1()
    elif opcao == "9":
        menu_principal()
    else:
        print("Opção inválida.")
        menu_operacoes_1()

# Menu de operações para professores
def menu_operacoes_2():
    print("***** [PROFESSORES] MENU DE OPERAÇÕES *****\n"
          "******************************************\n"
          "(1)  Incluir.\n"
          "(2)  Listar.\n"
          "(3)  Atualizar.\n"
          "(4)  Excluir.\n"
          "(9)  Voltar ao menu pirncipal.\n"
          " \n")
    
    opcao = input("informe a ação desejada: ")

    if opcao == "1":
        cadastrar_professores()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_2()
    elif opcao == "2":
        listar_professores()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_2()
    elif opcao == "3":
        editar_professores()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_2()
    elif opcao == "4":
        remover_professores()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_2()
    else:
        menu_principal()

# Menu de operações para disciplinas
def menu_operacoes_3():
    print("***** [DISCIPLINAS] MENU DE OPERAÇÕES *****\n"
          "******************************************\n"
          "(1)  Incluir.\n"
          "(2)  Listar.\n"
          "(3)  Atualizar.\n"
          "(4)  Excluir.\n"
          "(9)  Voltar ao menu pirncipal.\n"
          " \n")
    
    opcao = input("informe a ação desejada: ")

    if opcao == "1":
        cadastrar_disciplinas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_3()
    elif opcao == "2":
        listar_disciplinas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_3()
    elif opcao == "3":
        editar_disciplinas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_3()
    elif opcao == "4":
        remover_disciplinas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_3()
    else:
        menu_principal()

# Menu de operações para turmas
def menu_operacoes_4():
    print("***** [TURMAS] MENU DE OPERAÇÕES *****\n"
          "******************************************\n"
          "(1)  Incluir.\n"
          "(2)  Listar.\n"
          "(3)  Atualizar.\n"
          "(4)  Excluir.\n"
          "(9)  Voltar ao menu pirncipal.\n"
          " \n")
    
    opcao = input("informe a ação desejada: ")

    if opcao == "1":
        cadastrar_turmas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_4()
    elif opcao == "2":
        listar_turmas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_4()
    elif opcao == "3":
        editar_turmas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_4()
    elif opcao == "4":
        remover_turmas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_4()
    else:
        menu_principal()    

# Menu de operações para matriculas
def menu_operacoes_5():
    print("***** [MATRÍCULAS] MENU DE OPERAÇÕES *****\n"
          "******************************************\n"
          "(1)  Incluir.\n"
          "(2)  Listar.\n"
          "(3)  Atualizar.\n"
          "(4)  Excluir.\n"
          "(9)  Voltar ao menu pirncipal.\n"
          " \n")
    
    opcao = input("informe a ação desejada: ")

    if opcao == "1":
        cadastrar_matriculas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_5()
    elif opcao == "2":
        listar_matriculas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_5()
    elif opcao == "3":
        editar_matriculas()
        print("Finalizando aplicação...")
        menu_operacoes_5()
    elif opcao == "4":
        remover_matriculas()
        print("\n===== Voltando ao menu anterior =====\n")
        menu_operacoes_5()
    else:
        menu_principal()

menu_principal()