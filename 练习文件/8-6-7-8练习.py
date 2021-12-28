# 8-6 城市名 ： 编写一个名为city_country() 的函数， 它接受城市的名称及其所属的国家。
# 这个函数应返回一个格式类似于下面这样的字符串："Santiago, Chile"
# 至少使用三个城市-国家对调用这个函数， 并打印它返回的值。

def city_country(city,country):
    a = city + ', ' + country
    return a
b = city_country('china','shanghai')
print(b)

b = city_country('chian','shenzhen')
print(b)

b = city_country('chian','guangzhou')
print(b)

# 8-7 专辑 ： 编写一个名为make_album() 的函数， 它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名， 并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典， 并打印每个返回的值， 以核实字典正确地存储了专辑的信息。

def make_album(name,album):
    singer = {'Singer_Name':name,'Music Album':album}
    return singer
music = make_album('周杰伦','Jay')
print(music)

music = make_album('回音哥','回音Echo')
print(music)

music = make_album('刘德华','只知道此刻爱你')
print(music)


# 8-8 用户的专辑 ： 在为完成练习8-7编写的程序中， 编写一个while 循环， 让用户输入一个专辑的歌手和名称。
# 获取这些信息后， 使用它们来调用函数make_album() ，
# 并将创建的字典打印出来。 在这个while 循环中， 务必要提供退出途径。

def make_album(name,album):
    mc = name + ' ' + album
    return mc
while True:
    print("\n请在下方输入你喜欢的歌手和歌手的专辑名称 ")
    print("输入完成后,可以再歌手货歌手专辑名称的文本框里输入'q',就能结束程序了.")
    
    f_name = input("请输入你喜欢的歌手:")
    if f_name == 'q':
        break
    a_album = input("请输入你喜欢的歌手专辑名称: ")
    if a_album == 'q':
        break
    dj = make_album(f_name,a_album)
    print("\n" + dj +"!")