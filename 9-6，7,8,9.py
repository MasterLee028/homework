#9-6
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The name is: "+self.restaurant_name.title())
        print("The type is: "+self.cuisine_type.title())
    def open_restaurant(self):
        print("The restaurant is opening!")
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
     super().__init__(restaurant_name,cuisine_type)
     self.flavors = ['apple','banana','pear','peach']
    def show_icecream(self):
        for flavor in self.flavors:
            print(flavor)
icecream = IceCreamStand('happy','butter') #初始化
icecream.show_icecream()
#9-7
class User():
    def __init__(self,first_name,last_name,age,e_mail):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.e_mail = e_mail
    def describe_user(self):
        print("The name is: "+self.first_name.title()+" "+self.last_name.title()+".")
        print("The age is: "+self.age)
        print("The E_mail is: "+self.e_mail)
    def great_user(self):
        print("Thank you for this search!")
class Admin(User):
    def __init__(self,first_name,last_name,age,e_mail):
        super().__init__(first_name,last_name,age,e_mail)
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        print("The adminer has following rights:")
        for privilege in self.privileges:
            print(privilege)
admin = Admin('lee','tim','18','123@qq.com')
admin.show_privileges()
#9-8
class User():
    def __init__(self,first_name,last_name,age,e_mail):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.e_mail = e_mail
    def describe_user(self):
        print("The name is: "+self.first_name.title()+" "+self.last_name.title()+".")
        print("The age is: "+self.age)
        print("The E_mail is: "+self.e_mail)
    def great_user(self):
        print("Thank you for this search!")
class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        print("The adminer has following rights:")
        for privilege in self.privileges:
            print(privilege)
class Admin(User):
    def __init__(self,first_name,last_name,age,e_mail):
        super().__init__(first_name,last_name,age,e_mail)
        self.privileges = Privileges()
admin = Admin('lee','tom','20','456@qq.com')
admin.privileges.show_privileges()
#9-9
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self,mileage):
        print("This car has "+str(self.odometer_reading)+"mile on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
        else:
         print("You can not roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size ==85:
            range =270
        message = "This car can go approximately "+str(range)
        message += "miles on a full charge"
        print(message)
    def describe_battery(self):
        print("This car has a "+str(self.battery)+"-kwh battery.")
    def upgreade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
class ElectricCar(Car):
    def __init__(self,make,model,year):
       super().__init__(make,model,year)
       self.battery = Battery()
my_car = ElectricCar('tesla','model s','2020')
my_car.battery.get_range()
my_car.battery.upgreade_battery()
my_car.battery.get_range()






