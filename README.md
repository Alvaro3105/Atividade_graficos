# Atividade de Gráficos

Um script Python para cada arquivo de dados, cada um gerando um gráfico.

| Dados | Script | Gráfico |
|---|---|---|
| `dados_barras.csv` | `grafico_barras.py` | Barras agrupadas (categoria x região) |
| `dados_boxplot.csv` | `grafico_boxplot.py` | Boxplot (salário por departamento) |
| `dados_dispersao.csv` | `grafico_dispersao.py` | Dispersão (altura x peso por sexo) |
| `dados_distribuicao.csv` | `grafico_distribuicao.py` | Histograma (idade dos clientes) |
| `dados_frequencia.csv` | `grafico_frequencia.py` | Frequência (tipo de atendimento) |
| `dados_heatmap.csv` | `grafico_heatmap.py` | Mapa de calor (dia x horário) |
| `dados_linhas.csv` | `grafico_linhas.py` | Linhas (vendas diárias por loja) |
| `dados_pizza.csv` | `grafico_pizza.py` | Pizza (faturamento por canal) |
| `dados_regressao.csv` | `grafico_regressao.py` | Regressão linear (renda x gasto) |

## Como executar

```bash
pip install -r requirements.txt
python grafico_barras.py
```

Cada script lê o CSV da mesma pasta, salva o gráfico em PNG e o exibe na tela.
Exemplos dos resultados estão na pasta `graficos/`.

## Dashboard (Streamlit)

`app.py` reúne os 9 gráficos em um dashboard: três linhas de três gráficos, cada linha com uma
breve análise abaixo, e um sidebar recolhível com as informações do aluno.

```bash
streamlit run app.py
```

No sidebar, preencha o número da chamada.
