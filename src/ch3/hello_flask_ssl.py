from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

if __name__ == "__main__":
    # 証明書が保存されたディレクトリを指定(要書き換え) --- (*1)
    dir = '/etc/letsencrypt/live/bot.uta.pw/'
    # FlaskでSSLを使ってWebサーバーを起動 --- (*2)
    import ssl
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.load_cert_chain(
        f'{dir}fullchain.pem',
        f'{dir}privkey.pem')
    app.run(debug=True, port=443, host='0.0.0.0',
            ssl_context=ssl_context)

