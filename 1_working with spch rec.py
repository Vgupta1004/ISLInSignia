import speech_recognition as sr   #imports package SpeechRecogniton
import webbrowser  as wb          #imports package webbrowser
import pyaudio as py              #imprts package pyaudio

#creating three instances of class Recognizer

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("[search edureka: search youtube]")
    print('speak now')
    audio = r1.listen(source)
    
#making a query

if 'edureka' in r2.recognize_google(audio):
    
    url = 'https://www.edureka.co/'
    with sr.Microphone() as source:
        print('search your query')
        audio = r2.listen(source)
        
        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))
            
else:
    print("Not correct input")
        