import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_frequencia.csv")

contagem = df["tipo_atendimento"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(contagem.index, contagem.values)

ax.bar_label(barras)

ax.set_title("Frequência por tipo de atendimento")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Número de chamados")
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("grafico_frequencia.png", dpi=150)
plt.show()
