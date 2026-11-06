import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_linhas.csv", parse_dates=["data"])

fig, ax = plt.subplots(figsize=(10, 5))

for loja, grupo in df.groupby("loja"):
    grupo = grupo.sort_values("data")
    ax.plot(grupo["data"], grupo["vendas"], marker="o", markersize=3, label=loja)

ax.set_title("Vendas diárias por loja")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.legend(title="Loja")
ax.grid(alpha=0.3)
fig.autofmt_xdate()

plt.tight_layout()
plt.savefig("grafico_linhas.png", dpi=150)
plt.show()
