'''
8-9 魔术师 ： 创建一个包含魔术师名字的列表， 并将其传递给一个名为show_magicians() 的函数， 这个函数打印列表中每个魔术师的名字。
'''
'''
我将show_magician()定义成一个接受魔术师名字的列表.将其存储在形参name中.
这个函数遍历收到的列表并对其中的每位用户都打印一条告诉别人这位魔术师是谁
定义了一个用户列表——show ， 然后调用show_magician() ， 并将这个列表传递给它：
The magician's name is Simon
The magician's name is Jesse
The magician's name is Lucy
'''
def show_magician(name):
    '''打印魔术师名字'''
    for names in name:
        say = "The magician's name is " + names.title()
        print(say)
show = ['simon','jesse','lucy']
show_magician(show)


'''
8-10 了不起的魔术师 ： 在你为完成练习8-9而编写的程序中， 编写一个名为make_great() 的函数，
对魔术师列表进行修改， 在每个魔术师的名字中都加入字样“theGreat”。
调用函数show_magicians() ， 确认魔术师列表确实变了。
'''
'''
我定义了print_name(),它包含两个形参,一个是告诉观众魔术师的名称,
另外一个是加了the great字样
'''
def print_name(show_magician,make_great):
     while show_magician:
        magician_name = show_magician.pop()
        print("He is magicican " + magician_name.title())
        make_great.append(magician_name)
        
def make_name(make_great):
    for make_grea in make_great:
        print("the Great magicican " + make_grea.title())
show_magician = ['simon','jesse','lucy']
make_great = []
print_name(show_magician,make_great)
make_name(make_great)

'''
8-11 不变的魔术师 ： 修改你为完成练习8-10而编写的程序， 在调用函数make_great() 时， 向它传递魔术师列表的副本。 由于不想修改原始列表，
请返回修改后的列表， 并将其存储到另一个列表中。
分别使用这两个列表来调用show_magicians() ， 确认一个列表包含的是原来的魔术师名字， 而另一个列表包含的是添加了字样“the Great”的魔术师名字
'''
def print_name(show_magician,make_great):
    while show_magician:
        magician = show_magician.pop()
        print("HI, " + magician.title())
        make_great.append(magician)
def make_great_name(make_great):
    print("\nthe Great:")
    for make_grea in make_great:
        print(make_grea)
show_magician = ['simon','jesse','lucy']
make_great=[]
print_name(show_magician,make_great)
print_name(show_magician[:],make_great)
make_name(make_great)

'''
下面这些是其他的同学写的.
'''
# names=['Jane','Eric','Mike']
# def show_names(names):
#     for name in names:
#         print(name)
# show_names(names)
#     #显示原来的列表"""
#
# def make_great(names):
#     i=0
#     while i<len(names):
#         names[i]='the Great '+names[i]
#         i+=1
#         return names
#     #"""返回一个修改后的列表值"""
#
# changed_names=make_great(names[:])#"""修改原表的副本，并传递给一个新表"""
# show_names(changed_names)#"""显示修改后的列表"""
# show_names(names)#"""原来的表没有因为修改而改变，因为修改的是原表的副本"""
#
#
# def make_great(magicians):
#     modify = []
#     for magician in magicians:
#         info = 'theGreat '+ magician.title()
#         modify.append(info)
#         return modify
# def show_magicians(magician_info):
#     print(magician_info)
# magicians = []
# magicians.append('zhangsan')
# magicians.append('lisi')
# magicians.append('wangwu')
# new_magician_info = make_great(magicians[:])
# show_magicians(new_magician_info)
# show_magicians(magicians)
#
# def print_models(unprinted_designs, completed_models):
# # 模拟打印每个设计， 直到没有未打印的设计为止
# # 打印每个设计后， 都将其移到列表completed_models中
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#     # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)