import smtplib
import datetime as dt
#
# my_email = "saurabh1991Tidgam@gmail.com"
# password = "pfwuzmcfoybatwam"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="saurabhtidgam1991@gmail.com",
#         msg="Subject:hello\n\nThis is the body of my email")

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)
# print(now)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines
