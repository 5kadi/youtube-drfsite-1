import os
import whisper
from langdetect import detect
from pytube import YouTube
from youtubedrfsite.settings import MEDIA_ROOT
from .models import TranscribedText
from rest_framework.response import Response

def enhash_link(link: str) -> hash:
    """Хэширует ссылку"""
    return hash(link)

def delete_audio(link: str) -> None:
    """Удаляет аудиофайл по хэшу"""
    os.remove(MEDIA_ROOT + f"YoutubeAudios/audio_{enhash_link(link)}.mp3")

def create_youtube_link(link: str) -> YouTube:
    """Создаёт и возвращает объект YouTube с соответствующей ссылкой"""
    return YouTube(link)

def download_audio(link: str, youtube_object: YouTube) -> None:
    """Скачивает новое аудио на место audio.mp3"""
    audio_stream = youtube_object.streams.filter(only_audio=True).first()
    output_path = MEDIA_ROOT + "YoutubeAudios"
    filename = f"audio_{enhash_link(link)}.mp3"
    audio_stream.download(output_path=output_path, filename=filename)

def transcribe_audio(link: str) -> str:
    """Переводит речь аудио в текст и возвращает его"""
    model = whisper.load_model("base")
    result = model.transcribe(MEDIA_ROOT + f"YoutubeAudios/audio_{enhash_link(link)}.mp3")
    transcribed_text = result["text"]
    delete_audio(link)
    return transcribed_text

def check_link(link: str) -> bool:
    """Проверяет ссылку на наличие в бд"""
    try:
        obj = TranscribedText.objects.get(link=link)
    except:
        return False
    else: 
        return True
    


