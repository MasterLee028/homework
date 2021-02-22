#10-1
with open('learinng_python.txt') as file_object:
    infor = file_object.read()
    print(infor)
with open('learinng_python.txt') as file_object_1:
    for line in  file_object_1:
     print(line.rstrip())

with open('learinng_python.txt') as file_object_2:
    lines = file_object_2.readlines()
for line in lines:
    print(line.rstrip())
#10-2
with open('learinng_python.txt') as file_object_3:
    lines = file_object_3.readlines()
for line in lines:
    line = line.replace('python','C')
    print(line.rstrip())
#10-3
with open('guest.txt','w') as file_object_4:
    guest = input("请输入顾客姓名: ")
    file_object_4.write(guest)
#10-4
with open('guest.txt','w') as file_object_5:
    while True:
     guest = input("请输入顾客姓名: ")
     if guest == 'q':
        break
     else:
        print("Hello, "+guest.title()+" welcome to our restaurant!")
        file_object_5.write(guest+"\n")
#10-5
with open('guest.txt','a') as file_object_6:
    while True:
        reason = input("why do you like to code? ")
        if reason == 'q':
            break
        else:
            file_object_6.write(reason+"\n")
#10-6
f_number = input("请输入第一个数字: ")
s_number = input("请输入第二个数字: ")
try:
  answer = int(f_number) + int(s_number)
except ValueError:
    print("文本不能相加！")
else:
    print(answer)
#10-7
f_number = input("请输入第一个数字: ")
s_number = input("请输入第二个数字: ")
while True:
    try:
        answer = answer = int(f_number) + int(s_number)
    except ValueError:
        print("文本不能相加！")
        f_number = input("请重新输入第一个数字: ")
        s_number = input("请重新输入第二个数字: ")
    else:
        print(answer)
        break
#10-8
try:
     with open('cats.txt') as f_obj:
      infor = f_obj.read()
except FileNotFoundError:
    print("文件不存在！")
else:
    with open('cats.txt') as f_obj:
     infor = f_obj.read()
    print(infor)
#10-9
try:
     with open('cats.txt') as f_obj:
       infor = f_obj.read()
except FileNotFoundError:
    pass
else:
    print(infor)
#10-10
with open('The Gibson Book.txt',encoding='gb18030', errors='ignore') as f_obj_1:
    infor = f_obj_1.read()
print(infor.lower().count('the'))