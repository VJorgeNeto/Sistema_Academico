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
        print("===== INCLUSÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "2":
        print("===== LISTAGEM =====\n")
        print("Finalizando aplicação...")
    elif opcao == "3":
        print("===== ATUALIZAÇÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "4":
        print("===== EXCLUSÃO =====\n")
        print("Finalizando aplicação...")
    else:
        menu_principal()

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
        print("===== INCLUSÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "2":
        print("===== LISTAGEM =====\n")
        print("Finalizando aplicação...")
    elif opcao == "3":
        print("===== ATUALIZAÇÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "4":
        print("===== EXCLUSÃO =====\n")
        print("Finalizando aplicação...")
    else:
        menu_principal()

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
        print("===== INCLUSÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "2":
        print("===== LISTAGEM =====\n")
        print("Finalizando aplicação...")
    elif opcao == "3":
        print("===== ATUALIZAÇÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "4":
        print("===== EXCLUSÃO =====\n")
        print("Finalizando aplicação...")
    else:
        menu_principal()

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
        print("===== INCLUSÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "2":
        print("===== LISTAGEM =====\n")
        print("Finalizando aplicação...")
    elif opcao == "3":
        print("===== ATUALIZAÇÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "4":
        print("===== EXCLUSÃO =====\n")
        print("Finalizando aplicação...")
    else:
        menu_principal()    

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
        print("===== INCLUSÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "2":
        print("===== LISTAGEM =====\n")
        print("Finalizando aplicação...")
    elif opcao == "3":
        print("===== ATUALIZAÇÃO =====\n")
        print("Finalizando aplicação...")
    elif opcao == "4":
        print("===== EXCLUSÃO =====\n")
        print("Finalizando aplicação...")
    else:
        menu_principal()

menu_principal()
