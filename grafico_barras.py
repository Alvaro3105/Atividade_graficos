import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_barras.csv")

tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")

ax = tabela.plot(kind="bar", figsize=(9, 5), width=0.8)

ax.set_title("Vendas médias por categoria e região")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias")
plt.xticks(rotation=0)
ax.legend(title="Região")
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("grafico_barras.png", dpi=150)
plt.show()
