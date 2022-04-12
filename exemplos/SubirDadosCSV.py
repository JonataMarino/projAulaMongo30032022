import pymongo
#test git
myclient = pymongo.MongoClient("mongodb://localhost:27017/") #stream de conexão
mydb = myclient ["CSVclassInd"]
mycol = mydb["upCSV"]

dadosClassInd = open("I:/logatti/Linguagens de programação/30_03_22/SistemaClassInd- dadosgovbr/ListaJogosDadosAbertos.csv", encoding="utf8")

for linhas in dadosClassInd.readlines():
    cols = linhas.split(',')

    myList = [
            {'código': cols[0], 'Título no Brasil': cols[1], 'Título da Série': cols[2], 'produtor': cols[3],
            'País de Origem': cols[4], 'Ano de produção': cols[5], 'Observação: ': cols[6],
            'Distribuidor do jogo no Brasil': cols[7], 'Mídia de distribuição': cols[8],
            'Plataforma/Veículo de distribuição': cols[9], 'Gênero': cols[10],
            'Classificação pretendida': cols[11], 'Classificação Atribuída': cols[12],
            'Conteúdo': cols[13], 'Tipo de análise': cols[14], 'Tipo de Material': cols[15],
            'Requerente': cols[16], 'Data Portaria': cols[17], 'Número Portaria': cols[18],
            'Data DOU': cols[19], 'Seção I/Página': cols[20]
            }
        ]

    dados = mycol.insert_many(myList)
    print(dados.inserted_ids)




