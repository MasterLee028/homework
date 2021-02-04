#4-1
pizzas=['apple','peach','banana','orange']
for pizza in pizzas:
    print("I like "+pizza.title()+"\tpizza!\n")
    print(pizza)
print("I really like pizza!")
#4-2
animals=['lions','tigers','foxes','monkey']
for animal in animals:
    print(animal)
    print("A "+animal.title()+" would make a great pet! ")
print("Any of these animals would make great pet!")
#4-3
#方法一
naturals=[value+1 for value in range(0,21)]
print(naturals)
#方法二
naturals=[]
for value in range(0,21):
    natural=value+1
    naturals.append(natural)
print(naturals)
#方法三
natueals=list(range(1,21))
print(naturals)
#4-4,4-5
natural=[value+1 for value in range(0,1000000)]
print(natural)
print(min(natural))
print(max(natural))
print(sum(natural))
#4-6
numbers=list(range(1,21,2))
for value in numbers:
    print(value)
#4-7
numbers=list(range(3,31,3))
for value in numbers:
    print(value)
#4-8
numbers=[]
for value in range(1,11):
    values=value**3
    numbers.append(values)
print(numbers)
#4-9
numbers=[value**3 for value in range(1,11)]
print(numbers)
#4-10
pizzas=['apple','peach','banana','orange','meat','sheep']
f_pizza=pizzas[:3]
print("My first three items in the list are: ")
print(f_pizza)
o_pizza=pizzas[1:4]
print("Three items from the middle of the list are: ")
print(o_pizza)
l_pizza=pizzas[-3:]
print("The last three items in list are: ")
print(l_pizza)
#4-11
pizzas=['apple','peach','banana','orange']
friend_pizza=pizzas[:]
pizzas.append('meat')
friend_pizza.append('sheep')
for pizza in pizzas:
    print("My favorite pizzas are: "+pizza.title())
for friend_pizza in friend_pizza:
    print("My friend favorite pizzas are: "+friend_pizza.title())
#4-12
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print("My favorite foods are: ")
for my_food in my_foods:
    print(my_food)
print("My friend favorite food are: ")
for friend_food in friend_foods:
    print(friend_food)



