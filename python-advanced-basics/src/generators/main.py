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

def read_file_and_create_new_only_with_odd(file_path)
    with open(file_path, 'r', encodig='utf-8') as f:
        [isprime(line) for line in f.readlines()]

def isprime(value):
    true

if __name__ == "__main__":
    # create_file_more_than_n_lines("archivo.python.txt", 1000000)

    #  read file and create a new one with the odd numbers
    read_file_and_create_new_only_with_odd("archivo.python.txt")

