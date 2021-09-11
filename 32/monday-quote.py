import smtplib
import datetime as dt
import pandas
from random import choice

def send_mail(quote):

    my_email = "benncrew94@gmail.com"
    my_password = "pplamaepxgdpveuz"
    recipient_email = "benncrew94@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587


    subject = "Mondays Inspirational Quote"
    body = f"{quote}"
    msg = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(my_email, my_password)

        connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg=msg
        )

    print("Email sent.")

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 5:

    with open("32/Birthday Wisher (Day 32) start/quotes.txt") as quote_file:
        choice = choice(quote_file.readlines())
        
    send_mail(choice)
