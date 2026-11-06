"""Mapa de calor: movimento de clientes por dia da semana e horário."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_heatmap.csv")

# pivot: linhas = dia da semana, colunas = horário, células = movimento
matriz = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")

# O pivot ordena alfabeticamente; reordenamos os dias na sequência natural da semana
ordem = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
matriz = matriz.reindex([d for d in ordem if d in matriz.index])

fig, ax = plt.subplots(figsize=(9, 5))

# imshow pinta cada célula da matriz com uma cor proporcional ao valor
imagem = ax.imshow(matriz.values, cmap="YlOrRd", aspect="auto")
fig.colorbar(imagem, label="Movimento de clientes")   # barra de cores = legenda

# Nomeia os eixos com os rótulos da tabela
ax.set_xticks(range(len(matriz.columns)), labels=matriz.columns)
ax.set_yticks(range(len(matriz.index)), labels=matriz.index)

# Escreve o número dentro de cada célula
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        ax.text(j, i, matriz.values[i, j], ha="center", va="center", fontsize=9)

ax.set_title("Movimento de clientes por dia e horário")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")

plt.tight_layout()
plt.savefig("grafico_heatmap.png", dpi=150)
plt.show()
