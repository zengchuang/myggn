# 定义元组
# 元组看起来犹如列表， 但使用圆括号而不是方括号来标识。 定义元组后， 就可以使用索引来访问其元素， 就像访问列表元素一样。
# 例如， 如果有一个大小不应改变的矩形， 可将其长度和宽度存储在一个元组中， 从而确保它们是不能修改的：

yuanzu = (200,50)
print(yuanzu[0])
print(yuanzu[1])

# yuanzu[0]=250,代码试图修改第一个元素的值，
# 导致Python返回类型错误消息。 由于试图修改元组的操作是被禁止的，
# 因此Python指出不能给元组的元素赋值

yuanzu1 = (300,75)
for yuanzu2 in yuanzu1:
	print(yuanzu2)
	
# 我们首先定义了一个元组， 并将其存储的尺寸打印了出来 ； 接下来， 将一个新元组存储到变量dimensions 中 ；
# 然后， 打印新的尺寸 。 这次， Python不会报告任何错误， 因为给元组变量赋值是合法的：
dimensions = (200,50)
print("\nOrigina dimensions:")
for dimension in dimensions:
	print(dimension)
	
dimensions = (400,100)
print("\nOrigina dimensions:")
for dimension in dimensions:
	print(dimension)
# 相比于列表， 元组是更简单的数据结构。
# 如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。
