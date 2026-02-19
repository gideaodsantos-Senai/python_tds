
agentes = {
    "007": "Londres",
    "Viúva Negra": "Budapeste",
    "Ethan Hunt": "Paris"
}

agente_procurado = "Bourne"

localizacao = agentes.get(agente_procurado, "Agente Desconhecido")
print(f"Busca por {agente_procurado}: {localizacao}")

agentes["007"] = "Tóquio"

agentes["Trinity"] = "Matrix"

print("\n=== RELATÓRIO GERAL DE AGENTES ATIVOS ===")
for agente, local in agentes.items():
    print(f"Agente: {agente} | Localização Atual: {local}")