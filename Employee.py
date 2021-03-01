class Employee():
    def __init__(self,f_name,l_name,money):
        self.f_name = f_name
        self.l_name = l_name
        self.money = money
    def give_raise(self,r_money=0):
        if r_money:
            return self.money+r_money
        else:
            return self.money+5000