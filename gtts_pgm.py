from gtts import gTTS
import os

g=gTTS(text="Hello Deveopers Welcome to OneTeam",lang="en")
g.save("Welcome_note.mp3")
os.system("start Welcome_note.mp3") 