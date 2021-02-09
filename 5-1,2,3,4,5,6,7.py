#5-1
fruit='apple'
print("Is fruit=='banana'? I predict  True")
print(fruit=='banana')
print("Is fruit=='apple'? I predict True")
print(fruit =='apple')

fruits=['apple','banana','peach','orange','mango','pear','lemon','grape','blueberry','cherry']
for fruit in fruits:
    if fruit == 'apple' or fruit == 'banana' or fruit == 'pear' or fruit == 'grape' or fruit == 'cherry':
        print("True")
    else:
        print("False")
#5-2
conditional_tests=['1','23','45','love','Thanks']
print(conditional_tests)
for conditional_test in conditional_tests:
    if conditional_test == 'love':
        print("True")
    else:
        print("False")
for conditional_test in conditional_tests:
    if conditional_test == 1:
        print(conditional_test == 1)
for conditional_test in conditional_tests:
    if conditional_test !=23 or conditional_test != 45 or conditional_test != 1:
        print("False")
for conditional_test in conditional_tests:
    print('love' in conditional_test)
for conditional_test in conditional_tests:
    print('thanks' not in conditional_test)
#5-3
alien_color='green'
if alien_color == 'green':
    print("You have five points!")
if alien_color == 'red':
    print("You have five points!")
#5-4
alien_color='green'
if alien_color == 'green':
    print("You have five points!")
else:
    print("You have ten points!")
alien_color='red'
if alien_color == 'green':
    print("You have five points!")
else:
    print("You have ten points!")
#5-5
alien_color='green'
if alien_color == 'green':
    points=5
elif alien_color == 'red':
    points=10
else:
    points=15
print("You have "+str(points)+"\tpoints !")
alien_color='red'
if alien_color == 'green':
    points=5
elif alien_color == 'red':
    points=10
else:
    points=15
print("You have "+str(points)+"\tpoints !")
alien_color='yellow'
if alien_color == 'green':
    points=5
elif alien_color == 'red':
    points=10
else:
    points=15
print("You have "+str(points)+"\tpoints !")
#5-6
age=20
if age<2:
    print("He is a baby!")
elif age<4:
    print("He is learning walking!")
elif age<13:
    print("He is a young teen!")
elif age<20:
    print("He is a teenager!")
elif age<65:
    print("He is a adult!")
else:
    print("He is a old man!")
#5-7
fruits=['apple','banana','orange','lemon']
if 'apple' in fruits:
    print('apple' in fruits)
if 'banana' in fruits:
    print('banana' in fruits)
if 'orange' in fruits:
    print('orange' in fruits)
if 'lemon' in fruits:
    print('lemon' in fruits)
if 'pear' in fruits:
    print('pear' in fruits)
favorite_fruits=fruits[1:4]
if 'apple' in favorite_fruits:
    print("I really like apple!")
if 'banana' in favorite_fruits:
    print("I really like banana!")
if 'orange' in favorite_fruits:
    print("I really like orange!")
if 'lemon' in favorite_fruits:
    print("I really like lemon!")
if 'pear' in favorite_fruits:
    print("I really like pear!")








