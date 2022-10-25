import speech_recognition as sr
import pyttsx3
import requests
import pywhatkit
import webbrowser
from bs4 import BeautifulSoup
from ShazamAPI import Shazam
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

headers = {
    'Accept' : '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }


# -----------------------------------------------------------------------
# text to speech
def talk(text):
    print('< OUT: def talk')
    tts.say(text)
    tts.runAndWait()

def greeting():
    print('< OUT: greeting')
    tts.say("Hello, I'm Monika. Your Personal AI Companion.")
    tts.say("How can I help you Today?")
    tts.runAndWait()

# -----------------------------------------------------------------------
# speech to text

def query_input():
    try:
        with sr.Microphone() as source:
            print('> INPUT: query input')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'monika' in command or 'monica' in command:
                command = command.replace('monika','monica','')
                print('> INPUT:' + command)
    except:
        pass
    return command
# -----------------------------------------------------------------------
# queries

def weather_today():
    print('For which city?')
    talk('For which city?')
    command = query_input()
    print('> INPUT:' + command + ' IN: weather_today')

    talk("getting today's weather forecast.")
    print("getting today's weather forecast...")

    city = command + " weather"
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
    print('> INPUT: ' + command + ' IN play_music')
    song = command.replace('play', '')
    print('playing ' + song)
    talk('playing ' + song)
    pywhatkit.playonyt(song)

def open_site():
    print('What would you like to do in browser?')
    talk('What would you like to do in browser?')
    command = query_input()
    #command = command.replace(" ", "")
    print('> INPUT: '+ command + ' IN open_site')
    if 'open' in command or 'use' in command:
        for word in ['open', 'use']:
            command = command.replace(word, "")

    search = command
    url = 'https://www.google.com/search'
    parameters = {'q': search}
    content = requests.get(url, headers = headers, params = parameters).text
    soup = BeautifulSoup(content, 'html.parser')
    search = soup.find(id = 'search')
    first_link = search.find('a')
    print("Opening: " + first_link['href'])
    talk('Opening ' + command)
    webbrowser.open(first_link['href'])

def find_song():
    print('> OUT: listening...')
    print('listening...')
    #TODO add text here that says in the gui "listening..."
    command = query_input()
    mp3_file_content_to_recognize = open('a.mp3', 'rb').read()

    shazam = Shazam(mp3_file_content_to_recognize)
    recognize_generator = shazam.recognizeSong()
    while True:
        print(next(recognize_generator)) # current offset & shazam response to recognize requests
