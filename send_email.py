import smtplib
import ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'email2221@prova1212.it22'
    password = 'password2323424'
    receiver = 'email2221@prova1212.it22'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)