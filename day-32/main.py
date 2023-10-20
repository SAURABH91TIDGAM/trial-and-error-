import datetime as dt
import smtplib
import random

MY_EMAIL = "saurabh1991Tidgam@gmail.com"
MY_PASSWORD = "pfwuzmcfoybatwam"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="saurabhtidgam1991@gmail.com",
                            msg=f"subject:Monday Motivation\n\n{quote}")