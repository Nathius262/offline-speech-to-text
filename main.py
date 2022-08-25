from myVAS import SpeechRecognition

srt = SpeechRecognition
name = srt()
user_name = name.user
greetings = srt.greetings()
speak = srt.speak

while True:
    word = srt.myVoice()
    if ('hello' or 'hi') in word:
        srt.speak
    elif ('how do you do' or 'how are you') in word:
        srt.speak
    elif 'what is your name' in word:
        srt.speak
    elif 'internet status' in word:
        if srt.is_internet():
            srt.speak
        else:
            srt.speak
    elif 'date' in word:
        import datetime

        date = datetime.datetime.now().date()
        srt.speak
    elif 'time' in word:
        import datetime

        time = datetime.datetime.now().strftime('%I:%M')
        srt.speak
    elif 'today' in word:
        import datetime

        day = datetime.datetime.now().day
        srt.speak
    elif 'open' in word:
        srt.speak
        word = word
        if 'speech to' in word:
            srt.speak
            pass
        else:
            print(word)
            srt.speak
    elif 'stop' in word:
        srt.speak
        exit()
    else:
        srt.speak
