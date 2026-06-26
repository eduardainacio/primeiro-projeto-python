# Programa para cálculo de mensalidade de plano de saúde baseado na idade
# Desenvolvido por: Eduarda dos Santos Inacio RU: 5540849

print("Bem-vindo(a) ao Sistema da Eduarda dos Santos Inacio")

# Entrada de dados
valorBase = float(input("Informe o valor Base do plano: R$ "))

idade = int(input("Informe a Idade do cliente: "))

# Estrutura para definir porcentagem adicional
if idade >= 0 and idade < 19:

    # Se a idade for maior ou igual que 0 e menor que 19, o valor será de 100%
    porcentagem = 100 / 100

elif idade >= 19 and idade < 29:

    # Se a idade for maior ou igual que 19 e menor que 29, o valor será de 150%
    porcentagem = 150 / 100

elif idade >= 29 and idade < 39:

    # Se a idade for maior ou igual que 29 e menor que 39, o valor será de 225%
    porcentagem = 225 / 100

elif idade >= 39 and idade < 49:

    # Se a idade for maior ou igual que 39 e menor que 49, o valor será de 240%
    porcentagem = 240 / 100

elif idade >= 49 and idade < 59:
  
    # Se a idade for maior ou igual que 49 e menor que 59, o valor será de 350%
    porcentagem = 350 / 100

else:
    porcentagem = 600 / 100 # Se a idade for maior ou igual que 59, o valor será de 600%


# Aplica a porcentagem sobre o valor base
valorMensal = valorBase * porcentagem



# Exibe o resultado formatado para o usuário

print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")
