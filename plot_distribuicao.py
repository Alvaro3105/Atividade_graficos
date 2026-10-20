import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_dist = pd.read_csv(r'dados\dados_distribuicao.csv')
nomes_colunas = df_dist.columns

plt.figure(figsize=(10, 6))
sns.histplot(df_dist[nomes_colunas[0]], kde=True, color='teal')

plt.title('Gráfico de Distribuição')
plt.xlabel(nomes_colunas[0])
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()