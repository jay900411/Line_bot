from line_bot_api import *
from events.basic import *
from events.oil import *
app = Flask(__name__)



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
def handle_message(event):
    message_text = str(event.message.text).lower()
    
    if message_text == '@使用說明':
        about_us_event(event)
        Usage(event)
    # message = TemplateSendMessage(text = event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    elif message_text == '@小幫手':
        helper(event)
    ############## 油價查詢 ##############
    if message_text == '想知道油價':
        content = oil_price()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = content))
if __name__ == '__main__':
    app.run()
