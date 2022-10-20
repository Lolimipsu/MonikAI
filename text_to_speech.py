import pyttsx3
#import speech_to_text

tts = pyttsx3.init()
voice = tts.getProperty('voices')
tts.setProperty('voice', voice[2].id)

# voice speed Can be more than 100
tts.setProperty('rate', 175)
tts.setProperty('volume', 0.8)

def greeting():
    tts.say("Hello, I'm Monika. Your Personal AI Companion.")
    tts.say("How can I help you Today?")
    tts.runAndWait()

def talk(text):
    tts.say(text)
    tts.runAndWait()
