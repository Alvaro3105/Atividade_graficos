"""Gráfico de linhas: evolução diária das vendas por loja."""
import pandas as pd
import matplotlib.pyplot as plt

# parse_dates converte a coluna "data" de texto para data de verdade (eixo X correto)
df = pd.read_csv("dados_linhas.csv", parse_dates=["data"])

fig, ax = plt.subplots(figsize=(10, 5))

# Uma linha para cada loja
for loja, grupo in df.groupby("loja"):
    grupo = grupo.sort_values("data")        # garante a ordem cronológica
    ax.plot(grupo["data"], grupo["vendas"], marker="o", markersize=3, label=loja)

ax.set_title("Vendas diárias por loja")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.legend(title="Loja")
ax.grid(alpha=0.3)
fig.autofmt_xdate()                           # inclina as datas para não sobrepor

plt.tight_layout()
plt.savefig("grafico_linhas.png", dpi=150)
plt.show()
