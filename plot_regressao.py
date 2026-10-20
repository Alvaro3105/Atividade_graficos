import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_regressao = pd.read_csv(r'dados\dados_regressao.csv')
variaveis = df_regressao.columns

plt.figure(figsize=(10, 6))
sns.regplot(data=df_regressao, x=variaveis[0], y=variaveis[1], scatter_kws={'alpha':0.6}, line_kws={'color':'red'})

plt.title('Gráfico de Regressão Linear')
plt.xlabel(variaveis[0])
plt.ylabel(variaveis[1])
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()