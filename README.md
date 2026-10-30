# Dashboard da Atividade 06

Dashboard interativo desenvolvido com Python e Streamlit para visualizar os gráficos da Atividade 06.

## Estrutura dos arquivos

```text
Atividade_graficos/
├── app.py
├── requirements.txt
└── arquivos/
    ├── dados_barras.csv
    ├── dados_boxplot.csv
    ├── dados_dispersao.csv
    ├── dados_distribuicao.csv
    ├── dados_frequencia.csv
    ├── dados_heatmap.csv
    ├── dados_linhas.csv
    ├── dados_pizza.csv
    └── dados_regressao.csv
```

## Como executar

1. Abra o terminal na pasta do projeto.
2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o dashboard:

   ```bash
   streamlit run app.py
   ```

4. O Streamlit abrirá o dashboard no navegador. No menu lateral, preencha o número da chamada.

O dashboard apresenta os dez gráficos em conjuntos de três, com uma breve análise após cada conjunto.
