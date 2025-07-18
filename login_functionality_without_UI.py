import re

user_db={
    "ram":"ram123",
    "suri":"12qwe12"
}

username=input("enter the username:")
password=input("enter the password:")

#regex

if re.fullmatch(r'[a-zA-Z]{3,}',username) and re.fullmatch(r'.{6,}',password):
  if username in user_db and user_db[username]==password:
    print("login successfull")
#ask for logout
    logout=input("do you want to logout! (yes/no)")
    if logout.lower()=="yes":
      print("loged out successfully")
    else:
      print("you are still login")
  else:
    print("invalid username or password")
else:
  print("invalid username must be 3  or password must 6")