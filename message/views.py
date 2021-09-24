from django.shortcuts import render
from django.http import HttpResponseBadRequest,HttpResponseForbidden,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


from linebot import LineBotApi,WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage,MessageEvent

from cloud.predictions import get_imdb_sentiment

linebot=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser=WebhookParser(settings.LINE_CHANNEL_SECRET)

# Create your views here.
@csrf_exempt
def LineReply(request):
    if request.method == 'POST':
        signature=request.headers["x-line-signature"]
        body=request.body.decode("utf-8")


        try:
            #verify request from specific linebot
            events=parser.parse(body,signature)

            for e in events:
                if isinstance(e,MessageEvent):
                    texts=e.message.text #get message

                    if texts=="@功能說明":
                        results="此為電影評論情緒分析工具.\n請直接輸入文字進行分析"
                    else:
                        texts=[{"data":str(texts)}] #convert to GCP api format
                        results=get_imdb_sentiment(settings.PROJECT_ID,settings.LOCATION,
                                        settings.ENDPOINT_ID,texts)

                    linebot.reply_message(e.reply_token,TextSendMessage(text=results))

            return HttpResponse()

        except InvalidSignatureError:
            return HttpResponseForbidden("403:Invalid line bot signature")
    else:
        return HttpResponseBadRequest()

