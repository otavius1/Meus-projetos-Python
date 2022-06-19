print("Bem-Vindo a pizzaria do Lenilton Rogério Rodrigues da Costa! :D ")
print(" --------------------Cardápio-----------------------")
print(" | Código | Descrição | Pizza Média | Pizza Grande |")
print(" |   21   | Napolitana| R$ 20.00    | R$ 26.00     |")
print(" |   22   | Margherita| R$ 20.00    | R$ 26.00     |")
print(" |   23   | Calabresa | R$ 25.00    | R$ 32.50     |")
print(" |   24   | Toscana   | R$ 30.00    | R$ 39.00     |")
print(" |   25   | Portuguesa| R$ 30.00    | R$ 39.00     |")
print(" ---------------------------------------------------")
# Função Principal
sabor = "21" or "22" or "23" or "24" or "25"
tamanho = "M" or "G"

def pede_pizza():
    global preco, preco1
    sabor = "21" or "22" or "23" or "24" or "25"
    tamanho = "M" or "G"
    preco = 20
    # Loop sabor
    while sabor != "21" or "22" or "23" or "24" or "25":
        sabor = input("Qual o sabor? Digite o código: ")
        if sabor == "21":
            print("Você pediu uma Pizza Napolitana")
            break
        elif sabor == "22":
            print("Você pediu uma Pizza Margherita")
            break
        elif sabor == "23":
            preco = preco + 5
            print("Você pediu uma pizza de Calabresa")
            break
        elif sabor == "24":
            preco = preco + 10
            print("Você pediu uma pizza de Toscana")
            break
        elif sabor == "25":
            preco = preco + 10
            print("Você pediu uma pizza de Portuguesa")
            break
        else:
            print("Opção Inválida!")
            continue
    # Loop tamanho
    while tamanho != "M" or "G":
        tamanho = input("Qual o tamanho? (M ou G): ")
        if tamanho == "G":
            preco = preco * 1.3
            break
        elif tamanho == "M":
            break
        elif tamanho != "M" or "G":
            print("Opção Inválida!!!")
            continue
    print("O valor a ser pago é de R$: ", preco)

# Função pedido novo
def novo_pedido(sabor, tamanho):
    global preco1, preco
    preco1 = 20
    adicional = "S" or "N"
    while adicional != "S" or "N":
        adicional = input("Deseja fazer mais algum pedido? (S/N): ")
        if adicional == "S":
            while sabor != "21" or "22" or "23" or "24" or "25":
                sabor = input("Qual o sabor? Digite o código: ")
                if sabor == "21":
                    print("Você pediu uma Pizza Napolitana")
                    break
                elif sabor == "22":
                    print("Você pediu uma Pizza Margherita")
                    break
                elif sabor == "23":
                    preco1 = preco1 + 5
                    print("Você pediu uma pizza de Calabresa")
                    break
                elif sabor == "24":
                    preco1 = preco1 + 10
                    print("Você pediu uma pizza de Calabresa")
                    break
                elif sabor == "25":
                    preco1 = preco1 + 10
                    print("Você pediu uma pizza de Calabresa")
                    break
                else:
                    print("Opção Inválida!")
                    continue
            # Loop tamanho
            while tamanho != "M" or "G":
                tamanho = input("Qual o tamanho? (M ou G): ")
                if tamanho == "G":
                    preco1 = preco1 * 1.3
                    break
                elif tamanho == "M":
                    break
                elif tamanho != "M" or "G":
                    print("Opção Inválida!!!")
                    continue
            print("O valor a ser pago é de R$: ", preco1)
        elif adicional == "N":
            print("Obrigado pela atenção!")
            break
        else:
            print("Opção Inválida")
            continue

def informa_valor():
    print("O valor total é de R$: ", preco + preco1)

# Execução das funções
pede_pizza()
novo_pedido(sabor, tamanho)
informa_valor()
