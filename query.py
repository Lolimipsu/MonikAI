from bs4 import BeautifulSoup
import requests
import text_to_speech
import speech_to_text

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def query_search():
    command = speech_to_text.take_query()
    #command = "weather today"
    if 'weather today' or 'weather like today' in command:
        #print("weather good.")
        get_w = get_weather()
        text_to_speech.tts.say("This is today's weather forecast in")
        text_to_speech.tts.say(get_w)
        text_to_speech.tts.runAndWait()
        return

def get_weather():
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
    tts_time = "as of "+ time
    tts_info = "It is expected to have " + info
    tts_weather =  "and it's "+ weather + " degree celcius"
    return tts_location, tts_time, tts_info, tts_weather

#get_weather()

query_search()
