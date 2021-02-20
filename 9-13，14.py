#9-13
from collections import OrderedDict
word = OrderedDict()
word['print'] = "打印"
word['append'] = "在列表最后添加元素"
word['del'] = "删除元素"
word['remove'] = "可使用元素的值的删除"
word['range'] = "创建数字列表"
for key,value in word.items():
    print("\nKey:"+key.title())
    print("Value:"+value.title())
#9-14
from random import randint
class Die():
    def __init__(self,sides):
        self.sides = 6
    def roll_die(self):
        x = randint(1,self.sides)
        print(x)
die_0 = Die(6)
die_1 = Die(10)
die_2 = Die(20)
for number in range(1,7):
 die_0.roll_die()
for number in range(1,11):
    die_1.roll_die()
for number in range(1,21):
    die_2.roll_die()


