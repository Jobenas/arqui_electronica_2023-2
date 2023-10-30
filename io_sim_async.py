import asyncio
import time


async def func1():
    print("Iniciando Funcion 1")
    await asyncio.sleep(2)
    print("Terminando Funcion 1")
    
    return 1


async def func2():
    print("Iniciando Funcion 2")
    await asyncio.sleep(3)
    print("Terminando Funcion 2")

    return 2


async def func3():
    print("Iniciando Funcion 3")
    await asyncio.sleep(1)
    print("Terminando Funcion 3")

    return 3


async def main():
    r = await asyncio.gather(func1(), func2(), func3())

    print(r)

if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")
