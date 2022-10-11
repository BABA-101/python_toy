# gtts 라이브러리 안에 gTTS 기능만 불러와서 사용.
from gtts import gTTS

text = "안녕하세요. 아메리카노 맛있당."
tts = gTTS(text=text, lang="ko")
tts.save(r"project-3\textTovoice\hi.mp3")
