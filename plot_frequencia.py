import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataframe = pd.read_csv(r'dados\dados_frequencia.csv')
cols_uteis = [item_col for item_col in dataframe.columns if 'id' not in item_col.lower()]

plt.figure(figsize=(10, 6))

if len(cols_uteis) > 0:
    coluna_principal = cols_uteis[0]
    sns.countplot(data=dataframe, x=coluna_principal, order=dataframe[coluna_principal].value_counts().index, palette='pastel')
    plt.xlabel(coluna_principal)
else:
    coluna_principal = dataframe.columns[0]
    sns.countplot(data=dataframe.head(10), x=coluna_principal, palette='pastel')
    plt.xlabel(f'{coluna_principal} (Apenas top 10)')

plt.title('Gráfico de Frequência (Contagem)')
plt.ylabel('Quantidade')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()