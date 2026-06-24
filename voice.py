import pyttsx3
import re

def clean_text(text):

    # Remove ALL asterisks
    text = text.replace("*", "")

    # Remove hashtags
    text = text.replace("#", "")

    # Remove backticks
    text = text.replace("`", "")

    return text

def speak(text):

    text = clean_text(text)

    engine = pyttsx3.init()

    engine.setProperty("rate", 130)   # speaking Speed

    engine.say(text)

    engine.runAndWait()

    engine.stop()