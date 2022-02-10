import pyttsx3
import speech_recognition as sr
from datetime import datetime
from datetime import date 
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit 
import requests
import json
import datetime
import pyautogui
 engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


#mails = [User1, User2, User3, User4] 

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

"""def speaktelecast(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 125)"""

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("Hello sir, I am olympus, please tell how may I help you..")

def takecommand():
    #it takes microphone input from the user and returns string output
  
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("Listening...")
       r.pause_threshold = 1
       audio = r.listen(source)

   try:
       print("Recognizing...")
       query = r.recognize_google(audio, language='en-in')
       print(f"User said: {query}\n")

   except Exception as e:
       #print(e)
       print("Say that again please...")
       speak("Say that again please...")
       return "None"
   return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sendmail@gmail.com', 'password')
    server.sendmail('sendmail@gmail.com', to, content)
    server.close()

def aiself():
    speak("I'm olympus, a well designed AI.. I perform many tasks and save your precious time")
def health():
    speak("I am Much better now that you are with me. Assuming you’re at your best too.")

def screenshot():
    speak("Ok, what should be the name of screenshot?")
    name = takecommand()
    screenshot_olympus = name + ".png"
    path = "D:\\" + screenshot_olympus
    scrnsht = pyautogui.screenshot()
    scrnsht.save(path)
    os.startfile("D:\\") #path
    speak("Your screenshot have been taken!")
    
def chromeautomation():
    speak("What do you want to open in chrome")
    chromecommand = takecommand()
    if "close this tab" in chromecommand:
        pyautogui.press('ctrl + w') 
    if "open new tab" in chromecommand:
        pyautogui.press('ctrl + t')
    if "new window" in chromecommand:
        pyautogui.press('ctrl + n')
    if "incognito" or "private" in chromecommand:
        pyautogui.press('alt + shift + n') 
        speak("Now what should I search?")
        srch = takecommand().lower()
        webbrowser.open(f"{srch}")

 
if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takecommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")  
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'who are you' in query:
            aiself()
        elif 'how are you' in query:
            health()
        
        
        elif 'open youtube' in query:
            speak("Opening youtube...")
            webbrowser.open("youtube.com")

#logic for playing song from youtube...
        elif 'song' in query:
            try:
                speak("Which song do you wanna play?")
                songserach = takecommand().lower()
                pywhatkit.playonyt(songserach)
                print("Playing...")
            except Exception as e:
                print(e)
                speak("Sorry, due to some technical error I was unable to play this song, you can try once more")
                
        elif 'play' in query:
            finalsongsearch = query.replace("play","")
            pywhatkit.playonyt(finalsongsearch)
            speak(f"Your song {finalsongsearch} is being played")


        
        elif 'open google' in query:
            speak("What should I search on google?")
            usersearch = takecommand().lower()
            webbrowser.open(f"{usersearch}")
        
        elif 'open facebook' in query:
            speak("Opening facebook...")
            webbrowser.open("facebook.com")

        elif 'open notepad' in query:
           speak("Opening notepad...")
           cmd = 'notepad'
           os.system(cmd) 

        elif 'email' in query:
           try:
#to command:
               speak("To whom should I send?")
               to = takecommand().lower()

               if ‘User1’ in to:
                   to = "user1@gmail.com"
               if ‘user2’ in to:
                   to = "user2@gmail.com"
               if 'user3' in to:
                   to = "user3@gmail.com"
               if 'user4' in to:
                   to = "user4@gmail.com"
#body command:              
               speak("What should I say?")
               content = takecommand()
               
               sendEmail(to, content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("Sorry, due to some technical error I was unable to send this mail, you can try again once more")
               
 #sms       
        elif "sms" in query:
            try:
                speak("Sir,to whom do you want to text?")
                tox = takecommand().lower()
                if 'user1' in tox:
                    tox = '+9-----------'
                if 'user2' in tox:
                    tox = '+9-----------'
                if ‘user3’ in tox:
                    tox = '+9-----------'
                if 'user4' in tox:
                    tox = '+9-----------
                speak("Sir what should I say?")
                msg = takecommand()

                from twilio.rest import Client

                account_sid = 'ACC_SID'
                auth_token = 'AUTH_TOKEN'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                        body=msg,
                        from_='+1----------',
                        to=tox
                    )
                print(message.sid)
                speak("sir, message has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry, due to some technical error I was unable to send this sms, you can try again once more")

#whatsapp mssg
            
        elif "whatsapp" in query:
             try:
                current_time = datetime.datetime.now() 
                
                speak("To whom do you wanna text on whatsapp?")
                tox = takecommand().lower()
                if 'user1' in tox:
                    tox = '+9-----------
                if 'user2' in tox:
                    tox = '+9-----------
                if 'user3' in tox:
                    tox = '+9-----------
                if 'user4' in tox:
                    tox = '+9-----------
                speak("Sir what do you wanna say?")
                mssg = takecommand()
                speak("Sir in two minutes your message will be whatsapped...")
                pywhatkit.sendwhatmsg(tox,mssg,current_time.hour,current_time.minute + 3)
                pyautogui.click(1328, 693)
                speak("Sir message have been delivered on whatsapp...")
                pyautogui.click(1328, 693)
            except Exception as e:
                print(e)
                speak("Sorry, due to some technical error I was unable to whatsapp your message, you can try again once more")

                
#phonecall
            
        elif "call" in query:
            speak("Sir,to whom do you want to call?")
            tox = takecommand().lower()
            if 'user1' in tox:
                tox = '+9-----------
            if 'user2' in tox:
                tox = '+9-----------
            if 'user3' in tox:
                tox = '+9-----------
            if 'usre4' in tox:
                tox = '+9-----------
            if 'user5' in tox:
                tox = '+9-----------
            if 'usre6' in tox:
                tox = '+9-----------
            from twilio.rest import Client
            account_sid = 'ACC_SID'
            auth_token = 'AUTH_TOKEN
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                                    twiml='<Response><Say>This is a test call...</Say></Response>',
                                    to=tox,
                                    from_='+1----------'
                                )

            print(call.sid)
            speak("Sir in few seconds your call will be made..")

#Logic for news reading...
        elif "news" in query:
            speak("Sure sir, the breaking news are as follows... news first")
            news = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=API_KEY')
            data = json.loads(news.content)
            for i in range(10):
                 headline = data['articles'][i]['description']
                 engine.setProperty('rate', 150)
                 engine.say(headline)
                 engine.runAndWait()
                 speak(f"News {i+2}")

#weather
        elif "weather" in query:
            user_api = 'API'
            location = "faizabad"

            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            #create variables to store and display data
            temp_city = ((api_data['main']['temp']) - 273.15)

            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            date_time = datetime.datetime.now().strftime("%I:%M %p")
            
            print ("-------------------------------------------------------------")
            print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
            print ("-------------------------------------------------------------")

            forspeaktemp = "{:.2f}".format(temp_city)
            print ("Current temperature is: {:.2f} deg C".format(temp_city))
            print ("Current weather desc  :",weather_desc)
            print ("Current Humidity      :",hmdt, '%')
            print ("Current wind speed    :",wind_spd ,'kmph')
            
            speak(f"It is {date_time} right now, currently the temprature of {location} is {forspeaktemp} degree celsius")
            speak(f"the amount of water vapur present in the atmosphere is {hmdt} percent")
            speak(f"the wind is blowing with {wind_spd} kilometer per hour and overall the weather description is {weather_desc}")
        
        elif "time" in query:
            date_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir currently the time is {date_time}")
        elif "date" in query:
            todays_date = date.today()
            print("Current date: ", todays_date)
            speak(f"today's date is {todays_date}")
        elif "screenshot" in query:
            screenshot()
        elif 'who is' in query:
            import wikipedia as googlescrap
            finalwhosearch = query.replace("who is","")
            pywhatkit.search(finalwhosearch)
            whoresult= googlescrap.summary(finalwhosearch)
            speak(whoresult)
               
        elif "where i am" in query:
            speak("Sure sir, wait for a second!")
            try:
                ipadd = requests.get('https://api.ipify.org').text
                print(ipadd)
                urladd = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_requests = requests.get(urladd)
                geo_data = geo_requests.json()
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                print(f"Sir I think we are in city of {city}  in {country}")
                speak(f"Sir I think we are in city of {city}  in {country}")
            except:
                speak("Sir due to technical error, I'm unable to resolve your location!")
        elif 'break' in query:
           speak("I'm much grateful that I was able to help you, thanks for the break, you can call back me anytime sir")
           break
        else:
            import wikipedia as googlescrap
            pywhatkit.search(query)

            try:
                resultx = googlescrap.summary(query)
                speak(resultx)

            except:
                speak("Sorry sir I'm unable to give answer to you!")
---------------------------------------------------------------------------###########################################___________________________________________
