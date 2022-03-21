import json 
import os
import shutil
from datetime import date

def backup():
    data_atual = date.today()
    data_em_texto = '{}-{}-{}'.format(data_atual.day, data_atual.month,data_atual.year)
    cur_path = os.path.dirname(__file__)
    source = f'{cur_path}/output/instruções.json'
    destination = f'{cur_path}/backup/{data_em_texto}_output.json'
    shutil.move(source,destination)


def novo_json(lista_hex,lista_mips):
    contador = 0
    json_formatado = {}
    for x in range(len(lista_hex)):
        contador+=1
        aux = {
            f"instrução_{contador}":{
                "hex": f"{lista_hex[x]}",
                "text": f"{lista_mips[x]}",
                "regs": {},
                "mem": {},
                "stdout": {}
            }
        }
        json_formatado.update(aux)
    return json_formatado


def cria_json(lista_hex,lista_mips):
    cur_path = os.path.dirname(__file__)
    lista_arquivos = [
        arquivo
        for arquivo in os.listdir(f"{cur_path}/output/")
        if arquivo.endswith(".json")
    ]
    print(lista_arquivos)
    data = {}
    if len(lista_mips) > 0:
        nome_arquivo = 'GrupoLucasAraujoMatheusFidelis.mips.output'
        caminho_arquivo = f"{cur_path}/output/{nome_arquivo}.json"
        print(caminho_arquivo)
        if nome_arquivo in lista_arquivos:
            with open(caminho_arquivo, encoding="utf-8") as json_file_read:
                data = json.load(json_file_read)
                dictdict = novo_json(lista_hex,lista_mips)
                data.update(dictdict)
                json_file_read.close()
            with open(caminho_arquivo, "w", encoding="utf-8") as outfile:
                json.dump(data, outfile,  indent=4,ensure_ascii=False)
                outfile.close()
        else:
            with open(caminho_arquivo, "w", encoding="utf-8") as outfile:
                data = novo_json(lista_hex,lista_mips)
                json.dump(data, outfile, indent=4,ensure_ascii=False)
                outfile.close()
                
    else:
        print("Lista Vazia")

