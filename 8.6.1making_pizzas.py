#
# from pizza import make_pizza
#
# pizza.make_pizza(16,'pepperoni')
# pizza.make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')
#
# #import pizza
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')


#下面给函数make_pizza() 指定了别名mp() 。
# 这是在import 语句中使用make_pizza as mp 实现的，
# 关键字as 将函数重命名为你提供的别名：

from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms', 'green peppers', 'extra cheese')

#你还可以给模块指定别名。 通过给模块指定简短的别名（如给模块pizza 指定别名p ） ，
#让你能够更轻松地调用模块中的函数。 相比于pizza.make_pizza()， p.make_pizza() 更为简洁：
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#使用星号（* ） 运算符可让Python导入模块中的所有函数：
from pizza import *
make_pizza(16,'pepperoni')