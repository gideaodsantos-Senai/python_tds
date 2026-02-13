import random
alunos = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana']

random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")

sorteada = random.choice(alunos)
print(f"Alunos sorteado: {sorteada}")