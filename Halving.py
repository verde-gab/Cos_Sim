#Código de algoritmo de similaridade do cosseno para análise do halving do Bitcoin
#Importando as bibliotecas necessárias:
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime, timedelta #converter o Timestamps da base (está em formato UNIX timestamp) de dados para formato de data padrão

#Carregando a base de dados
base = pd.read_csv('btcusd_1-min_data.csv')

#Convertendo TimeStamp para formato de data padrão
base['datetime'] = pd.to_datetime(base['Timestamp'], unit = 's') 

#Agrupando para frequência diária usando o último preço do dia (close)
freq_diária = base.set_index('datetime').resample('1D').agg({'Close': 'last'})
freq_diária  = freq_diária.dropna()

#Estabelecendo a data dos Halvings
halvings = {
    '2012-11-28': datetime(2012, 11, 28),
    '2016-07-09': datetime(2016, 7, 9),
    '2020-05-11': datetime(2020, 5, 11),
    '2024-04-19': datetime(2024, 4, 19)
    }

#Calculo da similaridade do cosseno
def sim_cos(v1, v2): 
    v1 = np.array(v1). reshape(1, -1)
    v2 = np.array(v2). reshape(1, -1)
    return cosine_similarity(v1, v2) [0] [0]

#analisando de 30,90,180 dias antes e depos de cada halving
dias = [30, 90, 180]
resultados = []

for id, data_halving in halvings.items():
    for dia in dias:
        inicio_antes = data_halving - timedelta(days = dia)
        fim_antes = data_halving - timedelta(days = 1)
        inicio_depois = data_halving + timedelta(days = 1)
        fim_depois = data_halving + timedelta(days = dia)
        vetor_anterior = freq_diária.loc[inicio_antes:fim_antes]
        vetor_posterior = freq_diária.loc[inicio_depois:fim_depois]
        vetor_antes2 = vetor_anterior['Close'].values
        vetor_depois2 = vetor_posterior['Close'].values 
        #Calculando se ambos os vetores tiverem o mesmo comprimento diferente de zero
        if len(vetor_anterior) > 0 and len(vetor_anterior) == len(vetor_posterior):
            sim = sim_cos(vetor_anterior, vetor_posterior)
            resultados.append({
                'Halving': id,
                'Data': dia,
                'Similaridade do Coseno': round(sim, 3)
                })

#Exibindo os resultados
resultados_atingidos = pd.DataFrame(resultados)
# checando se a variavel resultado_atingidos estiver vazia
if not resultados_atingidos.empty:
    resultados_atingidos = resultados_atingidos.pivot(index = 'Halving', columns = 'Data', values = 'Similaridade do Coseno')
    print(resultados_atingidos)