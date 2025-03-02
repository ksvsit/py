from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction

line_bot_api = LineBotApi('使用者Channel access token')
handler = WebhookHandler('使月者Channel secret')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if isinstance(event.message, TextMessage):
        mtext = event.message.text
        if mtext == '專業寫作團隊':
            picurl = 'https://imgur.com/OQyWDus.jpg'
            line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url=picurl, preview_image_url=picurl))
        if mtext == '以電話與我們聯絡':
            buttonsMessage = TemplateSendMessage(
                alt_text='Contact us',
                template=ButtonsTemplate(
                    title='聯絡我們',
                    text='0912345678',
                    actions=[
                        URIAction(label='撥打電話', uri='tel:0912345678')
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, messages=[buttonsMessage])

if __name__ == '__main__':
    app.run()
