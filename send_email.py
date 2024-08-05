import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"

    port = 465

    password = "eupzlweafsmdkwbv"

    username = "adityakendre1000@gmail.com"

    reciever = "adityakendre1000@gmail.com"

    mcontext = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = mcontext) as server:
        server.login(username,password)
        server.sendmail(username,reciever,message)