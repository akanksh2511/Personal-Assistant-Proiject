import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices[0].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Akanksh ")
    elif hour>=12 and hour<18:
        speak("Gooda Afternoon Akanksh ")
    else:
        speak("Good Evening Akanksh ")
    speak("I am jarvis. please tell me how may i help you?")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source) 
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language = "en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say Again Please!")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishme()
    if 1:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences = 2 )
            speak("According to wikipedia")
            speak(results)
        elif'open youtube' in query:
            webbrowser.open("youtube.com")
        elif'open gmail' in query:
            webbrowser.open("gmail.com")
        elif'open google' in query:
            webbrowser.open("google.com")
        elif'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif'open vs code' in query:
            path='C:\\Users\\Akanksh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(path)
        elif 'email to Akanksh' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "yourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Akanksh sir. I am not able to send this email")
        
        


   
    

