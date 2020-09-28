# json, py flask
#============================================================
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#============================================================
from Index import *
from Animation import *
from FlexMessage import *
#============================================================
app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('PpZXtWUOfOocv4On1fWAHOFUZEdJu6WNW/XPDBbppZ3/573sZ/eyvlfZ1KP3t29JhHzzF4JgzaD1IIfrdKVWV6ocNbhBi5O4Qy5Cqpy+NHmBwYs0uZlVwiyW5bdgJPUGh4ZQG8bD6vhaSMVhjQsedAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ce990a6162a1aa9f706d9d826fc8d615')

# testbot
#line_bot_api = LineBotApi('NSZjNpSJhMXhy6WMtt6246iOUKAEbD+51al+ekd2HN3XgTaAqPwJgbHkdEtjUcCY83lpySCAOUhZwVP850hEEpa969+Myw5usVkudLhQoLrU7q6UDAuhnjGbQgYmY6RqQTajb7m74CbWpTJUmxFDAAdB04t89/1O/w1cDnyilFU=')
#handler = WebhookHandler('9af4f308ad523c116890f9d91e121c7e')
#============================================================
# /callback  Post Request
@app.route("/callback", methods=['POST'])
def callback():
# get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
# get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
# handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
#============================================================
# welcome
@handler.add(JoinEvent)
def handle_join(event):
    newcoming_text = "我來到一個新世界了嗎\n這個世界應該不再充斥著背叛了吧?\n對不起學姊\n這次，我...\n是永遠屬於各位騎士君的那個優衣呦\n*人家目前不支援簡體中文呦~*"
    message = Log(event)
    line_bot_api.reply_message(event.reply_token,[TextMessage(text=newcoming_text),message])
# follow 
@handler.add(FollowEvent)
def handle_Follow(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    Follow_text = profile.display_name + "騎士君歡迎！\n\n車車、圖圖、meme為這個世界帶來希望與和平，也可以把人家拉入群組\n頭貼圖源: twitter@nohhun144"
    message = Log(event)
    line_bot_api.reply_message(event.reply_token,[TextMessage(text=Follow_text),message])

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_message = event.message.text
    user = event.source.user_id
#----------------------------------------------------------------------------------------------------
#獵巫(私密聊天)
    if (user=="U770bbc6dc15278742deaec9399644742") and input_message[:2] == '>>': 
        print("訊息已經成功寄出")
        line_bot_api.push_message('U770bbc6dc15278742deaec9399644742', TextSendMessage(text= input_message.replace(">>","") ))
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text= "已發送 "+input_message.replace(">>","")))
        return
        #你是誰，請回覆我，怎麼知道我是誰
#    if(user=="Ua4c171080f799a7741fea78adaced548"):
#        line_bot_api.push_message('U770bbc6dc15278742deaec9399644742', TextSendMessage(text= input_message ))
#----------------------------------------------------------------------------------------------------
    JUD = Index_Judgment()
    JUD.Judgment (line_bot_api,input_message,event)


# endmodule
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug= True)
    
# 創建時間2020/7/7

# heroku login
# heroku git:remote -a oldpan-linebot
# git init
#===================================
# git add .
# git commit -am'ok' 
# git push heroku master
#===================================
# heroku logs -app oldpan-linebot

# 會要求who you are再用terminal(Ctrl+~)回應
#