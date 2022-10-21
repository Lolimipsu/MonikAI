import pyttsx3
from multiprocessing.connection import Listener
import speech_recognition as sr


# -----------------------------------------------------------------------------

# text to speech
tts = pyttsx3.init()
voice = tts.getProperty('voices')
tts.setProperty('voice', voice[2].id)

# voice speed Can be more than 100
tts.setProperty('rate', 175)
tts.setProperty('volume', 0.8)

def greeting():
    print('step 1')
    tts.say("Hello, I'm Monika. Your Personal AI Companion.")
    tts.say("How can I help you Today?")
    tts.runAndWait()

def talk(text):
    tts.say(text)
    tts.runAndWait()

# -----------------------------------------------------------------------------
# speech to text

ai_name = ['hi', 'hey', 'monica', 'monika']
listener = sr.Recognizer()

def take_query():
    try:
        with sr.Microphone() as source:
            print('listening...')
            print('step 2')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'monica' or 'monika' or 'hey monika' or 'hey monica' in command:
                for word in ai_name:
                    command = command.replace(word, "")
        print(command)
    except:
        pass
    return command