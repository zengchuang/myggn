

motuoche = ['bendi','tiazi','jialing']
print(motuoche)

#删除索引第一个元素,
#del 删除了列表motuche 中的第一个元素——'bendi' (知道位置)
del motuoche[0]
print(motuoche)
#使用del 语句将值从列表中删除后， 你就无法再访问它了
#del 删除了列表motuche 中的第二个元素——'jialing'
del motuoche[1]
print(motuoche)


#修改值
motuoche[0] = 'lingmu'
print(motuoche)

#添加 append() 将元素'ducati' 添加到了列表末尾
motuoche.append('bendi')
print(motuoche)

#insert()将元素'benci'这个元素添加到列表首位或任意位置
#方法insert() 在索引0 处添加空间， 并将值'benci' 存储到这个地方。 这种操作将列表中既有的每个元素都右移一个位置：
motuoche.insert(0,'benci')
print(motuoche)



#使用 append()动态的在空列表页添加元素
motu = []
motu.append('beidi')
motu.append('jialin')
motu.append('lingmu')
motu.append('taizi')
#for循环,把列表的都打印出来
#x = [x.title() for x in motu] #变量X,title()把首字母变为大写,然后for循环X 把列表都打印出来,x in motu x就是motu
#print(x)
print([x.title() for x in motu])

for letter in motu:
	print('当前列表:%s' %letter)
#这个'python'是字符串,加了''for letter 就是把这个字符串拆分打印出来
for letter in 'Python':  # 第一个实例
	print("当前字母: %s" % letter)
#这里fruits是列表
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
	print('当前水果: %s' % fruit)

print("Good bye!")