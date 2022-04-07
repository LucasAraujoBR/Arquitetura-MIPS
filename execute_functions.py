
def execute_function_i(dicionario_composto, banco_de_registradores):
    funcao = dicionario_composto["instruction"]

    if funcao == "addi":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 + valor2
    #     Rever essa funcionalidade, acho que está incorreta
    elif funcao == "addiu":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 + valor2
    elif funcao == "slti":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        if valor1 < valor2:
            banco_de_registradores[dicionario_composto["operando1"]] =1
        else:
            banco_de_registradores[dicionario_composto["operando1"]] = 0
    elif funcao == "andi":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 & valor2
    elif funcao == "ori":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 | valor2
    elif funcao == "xori":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 ^ valor2
    else:
        print("não foi pedido!")


def divide_lo_hi(total_valor):
    pass


def execute_function_r(dicionario_composto, banco_de_registradores):
    funcao = dicionario_composto["instruction"]

    if funcao == "add":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 + valor2
    elif funcao == "sub":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 - valor2
    elif funcao == "slt":
        pass
    elif funcao == "and":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 & valor2
    elif funcao == "or":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 | valor2
    elif funcao == "xor":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 ^ valor2
    elif funcao == "nor":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        valor_or = valor1 | valor2
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 | valor2
    elif funcao == "mfhi":
        valor1 = banco_de_registradores["hi"]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1
    elif funcao == "mflo":
        valor1 = banco_de_registradores["lo"]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1
    elif funcao == "addu":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 + valor2
    elif funcao == "subu":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 - valor2
    elif funcao == "mult":
        valor1 = banco_de_registradores[dicionario_composto["operando1"]]
        valor2 = banco_de_registradores[dicionario_composto["operando2"]]
        total_valor = valor1 * valor2
        divide_lo_hi(total_valor)
        # banco_de_registradores[dicionario_composto["lo"]] = valor1 / valor2
        # banco_de_registradores[dicionario_composto['hi']] = valor1 % valor2
    elif funcao == "multu":
        valor1 = banco_de_registradores[dicionario_composto["operando1"]]
        valor2 = banco_de_registradores[dicionario_composto["operando2"]]
        total_valor = valor1 * valor2
        divide_lo_hi(total_valor)
        # banco_de_registradores[dicionario_composto["lo"]] = valor1 / valor2
        # banco_de_registradores[dicionario_composto['hi']] = valor1 % valor2
    elif funcao == "div":
        valor1 = banco_de_registradores[dicionario_composto["operando1"]]
        valor2 = banco_de_registradores[dicionario_composto["operando2"]]
        banco_de_registradores[dicionario_composto["lo"]] = valor1 / valor2
        banco_de_registradores[dicionario_composto['hi']] = valor1 % valor2
    elif funcao == "divu":
        valor1 = banco_de_registradores[dicionario_composto["operando1"]]
        valor2 = banco_de_registradores[dicionario_composto["operando2"]]
        banco_de_registradores[dicionario_composto["lo"]] = valor1 / valor2
        banco_de_registradores[dicionario_composto['hi']] = valor1 % valor2
    elif funcao == "sll":
        pass
    elif funcao == "srl":
        pass
    elif funcao == "sra":
        pass
    elif funcao == "sllv":
        pass
    elif funcao == "srlv":
        pass
    elif funcao == "srav":
        pass
    else:
        pass

