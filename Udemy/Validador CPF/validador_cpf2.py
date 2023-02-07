def valida_cpf(cpf):
    cpf = [int(x) for x in cpf]
    if len(cpf) != 11:
        return False
    if all(x == cpf[0] for x in cpf[1:]):
        return False
    soma1 = sum(cpf[i] * (10 - i) for i in range(9))
    divisao1 = 11 - soma1 % 11
    if divisao1 > 9:
        divisao1 = 0
    if divisao1 != cpf[9]:
        return False
    soma2 = sum(cpf[i] * (11 - i) for i in range(10))
    divisao2 = 11 - soma2 % 11
    if divisao2 > 9:
        divisao2 = 0
    if divisao2 != cpf[10]:
        return False
    return True


cpf = input("Digite o CPF: ")
if valida_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
