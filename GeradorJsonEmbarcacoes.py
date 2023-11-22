import mysql.connector as MC
import json
import os


 ##  Main variables
work_path = os.getcwd()  
images_path = f"{work_path}/images"
videos_path = f"{work_path}/videos"
dir_list_images = os.listdir(images_path)  
dir_list_videos = os.listdir(videos_path)  

 # Variables to create the JSON files
embarcacoes_novo_seminovo = []
embarcacoes_share_modelo = []
embarcacoes_share_localicazao = []


## Start


mydatabase = MC.connect(
    host='srv-dev',
    user='root',
    password='',
    database='allflags'
)

sql_novos_seminovos = mydatabase.cursor(buffered=True)
sql_share_localidade = mydatabase.cursor(buffered=True)
sql_share_modelo = mydatabase.cursor(buffered=True)

print('Conectado ao banco.')



sql_novos_seminovos.execute("""
    SELECT P.modelo, F.nome FROM produtos AS P 
    INNER JOIN fornecedores AS F ON P.id_fornecedor_fab = F.id_fornecedor 
    WHERE F.estaleiro = 'S' 
    AND F.ativo = 'S' 
    AND P.ativo = 'S'
    AND P.tipo_produto = 'C' 
    AND P.modelo != 'XXXX' 
    AND P.modelo != 'teste';
""")
sql_share_modelo.execute("""
        SELECT E.id_embarcacao, E.modelo,
        M.nome_marina, M.estado, M.cidade, M.bairro,
        M.complemento
            
        FROM embarcacoes as E
        INNER JOIN marinas AS M ON M.id_marina = E.id_marina
            
        WHERE M.ativo = 'S'
""")
sql_share_localidade.execute("""
        SELECT E.id_embarcacao, E.modelo,
        M.nome_marina, M.estado, M.cidade, M.bairro,
        M.complemento
            
        FROM embarcacoes as E
        INNER JOIN marinas AS M ON M.id_marina = E.id_marina
            
        WHERE M.ativo = 'S'
""")



results_sql_novos_seminovos = sql_novos_seminovos.fetchall()
results_sql_share_modelo = sql_share_modelo.fetchall()
results_sql_share_localidade = sql_share_localidade.fetchall()




######################################################## OPERAÇÕES ABAIXO

# Novo - Seminovo
for embarcacao in results_sql_novos_seminovos:
    embarcacoes_novo_seminovo.append({
        'marca': 'NX Boats',     # PRECISA SER FEITO DIFERENTE
        'modelos':[{
            'nome': embarcacao[1],
            'dados_tecnicos':{
                'peso':embarcacao[1],
                'cor': embarcacao[1],
                'tamanho': embarcacao[1],
            },
            'imagens':[],
            'videos':[],
            'tour':'Em análise.'
        }],
    })

# Share - por modelo
for embarcacao in results_sql_share_modelo:
    embarcacoes_share_modelo.append({
        'modelo':embarcacao[1],

        'dados_tecnicos':{
            'peso':embarcacao[1],
            'cor':embarcacao[1],
            'tamanho':embarcacao[1],
        },
        'imagens':[],
        'videos':[],
        'tour':'Em análise.'
        
    })

# Share - por localização
for embarcacao in results_sql_share_localidade:
    embarcacoes_share_localicazao.append({
        'localidade':embarcacao[1],
        'modelos':[{
            'nome': embarcacao[1],
                'dados_tecnicos':{
                'peso':embarcacao[1],
                'cor':embarcacao[1],
                'tamanho':embarcacao[1],
            },
            'imagens':[],
            'videos':[],
            'tour':'Em análise.'
        }],
        
})
    

for embarc in embarcacoes_novo_seminovo:
    for directory in dir_list_images:
        if embarc['marca'].upper() == directory.upper():
            for modelos in embarc['modelos']:
                try:
                    images = os.listdir(f'{images_path}/{directory.upper()}/{modelos["nome"].rstrip()}')
                    for image in images:
                        modelos['imagens'].append({'path':f'{images_path}/{directory.upper()}/{modelos["nome"].rstrip()}/{image}'})
                except FileNotFoundError:
                    print('Uma embarcação não foi encontrada na pasta de imagens.')
                except OSError:
                    print('Uma embarcação gerou um erro no seu nome de diretório das imagens.')

    for directory in dir_list_videos:
        if embarc['marca'].upper() == directory.upper():
            for modelos in embarc['modelos']:
                try:
                    videos = os.listdir(f'{videos_path}/{directory.upper()}/{modelos["nome"].rstrip()}')
                    for video in videos:
                        modelos['videos'].append({'path':f'{videos_path}/{directory.upper()}/{modelos["nome"].rstrip()}/{video}'})
                except FileNotFoundError:
                    print('Uma embarcação não foi encontrada na pasta de vídeos.')
                except OSError:
                    print('Uma embarcação gerou um erro no seu nome de diretório dos vídeos.')



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
    