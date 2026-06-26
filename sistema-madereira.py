# Programa para venda de madeira
# Desenvolvido por: Eduarda dos Santos Inacio RU: 5540849

print("Bem-vindo(a) a Madeireira da Lenhadora Eduarda Inacio")
print("")

# Função para a escolha do tipo de madeira e retornar seu valor por m³
def escolha_tipo():
    while True:
        print("Entre com o Tipo de Madeira desejado")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")

        tipo = input(">>").upper().strip()

        # Verificação da opção para retorna o valor correspondente à tabela de preços
        if tipo == "PIN":
            return 150.40
        elif tipo == "PER":
            return 170.20
        elif tipo == "MOG":
            return 190.90
        elif tipo == "IPE":
            return 210.10
        elif tipo == "IMB":
            return 220.70
        else: # Caso a opção seja inválida, o programa exibe erro e repete a pergunta
            print("Escolha inválida, entre com o modelo novamente")
            print(" ")

# Função para a quantidade de toras e calculo do desconto
def qtd_toras():
    while True:
        try:
            qtd = float(input("Entre com a quantidade de toras (m³): "))

            if qtd > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras")
                print("Por favor, entre com a quantidade novamente")
                print(" ")
                continue

            # Estrutura para definir o desconto
            if qtd < 100:
                desconto = 0 # Sem desconto para valores baixos
            elif qtd >= 100 and qtd < 500:
                desconto = 4/100
            elif qtd >= 500 and qtd < 1000:
                desconto = 9/100
            elif qtd >= 1000 and qtd <= 2000:
                desconto = 16/100

            return qtd, desconto

        except ValueError: # Captura erros caso o usuário não digite números
            print("Valor não numérico! Por favor, digite um número.")

# Função para seleção do valor adicional do transporte
def transporte():
    while True:
        print("Escolha o tipo de Transporte:")
        print("1 - Transporte Rodoviário - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")

        opcao_transporte = input(">>")

        if opcao_transporte == "1":
            return 1000.00
        elif opcao_transporte == "2":
            return 2000.00
        elif opcao_transporte == "3":
            return 2500.00
        else:
            print("Tipo de transporte invalido, entre com o número novamente.")
            print("")

# CÓDIGO PRINCIPAL (MAIN)

# Chama as funções e armazena em variáveis
tipoMadeira = escolha_tipo()
qtdToras, desconto = qtd_toras()
valorTransporte = transporte()

# Calculo do valor total: valor da madeira com desconto + transporte
total = ((tipoMadeira * qtdToras) * (1 - desconto)) + valorTransporte

# Exibição do resultado final
print(f"Total: R$ {total:.2f}")
