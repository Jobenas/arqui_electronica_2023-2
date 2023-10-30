import time


def count():
    idx = 99
    while idx > 0:
        print(f"{idx}")
        idx -= 1
        time.sleep(0.1)


def main():
    for _ in range(4):
        count()


if __name__ == '__main__':
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion {fin - inicio} segundos")
