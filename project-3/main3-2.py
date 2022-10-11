from gtts import gTTS
from playsound import playsound

text = "안녕하세용. 아메리카노 짱 마쉿당."

tts = gTTS(text=text, lang="ko")
tts.save(r"project-3\textTovoice\hi-2.mp3")
playsound(r"project-3\textTovoice\hi-2.mp3")
