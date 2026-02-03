import smtplib
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent


my_email =  "rafa.plamdeala@gmail.com"
recp_email = "jonnydeep2323@outlook.com"
my_password = "qpir kfww ocfi dpku"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls() # Encryption of the email.
# connection.login(my_email, password=my_password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs=recp_email,
#     msg="Subject:Hello\n\nThis is the body of email."
# )
# connection.close()

import datetime as dt
import random

# now = dt.datetime.now()
# year =  now.year
# month =  now.month
# day =  now.day
# day_of_the_week = now.weekday()
# print(now)

# date_of_birth = dt.datetime(year=1995 ,month=12 ,day=30, hour=23) # the required objects are year, month and day.
# print(date_of_birth)


def choose_motivation_quote():
    with open(BASE_DIR / "quotes.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return random.choice(lines)

def is_monday():
    # return true
    now = dt.datetime.now()
    day_of_the_week = now.weekday()
    if day_of_the_week == 0:
        return True
    return False

def send_motivation_quote():
    if is_monday():
        quote = choose_motivation_quote()
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls() # Encryption of the email.
        connection.login(my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recp_email,
            msg=f"Subject:Motivational Quote \n\n {quote}."
        )
        connection.close()
    else:
        print("Not Monday, so theres no quote.")
    

def main():
    send_motivation_quote()

if __name__ == "__main__":
    main()