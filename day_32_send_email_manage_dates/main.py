##################### Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas as pd

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
birthday_dir = BASE_DIR / "birthdays.csv"

my_email =  "rafa.plamdeala@gmail.com"
# recp_email = "jonnydeep2323@outlook.com"
my_password = "qpir kfww ocfi dpku"

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

birthday_df = pd.read_csv(birthday_dir)

birthday_dict = {
    (int(row['month']), int(row['day'])): row.to_dict()
    for _, row in birthday_df.iterrows()
}

now = dt.datetime.now()
current_day = (now.month, now.day)
for key in birthday_dict.keys():
    if current_day == key:
        # Get Email and Name info.
        info_dict = birthday_dict.get(key)
        birthday_name = info_dict.get("name")
        birthday_email = info_dict.get("email")
        print(birthday_name)
        print(birthday_email)
        
        # Composing Email.
        choice = random.randint(1,3)
        try:
            with open(BASE_DIR / f"letter_templates/letter_{choice}.txt", 'r', encoding='utf-8') as f:
                message = f.read()
        except FileNotFoundError:
            message = "Happy Birthday [NAME]!"
            
        message = f"Subject: Happy Birthday {birthday_name}\n\n{message.replace("[NAME]", birthday_name)}"
        print(message)
        
        # Starting connection to send email.
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=message
        )
        connection.close()
    # else:
    #     print("Nobody's birthday...")
    #     now = dt.datetime.now()
    #     year =  now.year
    #     month =  now.month
    #     day =  now.day
    #     print(year, month, day)



#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



