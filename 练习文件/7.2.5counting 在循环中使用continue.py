
''
''''
要返回到循环开头， 并根据条件测试结果决定是否继续执行循环， 可使用continue 语句， 它不像break 语句那样不再执行余下的代码并退出整个循环。 例如， 来看一个从1数
到10， 但只打印其中偶数的循环：
'''
''''
Python continue 语句跳出本次循环，而break跳出整个循环。
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue语句用在while和for循环中。
'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
'''
我们首先将current_number 设置成了0， 由于它小于10， Python进入while 循环。
进入循环后， 我们以步长1的方式往上数（见❶） ， 因此current_number 为1。
接下来， if 语句检查current_number 与2的求模运算结果。
如果结果为0（意味着current_number 可被2整除） ， 就执行continue 语句，
让Python忽略余下的代码， 并返回到循环的开头。
如果当前的数字不能被2整除， 就执行循环中余下的代码， Python将这个数字打印出来：
'''

x = 1
while x <= 5:
    print(x)
    x += 1 #不小心遗漏了代码行x += 1 ， 这个循环将没完没了地运行
           # x 的初始值为1 ， 但根本不会变， 因此条件测试x <= 5 始终为True ，
           # 导致while 循环没完没了地打印1
