"""Gráfico de barras agrupadas: vendas médias por categoria e região."""
import pandas as pd                # pandas: leitura e manipulação da tabela (CSV)
import matplotlib.pyplot as plt    # matplotlib: biblioteca que desenha o gráfico

# 1) Lê o arquivo CSV para um DataFrame (tabela em memória)
df = pd.read_csv("dados_barras.csv")

# 2) pivot: transforma as regiões em colunas -> cada linha é uma categoria
#    Resultado: linhas = categoria, colunas = Norte/Sul/Leste/Oeste
tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")

# 3) .plot(kind="bar") desenha uma barra por coluna, agrupadas por categoria
ax = tabela.plot(kind="bar", figsize=(9, 5), width=0.8)

# 4) Títulos e rótulos: todo gráfico precisa de título e eixos nomeados
ax.set_title("Vendas médias por categoria e região")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias")
plt.xticks(rotation=0)             # deixa os nomes das categorias na horizontal
ax.legend(title="Região")          # legenda explicando as cores
ax.grid(axis="y", alpha=0.3)       # linhas de grade horizontais discretas

# 5) Ajusta margens, salva em PNG e mostra na tela
plt.tight_layout()
plt.savefig("grafico_barras.png", dpi=150)
plt.show()
