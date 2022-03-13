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


def novo_json(dicionario,contador):
    json_formatado = {
        f"instrução_{contador}":{
            "hex": f"{dicionario['hex']}",
            "text": f"{dicionario['text']}",
            "regs": {"$8":23,"pc":124},
            "output":"",
        }
    }
    return json_formatado


def cria_json(dicionario,contador):
    cur_path = os.path.dirname(__file__)
    lista_arquivos = [
        arquivo
        for arquivo in os.listdir(f"{cur_path}/output/")
        if arquivo.endswith(".json")
    ]
    print(lista_arquivos)
    data = {}
    if len(dicionario) > 0:
        nome_arquivo = 'Instruções'
        caminho_arquivo = f"{cur_path}/output/{nome_arquivo}.json"
        print(caminho_arquivo)

        if f"{nome_arquivo}.json" in lista_arquivos:
            with open(caminho_arquivo, encoding="utf-8") as json_file_read:
                data = json.load(json_file_read)
                dictdict = novo_json(dicionario,contador)
                data.update(dictdict)
                json_file_read.close()
            with open(caminho_arquivo, "w", encoding="utf-8") as outfile:
                json.dump(data, outfile,  indent=4,ensure_ascii=False)
                outfile.close()
        else:
            with open(caminho_arquivo, "w", encoding="utf-8") as json_file:
                aux = novo_json(dicionario,contador)
                json.dump(aux, json_file, indent=4, ensure_ascii=False)
                json_file.close()
    else:
        print("Lista Vazia")

