import DadosDoSistema

def cadastrarproduto():
    codigo_produto = int(input("Insira o código do produto: "))
    nome_produto = input("Insira o nome do produto: ")
    valor_produto = float(input("Insira o valor do produto: "))
    estoque_produto = int(input("Insira quantos desse produto estão em estoque: "))

    for item in DadosDoSistema.produtos:
        if item["codigo"] == codigo_produto:
            print("Esse produto já está cadastrado")
            return
        
    produto = {
    "codigo": codigo_produto,
    "nome": nome_produto,
    "valor": valor_produto,
    "estoque": estoque_produto,
}
    DadosDoSistema.produtos.append(produto)
    print("O produto foi cadastrado no sistema!")

def listarprodutos():
    for itens in DadosDoSistema.produtos:
        print("Código:", itens["codigo"])
        print("Nome:", itens["nome"])
        print("Valor:", itens["valor"])
        print("Estoque:", itens["estoque"])