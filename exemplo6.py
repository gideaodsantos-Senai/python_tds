alunos = ['Adriana', 'João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana']

procurar = 'José'
if procurar in alunos:
    indice = alunos.index(procurar)
    print(f"{procurar} está na lista na posição {indice} .")
else:
    print(f"{procurar} não está na lista.")