import pandas as pd  # importa pandas para manipulação de dados

# Lê o arquivo CSV com os dados de vendas
df = pd.read_csv('vendas.csv')  
print(df.head())  # Exibe as primeiras linhas do DataFrame

# Remove linhas que contêm valores nulos (NaN)
df = df.dropna()

# Converte a coluna 'data' para o tipo datetime
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d')

# Converte a coluna 'valor' para numérico (float), se ainda não for
df['valor'] = df['valor'].astype(float)

# Verifica o resultado final após limpeza
print("\nDados após limpeza:")
print(df.info())
