# import external package 
# i am installing text to speech library
# to convert text to speech
# pip install pyttsx3
import pyttsx3
import pyjoke
engine = pyttsx3.init()
joke = pyjoke.get_joke()
engine.say(joke)
print(joke)
engine.runAndWait()
# engine.say("Hello, this is a text-to-speech conversion using Python.")
# engine.runAndWait()


