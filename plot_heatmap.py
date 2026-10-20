import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados_matriz = pd.read_csv(r'dados\dados_heatmap.csv')

matriz_num = dados_matriz.select_dtypes(include=['number'])

plt.figure(figsize=(10, 8))
sns.heatmap(matriz_num, annot=True, cmap='viridis', fmt='.2f')
plt.title('Mapa de Calor (Heatmap)')
plt.tight_layout()

plt.show()