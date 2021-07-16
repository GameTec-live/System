import speech_recognition as sr
import pyttsx3
import datetime
import time
import subprocess
import webbrowser

engine = pyttsx3.init()

def tts(text):
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 50
        audio = r.listen(source)

    try:
        print('Recognizing...')
        qry = r.recognize_google(audio, language='de-de')
        print(f"Query: {qry}\n")
        
    except:
        print('Say that again please\n')
        tts('Ich konnte das nicht verstehen!')
        return "None"


    return qry

def activate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Waiting...')
        r.pause_threshold = 1
        r.energy_threshold = 50
        audio = r.listen(source)

    try:
        print('Recognizing...')
        qry = r.recognize_google(audio, language='de-de')
        print(f"Query: {qry}\n")
        
    except:
        print('None\n')
        return "None"
        
    return qry

def command():
    qry = takecommand().lower()
    if 'beenden' in qry:
        tts('Tschüss!')
        exit()
    elif 'hallo' in qry:
        tts('Hallo!')
        command()
    elif 'wie geht es dir' in qry:
        tts('Gut, und Dir?')
    elif  qry == 'hilfe':
        tts('Einen moment!')
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    elif 'wie alt bist du' in qry:
        tts('Ich wurde am 14.7.2021 programmiert.')
    elif 'spät ist es' in qry:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        tts(f"die zeit beträgt {strTime}")
        print(strTime)
    elif 'tag ist heute' in qry:
        strDate = datetime.datetime.now().strftime("%d.%m.%Y")
        tts(f"Es ist der {strDate}")
        print(strDate)
    elif 'mute' in qry or 'stopp' in qry or 'deaktivier' in qry:
        try:
            tts('für wie lange soll ich deaktiviert bleiben? Sag 5')
            tme = int(takecommand())*60
            print(tme)
            time.sleep(tme)
            tts('Ich bin wieder aktiviert')
        except:
            tts('Das hat nicht geklappt!')
    elif 'herunterfahren' in qry:
        tts('in 5 Sekunden wird heruntergefahren!')
        subprocess.call(["shutdown", "/s"])


while True:
    qry = activate().lower()
    if 'system' in qry :
        tts('Ja?')
        print('Ready')
        command()

            
    