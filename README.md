## Análise de Dados do Teste do Pezinho(Qualidade das amostras)

###  Fonte dos Dados

A análise utiliza um conjunto de cinco arquivos CSV:

-   `tb_amostra.csv`: Tabela principal contendo os registros de cada amostra coletada.
-   `tb_motivo_inadequacao.csv`: Tabela de catálogo com as descrições dos motivos de inadequação.
-   `tb_ms_motivo_inadequacao.csv`: Tabela de ligação entre as amostras e os motivos de inadequação.
-   `tb_municipio.csv`: Tabela com informações sobre os municípios.
-   `tb_unidade_saude.csv`: Tabela com dados das unidades de saúde onde as coletas foram realizadas.

### ⚙️ Passos da Análise

O processo de análise foi estruturado da seguinte forma:

1.  **Configuração do Ambiente**: Importação das bibliotecas necessárias para a análise, como `pandas`, `matplotlib` e `seaborn`.
2.  **Carregamento dos Dados**: Leitura dos cinco arquivos CSV para DataFrames do `pandas`.
3.  **Análise de Cancelamentos**:
    *   Identificação das amostras canceladas (taxa de 0.11% do total).
    *   Análise de quem são os usuários que mais realizam cancelamentos.
4.  **Investigação dos Motivos de Inadequação**:
    *   Tentativa de cruzar as amostras canceladas com seus respectivos motivos.
    *   **Principal achado**: A grande maioria das amostras canceladas (cerca de 97%) não possui um motivo de cancelamento registrado no sistema, o que indica uma falha importante no processo de documentação.
5.  **Análise Geográfica**:
    *   Cruzamento dos dados de cancelamento com as unidades de saúde e os municípios.
    *   Identificação das unidades de saúde e municípios com maior número de cancelamentos.
    *   Visualização dos dados em gráficos de barras e de pizza para ilustrar a concentração geográfica.

### 📊 Principais Insights e Conclusões

-   **Falta de Documentação**: O principal problema identificado é a ausência de registro dos motivos para a maioria dos cancelamentos, dificultando a análise da causa raiz.
-   **Concentração Geográfica**: Os cancelamentos não são distribuídos uniformemente. Há uma forte concentração em alguns municípios, com destaque para **São Luís**, que representa mais de 21% de todas as amostras canceladas.
-   **Ação Recomendada**: A análise sugere que fatores locais (como treinamento, processos ou infraestrutura) em municípios específicos podem estar influenciando diretamente a taxa de cancelamento. Uma investigação mais aprofundada nessas localidades é recomendada.

### 🛠️ Tecnologias Utilizadas

-   **Python**: Linguagem de programação.
-   **Pandas**: Para manipulação e análise dos dados.
-   **Matplotlib & Seaborn**: Para a criação das visualizações gráficas.
-   **Jupyter Notebook**: Como ambiente de desenvolvimento interativo.
