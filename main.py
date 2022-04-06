from replit import db
import os
import time
import todo
import schedule
to_do_list= []


def login():
  start = input('New user: (N)\nReturning user: (R)\n')
  if start == 'N' or start == 'n':
    nusr = input("Username: ")
    npsw = input("Password: ")
    db[str(nusr)] = nusr, npsw
    print("Account Created")
    time.sleep(1)
    os.system("clear")
    mainmenu(to_do_list)
  elif start == 'R' or start == 'r':
    rusr = input("Username: ")
    rpsw = input("Password: ")
    if rusr in db.keys():
      if rpsw in db[rusr]:
        print("Logged in")
        time.sleep(1)
        os.system("clear")
        mainmenu(to_do_list)
      else:
        print("Wrong Password")
        rpsw = input("Password: ")
        if rpsw in db[rusr]:
          print("Logged in")
          time.sleep(1)
          os.system("clear")
          mainmenu(to_do_list)
        else:
          print("Wrong Password")
          time.sleep(2)
          os.system("clear")
          login()
    else:
      print("Invalid Username.")
      time.sleep(2)
      os.system("clear")
      login()


def mainmenu(to_do_list):
  choice = input('* * * * * * * * * * * * * * * *\n'
               '*                             *\n'
               '*   Welcome!                  *\n'
               '*                             *\n'
               '*   Please select an option   *\n'
               '*   from the choices below    *\n'
               '*                             *\n'
               "*   ('T') To-do list          *\n"
               "*   ('S') Schedule            *\n"
               "*   ('L') Logout              *\n"
               '*                             *\n'
               '* * * * * * * * * * * * * * * *\n')
  if choice == 'T' or choice == 't':
    os.system("clear")
    print("To do list")
    to_do_list = todo.to_do()
    os.system('clear')
    mainmenu(to_do_list)
  if choice == 'S' or choice == 's':
    os.system("clear")
    print("Schedule")
    to_do_list = schedule.settime(to_do_list)
    mainmenu(to_do_list)
  if choice == 'L' or choice == 'l':
    os.system("clear")
    login()
  


login()


