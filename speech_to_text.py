from multiprocessing.connection import Listener
import speech_recognition as sr

ai_name = ['hi', 'hey', 'monica', 'monika']

listener = sr.Recognizer()
def take_query():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'monica' or 'monika' or 'hey monika' or 'hey monica' in command:
                for word in ai_name:
                    command = command.replace(word, "")
        print(command)
    except:
        print("Error on listening")
        pass

    return command