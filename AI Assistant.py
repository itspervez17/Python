# Voice Talking AI Robot Similar to Amazon Alexa

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def execute_command(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif 'open' in command:
        website = command.split('open')[-1].strip()
        webbrowser.open(f"https://{website}")
        speak(f"Opening {website}.")
    elif 'play music' in command:
        os.startfile("path_to_your_music_file")  # Replace with your music file path
        speak("Playing music.")
    else:
        speak("I am not programmed to perform that action.")

def main():
    speak("Hello, I am your AI assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
