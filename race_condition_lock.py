from concurrent.futures import ThreadPoolExecutor
import time
from threading import Lock


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = Lock()
    
    def update(self, name):
        print(f"Thread {name}: iniciando actualizacion")
        print(f"Thread {name}: a punto de adquirir el lock")
        with self._lock:
            print(f"Thread {name} ha adquirido el lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print(f"Thread {name}: a punto de liberar el lock")
        print(f"Thread {name} ha liberado el lock")
        print(f"Thread {name}: finalizando actualizacion")


if __name__ == "__main__":
    worker = 2
    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")
    with ThreadPoolExecutor(max_workers=worker) as executor:
        for index in range(worker):
            executor.submit(db.update, index)

    print(f"Valor final de la base de datos: {db.value}")