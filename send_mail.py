import smtplib
from email.message import EmailMessage

sender = "mirahmadhacker2007@gmail.com"
password = 'izxgokfocivpgvdk'
server = "smtp.gmail.com"
port = 465
text = "Zohidov Mirahmad 4-module imtihoni github: https://github.com/MzMPrO/4-module_exam.git"
msg = EmailMessage()
msg["From"] = sender
msg["To"] = 'solihazohidova090909@gmail.com'
msg["Subject"] = text
with smtplib.SMTP_SSL(server, port) as server:
    server.login(sender, password)
    server.send_message(msg)
    print("Send message")