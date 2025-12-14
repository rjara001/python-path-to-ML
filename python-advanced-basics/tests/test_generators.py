from src.adv_basics_new.main import isPrime


def test_is_prime_success():
    series = [1, 2, 3, 4, 5, 10, 13, 16, 17, 18]
    primos_esperados = [1, 2, 3, 5, 13, 17]
    primos_obtenidos = [x for x in series if isPrime(x)]
    assert primos_obtenidos == primos_esperados


def test_printValoresPrimos(capsys):
    serie = [1, 2, 3, 4, 5, 10, 13, 16, 17, 18]
    from src.adv_basics_new.main import printValoresPrimos

    printValoresPrimos(serie)
    captured = capsys.readouterr()
    assert "Números primos: [1, 2, 3, 5, 13, 17]" in captured.out
