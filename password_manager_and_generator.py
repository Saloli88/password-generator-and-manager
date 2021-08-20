import random
import json
import sys
lists= ["Strong Password(Contains all the letters,numbers and symbols)","Numbers only","Letters only","Uppercase letters only",
"Lowercase letters only","Symbols only","No uppercase letters","No lowercase letters"]


class Generator(object):
      a = "Random Password Generator"
      s = "-"*30
      def __init__(self,letters):
          self.letters = letters
      def toupper(self):
       return self.letters[0:26].upper()
      def numbers(self):
        return self.letters[52:62]
      def symbols(self):
        return self.letters[62:73]
      def noupper(self):
        return self.letters.lower()
      def nolower(self):
        return self.letters.upper()
      def lettersonly(self):
        return self.letters[0:52]
class UserAction():
  def read():
      with open("passwords.json") as f:
       data = json.load(f)
      print(data)
  def add(generated):
        name = input("Username:")
        person_dict = {
  "records":[
    {name:generated}
  ]
}
        with open ("passwords.json","a") as f:
         json.dump(person_dict,f)
         print("Password has been successfully saved.")
  def delete():
    blank = {"records":[]}
    with open("passwords.json","w") as f:
            json.dump(blank,f)
            print("Records have been deleted successfully.")
  def options():
        while True:
         option = input("Your option(1,2,3):")
         if option == "1":
            UserAction.read()
            break
         elif option == "2":
            UserAction.add(passgen)
            break
         elif option == "3":
            UserAction.delete()
            break
         else:
            print("Please enter a number as stated above")


d = Generator("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?")
print(Generator.a)
print(Generator.s)
for i in range(len(lists)):
    print(f"{i}.{lists[i]}")

 
try:
  choice = int(input("How do you want your password to be:"))
except ValueError as err:
  print("Invalid value\nPlease enter an intenger \n Closing the program...")
  sys.exit()
if choice > 7 or choice < 1:
    print("Invalid value\nPlease enter an intenger \n Closing the program...")
    sys.exit()
try:  
  length = int(input("Length of your password(Max length:10):"))
except ValueError as err:
  print(err)
  print("Invalid value\nPlease enter an intenger \n Closing the program...")
  sys.exit()


while True:

 if choice == 0:
    passgen = "".join(random.sample(d.letters,length))
    print(f"Your password: {passgen}")
    break
 elif choice == 1:
    passgen = "".join(random.sample(d.numbers(),length))
    print(f"Your password: {passgen}")
    break
 elif choice == 2:
     passgen = "".join(random.sample(d.lettersonly(),length))
     print(f"Your password: {passgen}")
     break
 elif choice == 3:
    passgen = "".join(random.sample(d.toupper(),length))
    print(f"Your password: {passgen}")
    break
 elif choice == 4:
     passgen = "".join(random.sample(d.toupper().lower(),length))
     print(f"Your password: {passgen}")
     break
 elif choice == 5:
     passgen = "".join(random.sample(d.symbols(),length))
     print(f"Your password: {passgen}")
     break
 elif choice == 6:
     passgen = "".join(random.sample(d.noupper(),length))
     print(f"Your password: {passgen}")
     break
 elif choice == 7:
     passgen = "".join(random.sample(d.nolower(),length))
     print(f"Your password: {passgen}")
     break
 elif choice > 7 or choice <1 or length > 10 or length<1:
    print("Please enter a number as stated above \n Closing the program...")
    sys.exit()


while True:
  question = input("Open the password manager?(y,Y/n,N):")
  if question == "y" or question =="Y":
    print("1-Show the records \n2-Store your password \n3-Delete the records")
    UserAction.options()
    break
  elif question == "n" or question == "N":
    print("Closing the program...")
    break
  else:
    print("please enter as stated above")
    continue
