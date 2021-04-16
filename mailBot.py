import os
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

EMAIL_ADDRESS = os.environ.get("DEVMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("DEVMAIL_PASSWORD")


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_voiceInfo():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(reciever, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    email = EmailMessage()
    email['From'] = EMAIL_ADDRESS
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(body)
    server.send_message(email)

    #msg = f"Subject : {subject}\n\n{body}"
    #server.sendmail('dev.bluedruid@gmail.com', reciever, msg)
    print('Hey Email Has Been Sent')
    server.quit()


email_list = {"xyz": "xyz@gmail.com", "abc": "abc@gmail.com",
              "abs": "abs@gmail.com"}


def get_email_info():
    talk('To whom you want to send your email!')
    name = get_voiceInfo()
    reciver = email_list[name]
    print(reciver)
    talk('What is the subject of your email?')
    subject = get_voiceInfo()
    talk('Tell me the body of the email?')
    body = get_voiceInfo()
    send_email(reciver, subject, body)
    talk('Ok! I have sent the mail.')
    talk("Hey! Do you want to send more emails?")
    send_more = get_voiceInfo()
    if 'yes' in send_more:
        get_email_info()

    else:
        talk("Ok lasy a**! Bye.")


get_email_info()
