# print(list(range(10, 16)))
# print(list(range(10, 16, 2)))
# print(list(range(16, 10, -1)))
# print(list(range(16, 10, -2)))

print('Operação de Divisão')
while True:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    if n2 == 0:
        print('Divisão por zero não é permitida. Tente novamente.')
        break
    print(f"{n1} / {n2} = {(n1 / n2):.2f}")
print('Fim da Operação de Divisão')
