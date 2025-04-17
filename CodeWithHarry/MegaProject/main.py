import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()# class which help to recognize 

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if("open google" in c.lower() ):
        webbrowser.open("https://google.com")
    elif("open youtube" in c.lower() ):
        webbrowser.open("https://youtube.com")
    
if __name__ == "__main__" :
    speak("Initilizing Jarvis .......")
    # Listen for the wake word "Gayatri"
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
      
        print("recognizing......")

        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listining ....!")
                audio = r.listen(source , timeout=5 , phrase_time_limit=5)
            word = r.recognize_google(audio)
            print(word)
            if(word).lower() == "alexa":
                speak("yup")
                with sr.Microphone() as source:
                    print("alexa Listining ....!")
                    audio = r.listen(source , timeout=2 , phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    processCommand(command)
            # Listen for command
           
        except Exception as e:
            print("error; {0}".format(e))
            