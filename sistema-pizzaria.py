# Programa de vendas de Pizzaria
# Desenvolvido por: Eduarda dos Santos Inacio RU: 5540849


print("---------- Bem-vindo à Pizzaria da Eduarda Inacio ----------")
print("--------------------------- MENU ---------------------------")
print("--- Tamanho |   Pizza Salgada (PS)   |  Pizza Doce (PD)  ---")
print("---    P    |        R$ 30.00        |     R$ 34.00      ---")
print("---    M    |        R$ 45.00        |     R$ 48.00      ---")
print("---    G    |        R$ 60.00        |     R$ 66.00      ---")
print("------------------------------------------------------------")


# Variável para acumular o valor total de todos os itens do pedido
totalPedido = 0

# Laço de repetição infinito para pedidos
while True:

    # Entrada do Sabor da Pizza com validação
    sabor = input("\nEntre com o Sabor desejado(PS/PD): ").upper()

    if sabor != "PS" and sabor != "PD":
        print("Sabor inválido. Tente novamente")
        continue # Retorna ao início do laço caso o sabor seja inválido

    # Entrada do Tamanho da pizza com validação
    tamanho = input("Entre com o Tamanho desejado(P/M/G): ").upper()

    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente")
        continue # Retorna ao início do laço caso o tamanho seja inválido


# Modelo condicional aninhado para definir a pizza e seu preço
    if sabor == "PS":
        nomeSabor = "Salgada" # Variável auxiliar para a mensagem de exibição final
        if tamanho == "P":
          valorItem = 30.00
        elif tamanho == "M":
          valorItem = 45.00
        else:
          valorItem = 60.00

    elif sabor == "PD":
          nomeSabor = "Doce" # Variável auxiliar para a mensagem de exibição final
          if tamanho == "P":
            valorItem = 34.00
          elif tamanho == "M":
            valorItem = 48.00
          else:
            valorItem = 66.00


    # Atualização do acumulador com o valor da pizza escolhida
    totalPedido += valorItem
    print(f"Você pediu uma Pizza {nomeSabor} no tamanho {tamanho}: R$ {valorItem:.2f}")


    # Pergunta ao usuário se deseja adicionar mais itens ao pedido
    desejaMais = input("\nDeseja mais alguma coisa? (S/N): ").upper()

    if desejaMais == "N":
        print(f"\nO valor total a ser pago: R$ {totalPedido:.2f}")
        break # Interrupção do laço while e encerramento do programa

