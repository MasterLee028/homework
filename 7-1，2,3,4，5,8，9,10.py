#7-1
car = input("Please tell me what car do you want to rent: ")
print("\n"+car.title())
#7-2
number = input("how many people come to eat? ")
number = int(number)
if number >8:
    print("There is no empty seats!")
else:
    print("We have enough seat!")
#7-3
number = input("Please enter a number: ")
number = int(number)
if number%10 == 0:
    print("This number can be divided!")
else:
    print("This number can not be divided!")
#7-4
ingredient = input("Please enter what ingredient do you want eat? ")
active = True
while True:
    food = input(ingredient)
    if food == 'quit':
        break
    else:
        print("We will add this ingredient to your order!")
#7-5
age = input("how old are you? ")
age = int(age)
active = True
while True:
    if age<3:
        print("The charge is free!")
        break
    elif age <12:
        print("The charge is 10$!")
        break
    else:
        print("The charge is 15$!")
        break
#7-8
sandwich_orders = ['pork','vegetable','fruit']
finished_sandwiches = []
while sandwich_orders:
    making_sandwiches=sandwich_orders.pop()
    print("I will make "+making_sandwiches.title()+" for you!")
    finished_sandwiches.append(making_sandwiches)
print("____ the following sandwiches____")
print(finished_sandwiches)
#7-9
sandwich_orders = ['pork','vegetable','fruit','pastrami','pastrami','pastrami']
print("The pastrami has been sold out!")
while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    else:
        break
print(sandwich_orders)
#7-10
searchs={}
active = True
while active:
    name = input("What's your name? ")
    search = input("If you could visit one place in the world,where would you go? ")
    searchs[name] = search
    reapt = input("would you want to share another place?(Yes/No) ")
    if reapt.lower() == 'no':
       active = False
for name,search in searchs.items():
    print(name.title()+" want to go "+search.title()+".")







