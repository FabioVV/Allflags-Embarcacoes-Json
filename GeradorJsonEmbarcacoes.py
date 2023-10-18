import mysql.connector as MC
import json
import os

## Conexão e SELECT com o banco

mydatabase = MC.connect(
    host='localhost',
    user='root',
    password='root',
    database='allflags'
)


sql = mydatabase.cursor()


sql.execute("""
        SELECT id, Nome, marca FROM embarc 
""")
results_sql = sql.fetchall()


## Váriaveis

embarcacoes = {'embarcacoes':[]} 
cwd = os.getcwd()  
images_path = f"{cwd}/images"
videos_path = f"{cwd}/videos"
dir_list_images = os.listdir(images_path)  
dir_list_videos = os.listdir(videos_path)  



######################################################## OPERAÇÕES ABAIXO

for embarc in results_sql:
    embarcacoes['embarcacoes'].append({
        'id':embarc[0], 
        'nome':embarc[1], 
        'marca':embarc[2],
        'imagens':[],
        'videos':[]
    })





# Adiciona caminho das imagens e vídeos ao JSON das embarcações

for embarc in embarcacoes['embarcacoes']:
    for directory in dir_list_images:
        if embarc['marca'] == directory.upper():
            images = os.listdir(f'{images_path}/{directory.upper()}')
            for image in images:
                embarc['imagens'].append({'path':f'{images_path}/{directory.upper()}/{image}'})

    for directory in dir_list_videos:
        if embarc['marca'] == directory.upper():
            videos = os.listdir(f'{videos_path}/{directory.upper()}')
            for video in videos:
                embarc['videos'].append({'path':f'{videos_path}/{directory.upper()}/{video}'})



# Cria arquivo JSON baseado no dicionário de embarcações

with open("embarcacoes.json", "w") as arquivo:
    json.dump(embarcacoes, arquivo, indent=4)
