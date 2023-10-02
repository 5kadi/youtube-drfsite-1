from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import *
from .models import TranscribedText


@api_view(["POST"])
def convertAPIView(request) -> Response:
    """Конвертирует аудио по POST запросу"""
    link = request.data['link'] #получаем указанную в запросе ссылку (json)
    if check_link(link): #если ссылка уже есть в бд, то сразу выводим его
        text = TranscribedText.objects.get(link=link).text
        return Response({"message": "Transcribed audio successfully!", "text": text})
    try:
        yt = create_youtube_link(link) #пробуем создать объект YouTube
    except:
        return Response({"message": "Couldn't find this link!"}) #выводим JsonResponse в случае неудачи
    else:
        try:
            download_audio(link, yt) #пробуем скачать аудио в случае удачи
            text = transcribe_audio(link) #пробуем перевести аудио в текст
        except:
            return Response({"message": "Failed to transcribe audio!"}) #возвращаем в случае неудачи JsonResponse
        else: 
            TranscribedText.objects.create(link=link, text=text) #заносим объект в бд
            return Response({"message": "Transcribed audio successfully!", "text": text}) #в случае удачного перевода возвращаем переведённый текст