import json 
import os

def trata_nome_algoritmo(lista):
    nomes = []
    for x in range(len(lista)):
        aux = str(lista[x])
        lista2 = aux.split(".")
        nomes.append(lista2[0])
    return nomes

def nome_algoritmo():
    cur_path = os.path.dirname(__file__)
    lista_arquivos = [
        arquivo
        for arquivo in os.listdir(f"{cur_path}/input/")
        if arquivo.endswith(".json")
        ]
    a = trata_nome_algoritmo(lista_arquivos)
    return a

def leitura_json(nome):
    #Encontra o nome do arquivo
    cur_path = os.path.dirname(__file__)
    lista_arquivos = [
        arquivo
        for arquivo in os.listdir(f"{cur_path}/input/")
        if arquivo.endswith(".json")
        ]
    nome_arquivo = str(nome+".input.json")
    caminho_arquivo = f"{cur_path}/input/{nome_arquivo}"
    lista_hexadecimais = []
    #Abre o arquivo nomeado e executa sua leitura, transformando seus dados numa lista de hexadecimais
    if len(lista_arquivos)>0:
        with open(caminho_arquivo, encoding="utf-8") as json_file_read:
            data = json.load(json_file_read)
            total_hexadecimais = len(data['text'])
            for _ in range(total_hexadecimais):
                lista_hexadecimais.append(data['text'][_])
            json_file_read.close()
    else:
        print('Não possui arquivos na pasta de input.')
    return lista_hexadecimais

def leitura_json_regs(nome):
    #Encontra o nome do arquivo
    cur_path = os.path.dirname(__file__)
    lista_arquivos = [
        arquivo
        for arquivo in os.listdir(f"{cur_path}/input/")
        if arquivo.endswith(".json")
        ]
    nome_arquivo = str(nome+".input.json")
    caminho_arquivo = f"{cur_path}/input/{nome_arquivo}"
    lista_regs = []
    #Abre o arquivo nomeado e executa sua leitura, transformando seus dados numa lista de hexadecimais
    if len(lista_arquivos)>0:
        with open(caminho_arquivo, encoding="utf-8") as json_file_read:
            data = json.load(json_file_read)
            total_regs = len(data['config']['regs'])
            print(total_regs)
            regs_keys = list(data['config']['regs'].keys())
            print(regs_keys)
            for _ in range(total_regs):
                lista_regs.append(regs_keys[_])
                lista_regs.append(data['config']['regs'][regs_keys[_]])
            json_file_read.close()
    else:
        print('Não possui arquivos na pasta de input.')
    return lista_regs




