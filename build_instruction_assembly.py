import mnemonicos
from execute_functions import execute_function_i, execute_function_r



def popula_register_base(lista):
    register_base = {
        "$0":  0,
        "$1":  0,
        "$2":  0,
        "$3":  0,
        "$4":  0,
        "$5":  0,
        "$6":  0,
        "$7":  0,
        "$8":  0,
        "$9":  0,
        "$10": 0,
        "$11": 0,
        "$12": 0,
        "$13": 0,
        "$14": 0,
        "$15": 0,
        "$16": 0,
        "$17": 0,
        "$18": 0,
        "$19": 0,
        "$20": 0,
        "$21": 0,
        "$22": 0,
        "$23": 0,
        "$24": 0,
        "$25": 0,
        "$26": 0,
        "$27": 0,
        "$28": 0,
        "$29": 0,
        "$30": 0,
        "$31": 0,
        "pc": 0,
        "hi": 0,
        "lo": 0
    }
    for contador in range(len(lista)):
        if(lista[contador] in register_base):
            register_base[lista[contador]] = lista[contador+1]
    return register_base




def leitura_listagem_bins(binary_list, dict, register_base ):
    dicionario_registers = register_base
    contador = 0
    lista_regs = list()
    lista_stdout = list()
    for i in binary_list:
        contador += 1
        instruction_type = mnemonicos.instruction_type_definition(i)
        result_assembly, dicionario_registers = assembly(i, instruction_type, dicionario_registers)
        dicionario_registers["pc"] += 4
        json_formated = {
            f"i_{contador}": result_assembly
        }
        dict.update(json_formated)
        # O registrador $12 quando carregado com o valor 65299 significa que rodou uma excessão, então o stdout
        # deve ser carregado (mas não sei com o quê). O $12 já está sendo carregado, precisa conferir se ele tem esse valor e então carregar
        # o stdout no json

        # Esse dicionário que está sendo impresso aqui, pode ser utilizado para carregar a chave regs do json, nesse print apenas os registradores
        # com valores diferentes de 0 estão sendo impressos.
        registradores_alterados = diferentes_de_zero(dicionario_registers)
        # Fazendo a lista dos regs
        lista_regs.append(registradores_alterados)

        #Fazendo lista do stdout, coloquei zero, mas deveria ser Nada o 1 seria quando dá erro, mas eu não sei qual o valor.
        if "$12" in registradores_alterados.keys() and registradores_alterados["$12"] == 65299:
            lista_stdout.append("Overflow")
        else:
            lista_stdout.append({})
        print("regs: ", registradores_alterados)
    return dict,lista_regs,lista_stdout

def diferentes_de_zero(registers):
    registradores_ocupados = {}
    for x in registers.keys():
        if registers[x] != 0:
            registradores_ocupados[x] = registers[x]
    return registradores_ocupados


def assembly(binary, type_instruction, dicionario_registers):
    dictionary_hex_separator = dict()
    dictionary_instruction = dict()
    if type_instruction == "R":

        dictionary_hex_separator["funct"] = mnemonicos.functions[f"{binary[26:]}"]
        dictionary_hex_separator["rd"] = f"${int(binary[16:21], 2)}"
        dictionary_hex_separator["rs"] = f"${int(binary[6:11], 2)}"
        dictionary_hex_separator["rt"] = f"${int(binary[11:16], 2)}"
        dictionary_hex_separator["shamt"] = int(binary[21:26], 2)

        if structure_search_type_rs_rt(dictionary_hex_separator["funct"]):
            dictionary_instruction["function"] = dictionary_hex_separator["funct"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rs"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["rt"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}")
        elif dictionary_hex_separator['funct'] == "mfco":
            dictionary_instruction["function"] = dictionary_hex_separator["funct"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rt"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["rd"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}")
        elif structure_search_type_rd(dictionary_hex_separator["funct"]):
            dictionary_instruction["function"] = dictionary_hex_separator["funct"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rd"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}")
        elif structure_search_type_rs(dictionary_hex_separator["funct"]):
            dictionary_instruction["function"] = dictionary_hex_separator["funct"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rs"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}")
        elif structure_search_type_rd_rt_rs(dictionary_hex_separator["funct"]):
            dictionary_instruction["function"] = dictionary_hex_separator["funct"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rd"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["rt"]
            dictionary_instruction["operando3"] = dictionary_hex_separator["rs"]
        elif structure_search_type_shamt(dictionary_hex_separator["funct"]):
            dictionary_instruction["function"] = dictionary_hex_separator["funct"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rd"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["rt"]
            dictionary_instruction["operando3"] = dictionary_hex_separator["shamt"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}, {dictionary_instruction['operando3']}")
        elif dictionary_hex_separator["funct"] == "syscall":
            dictionary_instruction["function"] = dictionary_hex_separator["funct"]

            print(f"{dictionary_instruction['function']}")
        else:
            dictionary_instruction["function"] = dictionary_hex_separator["funct"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rd"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["rs"]
            dictionary_instruction["operando3"] = dictionary_hex_separator["rt"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}, {dictionary_instruction['operando3']}")
        dicionario_registers = execute_function_r(
            dictionary_instruction, dicionario_registers)
    elif type_instruction == "J":
        dictionary_instruction["funct"] = mnemonicos.type_j_instructions[f"{binary[0:6]}"]
        dictionary_instruction["operando1"] = int(binary[6:], 2)
        print(
            f"{dictionary_instruction['funct']} {dictionary_instruction['operando1']}")
    elif type_instruction == "I":
        dictionary_hex_separator[
            "instruction"] = mnemonicos.type_i_instructions[f"{binary[0:6]}"]
        dictionary_hex_separator["rs"] = f"${int(binary[6:11],2)}"
        dictionary_hex_separator["rt"] = f"${int(binary[11:16], 2)}"
        dictionary_hex_separator["immediate"] = convert_int(binary[16:], 16)
        if structure_search_type_rt_rs_imm(dictionary_hex_separator["instruction"]):
            dictionary_instruction["function"] = dictionary_hex_separator["instruction"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rt"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["rs"]
            dictionary_instruction["operando3"] = dictionary_hex_separator["immediate"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}, {dictionary_instruction['operando3']}")
        elif structure_search_type_rt_imm_parent(dictionary_hex_separator["instruction"]):
            dictionary_instruction["function"] = dictionary_hex_separator["instruction"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rt"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["immediate"]
            dictionary_instruction["operando3"] = dictionary_hex_separator["rs"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}({dictionary_instruction['operando3']})")
        elif structure_search_type_rt_imm(dictionary_hex_separator["instruction"]):
            dictionary_instruction["function"] = dictionary_hex_separator["instruction"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rt"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["immediate"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}")
        elif structure_search_type_rs_rt_imm(dictionary_hex_separator["instruction"]):
            dictionary_instruction["function"] = dictionary_hex_separator["instruction"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rs"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["rt"]
            dictionary_instruction["operando3"] = dictionary_hex_separator["immediate"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}, {dictionary_instruction['operando3']}")
        dicionario_registers = execute_function_i(
            dictionary_instruction, dicionario_registers)

    return dictionary_instruction, dicionario_registers


def structure_search_type_rs_rt(funct_value):
    if funct_value in mnemonicos.instructions_r_format_rs_rt:
        return True
    return False


def structure_search_type_rd(funct_value):
    if funct_value in mnemonicos.instructions_r_format_rd:
        return True
    return False


def structure_search_type_shamt(funct_value):
    if funct_value in mnemonicos.instructions_r_format_shamt:
        return True
    return False


def structure_search_type_rs(funct_value):
    if funct_value in mnemonicos.instructions_r_format_rs:
        return True
    return False


def structure_search_type_rt_rs_imm(funct_value):
    if funct_value in mnemonicos.instructions_i_format_rt_rs_imm:
        return True
    return False


def structure_search_type_rt_imm_parent(funct_value):
    if funct_value in mnemonicos.instructions_i_format_rt_imm_parent:
        return True
    return False


def structure_search_type_rt_imm(funct_value):
    if funct_value in mnemonicos.instructions_i_format_rt_imm:
        return True
    return False


def structure_search_type_rs_rt_imm(funct_value):
    if funct_value in mnemonicos.instructions_i_format_rs_rt_imm:
        return True
    return False


def structure_search_type_rd_rt_rs(funct_value):
    if funct_value in mnemonicos.instructions_r_format_rd_rt_rs:
        return True
    return False


def convert_int(binary, tam):
    final_bin = list()

    if binary[0] == "0":
        return int(binary, 2)

    else:
        valor = int(binary, 2) - 1
        # print(binary, valor)
        binary = bin(valor).replace("0b", "")

        if len(binary) < tam:
            binary = "0" + binary

        for i in range(0, tam):
            if binary[i] == "0":
                final_bin.append('1')
            else:
                final_bin.append('0')

    return -int(''.join(final_bin), 2)
