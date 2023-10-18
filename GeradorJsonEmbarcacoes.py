import mysql.connector as MC
import json


mydatabase = MC.connect(
    host='localhost',
    user='root',
    password='root',
    database='allflags'
)


sql = mydatabase.cursor()


sql.execute("SELECT id, Nome, marca FROM embarc")
results_sql = sql.fetchall()


embarcacoes = {'embarcacoes':[]} 

#FORMA 1

for embarc in results_sql:
    embarcacoes['embarcacoes'].append({
        'id':embarc[0], 
        'nome':embarc[1], 
        'marca':embarc[2],
    })



with open("embarcacoes.json", "w") as arquivo:
    json.dump(embarcacoes, arquivo)

