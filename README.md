
# Análise do Impacto do Halving do Bitcoin com Similaridade de Cosseno

Este projeto investiga o comportamento do preço do Bitcoin em torno dos eventos de halving utilizando a **similaridade de cosseno** aplicada a vetores de fechamento diário. Os dados foram extraídos de uma base minuto a minuto e agregados por dia para comparação de tendências.

## 📌 Objetivo

Avaliar se o padrão de preço do Bitcoin muda significativamente após os eventos de halving, comparando vetores de preços de **30, 90 e 180 dias antes e depois** de cada evento, usando **similaridade de cosseno**.

## 🔢 Dados Utilizados

- Dataset: `btcusd_1-min_data.csv` (Kaggle)
- Frequência original: 1 minuto
- Frequência usada: diária (fechamento do último minuto do dia)

## 📅 Eventos de Halving Considerados

- 1º Halving — 28/11/2012 — Recompensa: 50 → 25 BTC
- 2º Halving — 09/07/2016 — Recompensa: 25 → 12.5 BTC
- 3º Halving — 11/05/2020 — Recompensa: 12.5 → 6.25 BTC
- 4º Halving — 19/04/2024 — Recompensa: 6.25 → 3.125 BTC

## 🧠 Metodologia

1. Agregação dos dados minuto a minuto em **fechamentos diários**.
2. Extração de vetores de preços de **30, 90 e 180 dias** antes e depois de cada halving.
3. Cálculo da **similaridade de cosseno** entre os pares de vetores.
4. Interpretação dos valores obtidos (quanto mais próximo de 1, mais parecidos os padrões).

### Fórmula da Similaridade de Cosseno

\[
\cos(\theta) = \frac{{v \cdot w}}{{\|v\| \cdot \|w\|}}
\]

Onde \(v\) e \(w\) são vetores de preços.

## ✅ Resultados

| Halving | 30 dias | 90 dias | 180 dias |
|---------|---------|----------|-----------|
| 2012    | 0.999   | 0.947    | 0.838     |
| 2016    | 0.996   | 0.978    | 0.993     |
| 2020    | 0.994   | 0.985    | 0.988     |
| 2024    | 0.997   | 0.980    | 0.962     |

## 🧾 Conclusão

A análise mostra que os padrões de preço antes e depois dos halvings são altamente similares (similaridade > 0.98), indicando **continuidade de tendência**. A exceção foi 2012/180d, onde o padrão de alta foi mais explosivo, gerando menor similaridade.

## 📚 Referências

- INVESTOPEDIA. Bitcoin Halving. https://www.investopedia.com/bitcoin-halving-4843769
- LASHKARIPOUR, M. Some Stylized Facts About Bitcoin Halving. SSRN, 2024.
- WIKIPEDIA. Cosine similarity. https://en.wikipedia.org/wiki/Cosine_similarity
- CHAINALYSIS. What You Need to Know About the Bitcoin Halving, 2024.

## 👨‍🎓 Desenvolvido por

**Gabriel Gomes Ribeiro da Silva**  
Curso: Ciência de Dados - Fatec Rubens Lara  
Disciplina: Álgebra Linear  
Professor: Alexandre Garcia de Oliveira
