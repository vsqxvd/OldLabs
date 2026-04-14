import socket

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"File server listening on {HOST}:{PORT}")

    while True:  # Цикл для прийому нових клієнтів
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            filename = conn.recv(1024).decode()  # отримуємо ім'я файлу
            if not filename:
                continue
            print(f"Receiving file: {filename}")
            with open(f"received_{filename}", "wb") as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print(f"File {filename} saved successfully.")