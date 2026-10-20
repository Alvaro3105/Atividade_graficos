import pandas as pd
import matplotlib.pyplot as plt

dados_pizza = pd.read_csv(r'dados\dados_pizza.csv')
rotulos_colunas = dados_pizza.columns

plt.figure(figsize=(8, 8))
plt.pie(dados_pizza[rotulos_colunas[1]], labels=dados_pizza[rotulos_colunas[0]], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

plt.title('Gráfico de Pizza')
plt.tight_layout()

plt.show()