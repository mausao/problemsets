#!/usr/bin/env python3
import sys
import openpyxl                                                                      #Biblioteca para manipular .xlsx
planilha = sys.argv[1]

def mean_grouped(dados):
    mean_values = {}
    valores_tempo = {}
    for linha in range(2, dados.max_row + 1):
        valor_tempo = dados.cell(row = linha, column = 2).value
        valor = dados.cell(row = linha, column = 3).value
        if valor_tempo is not None and valor is not None:
#Criando/adicionando valores ao dicionário valores_tempo[] pela verificação se o dicionário contém a chave ou não
            valor = float(valor)
            if valor_tempo in (0, 1, 2, 4, 8):
                if valor_tempo not in valores_tempo:
                    valores_tempo[valor_tempo] = [valor]
                else:
                    valores_tempo[valor_tempo].append(valor)
        else:
            continue
#Calculando a média entre 3 valores 
    for tempo, valores in valores_tempo.items():
        medias_tempo = []
        for i in range(0, len(valores), 3):
            media = sum(valores[i:i+3]) / 3
            medias_tempo.append(media)
        mean_values[tempo] = medias_tempo
    return(mean_values)

try:
    arquivo = openpyxl.load_workbook(planilha)
    print(f"O arquivo foi aberto e salvo com sucesso!")
    pages_names = arquivo.sheetnames
    matriz = [[0.0 for _ in range(5)] for _ in range(5)]
    for name in pages_names:
        print(f"Processando a página {name}")
        dados = arquivo[name]
        resultado = mean_grouped(dados)
#loop para adicionar os valores do output da função em uma matriz 5x5
        for i, tempo in enumerate(sorted(resultado.keys())):
            medias = resultado[tempo]
            matriz[i] = medias
#loop para printar as linhas da matriz alimentada com os valores
        for linha in matriz:
            row_edit = [round(media, 3) for media in linha]
            print(row_edit)

except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")
except Exception as e:
    print(f"Erro desconhecido... {e}")
