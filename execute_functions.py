
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


def execute_function_r(dicionario_composto):
    funcao = dicionario_composto["instruction"]

    if funcao == "add":
        pass
    elif funcao == "sub":
        pass
    elif funcao == "slt":
        pass
    elif funcao == "and":
        pass
    elif funcao == "or":
        pass
    elif funcao == "xor":
        pass
    elif funcao == "nor":
        pass
    elif funcao == "mfhi":
        pass
    elif funcao == "mflo":
        pass
    elif funcao == "addu":
        pass
    elif funcao == "subu":
        pass
    elif funcao == "mult":
        pass
    elif funcao == "multu":
        pass
    elif funcao == "div":
        pass
    elif funcao == "divu":
        pass
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

