import json
numbers = [2,3,4,5,6,7]
filename = 'numbers.json'
with open('filename','w')as f_obj:
    json.dump(numbers,f_obj)
#10-11
import json
number = input("what is your favorite number? ")
filename_1 = 'number.json'
with open('filename_1','w')as f_1_obj:
    json.dump(number,f_1_obj)
with open('filename_1')as f_11_obj:
    numb = json.load(f_11_obj)
    print("My favorite number is "+numb+"!")
#10-12
import json
filename_2 = 'my_number.json'
try:
    with open(filename_2)as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    number = input("what is your favorite number? ")
    with open(filename_2,'w')as f_obj:
        json.dump(number,f_obj)
        print("We have remember your number!")
else:
    print("My favorite number is "+number+"!")
#10-13
import json
def get_stored_username():
  filename = 'username.json'
  try:
      with open(filename) as f_obj:
          username = json.load(f_obj)
  except FileNotFoundError:
   return None
  else:
      return username
def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back ,"+username+"!")
    else:
        username = get_new_user()
        print("We'll remember you when you come back !")
def get_new_user():
    username = input("what is your name? ")
    filename = 'username.json'
    with open(filename,'w')as f_obj:
        json.dump(username,f_obj)
    return username
with open('filename')as f_obj:
    json.load(f_obj)
creative = input("Does this name is your name? ")
if creative == 'no':
    get_new_user()
else:
 greet_user()

