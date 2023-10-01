from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import *

@api_view(["POST"])
def convertAPIView(request) -> Response:
    """Конвертирует аудио по POST запросу"""
    link = request.data['link'] #получаем указанную в запросе ссылку (json)
    try:
        yt = create_youtube_link(link) #пробуем создать объект YouTube
    except:
        return Response({"message": "Couldn't find this link!"}) #выводим JsonResponse в случае неудачи
    else:
        try:
            download_audio(yt) #пробуем скачать аудио в случае удачи
            text = transcribe_audio() #пробуем перевести аудио в текст
        except:
            return Response({"message": "Failed to transcribe audio!"}) #возвращаем в случае неудачи JsonResponse
        else:
            return Response({"message": "Transcribed audio successfully!", "text": text}) #в случае удачного перевода возвращаем переведённый текст