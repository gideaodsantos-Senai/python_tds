import random
alunos = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana']

random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
alunos.sort()

print(f"Lista ordenada crescentemente: {alunos}")
alunos.sort(reverse=True)

print(f"Lista ordenada decrescentemente: {alunos}")