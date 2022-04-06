import os

to_do_list=[]

def to_do():
  to_do_action= ''
  while to_do_action != 'done':
    print(to_do_list)
    to_do_action= input("What would you like to do with your to-do list? Add or remove items? (type 'add' or 'remove') \n If finished, type 'done'. ")
    os.system("clear")
    if to_do_action == "add":
      added_subject = ''
      while added_subject != "done":
        print(to_do_list)
        added_subject = input("What subject would you like to add to your to-do list? \nIf finished adding items to your to-do list then type (done) ")
        os.system('clear')
        to_do_list.append(added_subject)
      del to_do_list[-1]
    elif to_do_action == "remove":
      removed_subject= ''
      while removed_subject!= 'done':
        print(to_do_list)
        removed_subject = input("What subject would you like to remove? \n(Type as appears in list). Type 'done' when done. ")
        os.system('clear')
        if removed_subject != 'done':
          to_do_list.remove(removed_subject)
  print("Your to-do list is as follows: "+ str(to_do_list))
  return to_do_list