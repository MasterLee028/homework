from module_admin_up import User
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