import requests
import smtplib
from datetime import datetime

MY_LAT = 53.682968
MY_LNG = -1.499100


def send_email():

    my_email = "benncrew94@gmail.com"
    my_password = "pplamaepxgdpveuz"
    recipient_email = my_email
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    subject = "The ISS is above you!"
    body = f"{subject}"
    msg = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(my_email, my_password)

        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=msg)

    print("Email sent.")


def check_location(longitude, latitude, sunset, sunrise):
    time_now = datetime.now().hour

    # if my latitude -5 is less-than or equal to ISS longitude,
    # and the ISS longitude is less-than or equal to my longtitude +5.
    if MY_LNG - 5 <= longitude <= MY_LNG + 5 and MY_LAT - 5 <= latitude <= MY_LAT + 5:
        if time_now >= sunset or time_now <= sunrise:
            send_email()
        else:
            print("The ISS is near, but it's light outside.")
    else:
        print("The ISS isn't near.")


def get_my_position():

    parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return (sunrise, sunset)


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    return (longitude, latitude)


def main():
    longitude, latitude = get_iss_position()
    sunrise, sunset = get_my_position()
    check_location(longitude, latitude, sunset, sunrise)


if __name__ == "__main__":
    main()
