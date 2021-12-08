
'''
你经常需要遍历列表的所有元素， 对每个元素执行相同的操作。 例如， 在游戏中， 可能需要将每个界面元素平移相同的距离； 对于包含数字的列表， 可能需要对每个元素执行相
同的统计运算； 在网站中， 可能需要显示文章列表中的每个标题。 需要对列表中的每个元素都执行相同的操作时， 可使用Python中的for 循环。
假设我们有一个魔术师名单， 需要将其中每个魔术师的名字都打印出来。 为此， 我们可以分别获取名单中的每个名字， 但这种做法会导致多个问题。 例如， 如果名单很长， 将包
含大量重复的代码。 另外， 每当名单的长度发生变化时， 都必须修改代码。 通过使用for 循环， 可让Python去处理这些问题。
下面使用for 循环来打印魔术师名单中的所有名字：
'''
#for 循环来打印魔术师名单中的所有名字
# moshushi = ['vivi', 'coco', 'jekng']
# for moshushis in moshushi:
#        print(moshushis)
#
#        print(moshushis.title() + ', ta shi yige moshushi!')
#由于两条print 语句都缩进了， 因此它们都将针对列表中的每位魔术师执行一次。 第二条print 语句中的换行符"\n"
#在每次迭代结束后都插入一个空行， 从而整洁地将针对各位魔术师的消息编组
#        print('wo dengbuji kan ni xiayige moshule,' + moshushis.title() +'\n')
# print('Thank you, everyone. That was a great magic show!')
#
#
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#  print(magician)
 
 

#  4-1 比萨 ： 想出至少三种你喜欢的比萨， 将其名称存储在一个列表中， 再使用for 循环将每种比萨的名称都打印出来。
# 修改这个for 循环， 使其打印包含比萨名称的句子， 而不仅仅是比萨的名称。 对于每种比萨， 都显示一行输出， 如“I like pepperoni pizza”。
# 在程序末尾添加一行代码， 它不在for 循环中， 指出你有多喜欢比萨。 输出应包含针对每种比萨的消息， 还有一个总结性句子， 如“I really love pizza!”。
# 4-2 动物 ： 想出至少三种有共同特征的动物， 将这些动物的名称存储在一个列表中， 再使用for 循环将每种动物的名称都打印出来。
# 修改这个程序， 使其针对每种动物都打印一个句子， 如“A dog would make a great pet”。
# 在程序末尾添加一行代码， 指出这些动物的共同之处， 如打印诸如“Any of these animals would make a great pet!”这样的句子。
 
 
pisa = ['XXX','haixian','liulian']
for pisaa in pisa:
      #print(pisaa)
      print('I like pepperoni pizza ' + pisaa.title())
print('I really love pizza!\n')
