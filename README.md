# Projeto de Limpeza de Dados

Este projeto tem como objetivo aplicar técnicas de **limpeza de dados** em um conjunto de vendas de uma cafeteria fictícia. A limpeza foi realizada utilizando a biblioteca **Pandas** em Python, focando na preparação dos dados para análises futuras.

---

## Sobre o conjunto de dados

O arquivo `dirty_cafe_sales.csv` contém registros de transações de vendas em uma cafeteria. As colunas incluem:

- `Transaction ID`: identificador único da transação
- `Item`: item vendido
- `Quantity`: quantidade vendida
- `Price Per Unit`: preço unitário
- `Total Spent`: total gasto
- `Payment Method`: método de pagamento
- `Location`: local da transação
- `Transaction Date`: data da transação

---

## Etapas de limpeza realizadas

1. **Identificação de valores ausentes** (`NaN`, `UNKNOWN`, `ERROR`, espaços vazios)
2. **Substituição de valores problemáticos por `NaN`**
3. **Remoção de linhas com dados faltantes críticos**
4. **Remoção de duplicatas**
5. **Conversão de tipos de dados apropriados**
   - Inteiros (`int`) para `Quantity`
   - Ponto flutuante (`float`) para `Price Per Unit` e `Total Spent`
   - `datetime` para `Transaction Date`
   - `category` para `Payment Method` e `Location`
6. **Reparo de inconsistência nos totais**
   - `Total Spent` recalculado como `Quantity * Price Per Unit`
7. **Padronização de textos em colunas categóricas**
   - Correção de espaços e formatação de capitalização

---

## Resultado

Após a limpeza, o conjunto está pronto para análises estatísticas, visualizações ou integração com dashboards. Os dados agora são confiáveis, consistentes e estruturados.

---

## Sugestões de próximos passos

- Criar visualizações exploratórias (usando Matplotlib ou Seaborn)
- Construir um painel no Power BI ou Tableau com os dados limpos
- Aplicar análise de sazonalidade ou agrupamentos por localização



