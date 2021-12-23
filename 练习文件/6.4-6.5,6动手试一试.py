
# 6-4 词汇表2 ： 既然你知道了如何遍历字典，
# 现在请整理你为完成练习6-3而编写的代码， 将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。
# 确定该循环正确无误后， 再在词汇表中添加5个Python术语。 当你再次运行这个程序时， 这些新术语及其含义将自动包含在输出中。

lianxi={
    'str()':'将非字符串值表示为字符串',
    'del': '彻底删除一个元素',
    'sort()':'对列表进行永久性排序',
    'sorted()':'对列表进行临时排序',
    'range()':'生成一系列数字',
}

lianxi['title()']='首字母大写'
lianxi['lower()']='字母转换成小写'
lianxi['upper()']='字母转换成大写'
lianxi['append()']='在列表最后填写元素'
lianxi['insert()']='插入元素'

for key,value in lianxi.items():
    print(key+':\n\t'+value+'.')
    
# 6-5 河流 ：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt' 。
# 使用循环为每条河流打印一条消息，如“The Nileruns throughEgypt.”。
# 使用循环将该字典中每条河流的名字都打印出来。
# 使用循环将该字典包含的每个国家的名字都打印出来。

places = {
    '中国':'长江',
    '埃及':'尼罗河',
    '巴西':'亚马孙河',
}
#items() 方法的遍历：items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回。
for place,plac in places.items():
    print(place,plac)

    print('The Nileruns through '+ place.title() + plac.title() + '!')
# 6-6 调查 ：在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。

favorite_languages = {
    '老王':'c++',
    '老李':'python',
    '老周':'c#',
    '老费':'Java',
}
invited_people = ['老王','老周','老李']
for people in favorite_languages.keys():
    if people in invited_people:
        print(people.title()+' 非常感谢您参加我们的调查问卷!')
    else:
        print(people.title()+' 我们能邀请您参加我们的调查问卷吗?')