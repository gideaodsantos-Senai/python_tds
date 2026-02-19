# ATIVIDADE 1

produtos = {
    1: {"nome": "Monitor LED 24\"", "preco": 599.99, "quantidade": 1},
    2: {"nome": "Teclado wireless", "preco": 49.26, "quantidade": 1},
    3: {"nome": "Mouse wireless", "preco": 19.90, "quantidade": 1},
    4: {"nome": "Cartucho colorido", "preco": 54.00, "quantidade": 2}
}

print("-------- Carrinho de Compras --------")

total = 0

for codigo, dados in produtos.items():
    subtotal = dados["preco"] * dados["quantidade"]
    total += subtotal
    
    print(f'{dados["nome"]} - R$ {dados["preco"]:.2f} - '
          f'{dados["quantidade"]} un - R$ {subtotal:.2f}')

print("--------------------------------------")
print(f"Total: R$ {total:.2f}")

# ATIVIDADE 2

produtos = {}

quantidade_produtos = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade_produtos):
    print(f"\nProduto {i+1}")
    
    codigo = int(input("Código: "))
    nome = input("Nome: ")
    preco = float(input("Preço unitário: "))
    quantidade = int(input("Quantidade: "))
    
    produtos[codigo] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

print("\n-------- Carrinho de Compras --------")

total = 0

for codigo, dados in produtos.items():
    subtotal = dados["preco"] * dados["quantidade"]
    total += subtotal
    
    print(f'{dados["nome"]} - R$ {dados["preco"]:.2f} - '
          f'{dados["quantidade"]} un - R$ {subtotal:.2f}')

print("--------------------------------------")
print(f"Total: R$ {total:.2f}")