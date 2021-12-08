
#使用函数range()
#函数range() 让Python从你指定的第一个值开始数， 并在到达你指定的第二个值
#后停止， 因此输出不包含第二个值（这里为5）
for value in range(1,5):
	print(value)
'''
#要打印数字1~5， 需要使用range(1,6)

for values in range(1,6):
	print(values)
'''
#使用range() 创建数字列表
#要创建数字列表， 可使用函数list() 将range() 的结果直接转换为列表。 如果将range() 作为list() 的参数， 输出将为一个数字列表。
#在前一节的示例中， 我们打印了一系列数字。 要将这些数字转换为一个列表， 可使用list() ：

num = list(range(1,6))
print(num)
#在这个示例中， 函数range() 从2开始数， 然后不断地加2， 直到达到或超过终值（11） ， 因此输出如下
num = list(range(2,11,2))
print(num)
'''
# #  输出1 - 100内的所有偶数
#
# number = 1
#
# while number < 101:
#     # 如果number / 2 余数为 0，代表是偶数
#     # 如果number / 2 余数大于 1 代表奇数
#     if number % 2 > 0:
#     #if number % 2 ==0:
#         print(number,end=' ')
#     number += 1
'''

#两个星号（** ） 表示乘方运算
squares = []
for hanshu in range(1,11):
	square = hanshu**2
	squares.append(square)
	print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
#min的函数是找出最小值
print(min(digits))
#max的函数是找出最大值
print(max(digits))
#sum的函数是总和
print(sum(digits))
#要使用这种语法， 首先指定一个描述性的列表名， 如squares ； 然后， 指定一个左方括号， 并定义一个表达式， 用于生成你要存储到列表中的值。 在这个示例中，
#表达式为value**2 ， 它计算平方值。 接下来， 编写一个for 循环， 用于给表达式提供值， 再加上右方括号。 在这个示例中， for 循环为for value in range(1,11) ，
#它将值1~10提供给表达式value**2 。 请注意， 这里的for 语句末尾没有冒号。
squares = [value**2 for value in range(1,11)]
print(squares)
'''
4-3 数到20 ： 使用一个for 循环打印数字1~20（含） 。
4-4 一百万 ： 创建一个列表， 其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口） 。
调用函数sum() ， 看看Python将一百万个数字相加需要多长时间。
4-6 奇数 ： 通过给函数range() 指定第三个参数来创建一个列表， 其中包含1~20的奇数； 再使用一个for 循环将这些数字都打印出来。
4-7 3的倍数 ： 创建一个列表， 其中包含3~30内能被3整除的数字； 再使用一个for 循环将这个列表中的数字都打印出来。
4-8 立方 ： 将同一个数字乘三次称为立方。 例如， 在Python中， 2的立方用2**3 表示。 请创建一个列表， 其中包含前10个整数（即1~10） 的立方， 再使用一个for 循
环将这些立方数都打印出来。
4-9 立方解析 ： 使用列表解析生成一个列表， 其中包含前10个整数的立方。
'''
# for shu in range(1,21):
# 	print(shu)
shu = list(range(1,21))
print(shu)

baiwan = list(range(1,1000001))
print(min(baiwan))
print(max(baiwan))
print(sum(baiwan))

# for baiwan in range(1,1000001):
# 	print(baiwan)

qishu = list(range(1,21,2))
print(qishu)

oshu = list(range(2,21,2))
print(oshu)

s = list(range(3,31,3))
for ss in s:
	print(s)
	
sanpeilinfang = [lifang**3 for lifang in range(1,11)]
for e in sanpeilinfang:
	 print(e)
	


numbers = list(range(1,10))
result =[]
for num in numbers:
	result.append(num**3)
for num in result:
	print(num)