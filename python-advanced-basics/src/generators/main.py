from src.generators.utils import isPrime

def create_file_more_than_n_lines(file_path, n):
    """Crea un archivo de texto con más de n líneas.

    Cada línea contendrá el texto "Línea X", donde X es el número de línea.

    Args:
        file_path (str): La ruta del archivo a crear.
        n (int): El número mínimo de líneas que debe tener el archivo.
    """
    # should append to the file if it exists
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_lines = f.readlines()
            n = max(n, len(existing_lines))
    except FileNotFoundError:
        pass

    with open(file_path, 'a', encoding='utf-8') as f:
        for i in range(1, n + 2):  # Crear n + 1 líneas
            f.write(f"Línea {i}\n")


def create_prime_file(name_file):
    with open(name_file, 'w', encoding='utf-8') as f:
        for index, line in enumerate(lines_from_file("archivo.python.txt"), start=1):
            if isPrime(index):
                f.write(line)
            else:
                print(f"El índice {index} no es primo, se omite la línea.")

def lines_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line

#put = (writem(line) for line in f.readlines() if isPrime(index))

if __name__ == "__main__":
    # create_file_more_than_n_lines("archivo.python.txt", 1000)

    #  read file and create a new one with the odd numbers
    create_prime_file("archivo.python.out.txt")

