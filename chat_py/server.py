import socket
from faker import Faker

HOST = 'localhost'  # サーバーのIPアドレスまたはホスト名を指定
PORT = 5000        # 使用するポート番号を指定

fake = Faker()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024).decode('utf-8')
        print(data)
        response = f"サーバからの応答: \nあなたのメッセージ: {data}"
        conn.sendall(response.encode('utf-8'))
