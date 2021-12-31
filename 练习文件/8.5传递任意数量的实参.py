'''
有时候， 你预先不知道函数需要接受多少个实参， 好在Python允许函数从调用语句中收集任意数量的实参。
例如， 来看一个制作比萨的函数， 它需要接受很多配料， 但你无法预先确定顾客要多少种配料。
下面的函数只有一个形参*toppings ， 但不管调用语句提供了多少实参， 这个形参都将它们统统收入囊中：
'''
def make_pizza(*toppings):
    #形参名*toppings 中的星号让Python创建一个名为toppings 的空元组， 并将收到的所有值都封装到这个元组中。
    '''打印顾客点的所有配料'''
    print(toppings)#函数体内的print 语句通过生成输出来证明Python能够处理
#使用一个值调用函数的情形， 也能处理使用三个值来调用函数的情形。
#它以类似的方式处理不同的调用， 注意， Python将实参封装到一个元组中， 即便函数只收到一个值也如此：
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extea cheese')

#我们可以将这条print 语句替换为一个循环， 对配料列表进行遍历， 并对顾客点的比萨进行描述：
def make_pizza(*toopings):
    '''概述要制作的比萨'''
    print('\nMaking a pizza with the following toppings:')
    for tooping in toopings:
        print("- " + tooping)
        
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extea cheese')



