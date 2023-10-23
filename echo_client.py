import socket

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"conectando a servidor {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "Hola mundo!"
    print(f"Enviando mensaje: {msg}")
    sock.sendall(msg.encode("utf-8"))
    dato = sock.recv(SOCK_BUFFER)
    print(f"Recibí: {dato}")

    print("Cerrando conexión")
    sock.close()
