import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

smtp_server = "smtp.mail.ru"
smtp_port = 587

login_email = "sssss@bk.ru"
password_email = "zzzzzzz"

rec_email = "zzzzz@bk.ru"

subject = "Тема письма JavaRush"
body = "Lesson JavaRush"


message = MIMEMultipart()
message["Subject"] = subject
message["From"] = login_email
message["To"] = rec_email

html_body = '<h1>Тема письма</h1><p>Lesson JavaRush</p>'
message.attach(MIMEText(html_body, "html"))


try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(login_email, password_email)
    server.sendmail(login_email, rec_email, message.as_string())
    print('Всё отправили')
except Exception as e:
    print(e)
finally:
    server.quit()

