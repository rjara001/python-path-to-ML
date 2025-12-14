def printCuadradosYPares(serie):
    cuadrados = [x ** 2 for x in serie]
    print("Cuadrados:", cuadrados)

    pares = [x for x in serie if x % 2 == 0]
    print("Pares:", pares)

def printRedondeoNumerosFlotantes(serie):
    redondeados = [round(x, 2) for x in serie]
    print("Números redondeados:", redondeados)

def printValoresPrimos(serie):
    primos = [x for x in serie if isPrime(x)]
    print("Números primos:", primos)

def isPrime(n) -> bool:
    if n <= 2:
        return True

    if n % 2 == 0:
        return False

    limit = int(n * 0.5) + 1

    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True

def main() -> None:
    serie = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    flotantes = [1.234, 2.345, 3.456, 4.567]
    printCuadradosYPares(serie)
    printRedondeoNumerosFlotantes(flotantes)
    printValoresPrimos(serie)

if __name__ == "__main__":
    main()