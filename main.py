#Fluxo principal
from read_json import leitura_json,nome_algoritmo,leitura_json_regs
from hex_to_bin import convert_bin
from build_instruction_assembly import leitura_listagem_bins,popula_register_base
from funcoes import cria_json
from mnemonicos import register_base





# # #Leitura json
# lista_hexadecimais = leitura_json("exemplo_config")

# #Converte lista de hx para bin
# lista_binarios = convert_bin(lista_hexadecimais)

# #Converte lista bin para dicionário de instruções
# lista_instrucoes_mips = leitura_listagem_bins(lista_binarios, register_base, regs)


#retorna lista com nomes dos algoritmos
lista_algoritmos = nome_algoritmo()

for x in range (len(lista_algoritmos)):
    nome = str(lista_algoritmos[x])
    #Leitura json
    lista_hexadecimais = leitura_json(nome)
    #Converte lista de hx para bin
    #leitura regs
    regs = popula_register_base(leitura_json_regs(nome))

    lista_binarios = convert_bin(lista_hexadecimais)
    #Converte lista bin para dicionário de instruções
    lista_instrucoes_mips,list_reg,lista_stdout = leitura_listagem_bins(lista_binarios, register_base, regs)
    #Cria json na pasta output, caso o mesmo já exista, ele sobrescreve
    cria_json(lista_hexadecimais,lista_instrucoes_mips,list_reg,lista_stdout,nome)





