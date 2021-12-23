favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
# 我们创建了一个列表， 其中包含我们要通过打印消息，
# 指出其喜欢的语言的朋友。 在循环中， 我们打印每个人的名字，
# 并检查当前的名字是否在列表friends 中.如果在列表中， 就打印一句特殊的问候语，
# 其中包含这位朋友喜欢的语言。 为访问喜欢的语言，
# 我们使用了字典名， 并将变量name 的当前值作为键 。
# 每个人的名字都会被打印， 但只对朋友打印特殊消息：
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
        favorite_languages[name].title() + "!")
        
#你还可以使用keys() 确定某个人是否接受了调查。 下面的代码确定Erin是否接受了调查

if 'erin'not in favorite_languages.keys():
    print("Erin,please take our poll!")
#按顺序遍历字典中的所有键
# 字典总是明确地记录键和值之间的关联关系， 但获取字典的元素时， 获取顺序是不可预测的。
# 这不是问题， 因为通常你想要的只是获取与键相关联的正确的值。
# 要以特定的顺序返回元素， 一种办法是在for 循环中对返回的键进行排序。
# 为此， 可使用函数sorted() 来获得按特定顺序排列的键列表的副本：
for name in  sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking thr poll.")

#遍历字典中的所有值
# 主要是字典包含的值， 可使用方法values() ， 它返回一个值列表，
# 而不包含任何键。 例如， 如果我们想获得一个这样的列表， 即其中只包含被调查者选择的各
# 种语言， 而不包含被调查者的名字， 可以这样做：
print("The following languages habe been mentioned:")
#这条for 语句提取字典中的每个值， 并将它们依次存储到变量language 中。
# 通过打印这些值， 就获得了一个列表， 其中包含被调查者选择的各种语言
for languahe in favorite_languages.values():
    print(languahe.title())

# 这种做法提取字典中所有的值， 而没有考虑是否重复。 涉及的值很少时，
# 这也许不是问题， 但如果被调查者很多， 最终的列表可能包含大量的重复项。
# 为剔除重复项， 可使用集合（set） 。 集合 类似于列表， 但每个元素都必须是独一无二的：
#这个语句没有重复的语言出现.python不会出现两次
for languahe in set(favorite_languages.values()):
    print(languahe.title())
    