''
#可将函数同本书前面介绍的任何Python结构结合起来使用。
# 例如， 下面将结合使用函数get_formatted_name() 和while 循环，
# 以更正规的方式问候用户。 下面尝试使用名和姓跟用户打招呼：
'''
def get_formatted_name(first_name,last_name):
   
    full_name = first_name + ' ' +last_name
    return first_name.title()

# 这是一个无限循环!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formtted_name = get_formatted_name(f_name,l_name)
    print("\nHello, "+formtted_name+"!")
'''
# 在这个示例中， 我们使用的是get_formatted_name() 的简单版本， 不涉及中间名。
# 其中的while 循环让用户输入姓名： 依次提示用户输入名和姓（见❶） 。
# 但这个while 循环存在一个问题： 没有定义退出条件。 请用户提供一系列输入时，
# 该在什么地方提供退出条件呢？ 我们要让用户能够尽可能容易地退出，
# 因此每次提示用户输入时， 都应提供退出途径。
# 每次提示用户输入时， 都使用break 语句提供了退出循环的简单途径

def get_formatted_name(first_name,last_name):
    
    full_name = first_name + ' '+ last_name
    return  full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formtted_name = get_formatted_name(f_name,l_name)
    print("\nHello, "+formtted_name+"!")
#我们添加了一条消息来告诉用户如何退出， 然后在每次提示用户输入时，都检查他输入的是否是退出值，
# 如果是， 就退出循环。 现在， 这个程序将不断地问候， 直到用户输入的姓或名为'q' 为止：