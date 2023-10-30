import random
import time


def genera_labs():
    with open("notas_lab.csv", "w+", encoding='utf-8') as f:
        f.write("codigo,lab1,lab2,lab3,lab4,lab5,lab6,lab7,lab8,lab9,lab10,lab11,lab12\n")
        codigo_inicial = 20230001
        for i in range(100):
            fila = f"{codigo_inicial + i},"
            for _ in range(12):
                fila += f"{random.randint(0,20)},"
            fila = fila[:-1]
            fila += "\n"
            f.write(fila)


def genera_parcial():
     with open("notas_parcial.csv", "w+", encoding='utf-8') as f:
        f.write("codigo,nota\n")
        codigo_inicial = 20230001
        for i in range(100):
            fila = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            f.write(fila)


def genera_final():
     with open("notas_final.csv", "w+", encoding='utf-8') as f:
        f.write("codigo,nota\n")
        codigo_inicial = 20230001
        for i in range(100):
            fila = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            f.write(fila)


def main():
    print("Generando notas de lab")
    genera_labs()
    print("Generando notas de parcial")
    genera_parcial()
    print("Generando notas de final")
    genera_final()


if __name__ == '__main__':
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion {fin - inicio} segundos")

