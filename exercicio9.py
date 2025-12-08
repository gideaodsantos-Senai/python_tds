print("Bem vindo a sua conta Corrente!")
nome = input("Por favor, digite seu nome completo: ")

senha_correta = "123456"

senha = input("Por favor, digite sua senha de 6 dígitos: ")
if senha != senha_correta:
    print("Senha incorreta! Você tem 2 tentativas.")
    for tentativa in range(2):
        senha = input("Digite sua senha novamente: ")
        if senha == senha_correta:
            print("Senha correta! Acesso concedido.")
            break
        else:
            print("Senha incorreta! Você tem mais 1 tentantiva")
    else:
        print("Sua senha foi bloqueada. Dirija-se a um de nossos caixas")
        exit()

print(f"Olá, {nome}! Seja bem-vindo ao nosso banco!.")
saldo = 0.0

adicionar = float(input("Digite o valor a ser adicionado na sua conta: R$ "))
saldo += adicionar
print(f"Seu saldo atual é de R$ {saldo:.2f}")
