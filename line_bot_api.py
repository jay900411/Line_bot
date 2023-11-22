from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import random
import time
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('t3GglwAI98AmV9rf0s1uHXILs/QYPlEjIV7g7VaurSGBg7Hb1+iw5jD4qNGWi5xFmn0K/yPg1vBPZmpddxG6RytUvyR7qDXhRbpSptqgBNcHA39zQpeKCW4+wvoydpGE5//ojrHuZBaOQnP9r0itCgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('c246c5660535026024779b20c57a8e8d')
