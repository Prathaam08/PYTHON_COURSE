import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Optional: adjust speed

# Optional: set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Try voices[1].id if needed

names = ["Pratham", "John", "Kalpesh", "Sahil"]
for name in names:
    engine.say(f"Shoutout to {name}")

engine.runAndWait()
