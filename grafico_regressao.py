import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_regressao.csv")
x = df["renda_mensal"]
y = df["gasto_mensal"]

a, b = np.polyfit(x, y, 1)

r2 = np.corrcoef(x, y)[0, 1] ** 2

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=0.6, label="Observações")

xs = np.array([x.min(), x.max()])
ax.plot(xs, a * xs + b, color="red",
        label=f"y = {a:.2f}x + {b:.2f}  (R² = {r2:.3f})")

ax.set_title("Regressão linear: renda x gasto mensal")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")
ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("grafico_regressao.png", dpi=150)
plt.show()
