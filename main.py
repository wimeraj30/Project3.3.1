from replit import db

start = input('New user: (N)\nReturning user: (R)\n')
if start == 'N':
  nusr = input("Username: ")
  npsw = input("Password: ")
  db[str(nusr)] = nusr, npsw
elif start == 'R':
  rusr = input("Username: ")
  rpsw = input("Password: ")
  if rusr in db.keys():
    if rpsw in db[rusr]:
      print("Logged in")
