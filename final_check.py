import pandas as pd

df = pd.read_csv('datasets1/tb_amostra.csv')
df['dt_coleta'] = pd.to_datetime(df['dt_col_amostra'], format='%Y%m%d', errors='coerce')
df['dt_rec'] = pd.to_datetime(df['dt_rec_amostra'], format='%Y%m%d', errors='coerce')
df['tempo_transporte'] = (df['dt_rec'] - df['dt_coleta']).dt.days
df['cancelada'] = df['aut_cancelamento'].notnull()

# Filter valid transport times > 0
df_valid = df[(df['tempo_transporte'] > 0) & (df['tempo_transporte'] <= 60)].copy()

bins = [1, 2, 5, 10, 20, 60]
labels = ['1-2 dias', '3-5 dias', '6-10 dias', '11-20 dias', '>20 dias']
df_valid['faixa_transporte'] = pd.cut(df_valid['tempo_transporte'], bins=bins, labels=labels, include_lowest=True)

summary = df_valid.groupby('faixa_transporte')['cancelada'].agg(['mean', 'count']).reset_index()
summary['mean'] = summary['mean'] * 100
print("Taxa de Cancelamento por Faixa (Excluindo Dia 0):")
print(summary)
