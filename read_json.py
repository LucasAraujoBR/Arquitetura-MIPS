import json 
import os


def leitura_json():
    #Encontra o nome do arquivo
    cur_path = os.path.dirname(__file__)
    lista_arquivos = [
        arquivo
        for arquivo in os.listdir(f"{cur_path}/input/")
        if arquivo.endswith(".json")
        ]
    print(lista_arquivos)
    nome_arquivo = str(lista_arquivos[0])
    caminho_arquivo = f"{cur_path}/input/{nome_arquivo}"
    print(caminho_arquivo)
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
        
