import socket

HOST = 'localhost'  # サーバーのIPアドレスまたはホスト名を指定
PORT = 5000        # 使用するポート番号を指定



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input("メッセージを入力してください：")
    s.sendall(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received', repr(data))
