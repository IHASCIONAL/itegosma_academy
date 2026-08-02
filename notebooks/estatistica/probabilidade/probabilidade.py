def probablidade_frequentista(freqEventoA, total_n):
    prob = freqEventoA / total_n

    return prob


def regra_aditiva(p_a, p_b, p_a_intersecao_b=0):
    """P(A ∪ B) = P(A) + P(B) - P(A ∩ B). Eventos exclusivos: intersecção = 0."""
    return p_a + p_b - p_a_intersecao_b


def regra_multiplicativa(p_a, p_b):
    """P(A ∩ B) = P(A) * P(B), para eventos independentes."""
    return p_a * p_b


def probabilidade_condicional(p_a_intersecao_b, p_b):
    """P(A|B) = P(A ∩ B) / P(B)."""
    return p_a_intersecao_b / p_b
