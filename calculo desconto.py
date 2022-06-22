print("Bem vindo a loja do Lenilton Rogério Rodrigues!")

# Variáveis
valor = float(input("Qual o valor do produto? ")) #valor inicial do produto
quantidade = int(input("Qual a quantidade do produto? ")) #quantidade solicitada do produto
desconto_1 = valor * 0.97 #desconto de 3%
desconto_2 = valor * 0.94 #desconto de 6%
desconto_3 = valor * 0.9 #desconto de 10%

# Função Principal
def descontoProgressivo (valor, quantidade):
    if quantidade <= 4:
        print("O valor total é sem desconto e fica em R$: ", valor * quantidade)
    elif quantidade <= 19:
        print("O valor total tem o desconto de 3% e fica em R$: ", round(desconto_1 * quantidade, 2))
    elif quantidade <= 99:
        print("o valor total tem o desconto de 6% e fica em R$: ", round(desconto_2 * quantidade, 2))
    else:
        print("o valor total tem o desconto de 10% e fica em R$: ", round(desconto_3 * quantidade, 2))

# Execução
print("O valor total é R$: ", valor * quantidade)
descontoProgressivo(valor, quantidade)



