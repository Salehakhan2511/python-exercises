#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HADI
#
# Created:     09/04/2025
# Copyright:   (c) HADI 2025
# Licence:     <your licence>
#----------------------------------------------------------------------------

import pyttsx3

print("Welcome to RoboSpeaker...")
while True:
    to_speak = input("Enter what you want me to speak (or type q to quit): ")
    if to_speak == 'q':
        print("Goodbye...")
        break
    engine = pyttsx3.init()
    engine.say(to_speak)
    engine.runAndWait()