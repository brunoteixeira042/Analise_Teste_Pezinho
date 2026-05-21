import pandas as pd

df = pd.read_csv('datasets1/tb_amostra.csv')
df['dt_coleta'] = pd.to_datetime(df['dt_col_amostra'], format='%Y%m%d', errors='coerce')
df['dt_rec'] = pd.to_datetime(df['dt_rec_amostra'], format='%Y%m%d', errors='coerce')
df['tempo_transporte'] = (df['dt_rec'] - df['dt_coleta']).dt.days
df['cancelada'] = df['aut_cancelamento'].notnull()

# Analyze days 0, 1, 2
days_range = df[df['tempo_transporte'].isin([0, 1, 2])].copy()
summary = days_range.groupby('tempo_transporte')['cancelada'].agg(['mean', 'count']).reset_index()
summary['mean'] = summary['mean'] * 100
print("Taxa de Cancelamento por Dia (0-2):")
print(summary)

# Check samples with 0 days transport
print("\nExemplos de amostras com 0 dias de transporte e canceladas:")
print(df[(df['tempo_transporte'] == 0) & (df['cancelada'])][['dt_col_amostra', 'dt_rec_amostra', 'dt_hr_cancelamento', 'aut_cancelamento']].head(10))

