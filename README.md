youtube-drfsite-1 (API)

порядок установки (в venv):
pip install Django
pip install djangorestframework
pip install pytube
pip install git+https://github.com/openai/whisper.git
pip install langdetect

также необходимо установить ffmpeg. гайд по установке: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/

краткое пояснение концепта API:
с фронтенда посылается POST запрос такого типа: {"link": "(ссылка)"}. на стороне API ищется видео с такой ссылкой и его аудио преобразуется в текст. в зависимости от успеха операции выводится JsonResponse.
в каждом JsonResponse есть параметр message с сообщением об успехе или провале операции и в случае полного успеха выводится также и параметр text с текстом, полученным из аудио

вся API работает достаточно медленно, но можно в теории ускорить при помощи асинхронки, но это пока что не ко мне Xd


