# 7-8 熟食店：
# 创建一个名为sandwich_orders 的列表， 在其中包含各种三明治的名字；
# 再创建一个名为finished_sandwiches 的空列表。
# 遍历列表sandwich_orders ， 对于其中的每种三明治， 都打印一条消息，
# 如I made your tuna sandwich ， 并将其移到列表finished_sandwiches 。
# 所有三明治都制作好后， 打印一条消息， 将这些三明治列出来。
sandwich_orders = ['火腿三明治','烟熏三明治','海鲜三明治','鸡蛋三明治','肉肠三明治']
finished_sandwiches = []

while sandwich_orders:
    sanmingzi = sandwich_orders.pop()

    print("我做了," + sanmingzi)
    finished_sandwiches.append(sanmingzi)
print("\n显示已经做好的三明治:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)
#
# # 7-9 五香烟熏牛肉（ pastrami） 卖完了 ： 使用为完成练习7-8而创建的列表sandwich_orders ，
# # 并确保'pastrami' 在其中至少出现了三次。 在程序开头附近添加
# # 这样的代码： 打印一条消息， 指出熟食店的五香烟熏牛肉卖完了；
# # 再使用一个while 循环将列表sandwich_orders 中的'pastrami' 都删除。
# # 确认最终的列表finished_sandwiches 中不包含'pastrami' 。

sandwich_orders = ['火腿三明治', '五香烟熏牛肉', '五香烟熏牛肉', '烟熏三明治', '海鲜三明治', '鸡蛋三明治', '肉肠三明治', '五香烟熏牛肉']
new_orders = sandwich_orders.copy()
# print(sandwich_orders)
# str.format()，它增强了字符串格式化的功能。
#
# 基本语法是通过 {} 和 : 来代替以前的 % 。
#
# .format 函数可以接受不限个参数，位置可以不按顺序。
# "{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
# 'hello world'
#这个代码还限制了.只能输入现有的口味文字,输入其它的话,会循环
print("我们的口味有:{} \n请问您要什么口味的三明治? ".format(sandwich_orders))
while new_orders:
    try:
        diandan = input()
        if diandan not in sandwich_orders:
            raise ValueError("只能输入{}".format(sandwich_orders))
        if diandan == '五香烟熏牛肉':
            while diandan in new_orders:
                new_orders.remove(diandan)
            print("不好意思,我们这个口味卖完了!剩余的口味有{}".format(new_orders))
        else:
            print("好的,马上为您送上 " + diandan)
            new_orders.remove(diandan)
            break
    except ValueError as e:
        print("只能输入口味名称")

# 7-10 梦想的度假胜地 ： 编写一个程序， 调查用户梦想的度假胜地。
# 使用类似于“If you could visit one place in the world, where would you go?”的提示，
# 并编写一个打印调查结果的代码块。
dujia = {}

biaozhi = True

while biaozhi:
    name = input("\nwhat is your name? ")
    dujiao = input("Which resort do you like? ")

    dujia[name] = dujiao

    diaocha = input("Does anyone else want to say? (yes/ no)")
    if diaocha == 'no':
        biaozhi = False

print("\n ---Findings--- ")
for name,dujiao in dujia.items():
    print(name + " like " + dusjiao + ".")

