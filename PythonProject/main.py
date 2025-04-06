import pyttsx3

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1. Created by me")

while True:
        x = input("What do you want me to speak: ")
        if x=="bye":
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
