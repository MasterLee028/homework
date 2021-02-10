#5-8
names=['admin','james','harden','curry','tom']
for name in names:
    if name == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello\t"+name.title()+",thank you for logging in again.")
#5-9
names=['admin','james','harden','curry','tom']
for name in names:
    if names and  name == 'admin':
        print("Hello admin,would you like to see a status report?")
    elif names :
        print("Hello\t"+name.title()+",thank you for logging in again.")
    else:
        print("We need find some users!")
del names[0:6]
if names:
    print("we have users!")
else:
    print("We need find some users!")
#5-10
currrnt_users=['james','lee','tom','tim','fox']
new_users=['james','lee','jhon','pope','davis']
for new_user in new_users:
    if new_user.lower() in currrnt_users or new_user.upper() in currrnt_users:
        print("You need find another names!")
    else:
        print("The name is empty!")
#5-11
naturals=list(range(1,10))
print(naturals)
for natural in naturals:
    if natural < 2:
        print("1st\n")
    if natural < 3:
        print("2nd\n")
    if natural < 4:
        print("3rd\n")
    elif natural > 3:
        print(str(natural)+"th\n")
    else:
        print("There is no way to print!")








