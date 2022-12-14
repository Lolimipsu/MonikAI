import speech_recognition as sr
import pyttsx3
import requests
import pywhatkit
import webbrowser
import urllib.request
from bs4 import BeautifulSoup

## finding song
# shazam requirements
import asyncio
from shazamio import Shazam, Serialize

# translating the song to romanized version
from googletrans import Translator

# recording audio
import pyaudio
import wave

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
    
    #TODO add text here that says in the gui "listening..."
    
    # #recording the audio
    # chunk = 1024
    # sample_format = pyaudio.paInt16
    # channels = 1
    # fs = 44100
    # seconds = 16
    # filename = "find_this_song.mp3"

    # p = pyaudio.PyAudio()
    # print('> OUT: listening to song...')
    # print('listening...')

    # stream = p.open(format=sample_format,
    #                 channels=channels,
    #                 rate=fs,
    #                 frames_per_buffer=chunk,
    #                 input=True)

    # frames = [] 

    # for i in range(0, int(fs / chunk * seconds)):
    #     data = stream.read(chunk)
    #     frames.append(data)

    # stream.stop_stream()
    # stream.close()
    # p.terminate()

    # print('> OUT: recording stopped. finding the song...')
    # print('finding the song...')

    # # Save the recorded data as a WAV file
    # wf = wave.open(filename, 'wb')
    # wf.setnchannels(channels)
    # wf.setsampwidth(p.get_sample_size(sample_format))
    # wf.setframerate(fs)
    # wf.writeframes(b''.join(frames))
    # wf.close()

    # jump to finding_the_song
    finding_the_song()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(finding_the_song())

# Finding song
# TODO improve the romanization support
async def finding_the_song():
    shazam = Shazam()
    out = await shazam.recognize_song('find_this_song.mp3')
    result = Serialize.full_track(out)
    print(result.track.title)
    print(result.track.subtitle)

    translator = Translator()
    translated_to_en = translator.translate(result.track.title,  dest='en', src='auto')
    song_title_romanized = translated_to_en.pronunciation
    print(translated_to_en.pronunciation)

    # for the text to speech
    song_title_final = song_title_romanized + " by " + result.track.subtitle

    # for the query
    song_title_final_query = result.track.title + " - " + result.track.subtitle

    print('The song name is: ' + song_title_final)
    talk('The song name is: ' + song_title_final)

    print('Would you like me to play the song?')
    talk('Would you like me to play the song?')

    command = query_input()
    #command = command.replace(" ", "")
    print('> INPUT: '+ command + ' IN finding_song')
    if 'yes' in command or 'yeah' in command or 'yep' in command or 'sure' in command:
        print('Ok, playing ' + song_title_final)
        talk('Ok, playing ' + song_title_final)
        pywhatkit.playonyt(song_title_final_query)
    elif 'no' in command or 'nah' in command or 'nope' in command:
        print('Ok, let me know if you need anything.')
        talk('Ok, let me know if you need anything.')