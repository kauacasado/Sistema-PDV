import FuncCadastro

opcao = ""

while opcao != "0":
    print("-----Bem vindo ao PDV-----")
    print("-----escolha uma opção-----")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("0 - Sair")
    opcao = input("Digite sua opção de escolha: ")
    if opcao == "1":
        FuncCadastro.cadastrarproduto()
    elif opcao == "2":
        FuncCadastro.listarprodutos()
    elif opcao == "0":
        print("SISTEMA ENCERRADO")
    else:
        print("Opção inválida! Tente novamente.")