def valida_cpf(cpf):
    cpf = str(cpf)
    if len(cpf) != 11:
        return False
    if not cpf.isdigit():
        return False
    if cpf in ("00000000000", "11111111111", "22222222222", "33333333333", "44444444444",
               "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"):
        return False
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    dv = 11 - (soma % 11)
    if dv > 9:
        dv = 0
    if int(cpf[9]) != dv:
        return False
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    dv = 11 - (soma % 11)
    if dv > 9:
        dv = 0
    if int(cpf[10]) != dv:
        return False
    return True


cpf = input("Digite o número do seu CPF: ")
if valida_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")
