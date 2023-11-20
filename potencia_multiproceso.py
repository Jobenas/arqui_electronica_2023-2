from multiprocessing import cpu_count, Pool
import time

tareas = cpu_count() * 2

def potencia(n: int, div: int = tareas) -> int:
    res = 1

    if div <= 0:
        div = 1

    for _ in range(1, (n // div) + 1):
        res *= n
    
    return res


if __name__ == "__main__":
    inicio = time.perf_counter()
    p = Pool(processes=cpu_count())
    res = p.map(potencia, [100_000] * tareas)
    p.close()
    p.join()
    p = res[0] * res[1]
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion multiproceso: {fin - inicio} segundos")
