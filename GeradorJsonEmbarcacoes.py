import mysql.connector as MC
import json
import os

## Conexão: OP

mydatabase = MC.connect(
    host='srv-dev',
    user='root',
    password='',
    database='allflags'
)


sql = mydatabase.cursor()
print('Conectado ao banco.')


sql.execute("""
        SELECT E.id_embarcacao, E.modelo,
        M.nome_marina, M.estado, M.cidade, M.bairro,
        M.complemento
            
        FROM embarcacoes as E
        INNER JOIN marinas AS M ON M.id_marina = E.id_marina
            
        WHERE M.ativo = 'S'
""")
results_sql = sql.fetchall()



work_path = os.getcwd()  
embarcacoes = []
images_path = f"{work_path}/images"
videos_path = f"{work_path}/videos"
dir_list_images = os.listdir(images_path)  
dir_list_videos = os.listdir(videos_path)  



######################################################## OPERAÇÕES ABAIXO

for embarcacao in results_sql:
    embarcacoes.append({
        'id_embarcacao':embarcacao[0], 
        'modelo':embarcacao[1], 
        'marina':embarcacao[2],
        'cidade':embarcacao[3],
        'estado':embarcacao[4],
        'imagens':[],
        'videos':[]
    })

# print(embarcacoes)



# Adiciona caminho das imagens e vídeos ao JSON das embarcações

for embarc in embarcacoes:
    for directory in dir_list_images:
        if embarc['modelo'].upper() == directory.upper():
            images = os.listdir(f'{images_path}/{directory.upper()}')
            for image in images:
                embarc['imagens'].append({'path':f'{images_path}/{directory.upper()}/{image}'})

    for directory in dir_list_videos:
        if embarc['modelo'].upper() == directory.upper():
            videos = os.listdir(f'{videos_path}/{directory.upper()}')
            for video in videos:
                embarc['videos'].append({'path':f'{videos_path}/{directory.upper()}/{video}'})



## Cria arquivo JSON baseado no dicionário de embarcações

with open("embarcacoes.json", "w") as arquivo:
    json.dump(embarcacoes, arquivo, indent=4)

print('JSON gerado.')
