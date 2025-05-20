# Calcula o total de vendas (receita) por produto
vendas_por_produto = df.groupby('produto')['valor'].sum()
print("Total de vendas por produto:")
print(vendas_por_produto)

# Identifica o produto com maior receita total
produto_mais_vendido = vendas_por_produto.idxmax()
valor_mais_vendido = vendas_por_produto.max()
print(f"\nProduto com maior receita total: {produto_mais_vendido} (R$ {valor_mais_vendido:.2f})")

# Calcula a receita total por cidade
receita_por_cidade = df.groupby('cidade')['valor'].sum()
print("\nReceita total por cidade:")
print(receita_por_cidade)
