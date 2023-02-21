import json
import socket

# ソケットのファイルパス
SOCK_PATH = './rpc_socket'

# メソッドとパラメータの関数を定義
def subtract(a, b):
    return a - b

def floor(x):
    return int(x // 1)

def nroot(n, x):
    return int(x ** (1/n))

def add(a, b):
    return a + b

# メソッドと対応する関数を登録
methods = {
    'add' : add,
    'subtract': subtract,
    'floor': floor,
    'nroot': nroot,
}

# ソケットを作成し待ち受け状態にする
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(SOCK_PATH)
    server_socket.listen()
    # クライアントからの接続を受け付け、リクエストを処理する
    while True:
        # クライアントからの接続を待つ
        client_socket, _ = server_socket.accept()
        # リクエストを受信する
        data = client_socket.recv(1024)
        request = json.loads(data)
        # メソッド名とパラメータを取得し、関数を実行する
        method = request['method']
        params = request['params']
        param_types = request['param_types']
        print(request)
        # パラメータの型が正しいことを検証
        if len(params) != len(param_types):
            response = {'error': 'Invalid request'}
        else:
            # 関数を実行し、結果を取得
                func = methods.get(method)
                if func:
                    result = func(*params)
                    result_type = type(result).__name__
                    response = {'result': result, 'result_type': result_type}
                    print(response)
                else:
                    response = {'error': 'Method not found'}
                    print(response)
        print(response)
        # レスポンスを送信する
        client_socket.sendall(json.dumps(response).encode('utf-8'))
        # ソケットを閉じる
        client_socket.close()
