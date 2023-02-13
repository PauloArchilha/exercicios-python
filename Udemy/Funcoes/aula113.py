# Exercícios com funções
# ==================================================
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicar(*args):
    total = 1
    for num in args:
        total *= num
    return total


def par_impar(num):
    par = num % 2 == 0
    if par:
        return f'O {num} é Par!'
    return f'O número {num} é Impar!'


tot = multiplicar(2, 3, 4, 5, 6, 7, 8)
print(tot)
print(par_impar((tot)))
