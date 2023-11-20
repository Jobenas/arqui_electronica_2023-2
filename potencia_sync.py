import time

def potencia(n: int) -> int:
    res = 1

    for _ in range(1, n + 1):
        res *= n
    
    return res


if __name__ == "__main__":
    inicio = time.perf_counter()
    potencia(100_000)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")
