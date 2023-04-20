import query as q

# -----------------------------------------------------------------------
# definitions
# USE DOUBLE QUOTATION (NO '_' only "_")
weather_prompt = ["weather", "weather today", "today's weather", "weather like today", "weather for today", "weather forecast"]
play_song_prompt = ["play me a song", "play a song"]
open_browser_prompt = ["open browser"]
find_song_prompt = ["what song is this", "find this song", "name of song", "name of this song"]


def contains_command(command_list, command):
    return any(item in command for item in command_list)

# -----------------------------------------------------------------------

# q.greeting()

def run_monikAI():

    command = q.query_input()
    print("> INPUT: " + command + ' \tIN monikAI main.py')
    if contains_command(weather_prompt, command):
        q.weather_today()

    elif contains_command(play_song_prompt, command) : #or 'song' in command
        q.play_music()

    elif contains_command(open_browser_prompt, command):
        q.open_site()

    elif contains_command(find_song_prompt, command):
        q.find_song()
    
    else:
        q.talk("Sorry, I did not hear that very well, could you repeat that again?")
        print("< OUT: Sorry, I did not hear that very well, could you repeat that again?")

while True:
    run_monikAI()