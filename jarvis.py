import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import time
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.uic import loadUiType
from jarvisUI import Ui_jarvisUI
from requests import get
import wikipedia
import webbrowser
# import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import requests
import twitterbot as tb
import playsound


MASTER="ROHAN J BILLAVA"
engine = pyttsx3.init('sapi5') #audio driver sapi5
voices =engine.getProperty('voices')
engine.setProperty(voices,voices[0].id)

#text to speech


def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("here you go sir i have  changed my voice ")

def femalevoice():
    voice_change(1)

def malevoice():
    voice_change(0)

def speak(audio):
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1.0)
    # engine.setProperty('pitch', 32)
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def personal():
    speak(
        "Now its time to introduce myself, I am jarvis , a virtual artificial intelligence and i am her to assist you to a variety of task since best i can , 24 hours a day , 7days a week, importing all  preference  from home interface , system is now fully operational"
    )
#to wish me
def wishme():
    hour = int(datetime.datetime.now().hour)#to exteact time
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning "+MASTER+f" its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon "+MASTER+f" its {tt}")
    else:
        speak(f"good evening "+MASTER+f" its {tt}")

    # if hour >= 0 and hour < 12:
    #     speak("Good Morning " + MASTER)
    
    # elif hour >= 12 and hour < 18:
    #     speak("Good Afternoon " + MASTER)

    # else:
    #     speak("Good Evening " + MASTER)

    speak("I am jarvis sir. please tell me How may I help you")

#for news updates
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6dca7181504f468789ff4c3181779cc2'

    main_page = requests.get(main_url).json()
    # print(main_page)
    article = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in article:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

# class MainThread(QThread):
#     def __init__(self, parent):
#         super().__init__(MainThread,self).__init()
    
#     def run(self):
#         self.TaskExecution
    #to convert voice into text

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def  takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 1
            audio = r.listen(source,phrase_time_limit=8)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query


    def TaskExecution(self):
        # os.startfile("C:\\Users\\Rohan J Billava\\Downloads\\power up.mp3")
        playsound.playsound("C:\\Users\\Rohan J Billava\\Downloads\\power up.mp3")
        playsound.playsound("C:\\Users\\Rohan J Billava\\Downloads\\Jarvis.mp3")
        
        wishme()
        while True:
            self.query = self.takecommand().lower()

            #logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
            elif 'hi' in self.query or 'hello' in self.query:
                speak('Hello sir, how may I help you?')
            
            # elif "open adobe reader" in self.query:
            #     apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            #     os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            
            elif ("tell me about yourself" in self.query):
                    personal()
            
            elif ("who are you" in self.query):
                    personal()
            
            elif ("yourself" in self.query):
                    personal()
            
            elif 'full form of jarvis' in self.query:
                    speak ('Just A Rather Very Intelligent System')

            elif "play music" in self.query:
                music_dir = "C:\\Users\\Rohan J Billava\\Music"
                songs = os.listdir(music_dir)
                flag=True
                # rd = random.choice(songs)
                # if rd.endswith('.mp3'):
                # os.startfile(os.path.join(music_dir, rd))
                # for song in songs:
                #     if song.endswith('.mp3'):
                #         os.startfile(os.path.join(music_dir, song))
                for song in songs:
                    if ((song.endswith('.mp3')) and (flag)):
                        os.startfile(os.path.join(music_dir, song))
                        flag=False
            
            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")
            
            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to wikipedia")
                speak(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")
            
            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")
            # elif "send whatsapp message" in self.query:
            #     kit.sendwhatmsg("+91_To_number_you_want_to_send", "this is testing protocol",4,13)
            #     time.sleep(120)
            #     speak("message has been sent")

            # elif "song on youtube" in self.query:
            #     kit.playonyt("Hymn for the weekend")

            elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("For how many minutes?")
                timing = self.takecommand()
                timing =timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')

                time.sleep(timing)
                speak('Your time has been finished sir')
            
            #to close any application
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            #to close any application
            elif "close chrome" in self.query:
                speak("okay sir, closing chrome")
                os.system("taskkill /f /im chrome.exe")
            
            elif "close browser" in self.query:
                speak("okay sir, closing chrome")
                os.system("taskkill /f /im msedge.exe")

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "twitter" in self.query:
                speak("opening twitter,sir what should i tweet? ")
                bgh =self.takecommand().lower()
                tb.callthebot(bgh)

                    

            elif "news" in self.query:
                speak("please wait sir, feteching the latest news")
                news()

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
            # elif "no thanks" in self.query:
            #     speak("Executing shutdown protocol.thanks for using me sir, have a good day.")
            #     playsound.playsound("C:\\Users\\Rohan J Billava\\Downloads\\power down.mp3")
            #     sys.exit()

            # elif "bye" in self.query:
                # speak("Executing shutdown protocol,thanks for using me sir, have a good day.")
                # playsound.playsound("C:\\Users\\Rohan J Billava\\Downloads\\power down.mp3")
                # sys.exit()
            
            elif ("voice" in self.query):
                    if 'female' in self.query:
                        femalevoice()

                    else:
                        malevoice()
        
                # speak("Sir,do you have any other work")

startExcecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_jarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.Close)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("C:\\Users\\Rohan J Billava\\Desktop\\myjarvis\\images/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie=QtGui.QMovie("C:\\Users\\Rohan J Billava\\Desktop\\myjarvis\\images/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExcecution.start()

    def Close(self):
        speak("Executing shutdown protocol,thanks for using me sir, have a good day.")
        playsound.playsound("C:\\Users\\Rohan J Billava\\Downloads\\power down.mp3")
        self.close()

    def showTime(self):
        currentTime=QTime.currentTime()
        currentDate=QDate.currentDate()
        label_time=currentTime.toString('hh:mm:ss')
        label_date=currentDate.toString(Qt.ISODate)
        self.ui.textBrowser_3.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())
