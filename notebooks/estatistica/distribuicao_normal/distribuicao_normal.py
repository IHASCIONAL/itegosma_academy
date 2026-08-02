from scipy.stats import norm


def probabilidade_abaixo(x, media, desvio_padrao):
    """P(X <= x) para X ~ N(media, desvio_padrao)."""
    return norm.cdf(x, media, scale=desvio_padrao)


def probabilidade_acima(x, media, desvio_padrao):
    """P(X > x) para X ~ N(media, desvio_padrao)."""
    return 1 - norm.cdf(x, media, scale=desvio_padrao)


def probabilidade_entre(x1, x2, media, desvio_padrao):
    """P(x1 <= X <= x2) para X ~ N(media, desvio_padrao)."""
    return norm.cdf(x2, media, scale=desvio_padrao) - norm.cdf(x1, media, scale=desvio_padrao)
