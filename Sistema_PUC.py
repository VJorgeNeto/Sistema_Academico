'''
Nome: Valdionice Jorge da Silva Neto
Curso: Inteligência Artificial Aplicada
'''

nomes = []

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
            #menu_operacoes_2()
            print("EM DESENVOLVIMENTO")
            menu_principal()
        elif opcao == "3":
            #menu_operacoes_3()
            print("EM DESENVOLVIMENTO")
            menu_principal()
        elif opcao == "4":
            #menu_operacoes_4()
            print("EM DESENVOLVIMENTO")
            menu_principal()
        elif opcao == "5":
            #menu_operacoes_5()
            print("EM DESENVOLVIMENTO")
            menu_principal()
        elif opcao == "9":
            print("Finalizando aplicação...")
        else:
            print("Informe uma opção válida!")
            menu_principal()

# MENU DE OPERAÇÕES PARA A OPÇÃO: ESTUDANTES NO MENU PRIMCIPAL
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
        print("Para finalizar a inclusão digite: sair...")

        # LISTA: adição de alunos na lista nomes
        while True:
            nome = input("Digite o nome: ")    
            
            if nome.lower() == "sair":
              break
            
            nomes.append(nome)
        
        print("Nomes digitados: ")

        for nome in nomes:
            print(nome)
        menu_operacoes_1()
        
    elif opcao == "2":
        print("===== LISTAGEM =====\n")

        # LISTA: listagem dos alunos cadastrados seguido pela validação da lista vazia.
        if nomes:
            print("Listagem de estudantes:")
            for nome in nomes:
                print(nome)
        else:
            print("Não há estudantes cadastrados.\n")
            print("Voltando ao Menu de Operações...")
        menu_operacoes_1()

    elif opcao == "3":
        print("===== ATUALIZAÇÃO =====\n")
        print("Finalizando aplicação...")

    elif opcao == "4":
        print("===== EXCLUSÃO =====\n")
        print("Finalizando aplicação...")
    else:
        menu_principal()

'''
Abaixo já foi desenvolvido a navegação para as operações das outras opções do menu principal.
Porém suas chamadas foram comentadas e substituidas pela mensagem "EM DESENVOLVIMENTO" a fim de seguir o solicitado para entrega.
'''
# MENU DE OPERAÇÕES PARA A OPÇÃO: PROFESSORES NO MENU PRIMCIPAL
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

# MENU DE OPERAÇÕES PARA A OPÇÃO: DISCIPLINAS NO MENU PRIMCIPAL
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

# MENU DE OPERAÇÕES PARA A OPÇÃO: TURMAS NO MENU PRIMCIPAL
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

# MENU DE OPERAÇÕES PARA A OPÇÃO: MATRÍCULAS NO MENU PRIMCIPAL
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