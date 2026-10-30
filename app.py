from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


# ---------------------------------------------------------
# CONFIGURAÇÕES GERAIS
# ---------------------------------------------------------
st.set_page_config(
    page_title="Dashboard de Análise de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

PASTA_DADOS = Path(__file__).parent / "arquivos"

sns.set_theme(style="whitegrid", palette="deep")


# ---------------------------------------------------------
# FUNÇÕES AUXILIARES
# ---------------------------------------------------------
@st.cache_data
def carregar_csv(nome_arquivo):
    """Lê os arquivos CSV que estão na pasta arquivos."""
    caminho = PASTA_DADOS / nome_arquivo

    if not caminho.exists():
        raise FileNotFoundError(f"Não foi possível encontrar: {caminho}")

    return pd.read_csv(caminho)


def mostrar_grafico(figura):
    """Exibe uma figura do Matplotlib no Streamlit."""
    figura.tight_layout()
    st.pyplot(figura, use_container_width=True)
    plt.close(figura)


def titulo_grafico(numero, titulo):
    st.markdown(f"**{numero}. {titulo}**")


# ---------------------------------------------------------
# SIDEBAR - INFORMAÇÕES DO ALUNO
# ---------------------------------------------------------
st.sidebar.title("Informações do aluno")
st.sidebar.markdown("---")
st.sidebar.markdown("**Nome:** Álvaro Pires")
numero_chamada = st.sidebar.text_input(
    "Número da chamada",
    placeholder="Digite seu número"
)
st.sidebar.markdown("**Turma:** 3E2")
st.sidebar.markdown("---")
st.sidebar.caption("Dashboard desenvolvido com Streamlit a partir dos dados da Atividade 06.")


# ---------------------------------------------------------
# CARREGAMENTO DOS DADOS
# ---------------------------------------------------------
try:
    dados_linhas = carregar_csv("dados_linhas.csv")
    dados_barras = carregar_csv("dados_barras.csv")
    dados_boxplot = carregar_csv("dados_boxplot.csv")
    dados_dispersao = carregar_csv("dados_dispersao.csv")
    dados_distribuicao = carregar_csv("dados_distribuicao.csv")
    dados_frequencia = carregar_csv("dados_frequencia.csv")
    dados_heatmap = carregar_csv("dados_heatmap.csv")
    dados_pizza = carregar_csv("dados_pizza.csv")
    dados_regressao = carregar_csv("dados_regressao.csv")
except Exception as erro:
    st.error(f"Erro ao carregar os arquivos de dados: {erro}")
    st.info("Confira se a pasta 'arquivos' está no mesmo diretório do app.py.")
    st.stop()


# ---------------------------------------------------------
# CABEÇALHO
# ---------------------------------------------------------
st.title("📊 Dashboard de Análise de Dados")
st.write(
    "Visualização dos gráficos desenvolvidos na Atividade 06, "
    "com análises dos dados apresentados."
)
st.markdown("---")


# ---------------------------------------------------------
# LINHA 1 - LINHAS E GRÁFICOS DE BARRAS
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    titulo_grafico(1, "Gráfico de Linhas")
    df = dados_linhas.copy()
    df["data"] = pd.to_datetime(df["data"])
    df = df.sort_values("data")

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df["data"], df["vendas"], marker="o", linewidth=2, color="blue")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, linestyle="--", alpha=0.5)
    mostrar_grafico(fig)

with col2:
    titulo_grafico(2, "Barras: vendas por categoria e região")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=dados_barras,
        x="categoria",
        y="vendas_medias",
        hue="regiao",
        ax=ax
    )
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Vendas médias")
    ax.tick_params(axis="x", rotation=35)
    ax.legend(title="Região", fontsize=8)
    mostrar_grafico(fig)

with col3:
    titulo_grafico(3, "Gráfico de Barras")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=dados_barras,
        x="categoria",
        y="vendas_medias",
        hue="regiao",
        palette="Blues_d",
        ax=ax
    )
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Vendas médias")
    ax.tick_params(axis="x", rotation=35)
    ax.legend(title="Região", fontsize=8)
    mostrar_grafico(fig)


# Análise do primeiro conjunto
df_linhas_analise = dados_linhas.copy()
df_linhas_analise["data"] = pd.to_datetime(df_linhas_analise["data"])
df_linhas_analise = df_linhas_analise.sort_values("data")
venda_inicial = df_linhas_analise["vendas"].iloc[0]
venda_final = df_linhas_analise["vendas"].iloc[-1]
variacao_vendas = ((venda_final - venda_inicial) / venda_inicial) * 100

media_categoria = dados_barras.groupby("categoria")["vendas_medias"].mean()
media_regiao = dados_barras.groupby("regiao")["vendas_medias"].mean()
categoria_destaque = media_categoria.idxmax()
regiao_destaque = media_regiao.idxmax()

st.markdown("#### Análise dos gráficos 1, 2 e 3")
st.write(
    f"O gráfico de linhas apresenta uma tendência de crescimento das vendas no período "
    f"analisado: o valor passou de {venda_inicial:.2f} para {venda_final:.2f}, "
    f"uma variação de {variacao_vendas:.1f}%. Nos gráficos de barras, "
    f"a categoria com maior média de vendas é **{categoria_destaque}**, enquanto "
    f"a região com maior média é **{regiao_destaque}**. Os dois gráficos de barras "
    f"mostram o mesmo conjunto de dados em apresentações visuais semelhantes."
)
st.markdown("---")


# ---------------------------------------------------------
# LINHA 2 - BOXPLOT, DISPERSÃO E DISTRIBUIÇÃO
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    titulo_grafico(4, "Boxplot")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(y=dados_boxplot["salario"], color="mediumseagreen", ax=ax)
    ax.set_ylabel("Salário")
    ax.set_xlabel("Todos os departamentos")
    mostrar_grafico(fig)

with col2:
    titulo_grafico(5, "Gráfico de Dispersão")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(
        dados_dispersao["altura_cm"],
        dados_dispersao["peso_kg"],
        color="purple",
        alpha=0.7,
        edgecolors="black"
    )
    ax.set_xlabel("Altura (cm)")
    ax.set_ylabel("Peso (kg)")
    ax.grid(True, linestyle="--", alpha=0.5)
    mostrar_grafico(fig)

with col3:
    titulo_grafico(6, "Gráfico de Distribuição")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(
        dados_distribuicao["idade"],
        kde=True,
        color="teal",
        ax=ax
    )
    ax.set_xlabel("Idade")
    ax.set_ylabel("Frequência")
    mostrar_grafico(fig)


# Análise do segundo conjunto
mediana_salarios = dados_boxplot["salario"].median()
menor_salario = dados_boxplot["salario"].min()
maior_salario = dados_boxplot["salario"].max()
correlacao_altura_peso = dados_dispersao["altura_cm"].corr(dados_dispersao["peso_kg"])
idade_media = dados_distribuicao["idade"].mean()
idade_mediana = dados_distribuicao["idade"].median()

st.markdown("#### Análise dos gráficos 4, 5 e 6")
st.write(
    f"O boxplot resume a distribuição dos salários: a mediana é "
    f"{mediana_salarios:,.2f}, com valores entre {menor_salario:,.2f} e "
    f"{maior_salario:,.2f}. No gráfico de dispersão, a correlação entre altura "
    f"e peso é {correlacao_altura_peso:.2f}, indicando uma relação "
    f"{'positiva' if correlacao_altura_peso > 0 else 'negativa'} nos dados. "
    f"Já as idades apresentam média de {idade_media:.1f} anos e mediana de "
    f"{idade_mediana:.1f} anos."
)
st.markdown("---")


# ---------------------------------------------------------
# LINHA 3 - FREQUÊNCIA, HEATMAP E PIZZA
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    titulo_grafico(7, "Gráfico de Frequência")
    contagem_tipos = dados_frequencia["tipo_atendimento"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(
        data=dados_frequencia,
        x="tipo_atendimento",
        order=contagem_tipos.index,
        color="cornflowerblue",
        ax=ax
    )
    ax.set_xlabel("Tipo de atendimento")
    ax.set_ylabel("Quantidade")
    ax.tick_params(axis="x", rotation=35)
    mostrar_grafico(fig)

with col2:
    titulo_grafico(8, "Mapa de Calor (Heatmap)")
    ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    matriz_heatmap = dados_heatmap.pivot(
        index="dia_semana",
        columns="horario",
        values="movimento_clientes"
    )
    matriz_heatmap = matriz_heatmap.reindex(ordem_dias)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(
        matriz_heatmap,
        annot=True,
        cmap="viridis",
        fmt=".0f",
        ax=ax
    )
    ax.set_xlabel("Horário")
    ax.set_ylabel("Dia da semana")
    mostrar_grafico(fig)

with col3:
    titulo_grafico(9, "Gráfico de Pizza")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(
        dados_pizza["faturamento"],
        labels=dados_pizza["canal_venda"],
        autopct="%1.1f%%",
        startangle=140,
        colors=plt.cm.Paired.colors
    )
    mostrar_grafico(fig)


# Análise do terceiro conjunto
contagem_tipos = dados_frequencia["tipo_atendimento"].value_counts()
tipo_mais_frequente = contagem_tipos.idxmax()
quantidade_tipo = contagem_tipos.max()
percentual_tipo = quantidade_tipo / contagem_tipos.sum() * 100

pico_movimento = matriz_heatmap.stack().idxmax()
valor_pico = matriz_heatmap.max().max()

canal_destaque = dados_pizza.loc[dados_pizza["faturamento"].idxmax(), "canal_venda"]
faturamento_total = dados_pizza["faturamento"].sum()
faturamento_destaque = dados_pizza["faturamento"].max()
percentual_canal = faturamento_destaque / faturamento_total * 100

st.markdown("#### Análise dos gráficos 7, 8 e 9")
st.write(
    f"No gráfico de frequência, **{tipo_mais_frequente}** é o tipo de atendimento "
    f"mais registrado, representando {percentual_tipo:.1f}% dos registros. "
    f"O mapa de calor indica o maior movimento na combinação de "
    f"**{pico_movimento[0]} às {pico_movimento[1]}**, com {valor_pico:.0f} clientes. "
    f"No gráfico de pizza, o canal **{canal_destaque}** apresenta o maior "
    f"faturamento, correspondendo a {percentual_canal:.1f}% do total."
)
st.markdown("---")


# ---------------------------------------------------------
# LINHA 4 - REGRESSÃO LINEAR
# ---------------------------------------------------------
st.markdown("### 10. Gráfico de Regressão Linear")
col_esquerda, col_centro, col_direita = st.columns([1, 2, 1])

with col_centro:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.regplot(
        data=dados_regressao,
        x="renda_mensal",
        y="gasto_mensal",
        scatter_kws={"alpha": 0.6},
        line_kws={"color": "red"},
        ax=ax
    )
    ax.set_xlabel("Renda mensal")
    ax.set_ylabel("Gasto mensal")
    mostrar_grafico(fig)

correlacao_renda_gastos = dados_regressao["renda_mensal"].corr(
    dados_regressao["gasto_mensal"]
)

st.markdown("#### Análise do gráfico 10")
st.write(
    f"O gráfico apresenta uma correlação de {correlacao_renda_gastos:.2f} "
    f"entre renda e gasto mensal. A tendência é positiva: conforme a renda "
    f"aumenta, os gastos também tendem a aumentar. A correlação indica uma "
    f"associação entre as variáveis, mas não significa, por si só, que uma "
    f"cause a outra."
)

st.markdown("---")
st.caption("Atividade 07 — Dashboard desenvolvido em Python com Streamlit.")
