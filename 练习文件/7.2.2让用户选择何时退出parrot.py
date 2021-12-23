''
'''
可使用while 循环让程序在用户愿意时不断地运行，
如下面的程序parrot.py所示。 我们在其中定义了一个退出值， 只要用户输入的不是这个值， 程序就接着运行
'''

'''
在❶处， 我们定义了一条提示消息， 告诉用户他有两个选择： 要么输入一条消息， 要么输入退出值（这里为'quit' ） 。 接下来， 我们创建了一个变量——message （见❷） ，
用于存储用户输入的值。 我们将变量message 的初始值设置为空字符串"" ，
让Python首次执行while 代码行时有可供检查的东西。 Python首次执行while 语句时，
需要将message 的值与'quit' 进行比较， 但此时用户还没有输入。 如果没有可供比较的东西，
Python将无法继续运行程序。 为解决这个问题， 我们必须给变量message 指定一个初始值。
虽然这个初始值只是一个空字符串， 但符合要求， 让Python能够执行while 循环所需的比较。
只要message 的值不是'quit' ， 这个循环（见❸） 就会不断运行。
首次遇到这个循环时， message 是一个空字符串， 因此Python进入这个循环。
执行到代码行message = input(prompt) 时， Python显示提示消息， 并等待用户输入。 不管用
户输入是什么， 都将存储到变量message 中并打印出来； 接下来， Python重新检查while 语句中的条件。
只要用户输入的不是单词'quit' ， Python就会再次显示提示消息并等待用户输入。
等到用户终于输入'quit' 后， Python停止执行while 循环， 而整个程序也到此结束：
'''

parrot = "\nThell me something, and I will repeat it back to you:"
parrot += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(parrot)
    if message != 'quit':  #现在， 程序在显示消息前将做简单的检查， 仅在消息不是退出值时才打印它：
        print(message)

'''
这个程序很好， 唯一美中不足的是， 它将单词'quit' 也作为一条消息打印了出来。
为修复这种问题， 只需使用一个简单的if 测试：
'''
