from line_bot_api import *

def about_us_event(event):
    
    emoji = [
        {
            'index' : 0,
            'productId' : '5ac21c4e031a6752fb806d5b' ,
            'emojiId' : '006'
        }, 
        {
            'index' : 17,
            'productId' : '5ac21e6c040ab15980c9b444' ,
            'emojiId' : '004'
        }
    ]
    
    text_message = TextSendMessage(text = '''$ Master Finance $
Hello! 您好，歡迎您成為 Master Finance 的好友!

我是Master 財經小幫手

-這裡有股票，匯率資訊喔~
-直接點及下方【圖中】選單功能

-期待您的光臨!''', emojis = emoji)
    sticker_message = StickerMessage(
        package_id = '11538', 
        sticker_id = '51626508'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])
    
def push_msg(event, msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id, TextSendMessage(text = msg))
    except:
        room_id = event.source.room_id
        line_bot_api.push_message(room_id, TextSendMessage(text = msg))

def Usage(event):
    push_msg(event, "🔍查詢方法🔎\
                \n\
                \n小幫手可以查詢\
                \n🕯油價🕯匯率🕯股價 \
                \n\
                \n(´･･)ﾉ油價通知 ❁ 輸入查詢油價 \
                \n(._.`)匯率通知 ❁ 輸入查詢匯率 \
                \n(´◡`)匯率兌換 ❁ 換匯USD/TWD/金額(ex.:100) \
                \n( '◡' )股價查詢 ❁ 輸入#股票代碼 ")
def helper(event):
    buttons_template = TemplateSendMessage(
            alt_text = '小幫手template',
            template = ButtonsTemplate(
                title = '選擇服務', 
                text = '請選擇', 
                thumbnail_image_url = 'https://i.imgur.com/Sal19Wy.jpg', 
                actions = [
                    MessageTemplateAction(
                        label = '油價查詢', 
                        text = '想知道油價'
                    ), 
                    MessageTemplateAction(
                        label = '匯率查詢', 
                        text = '幣別種類'
                    ),
                    MessageTemplateAction(
                        label = '股價查詢', 
                        text = '想知道股價'
                    )
                ]
            )
        )
    line_bot_api.reply_message(event.reply_token, buttons_template)
def encourager(event) :
    messages = ['加油！是為了自己呢！', '你很棒！可以的！', '你很努力喔！值得值得！', '今天是艱難的一天 但你撐住了！', 
                '覺得累嗎！好好休息重新出發！', '一是嬰兒哭啼..二是別放棄！放鬆一下再繼續！！', '你說你很累..但你還能睡！', 
                '你是溫柔的人 但對自己不能太溫柔喔！', '今朝有酒今朝醉..你讀完書洗洗睡', '討拍完了嗎！出發！', '一天很短 開心就笑！不開心就..等等再笑！', 
                '一天就24小時 你不要想活成26小時！','前面的路崎嶇難行 後方的小姊姊問我：細狗你行不行！']

    # 45%的機會挑選一句，55%的機會挑選2~3句
    if random.random() < 0.4:
        encourage = [random.choice(messages)]
    elif 0.4 <= random.random() < 0.8:
        encourage = random.sample(messages, k = 2)
    else:
        encourage = random.sample(messages, k = 3)
    for i in encourage:
        push_msg(event, i)
        time.sleep(0.45)
        
