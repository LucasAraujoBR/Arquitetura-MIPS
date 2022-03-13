import mnemonicos
import opcode

def leitura_listagem_bins(binary_list):
    for i in binary_list:
        instruction_type = mnemonicos.instruction_type_definition(i)
        assembly(i,instruction_type)

def assembly(binary, type_instruction):
    dictionay_instruction = dict()
    if type_instruction == "R":
        dictionay_instruction["function"] = mnemonicos.functions[f"{binary[26:]}"]
        dictionay_instruction["register_resposta"] = mnemonicos.registers[f"{binary[16:21]}"]
        dictionay_instruction["register_font1"] = mnemonicos.registers[f"{binary[6:11]}"]
        dictionay_instruction["register_font2"] = mnemonicos.registers[f"{binary[11:16]}"]
        print(dictionay_instruction)
    elif type_instruction == "J":
        pass
    elif type_instruction == "I":
        pass

