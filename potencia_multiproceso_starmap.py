from itertools import repeat
from multiprocessing import cpu_count, Pool
import time

tareas = cpu_count() * 2

def potencia(n: int, div: int) -> int:
    res = 1

    if div <= 0:
        div = 1

    for _ in range(1, (n // div) + 1):
        res *= n
    
    return res


if __name__ == "__main__":
    inicio = time.perf_counter()
    num = [100_000] * tareas
    args = zip(num, repeat(tareas))
    p = Pool(processes=cpu_count())
    res = p.starmap(potencia, args)
    p.close()
    p.join()
    p = res[0] * res[1]
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion multiproceso: {fin - inicio} segundos")
