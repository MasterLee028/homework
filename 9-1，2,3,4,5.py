#9-1
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The name is: "+self.restaurant_name.title())
        print("The type is: "+self.cuisine_type.title())
    def open_restaurant(self):
        print("The restaurant is opening!")
restaurant = Restaurant('happy','sheep')
restaurant.describe_restaurant()
restaurant.open_restaurant()
#9-2
east_restaurant = Restaurant('sad','pork')
east_restaurant.describe_restaurant()
east_restaurant.open_restaurant()
west_reataurant = Restaurant('pleasure','fruit')
west_reataurant.describe_restaurant()
west_reataurant.open_restaurant()
#9-3
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
user_0 = User('lee','tom','29','123@qq.com')
user_0.describe_user()
user_0.great_user()
user_1 = User('harris','joe','30','456@qq.com')
user_1.describe_user()
user_1.great_user()
user_2 = User('james','harden','31','789@qq.com')
user_2.describe_user()
user_2.great_user()
#9-4
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("The name is: "+self.restaurant_name.title())
        print("The type is: "+self.cuisine_type.title())
    def open_restaurant(self):
        print("The restaurant is opening!")
    def increament_number_served(self,number):
        if number >= 0:
         self.number_served += number
        else:
         print("You can not change the number!")
restaurant = Restaurant('happy','food')
print("There are "+str(restaurant.number_served)+" people come to eat.")
restaurant.number_served = 45
print("There are "+str(restaurant.number_served)+" people come to eat.")
restaurant.increament_number_served(39)
print("There are "+str(restaurant.number_served)+" people come to eat.")
#9-5
class User():
    def __init__(self,first_name,last_name,age,e_mail,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.e_mail = e_mail
        self.login_attempts = login_attempts
    def describe_user(self):
        print("The name is: "+self.first_name.title()+" "+self.last_name.title()+".")
        print("The age is: "+self.age)
        print("The E_mail is: "+self.e_mail)
    def great_user(self):
        print("Thank you for this search!")
    def increnment_login_attempts(self):
        self.login_attempts += 1
        print("The number is "+str(self.login_attempts))
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("The number has been reset")
        print("\nThe number is "+str(self.login_attempts))

user_3 = User('lee','tim','20','123@qq.com',1)
user_3.increnment_login_attempts()
user_3.increnment_login_attempts()
user_3.increnment_login_attempts()
user_3.reset_login_attempts()

