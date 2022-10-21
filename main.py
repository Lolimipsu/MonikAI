import query
def run_monikAI():
    # TODO fix the one time greeting each open
    # first_run = 0
    # while first_run == 0:
    #     query.greeting()
    #     first_run += 1
    #     if first_run == 1:
    #         break

    command = query.query_input()
    print(command + ' step 4 - monikAI')

    if 'weather today' or 'weather like today' in command:
        query.talk("getting today's weather forecast.")
        query.weather_today()

    elif 'play' or 'song' in command:
        query.play_music()

while True:
    run_monikAI()