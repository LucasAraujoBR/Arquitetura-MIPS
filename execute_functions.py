from RegistersBase import RegistersBase
def execute_function_i(dicionario_composto, banco_de_registradores):
    funcao = dicionario_composto["function"]

    if funcao == "addi":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = dicionario_composto["operando3"]
        soma = valor2+valor1
        if soma > 2147483647:
            banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,
                                                                    "$12",65299)
        else:
            banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores, dicionario_composto["operando1"], soma )

    #     Rever essa funcionalidade, acho que está incorreta
    elif funcao == "addiu":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = dicionario_composto["operando3"]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor2+valor1)
    elif funcao == "slti":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = dicionario_composto["operando3"]
        if valor1 < valor2:
            banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], 1)
        else:
            banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], 0)
    elif funcao == "andi":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = dicionario_composto["operando3"]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor1 & valor2)
    elif funcao == "ori":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = dicionario_composto["operando3"]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 | valor2
    elif funcao == "xori":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = dicionario_composto["operando3"]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 ^ valor2
    elif funcao == "sll":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = dicionario_composto["operando3"]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 << valor2
    elif funcao == "srl":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = dicionario_composto["operando3"]
        banco_de_registradores[dicionario_composto["operando1"]] = srl(valor1, valor2)
    elif funcao == "sra":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = dicionario_composto["operando3"]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1 >> valor2
    else:
        print("não foi pedido: " + funcao)

    return banco_de_registradores

def divide_lo_hi(total_valor):
    pass


def execute_function_r(dicionario_composto, banco_de_registradores):
    funcao = dicionario_composto["function"]

    if funcao == "add":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        soma = valor2 + valor1
        if soma > 2147483647:
            banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores, "$12", 65299)
        else:
            banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores, dicionario_composto["operando1"], soma)

    elif funcao == "sub":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor1 - valor2)
    elif funcao == "slt":
        pass
    elif funcao == "and":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor1 & valor2)
    elif funcao == "or":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor1 | valor2)
    elif funcao == "xor":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor1 ^ valor2)
    elif funcao == "nor":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        valor_or = valor1 | valor2
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"],  valor1 | valor2)
    elif funcao == "mfhi":
        valor1 = banco_de_registradores["hi"]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1
    elif funcao == "mflo":
        valor1 = banco_de_registradores["lo"]
        banco_de_registradores[dicionario_composto["operando1"]] = valor1
    elif funcao == "addu":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor2 + valor1)
    elif funcao == "subu":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor1 - valor2)
    elif funcao == "mult":
        valor1 = banco_de_registradores[dicionario_composto["operando1"]]
        valor2 = banco_de_registradores[dicionario_composto["operando2"]]

        total_valor = valor1 * valor2
        if total_valor > 0:
            binario = complemento_palavra(total_valor, 64)
        else:
            binario = complemento_palavra_neg(total_valor, 64)
        lo = int(binario[0:31], 2)
        hi = int(binario[32:], 2)

        banco_de_registradores["lo"] = lo
        banco_de_registradores['hi'] = hi

    elif funcao == "multu":
        valor1 = banco_de_registradores[dicionario_composto["operando1"]]
        valor2 = banco_de_registradores[dicionario_composto["operando2"]]
        total_valor = valor1 * valor2
        if total_valor > 0:
            binario = complemento_palavra(total_valor, 64)
        else:
            binario = complemento_palavra_neg(total_valor, 64)
        lo = int(binario[0:31], 2)
        hi = int(binario[32:], 2)

        banco_de_registradores["lo"] = lo
        banco_de_registradores['hi'] = hi

    elif funcao == "div":
        valor1 = banco_de_registradores[dicionario_composto["operando1"]]
        valor2 = banco_de_registradores[dicionario_composto["operando2"]]
        banco_de_registradores["lo"] = valor1 // valor2
        banco_de_registradores['hi'] = valor1 % valor2
    elif funcao == "divu":
        valor1 = banco_de_registradores[dicionario_composto["operando1"]]
        valor2 = banco_de_registradores[dicionario_composto["operando2"]]
        banco_de_registradores["lo"] = valor1 // valor2
        banco_de_registradores['hi'] = valor1 % valor2
    elif funcao == "sllv":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor1 << valor2)
    elif funcao == "srlv":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores, dicionario_composto["operando1"], srl(valor1, valor2))
    elif funcao == "srav":
        valor1 = banco_de_registradores[dicionario_composto["operando2"]]
        valor2 = banco_de_registradores[dicionario_composto["operando3"]]
        banco_de_registradores = RegistersBase.alter_dicionario(banco_de_registradores,dicionario_composto["operando1"], valor1 >> valor2)
    else:
        print("não foi pedido: " + funcao)
    return banco_de_registradores


def srl(inteiro, shift):

    if inteiro >= 0:
        return inteiro >> shift
    else:
        numero = -inteiro
        binario = complemento_palavra(numero, 32)
        binario = complemento_a_1(binario)
        binario = complemento_a_2_int_bin(binario)
        binario = "0"*shift + binario[0:32-shift]
        return int(binario, 2)

def complemento_palavra_neg(numero, tam_palavra):
    binario = bin(numero)

    binario = binario.replace("-", "").replace("0b", "")

    binario = "1" * (tam_palavra -len(binario)) + binario
    return binario


def complemento_palavra(numero,tam_palavra):
    binario = bin(numero)

    binario = binario.replace("-", "").replace("0b", "")

    if not binario == tam_palavra:
        binario = "0" * (tam_palavra -len(binario)) + binario

    else:
        return binario

    return binario


def complemento_a_1(palavra):
    complemento1 = ""
    for x in palavra:
        if x == "0":
            complemento1 = complemento1 + "1"
        else:
            complemento1 = complemento1 + "0"

    return complemento1


def complemento_a_2_int_bin(palavra):
    val = int(palavra, 2)
    val = val + 1
    bin = complemento_palavra_neg(val, 32)
    return bin


def complemento_a_2_bin_int(palavra):
    val = int(palavra, 2)
    val = val - 1
    bin = complemento_palavra(val, 32)
    return bin


def complemento_a_1_bin_int(palavra):
    palavra_final  = ""
    for x in palavra:
        if x == "0":
            palavra_final += "1"
        else:
            palavra_final += "0"
    return palavra_final


