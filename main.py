#Fluxo principal
from read_json import leitura_json
from hex_to_bin import convert_bin
from build_instruction_assembly import leitura_listagem_bins
from funcoes import cria_json

# #Leitura json
lista_hexadecimais = leitura_json()

#Converte lista de hx para bin
lista_binarios = convert_bin(lista_hexadecimais)

#Converte lista bin para dicionário de instruções
lista_instrucoes_mips = leitura_listagem_bins(lista_binarios)
print(lista_instrucoes_mips)

#Cria json na pasta output, caso o mesmo já exista, ele sobrescreve
cria_json(lista_hexadecimais,lista_instrucoes_mips)




