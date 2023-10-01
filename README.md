<h1>youtube-drfsite-1 (API)</h1>

порядок установки (в venv):
<ul>
  <li>pip install Django</li>
  <li>pip install djangorestframework</li>
  <li>pip install pytube</li>
  <li>pip install git+https://github.com/openai/whisper.git</li>
  <li>pip install langdetect</li>
</ul>


<p>также необходимо установить ffmpeg. 
гайд по установке: </p>
<ul>
  <li>https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/</li>
</ul>

краткое пояснение концепта API:
<ul>
  <li>с фронтенда посылается POST запрос такого типа: {"link": "(ссылка)"}.</li>
  <li>на стороне API ищется видео с такой ссылкой и его аудио преобразуется в текст. </li>
  <li>в зависимости от успеха операции выводится JsonResponse.</li>
  <li>в каждом JsonResponse есть параметр message с сообщением об успехе или провале операции и в случае полного успеха выводится также и параметр text с текстом, полученным из аудио</li>
</ul>
 


<p>вся API работает достаточно медленно, но можно в теории ускорить при помощи асинхронки, но это пока что не ко мне Xd</p>


