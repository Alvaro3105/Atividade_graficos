from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Dashboard - Atividade 06",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

PASTA = Path(__file__).parent
TAMANHO = (6, 4)

@st.cache_data
def carregar(nome):
    return pd.read_csv(PASTA / nome)

def mostrar(fig):

    fig.tight_layout()
    st.pyplot(fig, width="stretch")
    plt.close(fig)

st.sidebar.title("Informações do aluno")
st.sidebar.markdown("**Nome:** Álvaro Pires")
chamada = st.sidebar.text_input("Número da chamada", placeholder="Digite seu número")
st.sidebar.markdown("**Turma:** 3E2")

barras = carregar("dados_barras.csv")
boxplot = carregar("dados_boxplot.csv")
dispersao = carregar("dados_dispersao.csv")
distribuicao = carregar("dados_distribuicao.csv")
frequencia = carregar("dados_frequencia.csv")
heatmap = carregar("dados_heatmap.csv")
linhas = pd.read_csv(PASTA / "dados_linhas.csv", parse_dates=["data"])
pizza = carregar("dados_pizza.csv")
regressao = carregar("dados_regressao.csv")

st.title("📊 Dashboard de Análise de Dados")
st.caption("Gráficos da Atividade 06, dispostos de três em três, com análise abaixo de cada linha.")
st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("1. Barras")

    tabela = barras.pivot(index="categoria", columns="regiao", values="vendas_medias")
    fig, ax = plt.subplots(figsize=TAMANHO)
    tabela.plot(kind="bar", ax=ax, width=0.8)
    ax.set(xlabel="Categoria", ylabel="Vendas médias")
    ax.tick_params(axis="x", rotation=0)
    ax.legend(title="Região", fontsize=7)
    ax.grid(axis="y", alpha=0.3)
    mostrar(fig)

with c2:
    st.subheader("2. Boxplot")
    deps = boxplot["departamento"].unique()
    fig, ax = plt.subplots(figsize=TAMANHO)
    ax.boxplot([boxplot.loc[boxplot["departamento"] == d, "salario"] for d in deps],
               tick_labels=deps, showmeans=True)
    ax.set(xlabel="Departamento", ylabel="Salário (R$)")
    ax.grid(axis="y", alpha=0.3)
    mostrar(fig)

with c3:
    st.subheader("3. Dispersão")
    fig, ax = plt.subplots(figsize=TAMANHO)
    for sexo, g in dispersao.groupby("sexo"):
        ax.scatter(g["altura_cm"], g["peso_kg"], alpha=0.7, label=sexo)
    ax.set(xlabel="Altura (cm)", ylabel="Peso (kg)")
    ax.legend(title="Sexo", fontsize=7)
    ax.grid(alpha=0.3)
    mostrar(fig)

media_cat = barras.groupby("categoria")["vendas_medias"].mean()
media_reg = barras.groupby("regiao")["vendas_medias"].mean()
mediana_dep = boxplot.groupby("departamento")["salario"].median()
corr_ap = dispersao["altura_cm"].corr(dispersao["peso_kg"])

st.markdown("#### Análise dos gráficos 1, 2 e 3")
st.write(
    f"Nas vendas, a categoria com maior média é **{media_cat.idxmax()}** "
    f"({media_cat.max():.1f}) e a região de maior média é **{media_reg.idxmax()}** "
    f"({media_reg.max():.1f}). Nos salários, **{mediana_dep.idxmax()}** tem a maior "
    f"mediana (R$ {mediana_dep.max():,.2f}) e **{mediana_dep.idxmin()}** a menor "
    f"(R$ {mediana_dep.min():,.2f}); os pontos fora das caixas indicam salários "
    f"atípicos. Entre altura e peso há correlação "
    f"{'positiva' if corr_ap > 0 else 'negativa'} de {corr_ap:.2f}: "
    f"pessoas mais altas tendem a pesar mais."
)
st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("4. Distribuição")
    media_idade = distribuicao["idade"].mean()
    fig, ax = plt.subplots(figsize=TAMANHO)
    ax.hist(distribuicao["idade"], bins=15, edgecolor="white")
    ax.axvline(media_idade, color="red", linestyle="--", label=f"Média: {media_idade:.1f}")
    ax.set(xlabel="Idade (anos)", ylabel="Clientes")
    ax.legend(fontsize=7)
    mostrar(fig)

with c2:
    st.subheader("5. Frequência")
    contagem = frequencia["tipo_atendimento"].value_counts()
    fig, ax = plt.subplots(figsize=TAMANHO)
    ax.bar_label(ax.bar(contagem.index, contagem.values))
    ax.set(xlabel="Tipo de atendimento", ylabel="Chamados")
    ax.grid(axis="y", alpha=0.3)
    mostrar(fig)

with c3:
    st.subheader("6. Mapa de calor")
    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    matriz = heatmap.pivot(index="dia_semana", columns="horario",
                           values="movimento_clientes").reindex(dias)
    fig, ax = plt.subplots(figsize=TAMANHO)
    img = ax.imshow(matriz.values, cmap="YlOrRd", aspect="auto")
    fig.colorbar(img, ax=ax)
    ax.set_xticks(range(len(matriz.columns)), labels=matriz.columns, fontsize=7)
    ax.set_yticks(range(len(matriz.index)), labels=matriz.index, fontsize=7)
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            ax.text(j, i, matriz.values[i, j], ha="center", va="center", fontsize=6)
    ax.set(xlabel="Horário", ylabel="Dia da semana")
    mostrar(fig)

idade = distribuicao["idade"]
top_tipo = contagem.idxmax()
dia_pico, hora_pico = matriz.stack().idxmax()
st.markdown("#### Análise dos gráficos 4, 5 e 6")
st.write(
    f"As idades dos clientes vão de {idade.min()} a {idade.max()} anos, com média de "
    f"{idade.mean():.1f} e mediana de {idade.median():.1f}. O atendimento mais frequente "
    f"é **{top_tipo}** ({contagem.max()} de {contagem.sum()} chamados, "
    f"{contagem.max() / contagem.sum():.1%}). O maior movimento de clientes ocorre em "
    f"**{dia_pico} às {hora_pico}** ({matriz.max().max():.0f} clientes), e os fins de "
    f"semana concentram os valores mais altos."
)
st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("7. Linhas")
    fig, ax = plt.subplots(figsize=TAMANHO)
    for loja, g in linhas.groupby("loja"):
        g = g.sort_values("data")
        ax.plot(g["data"], g["vendas"], marker="o", markersize=3, label=loja)
    ax.set(xlabel="Data", ylabel="Vendas")
    ax.tick_params(axis="x", rotation=45)
    ax.legend(title="Loja", fontsize=7)
    ax.grid(alpha=0.3)
    mostrar(fig)

with c2:
    st.subheader("8. Pizza")
    fig, ax = plt.subplots(figsize=TAMANHO)
    ax.pie(pizza["faturamento"], labels=pizza["canal_venda"],
           autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    mostrar(fig)

with c3:
    st.subheader("9. Regressão linear")
    x, y = regressao["renda_mensal"], regressao["gasto_mensal"]
    a, b = np.polyfit(x, y, 1)
    r2 = np.corrcoef(x, y)[0, 1] ** 2
    xs = np.array([x.min(), x.max()])
    fig, ax = plt.subplots(figsize=TAMANHO)
    ax.scatter(x, y, alpha=0.6)
    ax.plot(xs, a * xs + b, color="red", label=f"R² = {r2:.3f}")
    ax.set(xlabel="Renda mensal (R$)", ylabel="Gasto mensal (R$)")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3)
    mostrar(fig)

total_loja = linhas.groupby("loja")["vendas"].sum()
canal_top = pizza.loc[pizza["faturamento"].idxmax()]
st.markdown("#### Análise dos gráficos 7, 8 e 9")
st.write(
    f"No período, **{total_loja.idxmax()}** vendeu mais ({total_loja.max():,.0f} contra "
    f"{total_loja.min():,.0f} de {total_loja.idxmin()}). O canal **{canal_top['canal_venda']}** "
    f"gera a maior fatia do faturamento ({canal_top['faturamento'] / pizza['faturamento'].sum():.1%}). "
    f"Na regressão, cada R$ 1,00 a mais de renda soma cerca de R$ {a:.2f} de gasto "
    f"(R² = {r2:.2f}), uma relação linear forte; correlação, porém, não prova causa."
)
