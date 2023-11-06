import time
from threading import Thread


def func1():
    print("Iniciando Funcion 1")
    time.sleep(2)
    print("Terminando Funcion 1")


def func2():
    print("Iniciando Funcion 2")
    time.sleep(3)
    print("Terminando Funcion 2")


def func3():
    print("Iniciando Funcion 3")
    time.sleep(1)
    print("Terminando Funcion 3")


def main():
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t3 = Thread(target=func3)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion multihilo: {fin - inicio} segundos")
