import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_distribuicao.csv")

fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(df["idade"], bins=15, edgecolor="white")

media = df["idade"].mean()
ax.axvline(media, color="red", linestyle="--", label=f"Média: {media:.1f} anos")

ax.set_title("Distribuição da idade dos clientes")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Número de clientes")
ax.legend()
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("grafico_distribuicao.png", dpi=150)
plt.show()
