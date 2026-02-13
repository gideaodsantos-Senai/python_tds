numeros = []

print('Digite 5 números inteiros:')
for i in range(5):
    numero = int(input(f'Número {i + 1}: '))
    numeros.append(numero)

print(f"A soma dos números é: {sum(numeros)}")
print(f"O maior número é: {max(numeros)}")
print(f"O menor número é: {min(numeros)}")
print(f"A média dos números é: {sum(numeros) / len(numeros)}")
