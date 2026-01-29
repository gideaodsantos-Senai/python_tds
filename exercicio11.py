print("Calculadora de Resistor Limitador")

fonte = float(input("Insira a tensão da fonte de alimentação: "))
operacao = float(input("Insira a tensão de operação do dispositivo/LED: "))
correnDese = float(input("Corrente desejada: "))

resistor = (fonte - operacao) / correnDese

print(f"O resistor necessário é {resistor} Ohms")