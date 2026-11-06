"""Histograma: distribuição da idade dos clientes."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_distribuicao.csv")

fig, ax = plt.subplots(figsize=(8, 5))

# hist agrupa as idades em "faixas" (bins) e conta quantos clientes caem em cada uma
ax.hist(df["idade"], bins=15, edgecolor="white")

# Linha vertical com a média, para dar referência ao leitor
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
