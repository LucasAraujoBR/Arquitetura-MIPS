registers = {
    "00000": "$0",
    "00001": "$1",
    "00010": "$2",
    "00011": "$3",
    "00100": "$4",
    "00101": "$5",
    "00110": "$6",
    "00111": "$7",
    "01000": "$8",
    "01001": "$9",
    "01010": "$10",
    "01011": "$11",
    "01100": "$12",
    "01101": "$13",
    "01110": "$14",
    "01111": "$15",
    "10000": "$16",
    "10001": "$17",
    "10010": "$18",
    "10011": "$19",
    "10100": "$20",
    "10101": "$21",
    "10110": "$22",
    "10111": "$23",
    "11000": "$24",
    "11001": "$25",
    "11010": "$26",
    "11011": "$27",
    "11100": "$28",
    "11101": "$29",
    "11110": "$30",
    "11111": "$31",
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
instructions_r_format_shamt = ("sll", "srl")


instructions_i_format_rs_rt_imm = ("addi", "addiu", "andi", "ori", "slti", "sltiu")
instructions_i_format_rt_imm_parent = ("lw", "sw", "lbu", "sb")
instructions_i_format_rt_imm = ("lui")

def instruction_type_definition(binary):
    decimal_value = int(binary[:6], 2)
    if decimal_value == 0:
        return "R"
    elif decimal_value in [2, 3]:
        return "J"
    else:
        return "I"

