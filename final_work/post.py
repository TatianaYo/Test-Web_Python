import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail():
    message = MIMEMultipart()
    message['From'] = 'yoienko@mail.ru'
    message['To'] = 'yoienko@mail.ru'
    message['Subject'] = 'Test report'
    mypass = 'kqNE2GThgmxs590sUtEt'

    text = 'Test result'
    message.attach(MIMEText(text))

    with open('log.txt', 'rb') as f:
        attachment = MIMEApplication(f.read(), Name='log.txt')

    message.attach(attachment)

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(message['From'], mypass)
    text = message.as_string()
    server.sendmail(message['From'], message['To'], text)
    server.quit()