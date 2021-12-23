'''
一，假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color的变量，并将其设置为"green","yellow",或"red".

（1）编写一条if语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。

（2）编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
'''
# alien_color = ['green','yellow','red']
# alien_colo=input("请输入你的外星人颜色")
# if alien_colo=='green':
#     print("获得5个点")
# else:
#     print("")
#
# 每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试
# 如果条件测试的值为True，Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码
# 检查多个条件：
#               1. 使用and检查多个条件
#               2. 使用or检查多个条件  关键字or也能够检查，只要至少有一个条件满足，就能通过整个测试
#
# 函数lower()   功能将字符串中的大写字母转换为小写字母
# upper()        功能将字符串中的小写字母转换为大写字母
# 要判断特定的值是否已包含在列表中，可使用关键字in
# 布尔表达式的结果要么为True，要么为False
# 5-1 条件测试：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结
# 果都打印出来。你编写的代码应类似于下面这样：
car = 'subaru'
print("ls car == 'subaru? i predict True")
print(car == 'subaru')
print("\nls car == 'audi'? i predict False.")
print(car == 'audi')
# 详细研究实际结果，直到你明白了它为何为True 或False。
# 创建至少10 个测试，且其中结果分别为True 和False 的测试都至少有5 个。
# 5-2 更多的条件测试：你并非只能创建10 个测试。如果你想尝试做更多的比较，可
# 再编写一些测试，并将它们加入到conditional_tests.py 中。对于下面列出的各种测试，
# 至少编写一个结果为True 和False 的测试。
# 检查两个字符串相等和不等。
a = 'the weater is cool'
b = 'The weater is warm'
c = 'the weater is cool'
# print(a == b)
# print(a == c)
# 检查两个数字相等、不等、大于、小于、大于等于和小于等于。
print(1>2)
print(2!=3)
print(3<=4)
# 使用函数lower()的测试。
e = b.lower()#这个b是上面的变量.所以是True
d = 'the weater is warm'
print(d == e)
# 使用关键字and 和or 的测试。
if 'The'in a or "The" in b:
    print("yes")
if 'The' in a and "the" not in b:
    print("yes")
# 测试特定的值是否包含在列表中。
if 'cool'in a:
    print("yes")
# 测试特定的值是否未包含在列表中。
if 'cool' in b:
    print("yes")

#经常需要检查超过两个的情形，为此可使用Python提供的if-elif-else结构

# 5-3 外星人颜色#1：假设在游戏中刚射杀了一个外星人，请创建一个名为
# alien_color 的变量，并将其设置为'green'、'yellow'或'red'。
#  编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出
# 玩家获得了5 个点。
alie_color = 'green'
if alie_color == 'green':
    print("获得5个点")
else:
    print("无")
#  编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中
# 未通过（未通过测试时没有输出）。
alie_color = 'red'
if alie_color == 'green':
    print("获得5个点")
else:
    print("无")
    
# 5-4 外星人颜色#2：像练习5-3 那样设置外星人的颜色，并编写一个if-else 结构。
#  如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5 个点。
#  如果外星人不是绿色的，就打印一条消息，指出玩家获得了10 个点。
alie_color = 'red'
if alie_color == 'green':
    print("获得5个点")
else:
    print("获得10个点")
#  编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执
# 行else 代码块。
# 5-5 外星人颜色#3：将练习5-4 中的if-else 结构改为if-elif-else 结构。
#  如果外星人是绿色的，就打印一条消息，指出玩家获得了5 个点。
#  如果外星人是黄色的，就打印一条消息，指出玩家获得了10 个点。
#  如果外星人是红色的，就打印一条消息，指出玩家获得了15 个点。
#  编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
if alie_color == 'red':
    print("玩家获得15个点")
elif alie_color == 'yellow':
    print("玩家获得10个点")
else:
    print("玩家获得5个点")
# 5-6 人生的不同阶段：设置变量age 的值，再编写一个if-elif-else 结构，根据age
# 的值判断处于人生的哪个阶段。
#  如果一个人的年龄小于2 岁，就打印一条消息，指出他是婴儿。
#  如果一个人的年龄为2（含）～4 岁，就打印一条消息，指出他正蹒跚学步。
#  如果一个人的年龄为4（含）～13 岁，就打印一条消息，指出他是儿童。
#  如果一个人的年龄为13（含）～20 岁，就打印一条消息，指出他是青少年。
#  如果一个人的年龄为20（含）～65 岁，就打印一条消息，指出他是成年人。
#  如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。
age = 75
if age < 2:
    print("婴儿")
elif 2 <= age<4:
    print("婴儿学步")
elif 4 <= age <13:
    print("儿童")
elif 13 <= age <20:
    print("青年")
elif 20 < age < 65:
    print("成年人")
else:
    print("老年人")
# 5-7 喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if
# 语句，检查列表中是否包含特定的水果。
#  将该列表命名为favorite_fruits，并在其中包含三种水果。
favorite_fruits = ['apple','salad','durian']
#  编写 5 条if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，
# 就打印一条消息，如“You really like bananas!”
for value in favorite_fruits:
    if 'yacon' == value:
        print("You rellly like"+value+"!")
    elif "apple" == value:
        print("You rellly like"+value+"!")
    elif "salad" == value:
        print("You rellly like"+value+"!")
    elif "orange" == value:
        print("You rellly like" + value + "!")
    elif "jujube" == value:
        print("You rellly like" + value + "!")
        