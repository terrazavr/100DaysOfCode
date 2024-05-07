import datetime as dt
import pandas
import random
import smtplib


MY_EMAIL = "your-email@gmail.com"
PASSWORD = "app_password_from_google"

# Creating today date in tuple (month, day)
now = dt.datetime.today()
today = (now.month, now.day)

# Creating dictionary from csv with key - (month, day)
b_days = pandas.read_csv("birthdays.csv")
birthdays_dict = {(info_row.month, info_row.day): info_row for (index, info_row) in b_days.iterrows()}

# Checking if today is someone's birthday
if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    persons_birthday = birthdays_dict[today]
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", persons_birthday["name"])

    # Sending email with congrats
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=persons_birthday["email"],
                            msg=f"Subject: Happy birthday!\n\n{letter}")
