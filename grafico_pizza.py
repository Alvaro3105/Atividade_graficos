import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_pizza.csv")

fig, ax = plt.subplots(figsize=(7, 7))

ax.pie(df["faturamento"], labels=df["canal_venda"],
       autopct="%1.1f%%", startangle=90)

ax.set_title("Faturamento por canal de venda")
ax.axis("equal")

plt.tight_layout()
plt.savefig("grafico_pizza.png", dpi=150)
plt.show()
