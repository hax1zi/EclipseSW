import subprocess

def send_netcat(filename, ip, port):
    with open(filename, 'rb') as file:
        subprocess.run(["nc", "-w", "1", ip, str(port)], stdin=file)