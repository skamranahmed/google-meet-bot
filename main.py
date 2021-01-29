import time
import datetime
import os

from class_schedule import class_schedule
from bot import GoogleMeetBot

gmail_id = os.getenv('GMAIL_ID')
password = os.getenv('PASSWORD')

def join_class(teacher_name, class_duration_in_secs):
    class_meeting_link = class_schedule[teacher_name]
    class_bot = GoogleMeetBot(class_meeting_link)
    class_bot.google_login(gmail_id, password)
    class_bot.join_meeting()
    print(f"Joined {teacher_name}'s class")
    time.sleep(class_duration_in_secs)
    class_bot.leave_meeting()
    print(f"Left {teacher_name}'s class")
    del class_bot

current_time = datetime.datetime.now().strftime('%H:%M %p')

#  if all your classes end up by 14:00 PM you can stop the while loop after that
while current_time < '14:00 PM':
    current_time = datetime.datetime.now().strftime('%H:%M %p')

    #  Teacher 1 class time is 10:30 PM
    #  keeping 2 min window for joining the class
    if ('10:30 PM' <= current_time < '10:32 PM'):
        #  after joining the class, stay there for 200 secs
        join_class('teacher_1', 200)

    #  Teacher 2 class time is 11:30 AM
    #  keeping 2 min window for joining the class
    if ('11:30 PM' <= current_time < '11:32 PM'):
        #  after joining the class, stay there for 2400 secs i.e 40 mins
        join_class('teacher_2', 2400)