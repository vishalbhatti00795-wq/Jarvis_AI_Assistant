from voice import speak
from brain import ask_gemini
from commands import execute

print("Jarvis Started")
speak("Hi Vishal. I am Jarvis.")

speak('Testing Speakers')

while True:

    user = input("You: ")

    if user.lower() == "exit":
        speak("Goodbye Vishal")
        break

    result = execute(user)
    if result:
        print("COMMAND RESULT:", result)
        speak(result)

    else:
        answer = ask_gemini(user)

        print("GEMINI RESPONSE:")
        print(answer)

        speak(answer)