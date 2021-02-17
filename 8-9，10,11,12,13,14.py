#8-9
magicians=['tom','edward','master','lee']
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
show_magicians(magicians)
#8-10
magicians=['tom','edward','master','lee']
great_magicians=[]
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_magicinans(magicians):
    while magicians:
        current_magician="the Great"+" "+magicians.pop().title()
        great_magicians.append(current_magician)
make_magicinans(magicians)
show_magicians(great_magicians)
#8-11
magicians=['tom','edward','master','lee']
make_magicinans(magicians[:])
show_magicians(great_magicians)
show_magicians(magicians)
#8-12
def show_toppings(*toppings):
    for topping in toppings:
        print("The following toppings: "+topping.title())
show_toppings('apple')
show_toppings('banana','pear')
show_toppings('pork','meat','sandwich')
#8-13
def build_profile(first,last,**user_infor):
    profile={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_infor.items():
        profile[key] = value
    return profile
user_profile=build_profile('lee','tong',city='cheng du',food='noodles',sports='basketball')
print(user_profile)
#8-14
def car_infor(maker,brand,**user_pick):
    infor={}
    infor['maker'] = maker
    infor['brand'] = brand
    for key,value in user_pick.items():
        infor[key] = value
    return infor
car=car_infor('shang qi','bmw',color='blue',tow_package='True')
print(car)

