#!/usr/bin/env python3
import sys
import openpyxl                                                                      #Biblioteca para manipular .xlsx
planilha = sys.argv[1]

def mean_grouped(dados):
    mean_values = {}
    valores_tempo = {}
    x = 1
    for linha in range(2, dados.max_row + 1):
        valor_tempo = dados.cell(row = linha, column = 2).value
        valor = dados.cell(row = linha, column = 3).value
        if valor_tempo is not None and valor is not None:
#Criando/adicionando valores ao dicionário valores_tempo[] pela verificação se o dicionário contém a chave ou não
            valor = float(valor)
            if valor_tempo in (0, 1, 2, 4, 8, 12):
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
    dados1 = arquivo['FvFm']
    dados2 = arquivo['ChlIdx']
    dados3 = arquivo['AriIdx']
    print(f"O arquivo foi aberto e salvo com sucesso!")
    resultado1 = mean_grouped(dados1)
    resultado2 = mean_grouped(dados2)
    resultado3 = mean_grouped(dados3)
    print(resultado)
    for tempo in resultado1.keys():
        print("As médias da primeira planilha (FvFm) são:")
        print(tempo)
        print(resultado1[tempo])
    for tempo in resultado2.keys():
        print("As médias da segunda planilha (ChlIdx) são: ")
        print(tempo)
        print(resultado2[tempo])
    for tempo in resultado3.keys():
        print("As médias da terceira planilha (AriIdx) são: ")
        print(tempo)
        print(resultado3[tempo])



except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")
except Exception as e:
    print(f"Erro desconhecido... {e}")
