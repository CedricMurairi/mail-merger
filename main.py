from flask import Flask
from flask_mail import Mail, Message
import csv

app = Flask(__name__)
app.config['MAIL_SERVER']= "smtp.gmail.com"
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USERNAME']= ""
app.config['MAIL_PASSWORD']= ""

mail = Mail(app)

sender = "Cédric Murairi <email>"

message = """
Hello {name}. Good day to you!

Welcome to CODEXTREME Hackathon Season Launch! We're thrilled to have you on board, and we can't wait to embark on this incredible hackathon journey together.

Confirm your attendance by joining our Discord server, where all communications will happen! Connect with fellow hackers, share ideas, and be part of the excitement.

Use this link to join the conversation: https://discord.gg/XXXXXX

Important Information:
- Event Dates: January 24th to 27th, 2024 [In-Person]
- Discord Link: https://discord.gg/XXXXXX
- Schedule: https://codextreme.infinitloop.io/#schedule

If you have any questions or need assistance, our organizing team is ready to assist on Discord. 

Get ready to create and innovate!

Best Regards,
Cédric Murairi
Lead Organizer, CODEXTREME
+250737026499
"""
            
@app.route("/send-mail")
def send_mail():
    with mail.connect() as conn:
        with open("students.csv") as file:
            reader = csv.reader(file)
            next(reader)
            for name, email in reader:
                subject = "Welcome to CODEXTREME Hackathon Season Launch, {}!".format(name)
                msg = Message(subject, sender=sender, recipients=[email], body=message.format(name=name, recipient=email, sender=sender))
                conn.send(msg)
                
    return "Mail sent successfully"
                
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)