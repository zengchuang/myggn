'''
8-16 导入 ： 选择一个你编写的且只包含一个函数的程序， 并将这个函数放在另一个文件中。
在主程序文件中， 使用下述各种方法导入这个函数， 再调用它：
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''
#编写一条import 语句并在其中指定模块名， 就可在程序中使用该模块中的所有函数。
import identity
username = ['Simon']
identity.identity(username)

#导入模块中的特定函数
from identity import identity
username = ['jer']
identity(username)

#使用as 给identity函数指定别名
from identity import identity as id
username = ['peter']
id(username)

#使用as 给模块identity指定别名
import identity as id
username = ['liz']
id.identity(username)

#导入模块中的所有函数
#使用星号（* ） 运算符可让Python导入模块中的所有函数
from identity import *
username = ['python']
identity(username)