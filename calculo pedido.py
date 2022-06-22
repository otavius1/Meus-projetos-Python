print("Bem vindo a Feijoada do Lenilton Rogério Rodrigues da Costa:D")

# Função que determina o volume da feijoada e o primeiro parâmetro de preço
def volumeFeijoada():
    global valor_feijoada
    global volume_da_porcao
    volume_da_porcao = 0
    valor_feijoada = 0
    while volume_da_porcao not in range(300,5000):
        volume_da_porcao = int(input("Qual o volume da porção do pedido? "))
        if volume_da_porcao >= 300 and volume_da_porcao < 5000:
            valor_feijoada = volume_da_porcao * 0.08
            break
        elif volume_da_porcao > 5000:
            print("Não aceitamos valores superiores a 5000")
            continue
        elif volume_da_porcao < 300:
            print("O volume mínimo é de 300ml! Qual o volume desejado? ")
            continue
        else:
            try:
                isinstance(volume_da_porcao, int)
                break
            except:
                print("Algum erro ocorreu!!")

# Função que determina a opção da feijoada, e o segundo parâmetro de preço
def opcaoFeijoada():
    global opcao
    global acompanhamento
    global volume_da_porcao
    global valor_feijoada
    opcao = "Básica" or "Premium" or "Suprema"
    while opcao != "Básica" or "Premium" or "Suprema":
        print("B - Básica (Feijão + Paiol + Costelinha)")
        print("P - Premium (Feijão + Paiol + costelinha + partes do porco)")
        print("S - Suprema (Feijão + Paiol + costelinha + partes do corpo + charque + calabresa + bacon")
        opcao = str(input("Qual a sua opção de feijoada, Básica, Premium ou Suprema? "))
        if opcao == "B":
            valor_feijoada = valor_feijoada * 1
            break
        elif opcao == "P":
            valor_feijoada = valor_feijoada * 1.25
            break
        elif opcao == "S":
            valor_feijoada = valor_feijoada * 1.50
            break
        else:
            print("Opção Inválida!")
            continue

# Função que determina o acompanhamento e o terceiro parâmetro de preço
def acompanhamentoFeijoada():
    global valor_feijoada
    global acompanhamento
    acompanhamento = 9
    while acompanhamento != 0:
        print("0 - Não desejo acompanhamentos (encerrar conta)")
        print("1 - 200g de arroz R$ 5")
        print("2 - 150g de farofa especial R$ 6")
        print("3 - 100g de couve cozida R$ 7")
        print("4 - 1 laranja descascada R$ 3")
        acompanhamento = int(input("Gostaria de algum acompanhamento? "))
        if acompanhamento == 0:
            print("O valor total é de R$: ", round(valor_feijoada, 2))
            break
        elif acompanhamento == 1:
            valor_feijoada = valor_feijoada + 5
            continue
        elif acompanhamento == 2:
            valor_feijoada = valor_feijoada + 6
            continue
        elif acompanhamento == 3:
            valor_feijoada = valor_feijoada + 7
            continue
        elif acompanhamento == 4:
            valor_feijoada = valor_feijoada + 3
            continue
        else:
            print("Opção inexistente")



#Execução de Funções
volumeFeijoada()
opcaoFeijoada()
acompanhamentoFeijoada()
