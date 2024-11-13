import pyttsx3
import speech_recognition 
import webbrowser
from datetime import datetime
import os
import time
import requests
from dotenv import load_dotenv
from newsapi import NewsApiClient
import google.generativeai as genai

#Loading Environment Varriables from .env file
load_dotenv()

#Configure AI Model
def Configure_AI_MODEL():
    GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

    model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    return model
#Artificial Intelligence Function to do any task
def Artificial_Intelligence(text):
    model=Configure_AI_MODEL()
    response = model.generate_content(text)


#Artificial Intelligence Function to chat
def Artificial_Intelligence_chat(text):
    model=Configure_AI_MODEL()
    chat = model.start_chat(history=[])
    response = chat.send_message(text)
    say(response.text.replace("*"," "))

#Speak Function(Uses pyttsx3 module)
def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

#Speech Recognition fucntion(Uses speech_recognition module)
def take_command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en_in")
            print(f"User say:{query}")
            return query
        except Exception:
            return "Some Error Occured.Sorry From Veronica"

if __name__ == '__main__':
    say("Greetings Sir! This is Veronica. How may I help you?")
    while True:
        print("Veronica Listening.....")
        query = take_command()
        
        if "open" in query.lower():
            #Opening Applications 
            applications=[["Chrome",r"C:\Users\Public\Desktop\Google Chrome.lnk"],["Firefox",r"C:\Users\Public\Desktop\Firefox.lnk"],["VLC media Player",r"C:\Users\Public\Desktop\VLC media player.lnk"],["Vs Code",r"C:\Users\indra\Desktop\Visual Studio Code.lnk"],["OBS Studio",r"C:\Users\Public\Desktop\OBS Studio.lnk"]]

            for apps in applications:
                if f"Open {apps[0]}".lower() in query.lower():
                    say(f"Opening {apps[0]}")
                    os.startfile(apps[1])

            #Opening Any Site
            sites=[["YouTube","https://www.youtube.com/"],["Linkedin","https://www.linkedin.com/feed/"],["Google","https://www.google.com/"],["Facebook","https://www.facebook.com/"],["Instagram","https://www.instagram.com/"],["Whatsapp","https://web.whatsapp.com/"]]

            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]}")
                    webbrowser.open(site[1])
        
        #Current Time
        elif "the time".lower() in query.lower():
            time =datetime.now().strftime("%I:%M %p")
            say(f"Sir.The  time is {time}")
        
        #Current Date
        elif "the date".lower() in query.lower():
            date=datetime.now().strftime("%A, %B %d, %Y")
            say(f"Sir.The Date is{date}")
        
        #Weather Function
        elif "the weather".lower()  in query.lower():
            say("Which City Sir:")
            print("Veronica Listening....")
            city=take_command()
            key=os.getenv("WEATHER_API_KEY")
            url=f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no"
            response = requests.get(url).json()
            say(f"Sir the temprature of {city} is {response['current']['temp_c']} degree centigrade or {response['current']['temp_f']} degree farenhite")

        #News Function
        elif "the news".lower() in query.lower():
            key=os.getenv("NEWS_API_KEY")
            newsapi = NewsApiClient(api_key=key)
            say("What News You want to search Sir!")
            print("Veronica Listening....")
            news=take_command()
            all_articles = newsapi.get_everything(q=f'{news}',language='en',sort_by='relevancy',page=2)
            articles=(all_articles['articles'])
            say("Plz have a look at the Output Window sir:")
            for i in range(len(articles)):
                print(f"Title: {articles[i]['title']}\n")
                print(f"Description: {articles[i]['description']}\n")

        else:
            Artificial_Intelligence_chat(query)







        
        
            
            


    