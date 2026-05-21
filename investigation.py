import pandas as pd

df = pd.read_csv('datasets1/tb_amostra.csv')
df['dt_coleta'] = pd.to_datetime(df['dt_col_amostra'], format='%Y%m%d', errors='coerce')
df['dt_rec'] = pd.to_datetime(df['dt_rec_amostra'], format='%Y%m%d', errors='coerce')
df['tempo_transporte'] = (df['dt_rec'] - df['dt_coleta']).dt.days

# Define cancellation as per notebook
df['cancelada'] = df['aut_cancelamento'].notnull()

# Filters used in notebook
df_filtered = df[(df['tempo_transporte'] >= 0) & (df['tempo_transporte'] <= 60)].copy()

# Faixas de transporte
bins = [0, 2, 5, 10, 20, 60]
labels = ['0-2 dias', '3-5 dias', '6-10 dias', '11-20 dias', '>20 dias']
df_filtered['faixa_transporte'] = pd.cut(df_filtered['tempo_transporte'], bins=bins, labels=labels, include_lowest=True)

# Taxa de cancelamento por faixa
summary = df_filtered.groupby('faixa_transporte')['cancelada'].agg(['mean', 'count']).reset_index()
summary['mean'] = summary['mean'] * 100
print("Taxa de Cancelamento por Faixa de Transporte:")
print(summary)

# Check co_seq_tp_amostra distribution for 0-2 days
print("\nDistribuição de co_seq_tp_amostra para faixa 0-2 dias:")
print(df_filtered[df_filtered['faixa_transporte'] == '0-2 dias']['co_seq_tp_amostra'].value_counts())

