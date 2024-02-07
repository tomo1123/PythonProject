'''メールを送信する'''
from email import message
import smtplib


smtp_host = 'smtp-mail.outlook.com'
smtp_port = 587

from_email = 'test@example.com'
to_email = 'test@example.com'
username = 'test@example.com'
password = 'feiwafjdafjeiwaf'

msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()