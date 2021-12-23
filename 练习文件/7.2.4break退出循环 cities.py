
''
'''
以while True 打头的循环（见❶） 将不断运行， 直到遇到break 语句。 这个程序中的循环不断输入用户到过的城市的名字， 直到他输入'quit' 为止。 用户输入'quit'
后， 将执行break 语句， 导致Python退出循环：

在任何Python循环中都可使用break 语句。 例如， 可使用break 语句来退出遍历列表或字典的for 循环
'''

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' whe you are finished.)"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
        