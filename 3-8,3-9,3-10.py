#3-8
places=['tokyo','hong kong','los angles','paris','new york']
print(places)#打印原始列表
print(sorted(places))#将列表顺序进行临时排序
print(places)#验证列表是进行临时排序
print(sorted(places,reverse=True))#将列表进行临时的倒排序
print(places)#验证列表是进行临时的倒排序
places.reverse()#将列表进行永久的倒排序
print(places)#打印倒排序的列表
places.reverse()#再次进行倒排序
print(places)#验证列表是否回复原来的顺序
places.sort()#将列表进行永久的正排序
print(places)#验证列表是否是正排序
places.sort(reverse=True)#将列表进行按字母倒序进行永久排序
print(places)#验证
#3-9
guest=['james','curry','harden','durant']
counts=len(guest)
print(counts)
#3-10
factries=['china','chengdu','food','life','huo guo','pleased']
print(factries)#打印这个列表
factries.append('landscape')#在末尾添加一个元素
print(factries)
factries.insert(1,'trip')#在列表任意位置添加元素
print(factries)#打印这个列表
message="My favourite things to do is "+factries[5].title()+"."#将列表的某个元素首字符大写
print(message)#验证
del factries[0]#永久删除列表的某个元素
print(factries)#验证
factries[3]='meat'#修改列表元素中的某个元素
print(factries)#打印并验证
favourite_food=factries.pop(4)#弹出列表某个元素
message="My favourite food is "+favourite_food.title()+"."#并使用其值
print(message)#打印并验证
hate_thing='trip'#指明删除那个元素
factries.remove(hate_thing)#删除这个元素但要使用其值
print("I hate "+hate_thing.title()+".")#打印并验证
print(sorted(factries))#临时的正排序
print(sorted(factries,reverse=True))#临时的倒排序
factries.sort()#永久性的正排序
print(factries)#打印并验证
factries.sort(reverse=True)#永久性的倒排序
print(factries)#打印并验证
factries.reverse()#将列表倒过来打印
print(factries)#打印并验证
print(len(factries))#求列表的长度



