import pyttsx3  #This is for Speak #pip install pyttsx3 
import speech_recognition as sr   # This will take voices #pip install speechRecognition
import datetime  
import wikipedia # pip install wikipedia
import webbrowser
import os # for music in out operating system
import smtplib #To send gmail 

engine = pyttsx3.init('sapi5')  # sapi5 is used to take inbuilt voice
voice = engine.getProperty('voices')
# print(voice)  
# print(voice[0].id) this will print David
# print(voice[1].id) this will print Zira

engine.setProperty('voice',voice[0].id) # setting the voice 
# 0 is for male voice i.e. David
# 1 is for female voice i.e. ZIRA

def speak(audio):  # audio is argument
    engine.say(audio)  #Egnine will speak audio
    engine.runAndWait()  #This will run the audio 

def wishMe():
    hour = int(datetime.datetime.now().hour)  #This will typecase hour into int and Jarvis will wish me according to the time.
    if hour >= 0 and hour <12:
        speak("Good morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak(" I am Jarvis sir. Speed 1 Terabyte . How may i help you !!! ")


def takeCommand():
# It takes microphone input from the user and returns string output
   
    r = sr.Recognizer()  # Recognize class will help us to recognize the audio 
    with sr.Microphone() as source:  
        print("Listening...")
        r.energy_threshold = 100  # The more the value , The high pitch you need to speak in microphone
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete 
        # 1 second of gap will be there while speaking a sentence through microphone
        audio = r.listen(source) #This will record

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language= 'en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None" # this is a string
   
    return query

def sendEmail(to,content):

# we need to enable less secure app in our google account otherwise it will not work

    server = smtplib.SMTP('smtp.gmail.com',587)  #
    server.ehlo()
    server.starttls()
    server.login('aishwarsharma09@gmail.com','07860919')
    server.sendmail('aishwarsharma09@gmail.com',to,content)
    server.close()

if __name__ == "__main__":   # This is our main function 
    wishMe()
    
    while True:
        query = takeCommand().lower()  # converted to lower string

    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","") # wikipedia will be replaced by blank
            results = wikipedia.summary(query,sentences =2)  # sentences depends upon user.
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))  # this will play first song
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to sharma' in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "aishwarsharma09@gmail.com"
                sendEmail(to , content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry my friend aishwar . I am not able to send this email at this moment ...")