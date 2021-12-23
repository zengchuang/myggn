
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
'''
我们将变量active 设置成了True （见❶） ， 让程序最初处于活动状态。
这样做简化了while 语句， 因为不需要在其中做任何比较——相关的逻辑由程序的其他部分处理。
只要变量active 为True ， 循环就将继续运行（见❷） 。
在while 循环中， 我们在用户输入后使用一条if 语句来检查变量message 的值。
如果用户输入的是'quit' （见❸） ， 我们就将变量active 设置为False ，
这将导致while 循环不再继续执行。 如果用户输入的不是'quit' （见❹） ， 我们就将输入作为一条消息打印出来。
这个程序的输出与前一个示例相同。 在前一个示例中， 我们将条件测试直接放在了while 语句中， 而在这个程序中， 我们使用了一个标志来指出程序是否处于活动状态， 这样如
果要添加测试（如elif 语句） 以检查是否发生了其他导致active 变为False 的事件， 将很容易。 在复杂的程序中， 如很多事件都会导致程序停止运行的游戏中， 标志很有
用： 在其中的任何一个事件导致活动标志变成False 时， 主游戏循环将退出， 此时可显示一条游戏结束消息， 并让用户选择是否要重新玩。
'''

