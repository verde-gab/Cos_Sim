import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.metrics.pairwise import cosine_similarity

# 1. Carregando o dataset
df = pd.read_csv('btcusd_1-min_data.csv')

# 2. Convertendo o timestamp para datetime
df['datetime'] = pd.to_datetime(df['Timestamp'], unit='s')

# 3. Agrupando para frequência diária, usando o último preço do dia (fechamento)
df_daily = df.set_index('datetime').resample('1D').agg({'Close': 'last'})
df_daily = df_daily.dropna()

# 4. Datas dos halvings
halvings = {
    '2012-11-28': datetime(2012, 11, 28),
    '2016-07-09': datetime(2016, 7, 9),
    '2020-05-11': datetime(2020, 5, 11),
    '2024-04-19': datetime(2024, 4, 19)
}

# 5. Função para calcular similaridade de cosseno
def cosine_sim(vec1, vec2):
    vec1 = np.array(vec1).reshape(1, -1)
    vec2 = np.array(vec2).reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]

# 6. Analisando 30, 90 e 180 dias antes e depois de cada halving
windows = [30, 90, 180]
results = []

for label, halving_date in halvings.items():
    for window in windows:
        start_before = halving_date - timedelta(days=window)
        end_before = halving_date - timedelta(days=1)
        start_after = halving_date + timedelta(days=1)
        end_after = halving_date + timedelta(days=window)
        vec_before_df = df_daily.loc[start_before:end_before]
        vec_after_df = df_daily.loc[start_after:end_after]
        vec_before = vec_before_df['Close'].values
        vec_after = vec_after_df['Close'].values

        #Calculando se ambos os vetores tiverem o mesmo comprimento diferente de zero
        if len(vec_before) > 0 and len(vec_before) == len(vec_after):
            sim = cosine_sim(vec_before, vec_after)
            results.append({
                'Halving': label,
                'Window (days)': window,
                'Cosine Similarity': round(sim, 3)
            })

# 7. Exibindo os resultados
df_results = pd.DataFrame(results)

# Checando df_results se estiver vazio
if not df_results.empty:
    df_results = df_results.pivot(index='Halving', columns='Window (days)', values='Cosine Similarity')
    print(df_results)
else:
    print("No results to display. Dataframe is empty.")