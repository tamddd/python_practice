const net = require('net');

// サーバのソケットファイルパス
const SOCK_PATH = './rpc_socket';

// リクエストを送信する関数
function sendRequest(method, params, paramTypes, callback) {
    // ソケットを作成し、サーバに接続する
    const client = net.connect(SOCK_PATH, () => {
        // リクエストを作成し、サーバに送信する
        const request = {
            method: method,
            params: params,
            param_types: paramTypes,
            id: 1
        };
        const requestData = JSON.stringify(request);
        client.write(requestData);
    });
}

sendRequest('exampleMethod', [1, 2, 3], ['int', 'int', 'int'], (response) => {
    console.log(response);
});
