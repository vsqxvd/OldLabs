import socket

HOST = '127.0.0.1'
PORT = 8000
FILENAME = 'test.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(FILENAME.encode())  # Надсилання ім'я файла
    with open(FILENAME, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.sendall(data) # Надсилання змісту файла
print(f"File {FILENAME} sent successfully.")