import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_boxplot.csv")

departamentos = df["departamento"].unique()
dados = [df.loc[df["departamento"] == d, "salario"] for d in departamentos]

fig, ax = plt.subplots(figsize=(9, 5))

ax.boxplot(dados, tick_labels=departamentos, showmeans=True)

ax.set_title("Distribuição de salários por departamento")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("grafico_boxplot.png", dpi=150)
plt.show()
