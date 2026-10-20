import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'dados\dados_dispersao.csv')
lista_colunas = dataset.columns

plt.figure(figsize=(10, 6))
plt.scatter(dataset[lista_colunas[0]], dataset[lista_colunas[1]], color='purple', alpha=0.7, edgecolors='black')

plt.title('Gráfico de Dispersão')
plt.xlabel(lista_colunas[0])
plt.ylabel(lista_colunas[1])
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()