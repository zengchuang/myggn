def describe_pet(animal_type,pet_name):
    ''' 显示宠物的信息 '''
    print("\nI habe a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
'''
关键字实参 是传递给函数的名称—值对。 你直接在实参中将名称和值关联起来了， 因此向函数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果） 。 关键字实参让
你无需考虑函数调用中的实参顺序， 还清楚地指出了函数调用中各个值的用途。
下面来重新编写pets.py， 在其中使用关键字实参来调用describe_pet() ：
函数describe_pet() 还是原来那样， 但调用这个函数时， 我们向Python明确地指出了各个实参对应的形参。 看到这个函数调用时， Python知道应该将实参'hamster'
和'harry' 分别存储在形参animal_type 和pet_name 中。 输出正确无误， 它指出我们有一只名为Harry的仓鼠。
关键字实参的顺序无关紧要， 因为Python知道各个值该存储到哪个形参中。 下面两个函数调用是等效的：
注意 使用关键字实参时， 务必准确地指定函数定义中的形参名。
'''

'''
8.2.3 默认值
编写函数时， 可给每个形参指定默认值 。 在调用函数中给形参提供了实参时， Python将使用指定的实参值； 否则， 将使用形参的默认值。 因此， 给形参指定默认值后， 可在函数
调用中省略相应的实参。 使用默认值可简化函数调用， 还可清楚地指出函数的典型用法。
例如， 如果你发现调用describe_pet() 时， 描述的大都是小狗， 就可将形参animal_type 的默认值设置为'dog' 。 这样， 调用describe_pet() 来描述小狗时， 就可不
提供这种信息：
'''
#这里修改了函数describe_pet() 的定义，
# 在其中给形参animal_type 指定了默认值'dog' 。
# 这样，调用这个函数时，如果没有给animal_type 指定值，
# Python将把这个形参设置为'dog' ：
def describe_pet(pet_name,animal_type='dog'):
    print("\nI habe a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='willie')
# 请注意,在这个函数的定义中， 修改了形参的排列顺序。
# 由于给animal_type 指定了默认值， 无需通过实参来指定动物类型，
# 因此在函数调用中只包含一个实参——宠物的名字。
# 然而，Python依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，
# 这个实参将关联到函数定义中的第一个形参。 这就是需要将pet_name 放在形参列表开头的原因所在。
# 现在， 使用这个函数的最简单的方式是， 在函数调用中只提供小狗的名字：
describe_pet('willie')#这里输出还是和上面一样的.
# 这个函数调用的输出与前一个示例相同。
# 只提供了一个实参——'willie' ， 这个实参将关联到函数定义中的第一个形参——pet_name 。
# 由于没有给animal_type 提供实参， 因此Python使用其默认值'dog' 。

#如果要描述的动物不是小狗， 可使用类似于下面的函数调用：
describe_pet(pet_name='harry',animal_type='hamster')
#由于显式地给animal_type 提供了实参， 因此Python将忽略这个形参的默认值。


'''
8.2.4 等效的函数调用
鉴于可混合使用位置实参、 关键字实参和默认值， 通常有多种等效的函数调用方式。
请看下面的函数describe_pets() 的定义， 其中给一个形参提供了默认值：
'''
def describe_pe(pet_name,animal_type='dog'):
    print('I like ' + pet_name)
    print('I like '+ pet_name)
# 基于这种定义， 在任何情况下都必须给pet_name
# 提供实参； 指定该实参时可以使用位置方式， 也可以使用关键字方式。
#如果要描述的动物不是小狗， 还必须在函数调用中给animal_type
# 提供实参； 同样， 指定该实参时可以使用位置方式， 也可以使用关键字方式。
# 下面对这个函数的所有调用都可行：
#一条名为willie的小狗
describe_pe('willie')
describe_pe(pet_name='willie')

#一只名为Harry的仓鼠
describe_pe('harry','hamster')
describe_pe(pet_name='harry',animal_type='hamster')
describe_pe(animal_type='hamster',pet_name='harry')
# 这些函数调用的输出与前面的示例相同。
# 注意 使用哪种调用方式无关紧要， 只要函数调用能生成你希望的输出就行。
# 使用对你来说最容易理解的调用方式即可。