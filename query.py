import speech_recognition as sr
import pyttsx3
import requests
import pywhatkit
from bs4 import BeautifulSoup

# -----------------------------------------------------------------------
# definitions
ai_name = ['hi', 'hey', 'hello', 'monica', 'monika']
listener = sr.Recognizer()

tts = pyttsx3.init()
voice = tts.getProperty('voices')
tts.setProperty('voice', voice[2].id)
# voice speed RATE Can be more than 100
tts.setProperty('rate', 175)
tts.setProperty('volume', 0.8)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


# -----------------------------------------------------------------------
# text to speech
def talk(text):
    print('step 1 - talk')
    tts.say(text)
    tts.runAndWait()

def greeting():
    print('step 1 - greeting')
    tts.say("Hello, I'm Monika. Your Personal AI Companion.")
    tts.say("How can I help you Today?")
    tts.runAndWait()

# -----------------------------------------------------------------------
# speech to text

def query_input():
    try:
        with sr.Microphone() as source:
            print('step 2 - query input')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command
# -----------------------------------------------------------------------
# queries

def weather_today():
    city = "Manila weather"
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    tts_location = location
    tts_time = " as of "+ time
    tts_info = ". It is expected to have " + info
    tts_info_print = "It is expected to have " + info
    tts_weather =  " and it's "+ weather + " degree celcius"
    tts_weather_today = tts_location + tts_time + tts_info + tts_weather
    # TODO This used in the GUI app not backend.
    tts_weather_today_print = tts_location + tts_time + "\n" + tts_info_print + tts_weather

    print("This is today's weather forecast in")
    print(tts_weather_today_print)

    tts.say("This is today's weather forecast in")
    tts.say(tts_weather_today)
    tts.runAndWait()

def play_music():
    print('What song would you like to play?')
    talk('What song would you like to play?')
    command = query_input()
    song = command.replace('play', '')
    print('playing ' + song)
    talk('playing ' + song)
    pywhatkit.playonyt(song)