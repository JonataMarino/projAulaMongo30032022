import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") #stream de conexão
mydb = myclient ["CSVclassInd"]
mycol = mydb["upCSV"]
i = 0
x = 0
y = 0
while (i == 0):
   x = int(input('Digite 1 para enviar os dados para o MongoCompass \n Digite 2 '
                 'para consultar dados no Banco\nDigite 3 para sair\n'
                 'Digite 4 para limpar o banco de dados\n'))


   if x == 1 :
       dadosClassInd = open(
           "I:/logatti/Linguagens de programação/30_03_22/SistemaClassInd- dadosgovbr/ListaJogosDadosAbertos.csv",
           encoding="utf8")

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

   elif x == 2:
       print('CONSULTA DE DADOS')
       y = int(input('Digite 1 para consultar  Anos de produção\n Digite 2 para consultar as Classifiações Atribuidas\n'
                     'Digite 3 para consultar o País de Origem.\n'))
       if y == 1:
           mydoc = mycol.find().sort("Ano de produção", 1)
           for x in mydoc:
               print(x)
       elif y == 2:
           mydoc = mycol.find().sort("Classificação Atribuída", 1)
           for x in mydoc:
               print(x)
       elif y == 3:
           mydoc = mycol.find().sort("País de Origem", 1)
           for x in mydoc:
               print(x)
       else:
           y= int(input('digite um valor de consuta válido!'))
   if x == 3:
    i = 1
   if x == 4:
        d= mycol.delete_many({})
        print(d.deleted_count, " documentos apagados.")

   elif x != 1 and x != 2 and x != 3:
       print('Digite um valor válido!')