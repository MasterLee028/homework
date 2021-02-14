#6-4
word={'print':'打印','append':'在列表末尾添加元素','del':'删除','pop':'冒出删除','remove':'可使用元素的值的删除','range':'创建数字列表'}
for key,value in word.items():
    print("\nKey:"+key.title())
    print("Value:"+value.title())
#6-5
rivers={'China':'Yang zi river','nile':'egypt','India':'Ganges river'}
for key,value in rivers.items():
    print("The "+key.title()+" run through "+value.title()+".")
print("The following rivers have been mentioned:")
for value in rivers.values():
    print(value)
print("The following countries have been mentioned:")
for key in rivers.keys():
    print(key.title())
#6-6
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
names=['jen','sarah','edward']
for key in favorite_languages.keys():
    if key in names:
        print("Thanks for joining us!")
    else:
        print("please come to join us!")
#6-7
infor_0={'first_name':'lee','last_name':'tom','age':'20','city':'cheng du'}
infor_1={'first_name':'wang','last_name':'gang','age':'19','city':'cheng du'}
infor_2={'first_name':'zhang','last_name':'qiang','age':'20','city':'shang hai'}
people=[infor_0,infor_1,infor_2]
for name in people:
    print(name)
#6-8
boy={'pocky':'harris'}
pretty={'Alaskan':'tom'}
lucky={'Golden Retriever'}
pets=[boy,pretty,lucky]
for pet in pets:
    print(pet)
#6-9
favorite_places={'tom':['Tokyo','Hon kong','New york'],
                 'harris':['cheng du','shang hai'],
                 'kate':['chong qing','hangzhou'],
                 }
for name,places in  favorite_places.items():
    print("\n"+name.title()+" likes:")
    for place in places:
        print(place)
#6-10
number={'lee':['7','2'],
        'tom':['1','2'],
        'wang':['2','3'],
        'zhang':['3','4'],
        'liu':['4','5'],
        }
for name,numbers in number.items():
    print("\n"+name.title()+" like:")
    for natural in numbers:
        print(natural)
#6-11
cities={
    'cheng du': {
    'country': 'China',
    'population': '1亿',
    'fact': 'pleasure',
},
    'chong qing': {
    'country': 'c=China',
    'population': '0.5亿',
    'fact': 'spicy',
    },
    'shang hai': {
     'country': 'China',
     'population': '3亿',
     'fact': 'money',
    },
}
for city,infors in cities.items():
    print("\n"+city.title()+":")
    for infor in infors.values():
        print(infor)






