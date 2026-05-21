# Plano de Implementação - Refinamento do Modelo Preditivo

Este plano propõe refinar o modelo de Machine Learning no notebook [Analise4_ML_Preditivo.ipynb](file:///home/bruno/VscodeProjetos/Teste_do_pezinho/Analise4_ML_Preditivo.ipynb) para reduzir a taxa de falsos positivos (aumentar a precisão) sem comprometer severamente a sensibilidade (recall).

---

## Análise do Problema

O modelo atual (Random Forest com `class_weight='balanced'`) obtém 88% de recall e 6% de precisão para a classe positiva porque:
1. **Limiar Padrão Inadequado**: Ao usar `.predict()`, o scikit-learn adota o limiar de decisão padrão de `0.5`. Com classes muito desbalanceadas (0.37% de casos positivos) e pesos balanceados, as probabilidades estimadas são inflacionadas, gerando muitos falsos positivos.
2. **Subutilização de Features**: O modelo atual usa apenas 5 features básicas, descartando dados clínicos, logísticos e demográficos valiosos contidos nos arquivos originais.
3. **Limitação do Algoritmo**: Random Forest é robusto, mas algoritmos de Gradient Boosting (como `HistGradientBoostingClassifier`) geralmente obtêm melhor desempenho em dados tabulares muito desbalanceados.

---

## Resultados dos Testes de Refinamento

Realizamos testes com os dados reais do seu projeto e obtivemos os seguintes resultados comparativos:

| Modelo / Abordagem | PR-AUC (Average Precision) | Recall @ Max F1 | Precision @ Max F1 | Precision @ 88% Recall |
| :--- | :---: | :---: | :---: | :---: |
| **Baseline (Atual)** (Limiar 0.5) | 0.4957 | 88.0% | 5.4% | 5.4% |
| **Baseline + Otimização de Limiar** (Limiar 0.83) | 0.4957 | 60.0% | **67.8%** | 5.4% |
| **Random Forest Enriquecido** (Limiar 0.95) | 0.7022 | 70.0% | **78.4%** | 6.7% |
| **HistGradientBoosting Enriquecido** (Limiar 0.75) | **0.7368** | 72.1% | **84.4%** | **28.7%** |

> [!IMPORTANT]
> Ao atualizar o algoritmo para **HistGradientBoosting** e enriquecer as features, a precisão para o nível de recall de 88% sobe de **5.4% para 28.7%** (reduzindo os falsos positivos de ~7.000 para ~1.100).
> Se optarmos por equilibrar o modelo buscando o melhor F1-score, conseguimos **84.4% de precisão com 72.1% de recall**!

---

## Alterações Propostas

### 1. Enriquecimento de Features
Adicionar as seguintes variáveis que estão nas tabelas originais, mas não são usadas atualmente:
*   `ide_fez_pre_natal` (Se a mãe realizou pré-natal)
*   `ide_mae_uso_corticoide` (Se a mãe usou corticoide)
*   `ide_transfusao_amostra` (Se o bebê recebeu transfusão de sangue - fator crítico para precisão do teste)
*   `co_seq_tp_triagem` (Tipo de triagem neonatal)
*   `co_seq_municipio` (Município de residência - captura variações geográficas de logística/genética)
*   `co_seq_tp_material_coletado` (Tipo de material coletado)
*   `ida_nascimento_mes` (Idade gestacional do bebê em meses/semanas)

### 2. Upgrade de Algoritmo
Substituir o `RandomForestClassifier` pelo `HistGradientBoostingClassifier` do scikit-learn.
*   **Vantagem**: Esse algoritmo é extremamente veloz, lida nativamente com valores nulos (sem precisar de imputação arbitrária por mediana) e suporta categorias de forma direta, melhorando muito a capacidade preditiva em conjuntos altamente desbalanceados.

### 3. Ajuste Fino do Limiar de Decisão
Adicionar ao final do notebook uma célula para:
*   Plotar a curva de **Precision-Recall**.
*   Encontrar e exibir o limiar ideal que maximiza o F1-score ou F-beta-score.
*   Permitir a predição utilizando esse limiar personalizado em vez do `.predict()` padrão.

---

## Arquivos Modificados

### [MODIFY] [Analise4_ML_Preditivo.ipynb](file:///home/bruno/VscodeProjetos/Teste_do_pezinho/Analise4_ML_Preditivo.ipynb)
*   Atualizar a carga de dados (`cols_pessoa` e `cols_amostra`) na Célula 3 para incluir as novas colunas.
*   Ajustar o processamento na Célula 4 para tratar as colunas como categóricas nativas.
*   Substituir a instanciação e o treino do Random Forest pelo HistGradientBoosting na Célula 6.
*   Adicionar avaliação com busca de limiar otimizado por F1 na Célula 12.

---

## Plano de Verificação

### Testes Automatizados
*   Executar o notebook ponta a ponta na máquina local usando o interpretador python do ambiente virtual:
    ```bash
    .venv/bin/python3 -m jupyter nbconvert --to notebook --execute --inplace Analise4_ML_Preditivo.ipynb
    ```
*   Confirmar que o notebook executa sem erros e gera a curva ROC / PR atualizada.
