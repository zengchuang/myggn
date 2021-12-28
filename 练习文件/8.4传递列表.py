'''
你经常会发现， 向函数传递列表很有用， 这种列表包含的可能是名字、 数字或更复杂的对象（如字典） 。
将列表传递给函数后， 函数就能直接访问其内容。 下面使用函数来提高处理列表的效率。
假设有一个用户列表， 我们要问候其中的每位用户。 下面的示例将一个名字列表传递给一个名为greet_users() 的函数， 这个函数问候列表中的每个人：
'''
def greet_users(names):
    '''向列表页中的每位用户都发出简单的问候'''
    for name in names:
        msg = "Hello, " + name.title() +"!"
        print(msg)
usernames = ['hannah','ty','margot']
greet_users(usernames)
'''
我们将greet_users() 定义成接受一个名字列表， 并将其存储在形参names 中。
 这个函数遍历收到的列表， 并对其中的每位用户都打印一条问候语。
 在❶处， 我们定义了一个用户列表——usernames ， 然后调用greet_users() ，
并将这个列表传递给它：输出完全符合预期， 每位用户都看到了一条个性化的问候语。
 每当你要问候一组用户时， 都可调用这个函数。
Hello, Hannah!
Hello, Ty!
Hello, Margot!
'''