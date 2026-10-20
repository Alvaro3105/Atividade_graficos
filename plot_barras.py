import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv(r'dados\dados_barras.csv')

plt.figure(figsize=(10, 6))

cols_num = dados.select_dtypes(include=['number']).columns

if len(cols_num) > 0:
    eixo_y = cols_num[0]
    agrupamento = 'regiao' if 'regiao' in dados.columns else None
    sns.barplot(data=dados, x='categoria', y=eixo_y, hue=agrupamento, palette='Blues_d')
    plt.ylabel(eixo_y)
else:
    sns.countplot(data=dados, x='categoria', hue='regiao' if 'regiao' in dados.columns else None, palette='Blues_d')
    plt.ylabel('Quantidade (Contagem)')

plt.title('Gráfico de Barras')
plt.xlabel('Categoria')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()