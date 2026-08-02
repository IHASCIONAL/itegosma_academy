# Probabilidade

<span class="ia-status ia-status--andamento">em andamento</span>

## Probabilidade frequentista

Para encontrar a probabilidade de um determinado evento ocorrer, podemos utilizar a **probabilidade frequentista**. Sendo $A$ um evento aleatório qualquer, podemos encontrar a probabilidade de $A$ da seguinte forma:

\[
\hat{P}(A) = \frac{\text{Número de vezes que o evento } A \text{ ocorreu}}{\text{Número total de observações}}
\]

Essa razão representa a **frequência relativa observada** do evento em um número finito de repetições. Na definição frequentista formal, a probabilidade verdadeira $P(A)$ é o **limite dessa frequência relativa** quando o número de observações tende ao infinito.

De tal forma que:

\[
0 \leq P(A) \leq 1
\]

A probabilidade de um evento é sempre um valor entre 0 e 1 (ou em percentual, 0% a 100%).

## Exemplo

Lançamos uma moeda 20 vezes e o evento $A$ = "deu cara" ocorreu 11 vezes:

```python
def probablidade_frequentista(freqEventoA, total_n):
    prob = freqEventoA / total_n
    return prob


p_hat = probablidade_frequentista(11, 20)
print(f"P̂(A) = {p_hat:.2f} ({p_hat:.0%})")
```

```text
P̂(A) = 0.55 (55%)
```

## Regra aditiva

Calcula a probabilidade de **um evento OU outro** ocorrer, combinando as probabilidades individuais:

\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

Em **eventos mutuamente exclusivos** (não podem ocorrer juntos), $P(A \cap B) = 0$ e a fórmula vira uma soma direta. Em **eventos não exclusivos**, é preciso subtrair a interseção para não contar duas vezes quem está nos dois grupos.

```python
def regra_aditiva(p_a, p_b, p_a_intersecao_b=0):
    return p_a + p_b - p_a_intersecao_b


# Exclusivos: promoção com dois sabores de suco, cliente escolhe só um
print(f"{regra_aditiva(0.25, 0.15):.0%}")  # P(laranja ∪ uva)

# Não exclusivos: padaria, pão e leite podem ser comprados juntos
print(f"{regra_aditiva(0.50, 0.35, 0.20):.0%}")  # P(pão ∪ leite)
```

```text
40%
65%
```

## Regra multiplicativa

Calcula a probabilidade de **dois eventos independentes ocorrerem juntos** (um E outro) — a ocorrência de um não afeta a probabilidade do outro:

\[
P(A \cap B) = P(A) \times P(B)
\]

```python
def regra_multiplicativa(p_a, p_b):
    return p_a * p_b


# Livraria: comprar revista e comprar chocolate são eventos independentes
print(f"{regra_multiplicativa(0.20, 0.40):.0%}")  # P(revista ∩ chocolate)
```

```text
8%
```

## Probabilidade condicional

Calcula a probabilidade de um evento ocorrer **dado que outro já ocorreu**. Lê-se $P(A \mid B)$ como "probabilidade de A dado B":

\[
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad \text{para } P(B) > 0
\]

```python
def probabilidade_condicional(p_a_intersecao_b, p_b):
    return p_a_intersecao_b / p_b


# Loja de esportes: qual a chance de levar meia, dado que já levou tênis?
print(f"{probabilidade_condicional(0.18, 0.40):.0%}")  # P(meia | tênis)
```

```text
45%
```

!!! note "Próximos passos"
    Ainda faltam: Lei dos Grandes Números, teorema de Bayes e as distribuições (binomial, normal etc.). Entram aqui assim que forem estudadas. O código completo e executado está em `notebooks/estatistica/probabilidade/anotacoes.ipynb`.
