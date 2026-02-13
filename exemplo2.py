alunos = ['Michele Oliveira']
alunos.append('João Silva')

while True:
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    resposta = input("Digite adicionar mais um aluno? (S/N) ")
    if resposta.upper() == 'N':
        break
print(f"Alunos cadsatrados: {alunos}")