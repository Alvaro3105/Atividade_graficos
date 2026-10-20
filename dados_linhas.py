import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv(r'dados\dados_linhas.csv')
campos = tabela.columns

plt.figure(figsize=(10, 6))
plt.plot(tabela[campos[0]], tabela[campos[1]], marker='o', linewidth=2, color='blue')

plt.title('Gráfico de Linhas')
plt.xlabel(campos[0])
plt.ylabel(campos[1])
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()