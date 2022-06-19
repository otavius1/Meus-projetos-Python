listaProduto = []
def cadastrarProduto(codigo):
  print('Você selecionou a opção de Cadastrar Produto')
  print('O código do produto é: {:0>3}'.format(codigo))
  nome = input("Entre com o nome do produto: ")
  fabricante = input("Entre com o fabricante do produto: ")
  valor = float(input("Entre com o valor R$ do produto: "))
  dicionarioProduto = {'codigo'   : codigo,
                         'nome' : nome,
                         'fabricante': fabricante,
                         'valor': valor}
  listaProduto.append(dicionarioProduto.copy())
def consultarProduto():
  while True:
    try:
      print('Você Selecionou a Opção de Consultar Produto')
      opConsultar = int(input('Entre com a opção desejada\n1- Consultar Todos os Produtos\n2- Consultar Produtos pelo Código\n3- Consultar Produtos pelo Fabricante\n4- Retornar\n-->'))
      if opConsultar == 1:
        print('-' * 20)
        for produto in listaProduto:
            for key, value in produto.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 2:
        print("Você Selecionou a Opção Produtos por Código")
        entrada = int(input('Digite o Código: '))
        print('-' * 20)
        for produto in listaProduto:
          if(produto['codigo'] == entrada):
            for key, value in produto.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 3:
        print("Você Selecionou a Opção Consultar Produto pelo Fabricante")
        entrada = input("Digite o Fabricante: ")
        print('-' * 20)
        for produto in listaProduto:
          if(produto['fabricante'] == entrada):
            for key, value in produto.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 4:
        break
      else:
        print('Por favor digite somente o que pede')
        continue
    except ValueError:
      print('Esse número não existe')
      continue
def removerProduto():
    print("Você Selecionou para Remover Produto")
    entrada = int(input("Digite o Código do produto que irá remover: "))
    for produto in listaProduto:
      if(produto['codigo'] == entrada):
        listaProduto.remove(produto)
    else:
      print("Você removeu o código.")


print("Bem-vindo ao Controle de Estoque do Lenilton Rogério Rodrigues da Costa")
registroProduto = 0
while True:
    try:
      opcao = int(input("Digite a opção desejada:\n1- Cadastrar Produtos\n2- Consultar Produtos\n3- Remover Produtos\n4- Sair\n--> "))
      if opcao == 1:
        registroProduto = registroProduto + 1
        cadastrarProduto(registroProduto)
      elif opcao == 2:
        consultarProduto()
      elif opcao == 3:
        removerProduto()
      elif opcao == 4:
        print("Programa finalizado")
        break
      else:
        print("Digite apenas uma opção do MENU")
        continue
    except ValueError:
        print("Esse número não existe")
