import mysql.connector as MC
import json
import os


 # Main variables
work_path = os.getcwd()  
images_path = f"{work_path}/images"
videos_path = f"{work_path}/videos"
dir_list_images = os.listdir(images_path)  
dir_list_videos = os.listdir(videos_path)  

embarcacoes_novo_seminovo = []
embarcacoes_share_modelo = []
embarcacoes_share_localicazao = []



# Adiciona caminho das imagens e vídeos ao JSON das embarcações
def addImagesAndVideosToJson(json_list, sql_novo_seminovo, sql_share_modelo, sql_share_localidade):
     
    # Novo - Seminovo
    for embarcacao in range(5):#sql_novo_seminovo:
        embarcacoes_novo_seminovo.append({
            'marca':'NX boats',     # PRECISA SER FEITO DIFERENTE
            'modelos':[{
                'nome': 'NX 250',
                 'dados_tecnicos':{
                    'peso':0,
                    'cor':'azul',
                    'tamanho':0,
                },
                'imagens':[],
                'videos':[],
                'tour':'Em análise.'
            }],
        })

    for embarcacao in range(5):#sql_novo_seminovo:
        embarcacoes_novo_seminovo.append({
            'marca':'NX boats',
            'modelos':[{
                'nome': 'NX 250',
                 'dados_tecnicos':{
                    'peso':0,
                    'cor':'azul',
                    'tamanho':0,
                },
                'imagens':[],
                'videos':[],
                'tour':'Em análise.'
            }],
        })




    # Share - por modelo
    for embarcacao in range(5):#sql_share_modelo:
        embarcacoes_share_modelo.append({
            'modelo':'Focker 280 GT 2012',

            'dados_tecnicos':{
                'peso':0,
                'cor':'azul',
                'tamanho':0,
            },
            'imagens':[],
            'videos':[],
            'tour':'Em análise.'
            
        })

    # Share - por localização
    for embarcacao in range(5):#sql_share_localidade:
        embarcacoes_share_localicazao.append({
            'localidade':'bertioga',
            'modelos':[{
                'nome': 'NX 250',
                 'dados_tecnicos':{
                    'peso':0,
                    'cor':'azul',
                    'tamanho':0,
                },
                'imagens':[],
                'videos':[],
                'tour':'Em análise.'
            }],
            
    })


    for embarc in json_list:
        for directory in dir_list_images:
            if 'marca' in embarc:
                if embarc['marca'].upper() == directory.upper():
                    images = os.listdir(f'{images_path}/{directory.upper()}')
                    for image in images:
                        embarc['imagens'].append({'path':f'{images_path}/{directory.upper()}/{image}'})
            elif 'modelo' in embarc:
                if embarc['modelo'].upper() == directory.upper():
                    images = os.listdir(f'{images_path}/{directory.upper()}')
                    for image in images:
                        embarc['imagens'].append({'path':f'{images_path}/{directory.upper()}/{image}'})
            elif 'localidade' in embarc:
                if embarc['localidade'].upper() == directory.upper():
                    images = os.listdir(f'{images_path}/{directory.upper()}')
                    for image in images:
                        embarc['imagens'].append({'path':f'{images_path}/{directory.upper()}/{image}'})

    for directory in dir_list_videos:
        if 'marca' in embarc:
            if embarc['marca'].upper() == directory.upper():
                videos = os.listdir(f'{videos_path}/{directory.upper()}')
                for video in videos:
                    embarc['imagens'].append({'path':f'{videos_path}/{directory.upper()}/{video}'})
        elif 'modelo' in embarc:
            if embarc['modelo'].upper() == directory.upper():
                videos = os.listdir(f'{videos_path}/{directory.upper()}')
                for video in videos:
                    embarc['imagens'].append({'path':f'{videos_path}/{directory.upper()}/{video}'})
        elif 'localidade' in embarc:
            if embarc['localidade'].upper() == directory.upper():
                videos = os.listdir(f'{videos_path}/{directory.upper()}')
                for video in videos:
                    embarc['imagens'].append({'path':f'{videos_path}/{directory.upper()}/{video}'})


## Start


# mydatabase = MC.connect(
#     host='srv-dev',
#     user='root',
#     password='',
#     database='allflags'
# )


# sql_novos_seminovos = mydatabase.cursor()
# sql_share = mydatabase.cursor()

# print('Conectado ao banco.')


# sql_novos_seminovos.execute("""
#         SELECT E.id_embarcacao, E.modelo,
#         M.nome_marina, M.estado, M.cidade, M.bairro,
#         M.complemento
            
#         FROM embarcacoes as E
#         INNER JOIN marinas AS M ON M.id_marina = E.id_marina
            
#         WHERE M.ativo = 'S'
# """)
# sql_share_modelo.execute("""
#         SELECT E.id_embarcacao, E.modelo,
#         M.nome_marina, M.estado, M.cidade, M.bairro,
#         M.complemento
            
#         FROM embarcacoes as E
#         INNER JOIN marinas AS M ON M.id_marina = E.id_marina
            
#         WHERE M.ativo = 'S'
# """)
# sql_share_localidade.execute("""
#         SELECT E.id_embarcacao, E.modelo,
#         M.nome_marina, M.estado, M.cidade, M.bairro,
#         M.complemento
            
#         FROM embarcacoes as E
#         INNER JOIN marinas AS M ON M.id_marina = E.id_marina
            
#         WHERE M.ativo = 'S'
# """)



# results_sql_novos_seminovos = sql_novos_seminovos.fetchall()
# results_sql_share_modelo = sql_share.fetchall()
# results_sql_share_localidade = sql_share_localidade.fetchall()




######################################################## OPERAÇÕES ABAIXO



addImagesAndVideosToJson(embarcacoes_novo_seminovo, '', '', '')
addImagesAndVideosToJson(embarcacoes_share_modelo, '', '', '')
addImagesAndVideosToJson(embarcacoes_share_localicazao, '', '', '')



## Cria arquivo JSON baseado no dicionário de embarcações

with open("embarcacoes_novos_seminovos.json", "w") as arquivo:
    json.dump(embarcacoes_novo_seminovo, arquivo, indent=4)

print('JSON Novo/Semi-novos gerado.')

with open("embarcacoes_share_modelo.json", "w") as arquivo:
    json.dump(embarcacoes_share_modelo, arquivo, indent=4)

print('JSON Share por modelos gerado.')

with open("embarcacoes_share_localizacao.json", "w") as arquivo:
    json.dump(embarcacoes_share_localicazao, arquivo, indent=4)

print('JSON Share por localização gerado.')
    