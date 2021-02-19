# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:29:36 2021

@author: DELL
"""

import speech_recognition as sr
AUDIO_FILE=("Downloads/Dil_Todi_Na_Song.wav")
#use audio file as the source

r=sr.Recognizer()
#initialise the recogniser

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
    #reads the audio file
    
try:
    print("audio file contains " +r.recognize_google(audio))
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
except sr.RequestError:
    print("Could not get the results from google Speec Recognition")    
