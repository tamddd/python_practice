const net = require('net');

// サーバのソケットファイルパス
const SOCK_PATH = './rpc_socket';

// リクエストを送信する関数
function sendRequest(method, params, paramTypes, callback) {
    const client = net.connect(SOCK_PATH, () => {
        const request = {
            method: method,
            params: params,
            param_types: paramTypes,
            id: 1
        };
        const requestData = JSON.stringify(request);
        client.write(requestData);
    });

    client.on('data', (data) => {
        const response = JSON.parse(data.toString());
        if (response.error) {
            console.error(response.error);
        } else {
            callback(response.result);
        }
        client.end();
    });

    client.on('error', (error) => {
        console.error(error);
        client.end();
    });
}


sendRequest('add', [1, 2], ['int', 'int'], (response) => {
    console.log(response);
});

sendRequest('sub', [123, 321], ['int', 'int'], (response) => {
    console.log(response);
});
