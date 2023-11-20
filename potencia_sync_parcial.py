import time

def potencia(n: int, div: int) -> int:
    res = 1

    if div <= 0:
        div = 1

    for _ in range(1, (n // div) + 1):
        res *= n
    
    return res


if __name__ == "__main__":
    inicio = time.perf_counter()
    p1 = potencia(100_000, 2)
    p2 = potencia(100_000, 2)
    p = p1 * p2
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")
