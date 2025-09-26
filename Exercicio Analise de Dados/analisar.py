import pandas as pd

# 1. Importar o arquivo Excel
arquivo = "vendas.xlsx"
df = pd.read_excel(arquivo)

print("=== Dados Importados ===")
print(df.head())

# 2. Estatísticas básicas
print("\n=== Estatísticas ===")
print("Total de vendas:", df["Valor"].sum())
print("Média de vendas:", df["Valor"].mean())
print("Maior venda:", df["Valor"].max())
print("Menor venda:", df["Valor"].min())

# 3. Vendedor que mais vendeu
print("\n=== Vendedor com mais vendas ===")
vendedor_top = df.groupby("Vendedor")["Valor"].sum().idxmax()
valor_top = df.groupby("Vendedor")["Valor"].sum().max()
print(f"{vendedor_top} foi o campeão de vendas com R$ {valor_top}")
