#3-4
guest=['james','curry','harden','durant']
message1="I want to invite "+guest[0].title()+"to come my party."
message2="I want to invite "+guest[1].title()+"to come my party."
message3="I want to invite "+guest[2].title()+"to come my party."
message4="I want to invite "+guest[3].title()+"to come my party."
print(message1)
print(message2)
print(message3)
print(message4)
#3-5
guest=['james','curry','harden','durant']
reason=guest[0].title()+" "+"will not come because of ill."
print(reason)
guest[0]='buttler'
print(guest)
message1="I want to invite "+guest[0].title()+"to come my party."
message2="I want to invite "+guest[1].title()+"to come my party."
message3="I want to invite "+guest[2].title()+"to come my party."
message4="I want to invite "+guest[3].title()+"to come my party."
print(message1)
print(message2)
print(message3)
print(message4)
#3-6
guest=['james','curry','harden','durant']
good_news="we found a bingger house so that we can invite much more than before."
guest.insert(0,'lily')
guest.insert(3,'tom')
guest.append('john')
print(guest)
message1="I want to invite "+guest[0].title()+"\tto come my party."
message2="I want to invite "+guest[1].title()+"\tto come my party."
message3="I want to invite "+guest[2].title()+"\tto come my party."
message4="I want to invite "+guest[3].title()+"\tto come my party."
message5="I want to invite "+guest[4].title()+"\tto come my party."
message6="I want to invite "+guest[5].title()+"\tto come my party."
message7="I want to invite "+guest[6].title()+"\tto come my party."
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message7)
#3-7
guest=['james','curry','harden','durant']
bad_news="it was a pity that desk was delivered lately,so we only invite two friend to come."
print(bad_news)
guest1=guest.pop(3)
message1=guest1.title()+"\ti am sorry to tell you that you can not come to party."
print(message1)
guest2=guest.pop(2)
message2=guest2.title()+"\ti am sorry to tell you that you can not come to party."
print(message2)
message3=guest[0].title()+" "+"i am glad to tell you will be invited to party."
print(message3)
message4=guest[1].title()+" "+"i am glad to tell you will be invited to party."
print(message4)
del guest[1]
del guest[0]
print(guest)

