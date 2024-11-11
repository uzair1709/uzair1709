from gtts import gTTS
import os

text="welcome back to my new vlog kehse hein ab sab lon "

language='en'
uzair=gTTS(text=text,lang=language,slow=False)
uzair.save("practice.mp3")