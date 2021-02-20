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