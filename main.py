import query as q
def run_monikAI():
    # TODO fix the one time greeting each open
    # first_run = 0
    # while first_run == 0:
    #     q.greeting()
    #     first_run += 1
    #     if first_run == 1:
    #         break

    command = q.query_input()
    print(command + ' = step 4 - monikAI')
    if 'weather' in command or 'weather today' in command or "today's weather" in command or 'weather like today' in command or "weather for today" in command:
        q.talk("getting today's weather forecast.")
        q.weather_today()

    elif 'play me a song' in command or 'play a song' in command or 'song' in command:
        q.play_music()

    elif 'open browser' in command:
        q.open_site()
    
    else:
        q.talk("Sorry, I didn't hear that very well, could you repeat that again?")

while True:
    run_monikAI()