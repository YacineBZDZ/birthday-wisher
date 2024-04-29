##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random

file = "birthdays.csv"
# for information you can chose any provider (outlook, gmail, yahoo) just don't forget to change the SMTP host in line 40
my_email = "put_the_eamil_that_sends_the_message_here@gmail.com"
password = "your_emails_password"


# 1. Update the birthdays.csv
birthdays = pd.read_csv(file)
birthdays_list = birthdays.to_dict(orient="records")
birthdays.to_csv(file, index= False)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_year = now.today().year
today_month = now.today().month
today_day = now.today().day

birthday_data = birthdays[(birthdays.month == today_month) & (birthdays.day == today_day)]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def create_letter():
    letters_lists = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # chose_letter = random.choice(letters_lists)
    with open(letters_lists, mode="r") as file_letter :
        letter = file_letter.read()
        name = birthday_data["name"].iloc[0]
        new_letter = letter.replace("[NAME]", f"{name}")
        return new_letter

# 4. Send the letter generated in step 3 to that person's email address.
try:
    with smtplib.SMTP("smtp.gmail.com" , port=587 ) as connection:
            email = birthday_data["email"].iloc[0]
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Happy Birthday\n\n{create_letter()}"
             )
except IndexError:
    print("There is no Birthdays on this day")


