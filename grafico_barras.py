
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("dados/dados_barras.csv")

print(dados.head())
print(dados.info())
print(dados.isnull().sum())

plt.figure(figsize=(10, 6))

sns.barplot(
    data=dados,
    x="categoria",
    y="vendas_medias",
    hue="regiao"
)

plt.title("Vendas Médias por Categoria e Região")
plt.xlabel("Categoria")
plt.ylabel("Vendas Médias")

plt.tight_layout()
plt.savefig("graficos/grafico_barras.png", dpi=300)
plt.show()