'''
如果要让函数接受不同类型的实参， 必须在函数定义中将接纳任意数量实参的形参放在最后。
Python先匹配位置实参和关键字实参， 再将余下的实参都收集到最后一个形参中。
例如， 如果前面的函数还需要一个表示比萨尺寸的实参， 必须将该形参放在形参*toppings 的前面：
'''
def make_pizza(size,*toppings):
    '''概述要制作的比萨'''
    print("\nMaking a "+str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')
# 基于上述函数定义， Python将收到的第一个值存储在形参size 中， 并将其他的所有值都存储在元组toppings 中。
# 在函数调用中， 首先指定表示比萨尺寸的实参， 然后根据需要指定任意数量的配料