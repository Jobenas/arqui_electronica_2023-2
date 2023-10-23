import socket
import time

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"conectando a servidor {server_address[0]}:{server_address[1]}")

    inicio = time.perf_counter()
    sock.connect(server_address)

    msg = "Hola mundo!"
    amnt_expected = len(msg.encode("utf-8"))
    amnt_received = 0
    # print(f"Enviando mensaje: {msg}")
    msg_rcvd = b""
    sock.sendall(msg.encode("utf-8"))
    while amnt_received < amnt_expected:
        dato = sock.recv(SOCK_BUFFER)
        # print(f"Recibí: {dato}")
        amnt_received += len(dato)
        msg_rcvd += dato
    # print(f"Total recibido: {msg_rcvd}")
    # print("Cerrando conexión")
    sock.close()
    fin = time.perf_counter()

    print(f"Total recibido: {msg_rcvd}")
    print(f"Tiempo de ejecución de operación parcial: {fin - inicio} segundos")
