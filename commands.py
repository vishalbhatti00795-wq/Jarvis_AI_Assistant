import os
import webbrowser
import datetime
import pyautogui

def execute(command):

    command = command.lower()

    if "chrome" in command:
        os.startfile(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )

    elif "youtube" in command:
        webbrowser.open("https://youtube.com")

    elif "google" in command:
        webbrowser.open("https://google.com")

    elif "time" in command:
        return str(datetime.datetime.now().strftime("%H:%M"))

    elif "screenshot" in command:

        image = pyautogui.screenshot()

        image.save("screenshots/shot.png")

        return "Screenshot taken"

    return None