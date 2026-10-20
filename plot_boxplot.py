import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

base_dados = pd.read_csv(r'dados\dados_boxplot.csv')

plt.figure(figsize=(10, 6))
dados_quantitativos = base_dados.select_dtypes(include=['number'])
sns.boxplot(data=dados_quantitativos, palette='Set2')

plt.title('Gráfico de Boxplot')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()