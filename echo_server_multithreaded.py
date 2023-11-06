import socket
from threading import Thread

SOCK_BUFFER = 1024

num_clientes = 0

def client_handler(conn, client_address):
    global num_clientes

    print(f"Conexion de {client_address[0]}:{client_address[1]}")
    num_clientes += 1
    print(f"Numero de clientes actualmente conectados: {num_clientes}")

    try:
        while True:
            dato = conn.recv(SOCK_BUFFER)

            if dato: 
                print(f"Recibi {dato}")
                conn.sendall(dato)
            else:
                print("No hay más datos")
                break
    except ConnectionResetError:
        print("El cliente cerró la conexión de manera abrupta")
    finally:
        print("cerrando la conexion")
        conn.close()
        num_clientes -= 1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5000)

    print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones...")
        connection, c_address = sock.accept()

        t = Thread(target=client_handler, args=(connection, c_address))
        t.start()        

        print("Cliente delegado, terminando iteracion")
