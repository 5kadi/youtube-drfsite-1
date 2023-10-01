import os
import whisper
from langdetect import detect
from pytube import YouTube
from youtubedrfsite.settings import MEDIA_ROOT

def create_youtube_link(link: str) -> YouTube:
    """Создаёт и возвращает объект YouTube с соответствующей ссылкой"""
    return YouTube(link)

def download_audio(youtube_object: YouTube) -> None:
    """Скачивает новое аудио на место audio.mp3"""
    audio_stream = youtube_object.streams.filter(only_audio=True).first()
    output_path = MEDIA_ROOT + "YoutubeAudios"
    filename = "audio.mp3"
    audio_stream.download(output_path=output_path, filename=filename)

def transcribe_audio() -> str:
    """Переводит речь аудио в текст и возвращает его"""
    model = whisper.load_model("base")
    result = model.transcribe(MEDIA_ROOT + "YoutubeAudios/audio.mp3")
    transcribed_text = result["text"]
    return transcribed_text
