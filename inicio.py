# from datetime import datetime
# print("Olá Mundo!!!")


# ano_atual = datetime.now() .year
# clube = "SPFC"
# campeonato_mundial = 3
# ano_fundacao = 1930

# print(f"{clube} possui {campeonato_mundial} títulos mundiais.")
# print(f"São {ano_atual - ano_fundacao} anos de existência.")

# escola = 'Senai'
# curso = 'Técnico em Desenvolvimento de Sistemas'
# uc = 'Lógica de Programação e Algoritmos'

# print(
#     f"Escola: {escola}\n"
#     f"Curso: {curso}\n"
#     f"Unidade Curricular: {uc}"
# )

print(f'Programa de empréstimo.'
      f'Responda: (0-Não) (1-Sim)')

nome_negativado = int(input('Possui nome negativado? '))
if nome_negativado == 1: # Sim
    print('Não pode realizar empréstimo.')
else:
    carteira_assinada = int(input('Possui carteira assinada? '))
    if carteira_assinada == 0: # Não
        print('Não pode realizar empréstimo.')
    else:
        possui_casa_propria = int(input('Possui casa própria? '))
        if possui_casa_propria == 0: # Não
            print('Não pode realizar empréstimo.')
        else:
            print('Conceder empréstimo.')
