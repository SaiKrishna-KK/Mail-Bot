# Mail-Bot

This script uses the `speech_recognition` and `pyttsx3` libraries to convert voice commands into text and then sends an email using the `smtplib` and `email` libraries.

## Prerequisites

- `Python 3.7+`
- `speech_recognition` library (`pip install SpeechRecognition`)
- `pyttsx3` library (`pip install pyttsx3`)

## Setup

1. Clone the repository
2. Install the required libraries
3. Set up your Gmail account credentials as environment variables in your terminal:
   - `export DEVMAIL_ADDRESS=your_email_address`
   - `export DEVMAIL_PASSWORD=your_email_password`

## How to Use

1. Run the script using `python mail-bot.py`
2. The script will prompt you to say the name of the person you want to send an email to, followed by the subject and body of the email.
3. After you have dictated the email information, the script will send the email and ask if you want to send more emails.
4. If you say "yes," the script will prompt you for another email recipient and repeat the process.
5. If you say "no," the script will exit.

## Notes

- The email addresses and associated names are stored in the `email_list` dictionary at the top of the script.
- If you are not using a Gmail account, you will need to change the `server` and `EMAIL_ADDRESS` variables in the `send_email` function to match your email provider.
