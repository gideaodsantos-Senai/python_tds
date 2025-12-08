import requests #biblioteca para fazer requisições HTTP

cep = input("Digite o CEP (somente números): ")
cep = cep.replace("-", "").strip()  # Remove hífens e espaços em branco

if len(cep) != 8 or not cep.isdigit():
    print("CEP inválido. Digite um CEP com 8 números.")
else:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    dados = resposta.json()
    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        logradouro = dados.get("logradouro", "")
        complemento = dados.get("complemento", "")
        bairro = dados.get("bairro", "")
        cidade = dados.get("localidade", "")
        estado = dados.get("uf", "")

        print(f"\n --- Endereço encontrado ---")
        print(f"Logradouro: {logradouro}")
        print(f"Complemento: {complemento}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")