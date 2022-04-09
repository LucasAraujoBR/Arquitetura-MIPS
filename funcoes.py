import json
import os
import shutil
from datetime import date


def backup():
    data_atual = date.today()
    data_em_texto = '{}-{}-{}'.format(data_atual.day,
                                      data_atual.month, data_atual.year)
    cur_path = os.path.dirname(__file__)
    source = f'{cur_path}/output/instruções.json'
    destination = f'{cur_path}/backup/{data_em_texto}_output.json'
    shutil.move(source, destination)


def valida_nomeclatura(json):
    if(json != {}):
        try:
            print(json["function"])
            return "function"
        except:
            print(json["funct"])
            return "funct"
    else:
        return ""


def novo_json(lista_hex, dict_mips):
    print(dict_mips)
    contador = 0
    json_formatado = []
    for x in range(len(lista_hex)):
        contador += 1
        temp_json = dict_mips["i_"+str(contador)]
        # print(temp_json['function']+f" {temp_json['operando1']}",)
        function = valida_nomeclatura(temp_json)
        if(function != ''):
            
            if(temp_json[function] == 'syscall'):
                aux = {

                    "hex": f"{lista_hex[x]}",
                    "text": f"{temp_json[function]}",
                    "regs": {},
                    "mem": {},
                    "stdout": {}

                }
            elif(temp_json[function] == 'lw' or temp_json[function] == 'sw' or temp_json[function] == 'lb' or temp_json[function] == 'lbu' or temp_json[function] == 'sb'):
                aux = {

                    "hex": f"{lista_hex[x]}",
                    "text": f"{temp_json[function]}"+f" {temp_json['operando1']}"+f", {temp_json['operando2']}" + f"({temp_json['operando3']})",
                    "regs": {},
                    "mem": {},
                    "stdout": {}

                }
            elif('operando2' not in temp_json and temp_json[function] != 'syscall'):
                aux = {

                    "hex": f"{lista_hex[x]}",
                    "text": f"{temp_json[function]}"+f" {temp_json['operando1']}",
                    "regs": {},
                    "mem": {},
                    "stdout": {}

                }
            elif('operando3' not in temp_json and 'operando2' in temp_json and temp_json[function] != 'syscall'):
                aux = {

                    "hex": f"{lista_hex[x]}",
                    "text": f"{temp_json[function]}"+f" {temp_json['operando1']}"+f", {temp_json['operando2']}",
                    "regs": {},
                    "mem": {},
                    "stdout": {}

                }
            elif(temp_json[function] != 'syscall'):
                aux = {

                    "hex": f"{lista_hex[x]}",
                    "text": f"{temp_json[function]}"+f" {temp_json['operando1']}"+f", {temp_json['operando2']}" + f", {temp_json['operando3']}",
                    "regs": {},
                    "mem": {},
                    "stdout": {}

                }
        else:
            aux = {
                "hex": f"{lista_hex[x]}",
                "text": {},
                "regs": {},
                "mem": {},
                "stdout": {}
            }

        json_formatado.append(aux)
    return json_formatado


def cria_json(lista_hex, lista_mips, nome):
    cur_path = os.path.dirname(__file__)
    lista_arquivos = [
        arquivo
        for arquivo in os.listdir(f"{cur_path}/output/")
        if arquivo.endswith(".json")
    ]
    print(lista_arquivos)
    data = {}
    if len(lista_mips) > 0:
        nome_arquivo = f'GrupoA.{nome}.output'
        caminho_arquivo = f"{cur_path}/output/{nome_arquivo}.json"
        print(caminho_arquivo)
        if nome_arquivo in lista_arquivos:
            with open(caminho_arquivo, encoding="utf-8") as json_file_read:
                data = json.load(json_file_read)
                dictdict = novo_json(lista_hex, lista_mips)
                json_file_read.close()
            with open(caminho_arquivo, "w", encoding="utf-8") as outfile:
                json.dump(dictdict, outfile,  indent=4, ensure_ascii=False)
                outfile.close()
        else:
            with open(caminho_arquivo, "w", encoding="utf-8") as outfile:
                data = novo_json(lista_hex, lista_mips)
                json.dump(data, outfile, indent=4, ensure_ascii=False)
                outfile.close()

    else:
        print("Lista Vazia")
