'''
函数get_formatted_name() 的定义通过形参接受名和姓（见❶） 。 它将姓和名合而为一， 在它们之间加上一个空格， 并将结果存储在变量full_name 中（见❷） 。 然后，
将full_name 的值转换为首字母大写格式， 并将结果返回到函数调用行（见❸） 。
调用返回值的函数时， 需要提供一个变量， 用于存储返回的值。 在这里， 将返回值存储在了变量musician 中（见❹） 。 输出为整洁的姓名
'''
def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)


'''
只要同时提供名、 中间名和姓， 这个函数就能正确地运行。 它根据这三部分创建一个字符串，
 在适当的地方加上空格， 并将结果转换为首字母大写格式：

'''

def get_formatted_name(first_name,middle_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + middle_name +' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi','lee','hendrix')
print(musician)


'''
然而， 并非所有的人都有中间名， 但如果你调用这个函数时只提供了名和姓， 它将不能正确地运行。 为让中间名变成可选的， 可给实参middle_name 指定一个默认值——空字
符串， 并在用户没有提供中间名时不使用这个实参。 为让get_formatted_name() 在没有提供中间名时依然可行， 可给实参middle_name 指定一个默认值——空字符串，
并将其移到形参列表的末尾：
'''
def get_formatted_name(first_name,last_name,middle_name=''):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + ' ' + middle_name +' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)

'''
在这个示例中， 姓名是根据三个可能提供的部分创建的。 由于人都有名和姓， 因此在函数定义中首先列出了这两个形参。 中间名是可选的， 因此在函数定义中最后列出该形参，
并将其默认值设置为空字符串（见❶） 。
在函数体中， 我们检查是否提供了中间名。 Python将非空字符串解读为True ， 因此如果函数调用中提供了中间名， if middle_name 将为True （见❷） 。 如果提供了中间
名， 就将名、 中间名和姓合并为姓名， 然后将其修改为首字母大写格式， 并返回到函数调用行。 在函数调用行， 将返回的值存储在变量musician 中； 然后将这个变量的值打印
出来。 如果没有提供中间名， middle_name 将为空字符串， 导致if 测试未通过， 进而执行else 代码块（见❸） ： 只使用名和姓来生成姓名， 并将设置好格式的姓名返回给函
数调用行。 在函数调用行， 将返回的值存储在变量musician 中； 然后将这个变量的值打印出来。
调用这个函数时， 如果只想指定名和姓， 调用起来将非常简单。 如果还要指定中间名， 就必须确保它是最后一个实参， 这样Python才能正确地将位置实参关联到形参（见❹） 。
这个修改后的版本适用于只有名和姓的人， 也适用于还有中间名的人：
'''

