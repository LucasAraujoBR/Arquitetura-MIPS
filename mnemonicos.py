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
    "pc": 4194304,
    "hi": 0,
    "lo": 0
}
functions = {
    "100000": "add",
    "100001": "addu",
    "100100": "and",
    "011010": "div",
    "011011": "divu",
    "001000": "jr",
    "010000": "mfhi",
    "010010": "mflo",
    "011000": "mult",
    "011001": "multu",
    "100111": "nor",
    "100101": "or",
    "000000": "sll",
    "000100": "sllv",
    "101010": "slt",
    "000011": "sra",
    "000111": "srav",
    "000010": "srl",
    "000110": "srlv",
    "100010": "sub",
    "100011": "subu",
    "001100": "syscall",
    "100110": "xor"
}
type_j_instructions = {
    "000010": "j",
    "000011": "jal"
}
type_i_instructions = {
    "001000": "addi",
    "001001": "addiu",
    "001100": "andi",
    "000111": "bgtz",
    "000100": "beq",
    "000001": "bltz",
    "000110": "blez",
    "000101": "bne",
    "100000": "lb",
    "100100": "lbu",
    "001111": "lui",
    "100011": "lw",
    "001101": "ori",
    "001010": "slti",
    "101011": "sw",
    "001110": "xori",
    "101000": "sb"
}
indexing = {
    "R": [26, 21, 16, 11, 6, 5],
    "J": [26],
    "I": [26, 21, 16]
}

instructions_r_format_rs_rt = ("mult", "multu", "div", "divu")
instructions_r_format_rt_rd = ("mfco")
instructions_r_format_rd = ("mfhi", "mflo")
instructions_r_format_rs = ("jr")
instructions_r_format_shamt = ("sll", "srl", "sra")
instructions_r_format_rd_rt_rs = ("sllv", "srav", "srlv")
instruction_syscall = ("syscall")

instructions_i_format_rt_rs_imm = ("addi", "addiu", "andi", "ori", "slti", "sltiu", "xori")
instructions_i_format_rt_imm_parent = ("lw", "sw", "lbu", "sb", "lb")
instructions_i_format_rt_imm = ("lui", "bltz")
instructions_i_format_rs_rt_imm = ("beq", "bne")

def instruction_type_definition(binary):
    decimal_value = int(binary[:6], 2)
    if decimal_value == 0:
        return "R"
    elif decimal_value in [2, 3]:
        return "J"
    else:
        return "I"

