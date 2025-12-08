reais = (int(input("Digite o valor que você possue em reais: ")))
dolarAtual = (float(input("Digite a cotação atual do dólar: ")))
euroAtual = (float(input("Digite a cotação atual do euro: ")))

dolarConvertido = reais / dolarAtual
euroConvertido = reais / euroAtual

print(f"O valor em dólar é: {dolarConvertido:.2f}")
print(f"O valor em euro é: {euroConvertido:.2f}")

