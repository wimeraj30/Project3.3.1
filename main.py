import time
import datetime
to_do_list=[]
finished= []
added_subject= ""
subject_finsihed = ""

while added_subject != "done":
  added_subject = input("What subject would you like to add to your to-do list? \nIf finished adding items to your to-do list then type (done) ")
  to_do_list.append(added_subject)
del to_do_list[-1]
print("You have entered these subjects to study \n", to_do_list)


def countdown(h,m,s, item):
  total_seconds = h * 3600  + m * 60 +s
  while total_seconds > 0:
    timer = datetime.timedelta(seconds= total_seconds)
    print(timer, end = "\r")
    time.sleep(1)
    total_seconds -=1
  print("Time is up for "+ item+ ". ")


for item in to_do_list:
  print("You should now set time for "+ item+ ".")
  hours = int(input("How many hours would you like to work on "+ item +"? "))
  minutes = int(input("How many minutes would you like to work on "+ item+ "? "))
  seconds = int(input("How many seconds would you like to work on "+ item+"? "))
  print("Time left for "+ item+ ":")
  countdown(int(hours), int(minutes), int(seconds), item)


for item in to_do_list:
  more_time = ''
  while more_time != 'no':
    subject_finished = input("Have you finished "+item+ "? (yes or no) ")
    if subject_finished == 'yes':
      finished.append(item)
      more_time = 'no'
    if subject_finished == 'no':
      more_time = input("Would you like to spend more time working on "+ item+ "? (yes or no) ")
      if more_time =='yes':
        hours = int(input("How many hours would you like to work on "+ item +"? "))
        minutes = int(input("How many minutes would you like to work on "+ item+ "? "))
        seconds = int(input("How many seconds would you like to work on "+ item+"? "))
        print("Time left for "+ item+ ": ")
        countdown(int(hours), int(minutes), int(seconds), item)


for item in finished:
  if item in to_do_list:
    to_do_list.remove(item)
