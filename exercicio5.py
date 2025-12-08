precoCamisa = 12.50
camisas = int(input("Digite o número que camisas compradas: "))

if camisas <= 5:
    desconto = 0.03

if camisas > 5 and camisas <= 10:
    desconto = 0.05

if camisas > 10:
    desconto = 0.07

valorTotal = (precoCamisa * camisas) * (1 - desconto)    

print(f"O valor total da compra é: R$ {valorTotal:.2f}")