import pytest
from probabilidade import (
    probabilidade_condicional,
    probablidade_frequentista,
    regra_aditiva,
    regra_multiplicativa,
)


class TestProbabilidadeFrequentista:
    @pytest.mark.parametrize(
        ("freq_evento_a", "total_n", "esperado"),
        [
            (11, 20, 0.55),
            (0, 20, 0.0),
            (20, 20, 1.0),
            (1, 3, pytest.approx(1 / 3)),
        ],
    )
    def test_calcula_proporcao(self, freq_evento_a, total_n, esperado):
        assert probablidade_frequentista(freq_evento_a, total_n) == esperado

    def test_zero_observacoes_levanta_erro(self):
        with pytest.raises(ZeroDivisionError):
            probablidade_frequentista(1, 0)


class TestRegraAditiva:
    def test_eventos_exclusivos_soma_direto(self):
        # promoção de suco: cliente só pode escolher um sabor
        assert regra_aditiva(0.25, 0.15) == pytest.approx(0.40)

    def test_eventos_nao_exclusivos_subtrai_intersecao(self):
        # padaria: pão e leite podem ser comprados juntos
        assert regra_aditiva(0.50, 0.35, 0.20) == pytest.approx(0.65)

    def test_intersecao_total_equivale_ao_maior_evento(self):
        # se B está contido em A, P(A ∪ B) = P(A)
        assert regra_aditiva(0.6, 0.3, p_a_intersecao_b=0.3) == pytest.approx(0.6)


class TestRegraMultiplicativa:
    def test_eventos_independentes(self):
        # livraria: comprar revista e comprar chocolate
        assert regra_multiplicativa(0.20, 0.40) == pytest.approx(0.08)

    def test_probabilidade_zero_anula_resultado(self):
        assert regra_multiplicativa(0.0, 0.5) == 0.0

    def test_probabilidade_um_preserva_o_outro_evento(self):
        assert regra_multiplicativa(1.0, 0.42) == pytest.approx(0.42)


class TestProbabilidadeCondicional:
    def test_calcula_probabilidade_dado_evento(self):
        # loja de esportes: P(meia | tênis)
        assert probabilidade_condicional(0.18, 0.40) == pytest.approx(0.45)

    def test_intersecao_igual_ao_condicionante_da_certeza(self):
        # se A sempre ocorre junto com B, P(A|B) = 1
        assert probabilidade_condicional(0.3, 0.3) == pytest.approx(1.0)

    def test_p_b_zero_levanta_erro(self):
        with pytest.raises(ZeroDivisionError):
            probabilidade_condicional(0.1, 0.0)
