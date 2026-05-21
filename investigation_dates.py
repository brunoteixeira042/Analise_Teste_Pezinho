import pandas as pd

df = pd.read_csv('datasets1/tb_amostra.csv')
df['dt_coleta'] = pd.to_datetime(df['dt_col_amostra'], format='%Y%m%d', errors='coerce')
df['dt_rec'] = pd.to_datetime(df['dt_rec_amostra'], format='%Y%m%d', errors='coerce')
df['dt_cancel'] = pd.to_datetime(df['dt_hr_cancelamento'].astype(str).str.slice(0, 8), format='%Y%m%d', errors='coerce')
df['cancelada'] = df['aut_cancelamento'].notnull()

# Calculate days between collection and cancellation
df['tempo_ate_cancelamento'] = (df['dt_cancel'] - df['dt_coleta']).dt.days

print("Distribuição do tempo entre Coleta e Cancelamento (para amostras canceladas):")
print(df[df['cancelada']]['tempo_ate_cancelamento'].value_counts().head(10))

# Compare with tempo_transporte
df['tempo_transporte'] = (df['dt_rec'] - df['dt_coleta']).dt.days
print("\nTempo de Transporte vs Cancelamento (Exemplos):")
print(df[df['cancelada']][['tempo_transporte', 'tempo_ate_cancelamento']].head(10))

