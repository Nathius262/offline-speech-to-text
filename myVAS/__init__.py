import speech_recognition as sr
import pyttsx3 as tts
import urllib
from urllib.request import urlopen
from pynput.keyboard import Key, Controller

r = sr.Recognizer()
keyboard = Controller()


def myVoice():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        listen = r.listen(source)
        audioFile = r.recognize_vosk(listen)
        return audioFile


class SpeechRecognition:
    def __init__(self):
        self.user = 'GCMI MEDIA HUB'
        self.assistant = 'GCMI MEDIA'

    @staticmethod
    def greetings():
        """greetings function"""
        import datetime
        test = SpeechRecognition()
        hour = datetime.datetime.now().hour
        if (hour >= 6) and (hour < 12):
            return f'good morning {test.user} \nhow may I be of assistant sir!'
        elif (hour >= 12) and (hour < 18):
            return f'good afternoon {test.user} \nhow may I be of assistant sir!'
        elif (hour >= 18) and (hour < 21):
            return f'good evening {test.user} \nhow may I be of assistant sir!'
        if (hour > 21) or (hour < 6):
            return f'quite late, you should be sleeping now sir! \nhow may I be of assistant sir!'

    @staticmethod
    def speak(audio_string):
        """sp"""
        engine = tts.init()
        engine.say(audio_string)
        print(audio_string)
        engine.runAndWait()
        engine.stop()
        return audio_string

    @staticmethod
    def is_internet():
        try:
            urlopen('https://www.google.com', timeout=1)
            return True
        except urllib.error.URLError as error:
            return False and error


class KeyboardAction:
    @staticmethod
    def type_my_words(value):
        """using myVoice function to type every speech from the user"""
        if 'enter' in value:
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif 'space' in value:
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif 'back space' in value:
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        else:
            keyboard.type(value)
        return value


srt = SpeechRecognition
obj = srt()

while True:
    word = myVoice()
    if ('hello' or 'hi') in word:
        srt.speak(srt.greetings())
    elif ('how do you do' or 'how are you') in word:
        srt.speak(word)
    elif 'what is your name' in word:
        srt.speak(obj.assistant)
    elif 'internet status' in word:
        if srt.is_internet():
            srt.speak("Active internet")
        else:
            srt.speak("Inactive internet")
    elif 'date' in word:
        import datetime

        date = datetime.datetime.now().date()
        srt.speak(f"today's date is {date}")
    elif 'time' in word:
        import datetime

        time = datetime.datetime.now().strftime('%I:%M')
        srt.speak(f'the time is {time}')
    elif 'today' in word:
        import datetime

        day = datetime.datetime.now().day
        srt.speak(f'today is {day}')
    elif 'open' in word:
        srt.speak('what do you want me to open?')
        word = myVoice()
        if 'speech to' in word:
            srt.speak('speech to text opened')
            keyAction = KeyboardAction
            while True:
                if 'stop' in keyAction.type_my_words(myVoice()):
                    break
                else:
                    print(keyAction.type_my_words(myVoice()))

        else:
            print(word)
            srt.speak("did not get that!")
    elif 'offline' in word:
        srt.speak(f"i'm offline now")
        exit()
    elif 'can you hear me' in word:
        srt.speak(f'yes i can hear you!')
