from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('XL2/iHYIZQlvHItwu492k+04ZxmlbTDfsJ7G3ap5ynTFC50/D3dV/QO5Fwniw4pfmn0K/yPg1vBPZmpddxG6RytUvyR7qDXhRbpSptqgBNd6E35+C9BhKLkDWZgwYuTxXRuD+reT86F1DlwKdOivFAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('c246c5660535026024779b20c57a8e8d')

# 監聽所有來自callback 的 Post Request
@app.route('/callback', methods = ['POST'])
def callback():
    # get X-Line-Signature headers value
    signature = request.headers[' X-Line-Signature headers']
    
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