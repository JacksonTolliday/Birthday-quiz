"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name

todaymonth = datetime.today().month
today = datetime.today().day
monthcheck = month_name[todaymonth]

name = input("Hello, what is your name? ")
month = input("Hi " + name + ", what was the name of the month you were born in? ")
year = int(input("And what year were you born in, " + name + "? "))
day = int(input("And the day? "))

monthlist = ['December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']
winter = monthlist[:3]
spring = monthlist[3:6]
summer = monthlist[6:9]
fall = monthlist[9:]

seasonprint = '0'

if month in winter:
    seasonprint = 'winter'
elif month in spring:
    seasonprint = 'spring'
elif month in summer:
    seasonprint = 'summer'
elif month in fall:
    seasonprint = 'two thousands'
else:
    seasonprint = '0'

yearprint = "0"

if year < 1980:
    yearprint = 'Stone Age'
elif year >= 1980:
    if year <= 1989:
        yearprint = 'eighties'
    elif year >= 1990:
        if year <= 1999:
            yearprint = 'nineties'
        else: # the only combination left is two thousands
            yearprint = 'two thousands'


if month == "October" and day == 31:
    print("You were born on Halloween!")
elif month == monthcheck and day == today:
    print('Happy birthday!')
else:
    print("" + str(name) + ", you are a " + str(seasonprint) + " baby of the " + str(yearprint) + ".")