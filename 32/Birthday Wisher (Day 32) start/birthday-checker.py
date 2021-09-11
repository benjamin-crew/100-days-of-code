import datetime as dt
import pandas
import os
from random import choice
import smtplib

PLACEHOLDER = "[NAME]"

def send_mail(email_body, email_addr):

    my_email = "benncrew94@gmail.com"
    my_password = "pplamaepxgdpveuz"
    recipient_email = email_addr
    smtp_server = "smtp.gmail.com"
    smtp_port = 587


    subject = "Happy Birthday!"
    body = f"{email_body}"
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


def generate_letter(name, email):

    letter_choice = choice(os.listdir(path="32/Birthday Wisher (Day 32) start/letter_templates/"))
    letter_path = "32/Birthday Wisher (Day 32) start/letter_templates/" + letter_choice
    
    with open(letter_path) as letter_file:
        letter = letter_file.read()

    body = letter.replace(PLACEHOLDER, name)

    send_mail(body, email)


birthdays = pandas.read_csv("32/Birthday Wisher (Day 32) start/birthdays.csv")


now = dt.datetime.now()
now_month = now.month
now_day = now.day


for index, data in birthdays.iterrows():
    name = data.person
    email = data.email

    month = data.month
    day = data.day
    

    if month == now_month:
        if day == now_day:
            generate_letter(name, email)
