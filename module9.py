class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The name is: "+self.restaurant_name.title())
        print("The type is: "+self.cuisine_type.title())
    def open_restaurant(self):
        print("The restaurant is opening!")