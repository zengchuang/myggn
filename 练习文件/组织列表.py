
#方法sort() （见❶） 永久性地修改了列表元素的排列顺序。 现在， 汽车是按字母顺序排列的， 再也无法恢复到原来的排列顺序
car = ['bmw','audi','toyota','subaru']
car.sort()
print(car)
#反方向排列
car.sort(reverse=True)
print(car)

#原始顺序打印
print("\nHere is thr original list:")
print(car)
#sorted方法 临时按字母排序
print("\nHere is the orginal list:")
print(sorted(car,reverse=True))#反向排序


#再次打印就正常的原始打印
print("\nHere s the orginal listL")
print(car)

#倒着打印列表
cars = ['beici','baoma','yema','baojun']
print(cars)
#方法reverse永久地修改列表元素的排序
cars.reverse()
print(cars)
#再次调用就恢复正常
cars.reverse()
print(cars)

#确定列表的长度
print(len(cars))
'''
# 3-8 放眼世界 ： 想出至少5个你渴望去旅游的地方。
# 将这些地方存储在一个列表中， 并确保其中的元素不是按字母顺序排列的。
# 按原始排列顺序打印该列表。 不要考虑输出是否整洁的问题， 只管打印原始Python列表。
# 使用sorted() 按字母顺序打印这个列表， 同时不要修改它。
# 再次打印该列表， 核实排列顺序未变。
# 使用sorted() 按与字母顺序相反的顺序打印这个列表， 同时不要修改它。
# 再次打印该列表， 核实排列顺序未变。
# 使用reverse() 修改列表元素的排列顺序。 打印该列表， 核实排列顺序确实变了。
# 使用reverse() 再次修改列表元素的排列顺序。 打印该列表， 核实已恢复到原来的排列顺序。
# 使用sort() 修改该列表， 使其元素按字母顺序排列。 打印该列表， 核实排列顺序确实变了。
# 使用sort() 修改该列表， 使其元素按与字母顺序相反的顺序排列。 打印该列表， 核实排列顺序确实变了。
# 3-9 晚餐嘉宾 ： 在完成练习3-4~练习3-7时编写的程序之一中， 使用len() 打印一条消息， 指出你邀请了多少位嘉宾来与你共进晚餐。
# 3-10 尝试使用各个函数 ： 想想可存储到列表中的东西， 如山岳、 河流、 国家、 城市、 语言或你喜欢的任何东西。
# 编写一个程序， 在其中创建一个包含这些元素的列表， 然后， 对于本章介绍的每个函数， 都至少使用一次来处理这个列表
'''
local = ['guangzhou','beijing','hunan','dongbei','fuoshan']
print(local)
print(sorted(local))
print(local)
print(sorted(local,reverse=True))
print(local)
local.reverse()
print(local)
local.reverse()
print(local)
local.sort()
print(local)
local.sort(reverse=True)
print(local)
print(len(local))
