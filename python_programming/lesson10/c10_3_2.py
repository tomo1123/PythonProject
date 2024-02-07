'''ファイルを添付したメールを送信する'''
from email import message
from email.mime import multipart
from email.mime import text
import smtplib


smtp_host = 'smtp-mail.outlook.com'
smtp_port = 587

from_email = 'test@example.com'
to_email = 'test@example.com'
username = 'test@example.com'
password = 'feiwafjdafjeiwaf'

msg = multipart.MIMEMultipart()
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('Test email', 'plain'))

with open('lesson.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='lesson.txt'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()