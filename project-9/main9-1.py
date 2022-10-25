#영어 문서 한글로 번역
import googletrans

translator = googletrans.Translator()

str1="행복하세요"
#translator.translate(string, dest=번역될문자,src=번역할문자(디폴트 auto))
result1=translator.translate(str1,dest='en',src='auto')
print(f"행복하세요 > {result1.text}")

str2="i am happy"
result2=translator.translate(str1,dest='ko',src='en')
print(f"행복하세요 > {result2.text}")