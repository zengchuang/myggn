
''''''
'''
6-7 人 ： 在为完成练习6-1而编写的程序中， 再创建两个表示人的字典， 然后将这三个字典都存储在一个名为people 的列表中。
遍历这个列表， 将其中每个人的所有信息都打印出来。
6-8 宠物 ： 创建多个字典， 对于每个字典， 都使用一个宠物的名称来给它命名；
在每个字典中， 包含宠物的类型及其主人的名字。 将这些字典存储在一个名为pets的列表中， 再遍历该列表， 并将宠物的所有信息都打印出来。
6-9 喜欢的地方 ： 创建一个名为favorite_places 的字典。 在这个字典中， 将三个人的名字用作键； 对于其中的每个人， 都存储他喜欢的1~3个地方。 为让这个练
习更有趣些， 可让一些朋友指出他们喜欢的几个地方。 遍历这个字典， 并将其中每个人的名字及其喜欢的地方打印出来。
6-10 喜欢的数字 ： 修改为完成练习6-2而编写的程序， 让每个人都可以有多个喜欢的数字， 然后将每个人的名字及其喜欢的数字打印出来。
6-11 城市 ： 创建一个名为cities 的字典， 其中将三个城市名用作键； 对于每座城市， 都创建一个字典， 并在其中包含该城市所属的国家、 人口约数以及一个有关该
城市的事实。 在表示每座城市的字典中， 应包含country 、 population 和fact 等键。 将每座城市的名字以及有关它们的信息都打印出来。
6-12 扩展 ： 本章的示例足够复杂， 可以以很多方式进行扩展了。 请对本章的一个示例进行扩展： 添加键和值、 调整程序要解决的问题或改进输出的格式。
'''
#6-7 人 ： 在为完成练习6-1而编写的程序中， 再创建两个表示人的字典， 然后将这三个字典都存储在一个名为people 的列表中。
#遍历这个列表， 将其中每个人的所有信息都打印出来。
people ={
    'simon' : {'first_name':'simon',
               'last_name':'xiao',
               'age':'18',
               'city':'shenzhen'},
    'create' : {'first_name':'create',
                'last_name':'zeng',
                'age':'25',
                'city':'guangzhou'},
    'hong' : {'first_name':'hong',
              'last_name':
                  'ren','age':'30',
              'city':'shanghai'},
}

print(people.items())

# 6-8 宠物 ： 创建多个字典， 对于每个字典， 都使用一个宠物的名称来给它命名；
# 在每个字典中， 包含宠物的类型及其主人的名字。 将这些字典存储在一个名为pets的列表中， 再遍历该列表， 并将宠物的所有信息都打印出来。

prts = {
    'tortoise':{
        'type':'陆龟',
        'master':'simon',
        'age':'20',
                },
    'turtle':{
        'type':'海龟',
        'master':'hong',
        'age':'30',
    },
    'tiger':{
        'type':'老虎',
        'master':'create',
        'age':'18',
    }
}
print(prts.items())

# 6-9 喜欢的地方 ： 创建一个名为favorite_places 的字典。 在这个字典中， 将三个人的名字用作键； 对于其中的每个人，
# 都存储他喜欢的1~3个地方。
# 为让这个练习更有趣些， 可让一些朋友指出他们喜欢的几个地方。 遍历这个字典， 并将其中每个人的名字及其喜欢的地方打印出来。

favorite_places = {
    'simon' : {
        'difang_1':'beijing',
        'difang_2':'shanghai',
        'difang_3':'guangzhou',},
    'CoCO':{
        'difang_1':'dongguang',
        'difang_2':'guangxi',
        'difang_3':'jiangsu',
    },
    'YoYo':{
        'difang_1':'hunan',
        'difang_2':'hubei',
        'difang_3':'jiangxi',
    }
}
for name,vuer in favorite_places.items():
    城市 = "\n" + vuer['difang_1'] + "\n" + vuer['difang_2'] + "\n" + vuer['difang_3']
    print("\n这个" + name + "," "最喜欢去的城市竟然有:" + 城市)
    
#6-10 喜欢的数字 ： 修改为完成练习6-2而编写的程序， 让每个人都可以有多个喜欢的数字， 然后将每个人的名字及其喜欢的数字打印出来。
#6-2的脚本
shuzi = {
    'tu':'1',
    'hong':'2',
    'nan':'3',
    'simon':'4',
    'car':'5',
}
#修改6-2的脚本
shuzi = {
    'tu':['1','2']
}
for shu,zi in shuzi.items():
    print(shu)
for lai in shuzi['tu']:
    print(lai)