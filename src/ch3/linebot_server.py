from flask import Flask, request, abort
import linebot, openai, os
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# OpenAIのAPIキーを環境変数から設定 --- (*1)
openai.api_key = os.getenv('OPENAI_API_KEY')
# LINEのトークンを環境変数から設定 --- (*2)
LINEBOT_TOKEN = os.getenv('LINEBOT_TOKEN')
LINEBOT_SECRET = os.getenv('LINEBOT_SECRET')
# Flaskのオブジェクトを生成 --- (*3)
app = Flask(__name__)
# LINEボットAPIのオブジェクトを生成 --- (*4)
line_bot_api = linebot.LineBotApi(LINEBOT_TOKEN)
handler = linebot.WebhookHandler(LINEBOT_SECRET)

# サーバールートにアクセスした時の処理 --- (*5)
@app.route("/")
def hello():
    return "hello" # 挨拶を返すだけ

# LINEボットのコールバックを設定する --- (*6)
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except linebot.exceptions.InvalidSignatureError:
        abort(400)
    return 'OK'

# LINEボットの応答を処理 --- (*7)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # LINEでユーザーからのメッセージを取得 --- (*8)
    text = event.message.text
    # ChatGPTのAPIを呼ぶ --- (*9)
    messages = [{'role': 'user', 'content': text}]
    rep_text = chat_completion(messages)
    # LINEにChatGPTの応答を返す --- (*10)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=rep_text))

# ChatGPTのAPIを呼び出す関数 --- (*11)
def chat_completion(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    # 応答からChatGPTの返答を取り出して返す
    return response.choices[0]['message']['content']


if __name__ == "__main__":
    # 証明書が保存されたディレクトリを指定(以下を変更) --- (*12)
    dir = '/etc/letsencrypt/live/bot.uta.pw/'
    # FlaskでSSLを使ってWebサーバーを起動 --- (*13)
    import ssl
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.load_cert_chain(
        f'{dir}fullchain.pem',
        f'{dir}privkey.pem')
    app.run(debug=True, port=443, host='0.0.0.0',
            ssl_context=ssl_context)
