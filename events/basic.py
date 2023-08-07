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