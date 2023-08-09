from line_bot_api import *
from events.basic import *
from events.oil import *
from events.Msg_Template import *
import twstock
import re
import datetime

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
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id
    
    message_text = str(event.message.text).lower()
    
    msg = str(event.message.text).upper().strip()
    emsg = event.message.text
    
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
    ############## 股價查詢 ##############
    if message_text == '想知道股價':
        line_bot_api.push_message(uid, TextSendMessage("請輸入'#'+'股票代碼'...ex:#0050"))

    if re.match("股價查詢", msg):
        msg = msg[4:]
        btn_msg = stock_reply_other(msg)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    
    if (msg.startswith('#')):
        ###############################
        text=msg[1:]
        content = ''
        
        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp'] + 8*60*60)
        my_time = my_datetime.strftime('%H:%M:%S')
        
        content += '%s (%s) %s\n' %(
            stock_rt['info']['name'], 
            stock_rt['info']['code'], 
            my_time
        )
        content += '現價: %s / 開盤: %s\n'%(
            stock_rt['realtime']['latest_trade_price'], 
            stock_rt['realtime']['open']
        )
        content += '最高: %s / 最低: %s\n'%(
            stock_rt['realtime']['high'], 
            stock_rt['realtime']['low']
        )
        content += '量: %s\n' %(stock_rt['realtime']['accumulate_trade_volume'])
        
        stock = twstock.Stock(text)
        content += '-----\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s\n' %(date5[i].strftime('%Y-%m-%d'), price5[i])
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text = content)
        )
    
############## 封鎖 / 解封 ##############
@handler.add(FollowEvent)        
def handle_follow(event):
    welcome_msg = '''Hello! 您好，歡迎您成為 Master Finance 的好友!

我是Master 財經小幫手

-這裡有股票，匯率資訊喔~
-直接點及下方【圖中】選單功能

-期待您的光臨!'''

    line_bot_api.reply_message(event.reply_token, TemplateSendMessage(text = welcome_msg))
                               
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)
    
if __name__ == '__main__':
    app.run()
