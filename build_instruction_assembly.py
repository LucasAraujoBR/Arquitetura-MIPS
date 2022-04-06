import mnemonicos
from execute_functions import execute_function_i

def leitura_listagem_bins(binary_list, dicio):
    dict = {}
    contador = 0
    for i in binary_list:
        contador += 1
        instruction_type = mnemonicos.instruction_type_definition(i)
        json_formated = {
            f"i_{contador}": assembly(i, instruction_type)
        }
        dict.update(json_formated)
    return dict


def assembly(binary, type_instruction):
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

    elif type_instruction == "J":
        dictionary_instruction["funct"] = mnemonicos.type_j_instructions[f"{binary[0:6]}"]
        dictionary_instruction["operando1"] = int(binary[6:], 2)
        print(
            f"{dictionary_instruction['funct']} {dictionary_instruction['operando1']}")

    elif type_instruction == "I":
        dictionary_hex_separator["instruction"] = mnemonicos.type_i_instructions[f"{binary[0:6]}"]
        dictionary_hex_separator["rs"] = f"${int(binary[6:11],2)}"
        dictionary_hex_separator["rt"] = f"${int(binary[11:16], 2)}"
        dictionary_hex_separator["immediate"] = convert_int(binary[16:], 16)
        execute_function_i(dictionary_hex_separator)
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
            print(f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}")

        elif structure_search_type_rs_rt_imm(dictionary_hex_separator["instruction"]):
            dictionary_instruction["function"] = dictionary_hex_separator["instruction"]
            dictionary_instruction["operando1"] = dictionary_hex_separator["rs"]
            dictionary_instruction["operando2"] = dictionary_hex_separator["rt"]
            dictionary_instruction["operando3"] = dictionary_hex_separator["immediate"]
            print(
                f"{dictionary_instruction['function']} {dictionary_instruction['operando1']}, {dictionary_instruction['operando2']}, {dictionary_instruction['operando3']}")

    return dictionary_instruction


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


