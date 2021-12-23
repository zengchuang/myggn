#8.1 定义函数
def greet_user():
    """显示简单的问候语"""
    print('Hello')

greet_user()

'''
这个示例演示了最简单的函数结构。
❶处的代码行使用关键字def 来告诉Python你要定义一个函数。
这是函数定义 ， 向Python指出了函数名， 还可能在括号内指出函数为完成其任务需要什么样的信息。
在这里， 函数名为greet_user() ， 它不需要任何信息就能完成其工作，
 因此括号是空的（即便如此， 括号也必不可少） 。 最后， 定义以冒号结尾。
紧跟在def greet_user(): 后面的所有缩进行构成了函数体。
❷处的文本是被称为文档字符串 （docstring） 的注释， 描述了函数是做什么的。
文档字符串用三引号括起， Python使用它们来生成有关程序中函数的文档。代码行print("Hello!")
（见❸） 是函数体内的唯一一行代码， greet_user() 只做一项工作： 打印Hello! 。
要使用这个函数， 可调用它。 函数调用 让Python执行函数的代码。
要调用 函数， 可依次指定函数名以及用括号括起的必要信息，
如❹处所示。 由于这个函数不需要任何信息， 因
此调用它时只需输入greet_user() 即可。 和预期的一样， 它打印Hello! ：
'''
#8.1.1 向函数传递信息
def greet_user(username):
    print('Hello, '+ username.title()+'!')
    
greet_user('jesse')
greet_user('sarah')

'''
只需稍作修改， 就可以让函数greet_user() 不仅向用户显示Hello! ， 还将用户的名字用作抬头。
为此， 可在函数定义def greet_user() 的括号内添加username 。 通过在这里添加username ，
就可让函数接受你给username 指定的任何值。
现在， 这个函数要求你调用它时给username 指定一个值。 调用greet_user() 时，
可将一个名字传递给它， 如下所示：
代码greet_user('jesse') 调用函数greet_user() ，
并向它提供执行print 语句所需的信息。 这个函数接受你传递给它的名字， 并向这个人发出问候：
'''
'''
同样， greet_user('sarah') 调用函数greet_user() 并向它传递'sarah' ，
 打印Hello, Sarah! 。 你可以根据需要调用函数greet_user() 任意次，
 调用时无论传入什么样的名字， 都会生成相应的输出。
'''
