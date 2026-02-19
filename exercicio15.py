
lista_compras = []

quantidade_produtos = int(input("Quantos produtos você deseja adicionar? "))

for i in range(quantidade_produtos):
    print(f"\nProduto {i + 1}")
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))

    lista_compras.append([nome, quantidade])

print("\n=== Lista de Compras ===")
for item in lista_compras:
    print(f"Produto: {item[0]} | Quantidade: {item[1]}")
