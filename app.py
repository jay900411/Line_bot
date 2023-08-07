from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('t3GglwAI98AmV9rf0s1uHXILs/QYPlEjIV7g7VaurSGBg7Hb1+iw5jD4qNGWi5xFmn0K/yPg1vBPZmpddxG6RytUvyR7qDXhRbpSptqgBNcHA39zQpeKCW4+wvoydpGE5//ojrHuZBaOQnP9r0itCgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('c246c5660535026024779b20c57a8e8d')

# 監聽所有來自callback 的 Post Request
@app.route('/callback', methods = ['POST'])
def callback():
    # get X-Line-Signature headers value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text = True)
    app.logger.info('Request body: ' + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
        
    return "OK"

# 處理訊息
@handler.add(MessageEvent, message = TextMessage)
def handler_message(event):
    message = TemplateSendMessage(text = event.message.text)
    line_bot_api.reply_message(event.reply_token, message)
    
if __name__ == '__main__':
    app.run()