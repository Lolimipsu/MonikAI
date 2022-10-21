import definitions
import query

def run_monikAI():
    definitions.greeting()
    query = definitions.take_query()
    print(query)

    if 'weather today' or 'weather like today' in query:
        print('step 4 - in main')
        query.get_weather()