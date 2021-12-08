#
# jiabin = ['biao','cui','hong']
# print(jiabin)
#
# # #方法pop() 可删除列表末尾的元素， 并让你能够接着使用它。
# # pop_jiaben = jiabin.pop()
# # print(jiabin)
# # print(pop_jiaben) #输出表明， 列表末尾的值'hong' 已删除， 它现在存储在变量pop_jiaben 中
#
# ##方法pop() 在括号中指定要删除的元素的索引即可
# pop_jiaben = jiabin.pop(0)
# print(jiabin) #这里打印出来就是['cui', 'hong']
#
# #方法pop() 是怎么起作用的呢？ 假设列表中的嘉宾是时间排序的， 就可使用方法pop() 打印一条消息， 指出排在最后的
# #输出简单的一个句子,指出那个是最后邀请的嘉宾
# pop_jiaben = jiabin.pop()
# yaoqing = '我邀请的嘉宾' + '是' + ' ' + pop_jiaben.title()
# print(yaoqing)

# 3-4 嘉宾名单 ： 如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的） ， 你会邀请哪些人？ 请创建一个列表， 其中包含至少3个你想邀请的人；
# 然后， 使用 这个列表打印消息， 邀请这些人来与你共进晚餐。
guest = ['simon','coco','vivi']
#print(guest)
guest = [x.upper() for x in guest]
#print(x)
invitation = "I will invite" + " " + guest[0] +","+ guest[1] + "," + guest[2] + " " + "to dinner"
print(invitation)

#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
guest = ['simon', 'coco', 'vivi']
guest = [x.title() for x in guest]
invitation = "I'd like to invite" + " " + ",".join(guest) + " " + "to dinner"
print(invitation)

# 3-5 修改嘉宾名单 ： 你刚得知有位嘉宾无法赴约， 因此需要另外邀请一位嘉宾。
# 以完成练习3-4时编写的程序为基础， 在程序末尾添加一条print 语句， 指出哪位嘉宾无法赴约。
# 修改嘉宾名单， 将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息， 向名单中的每位嘉宾发出邀请。
pop_guest = guest.pop(0)
print(guest)
guest.append('XIXI')
print(guest)
print(pop_guest)
A = 'The guests Unable to keep the appointment' + ' ' + pop_guest
print(A)
print(guest)


# 3-6 添加嘉宾 ： 你刚找到了一个更大的餐桌， 可容纳更多的嘉宾。 请想想你还想邀请哪三位嘉宾。
# 以完成练习3-4或练习3-5时编写的程序为基础， 在程序末尾添加一条print 语句， 指出你找到了一个更大的餐桌。
# 使用insert() 将一位新嘉宾添加到名单开头。
# 使用insert() 将另一位新嘉宾添加到名单中间。
# 使用append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息， 向名单中的每位嘉宾发出邀请。
table = 'I just found a bigger table'
so = "so I'd like to invite again"

guest.insert(0,'chacha')
guest.insert(3,'meimei')
guest.append('didi')
print(guest)
guest = (x.title() for x in guest)
san = table + so + ' '+ ',' .join(guest)
print(san)

# 3-7 缩减名单 ： 你刚得知新购买的餐桌无法及时送达， 因此只能邀请两位嘉宾。
# 以完成练习3-6时编写的程序为基础， 在程序末尾添加一行代码， 打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop() 不断地删除名单中的嘉宾， 直到只有两位嘉宾为止。 每次从名单中弹出一位嘉宾时， 都打印一条消息，
# 让该嘉宾知悉你很抱歉， 无法邀请他来共进晚餐。
# 对于余下的两位嘉宾中的每一位， 都打印一条消息， 指出他依然在受邀人之列。
# 使用del 将最后两位嘉宾从名单中删除， 让名单变成空的。 打印该名单， 核实程序结束时名单确实是空的。

guests = ['louie', 'lisa', 'eric']
#变量
msg = ", I hope to invite you to dinner."
#insert() 可在列表的任何位置添加新元素。
guests.insert(0, 'mary')

guests.insert(3, 'jams')
#append() 让动态地创建列表易如反掌
guests.append('antony')

print(guests)
#pop() 可删除列表末尾的元素， 并让你能够接着使用它。
print(guests.pop().title() + " I`m sorry to can not invite you to dinner")

print(guests.pop().title() + " I`m sorry to can not invite you to dinner")

#pop弹出，默认弹出后置位

guests.pop()

guests.pop()



print(guests)

# 遍历列表并打印

for guesta in guests:
 print(guesta.title() + msg)

# del语句删除

 del guests[0]

 del guests[0]

 print(guests)
#有时候， 你不知道要从列表中删除的值所处的位置。 如果你只知道要删除的元素的值， 可使用方法remove() 。

