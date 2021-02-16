#8-1
def display_message():
    """打印一个句子"""
    print("本章学习的是函数！")
display_message()
#8-2
def favorite_book(title):
    """打印一条消息，显示喜欢的书本"""
    print("One of my favorite books is "+title.title()+"!")
favorite_book('hero of story')
#8-3
def make_shirt(size,shape='long'):
    """说明衣服的尺码和字样"""
    print("The cloth's size is "+size.title()+".")
    print("The cloth's shape is "+shape.title()+".")
make_shirt('XL','circle')
make_shirt(shape='circle',size='XL')
make_shirt('XL')
#8-4
def make_shirt(size,shape='I love Python'):
    """有默认字样的衣服说明"""
    print("The cloth's size is "+size.title()+".")
    print("The cloth's shape is "+shape.title()+".")
make_shirt('large')
make_shirt('middle')
make_shirt('small','I love playing basketball')
#8-5
def describe_city(place,country='China'):
    """用于描述一个城市所属的国家"""
    print("The "+place.title()+" is in "+country.title()+".")
describe_city('cheng du')
describe_city('paris','france')
describe_city('new york','america')
#8-6
def city_country(city,country):
    relation=city+","+country
    return relation.title()
relate=city_country('chengdu','china')
print(relate)
relate=city_country('shang hai','china')
print(relate)
relate=city_country('tokyo','japan')
print(relate)
#8-7
def make_album(singer,album_name,song_number=''):
    if song_number:
        album={'singer':singer,'album_name':album_name,'song_number':song_number}
    else:
        album={'singer':singer,'album_name':album_name}
    return album
album = make_album('aldel','hello','2')
print(album)
album = make_album('enmnime','monster')
print(album)
album = make_album('jay zhou','love','3')
print(album)
#8-8
def make_album(singer,album_name,song_number=''):
    if song_number:
        album={'singer':singer,'album_name':album_name,'song_number':song_number}
    else:
        album={'singer':singer,'album_name':album_name}
    return album
while True:
    print("\nPlease tell us the message: ")
    print("(Enter q to quit)")
    singe = input("Singer: ")
    album['singe'] = singe
    if album['singe'] == 'q':
        break
    album_nam = input("album_name: ")
    album['album_nam'] = album_nam
    if album['album_nam'] == 'q':
        break
    song_numbe = input("song_number: ")
    album['song_numbe'] = song_numbe
    if album['song_numbe'] == 'q':
        break
    album = make_album(singe,album_nam,song_numbe)
    print(album)

