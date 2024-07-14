import pyttsx3
import random

tlk= ['hello world', 'im ur bot.', 'nothing here', 
        'what u want', 
        'speek slowly', 'jara jara', 
        'tan batan',
        'sar foo mee', 'mosam ashaa haa']
par1= pyttsx3.init()

voices= par1.getProperty('voices')
par1.setProperty('voice', voices[1].id)
for i in range(1, 10):
    tlk1= random.choice(tlk)
    par1.say(tlk1)
    par1.runAndWait()
