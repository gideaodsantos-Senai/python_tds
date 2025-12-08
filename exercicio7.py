N = input('Digite um número inteiro positivo N: ')

total = 0
for i in range(int(N)):
    numero = input(f'Digite o {i+1}º número: ')
    total += int(numero)

print(f'A média dos números digitados é: {total / int(N):.2f}')
