import pyttsx3
engine = pyttsx3.init()

input_file = "input.txt"
with open(input_file, "r") as file:
    text = file.read()
if not text:
    print("The file is empty")
else:
    engine.say(text)
    engine.runAndWait()