# Análise de Dados do Teste do Pezinho (Qualidade e Logística)

Este projeto visa analisar os dados do Teste do Pezinho para identificar gargalos operacionais, logísticos e de qualidade nas amostras coletadas no estado.

## 📂 Estrutura do Projeto e Notebooks

| Notebook | Foco da Análise | Principais Insights |
| :--- | :--- | :--- |
| **`Analise1.ipynb`** | **Cancelamentos e Motivos** | Taxa de cancelamento de 0.11%. A maioria dos motivos não é documentada. Forte concentração em São Luís (21%).<br>⚠️ *Nota: A análise por profissão apresenta dados parciais por falta de tabela de usuários.* |
| **`Analise2_Otimizada.ipynb`** | **Idade na Coleta** | Análise do tempo entre Nascimento e Coleta (Ideal: 3-5 dias). Verifica impacto do dia da semana na coleta. |
| **`Analise3_Logistica_Real.ipynb`** | **Logística de Transporte** | **Novo!** Foco no tempo de estrada (Coleta → Chegada no Lab). Identifica municípios com maiores atrasos e correlação com rejeição de amostras. |

---

## 📊 Detalhes das Análises

### 1. Qualidade da Amostra (Analise 1)
- **Foco**: Amostras recusadas/canceladas.
- **Achados**:
    - Grande subnotificação de motivos de cancelamento (97% sem motivo claro).
    - Discrepâncias regionais significativas.

### 2. Eficiência da Coleta (Analise 2)
- **Foco**: O quão cedo o bebê é testado.
- **KPI**: Delta (`Data Coleta` - `Data Nascimento`).
- **Classificação**: Precoce (<3 dias), Ideal (3-5 dias), Tardio (>5 dias).

### 3. Eficiência Logística (Analise 3)
- **Foco**: O tempo que a amostra passa em trânsito.
- **KPI**: Delta (`Data Recebimento` - `Data Coleta`).
- **Hipótese Confirmada**: Amostras com tempo de transporte elevado apresentam maior taxa de inadequação (hemólise/envelhecimento).
- **Ranking**: Lista de municípios críticos que necessitam de rotas de transporte revisadas.

---

## 💾 Fonte dos Dados
Os dados estão organizados na pasta `datasets1` e incluem:
- `tb_amostra.csv`: Tabela fato com datas cruciais (Coleta, Recebimento, Cadastro).
- `tb_municipio.csv` / `tb_unidade_saude.csv`: Dimensões geográficas.
- `tb_motivo_inadequacao.csv`: Catálogo de motivos de rejeição.

## ⚠️ Limitações Conhecidas
- **Análise por Profissional**: A tentativa de analisar a performance por profissional de saúde (`Analise1`) foi prejudicada pela ausência de uma tabela que vincule o login do usuário (`aut_registro`) ao seu cadastro profissional. Apenas 7 profissionais puderam ser mapeados.

## 🛠️ Tecnologias
- **Python 3.8+**
- **Pandas**: Processamento e ETL.
- **Seaborn / Matplotlib**: Visualização de dados.
- **Jupyter**: Ambiente de execução.
