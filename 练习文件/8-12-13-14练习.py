'''
8-12 三明治 ： 编写一个函数， 它接受顾客要在三明治中添加的一系列食材。
这个函数只有一个形参（它收集函数调用中提供的所有食材） ， 并打印一条消息，
对顾客点的三明治进行概述。 调用这个函数三次， 每次都提供不同数量的实参。
'''
def sandwich(*ingredients):
    '''打印三明治的所有食材'''
    print(ingredients)
sandwich('Ham')
sandwich('egg')
sandwich('romaine lettuce')

'''
8-13 用户简介 ： 复制前面的程序user_profile.py， 在其中调用build_profile() 来创建有关你的简介；
 调用这个函数时， 指定你的名和姓， 以及三个描述你的键-值对。
'''
def build_profile(first, last, **user_info):
#"""创建一个字典， 其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():#items() 函数以列表返回可遍历的(键, 值) 元组数组。
        profile[key] = value
 
    return profile

#user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
#修改
user_profile = build_profile('san','zhang',location='ShenZhen',field='Python',type='Test')
print(user_profile)


'''
8-14 汽车 ： 编写一个函数， 将一辆汽车的信息存储在一个字典中。
这个函数总是接受制造商和型号， 还接受任意数量的关键字实参。
这样调用这个函数： 提供必不可少的信息， 以及两个名称—值对， 如颜色和选装配件。
这个函数必须能够像下面这样进行调用：car = make_car('subaru', 'outback', color='blue', tow_package=True)
'''
def configuer(manufacturer,model,**number):
    sale = {}
    sale['manufacturer_name']=manufacturer
    sale['model_name']=model
    for key,value in number.items():
        sale[key]=value
    return sale
#car = build_profile('Mercedes-Benz','G63',quantity='1',colour='blacl',price='247.8万')
car = configuer('Mercedes-Benz','G63',quantity='1',colour='blacl',price='247.8万')
print(car)

