"""Gráfico de dispersão: relação entre altura e peso, colorido por sexo."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_dispersao.csv")

fig, ax = plt.subplots(figsize=(8, 6))

# Um scatter por grupo (sexo) para cada um ter sua cor e entrada na legenda
for sexo, grupo in df.groupby("sexo"):
    ax.scatter(grupo["altura_cm"], grupo["peso_kg"],
               label=sexo, alpha=0.7)   # alpha = transparência (ajuda com pontos sobrepostos)

ax.set_title("Altura x Peso por sexo")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(title="Sexo")
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("grafico_dispersao.png", dpi=150)
plt.show()
