from line_bot_api import *


def stock_reply_other(stockNumber):
    content_text = "即時股價K線圖"
    text_message = TextSendMessage(
                            text = content_text, 
                            quick_reply=QuickReply(
                                items=[
                                    QuickReplyButton(
                                        action=MessageAction(
                                            label="# + 股票代號查詢",
                                            text="#"+stockNumber
                                        )
                                    ),
                                    QuickReplyButton(
                                        action=MessageAction(
                                            label = "K線圖",
                                            text = "@K"+stockNumber
                                        )
                                    ),
                                ]
                            ))
    return text_message

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/y4NCGG4.jpg",
                    "size": "5xl"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "幣別種類",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#7C9D96"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "美USD",
                            "text": "查詢匯率USD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#7A9D54",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "日JPY",
                            "text": "查詢匯率JPY"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#071952",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "港HKD",
                            "text": "查詢匯率HKD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#7A9D54",
                            "margin": "sm"
                        }
                        ],
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "英GBP",
                            "text": "查詢匯率GBP"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#35A29F",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "澳AUD",
                            "text": "查詢匯率AUD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#7A9D54",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "加CAD",
                            "text": "查詢匯率CAD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#35A29F",
                            "margin": "sm"
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "瑞士CHF",
                            "text": "查詢匯率CHF"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#7A9D54",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "新SGD",
                            "text": "查詢匯率SGD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#071952",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "南非ZAR",
                            "text": "查詢匯率ZAR"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#7A9D54",
                            "margin": "sm"
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "瑞典SEK",
                            "text": "查詢匯率SEK"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#35A29F",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "泰THB",
                            "text": "查詢匯率THB"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#7A9D54",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "菲PHP",
                            "text": "查詢匯率PHP"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#35A29F",
                            "margin": "sm"
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "印尼IDR",
                            "text": "查詢匯率IDR"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#7A9D54",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "韓KRW",
                            "text": "查詢匯率KRW"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#071952",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "馬MYR",
                            "text": "查詢匯率MYR"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#7A9D54",
                            "margin": "sm"
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "越南VND",
                            "text": "查詢匯率VND"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#35A29F",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "中CNY",
                            "text": "查詢匯率CNY"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#7A9D54",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "紐NZD",
                            "text": "查詢匯率NZD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#35A29F",
                            "margin": "sm"
                        }
                        ]
                    }
                    ]
                }
            }
                    
    )
    return flex_message