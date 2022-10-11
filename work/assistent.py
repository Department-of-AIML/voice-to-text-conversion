import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib


listener = sr.Recognizer()
engine = pyttsx3.init()
engine. setProperty("rate", 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'apple' in command:
                command = command.replace('apple', '')
                print(command)
    except:
        pass
        return command


def run_apple():
    command = take_command()
    print(command)
if 'play' in command:
        song =command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
elif 'joke' in command:
         talk(pyjokes.get_joke())
elif 'date' in command:
        x = datetime.datetime.now()
        print(x)
        talk(x)
elif 'mail' in command:
        s = smtplib.SMTP('smtp.gmail.com',587)
        
        sender_mail_id = "vsnshipra08@gmail.com"
        password = ''
        mail_id_list = {"m":"1dt20ai037@dsatm.edu.com",
                        "b":"anubhav.sanket4@gamil.com"}
        talk('whom do you want me to send a mail?')
        receiver_mail_id = print(command)
        
        s.starttls()
        s.login(sender_mail_id, password)
        talk("what is the message?")
        message = take_command()
        s.sendmail(sender_mail_id,receiver_mail_id,message)
        talk("sending mail...")
        s.quit
        talk("mail sent succesfully!")
        
else:
        talk('Please say the command again.')


while True:
 run_apple()
