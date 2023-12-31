from concurrent.futures import ThreadPoolExecutor
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
    
    def update(self, name):
        print(f"Thread {name}: iniciando actualizacion")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print(f"Thread {name}: finalizando actualizacion")


if __name__ == "__main__":
    worker = 2
    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")
    with ThreadPoolExecutor(max_workers=worker) as executor:
        for index in range(worker):
            executor.submit(db.update, index)

    print(f"Valor final de la base de datos: {db.value}")