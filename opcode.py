from read_json import leitura_json
from hex_to_bin import convert_bin
import build_instruction_assembly
def binaryToDecimal(binary):
    decimal, i= 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    # print(decimal)   
    return decimal

def classifica_tipo(op,fn):
    op_decimal = binaryToDecimal(op)
    if(op_decimal == 0):
        fn_decimal = binaryToDecimal(fn)
        return ('R',fn_decimal)
    elif(op_decimal == 2 or op_decimal == 3):
        return 'J'
    else:
        return ('I',op_decimal)

# Driver code
if __name__ == '__main__':
    binary = '00100000000010000000000000000000'      #00
    op = binary[:6]
    op = int(op,2)
    fn = binary[-6:]
    fn = int(fn,2)
    word = "11001"

    print(fn)
    print("classifica tipo: ", classifica_tipo(op,fn))
    bins_list = convert_bin(leitura_json())
    build_instruction_assembly.leitura_listagem_bins(bins_list)


