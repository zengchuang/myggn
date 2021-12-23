'''
有时候， 需要将一系列字典存储在列表中， 或将列表作为值存储在字典中，
这称为嵌套 。 你可以在列表中嵌套字典、 在字典中嵌套列表甚至在字典中嵌套字典。
 正如下面的示例将演示的， 嵌套是一项强大的功能。
'''
'''
字典列表
字典alien_0 包含一个外星人的各种信息， 但无法存储第二个外星人的信息，
 更别说屏幕上全部外星人的信息了。 如何管理成群结队的外星人呢？ 一种办法是创建一个外星人列表，
其中每个外星人都是一个字典， 包含有关该外星人的各种信息。
例如， 下面的代码创建一个包含三个外星人的列表：
'''
alien_0 = {'color':'green','points':'5'}
alien_1 = {'color':'yellow','points':'10'}
alien_2 = {'color':'red','points':'15'}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)
    
# 更符合现实的情形是， 外星人不止三个，
# 且每个外星人都是使用代码自动生成的。 在下面的示例中， 我们使用range() 生成了30个外星人：

#创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色外星人
for alien_number in range(30):#range() 返回一系列数字
    new_alien = {'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)

# 鉴于我们要修改前三个外星人， 需要遍历一个只包含这些外星人的切片。
# 当前， 所有外星人都是绿色的， 但情况并非总是如此，
# 因此我们编写了一条if 语句来确保只修改绿色外星人。
# 如果外星人是绿色的， 我们就将其颜色改为'yellow' ，
# 将其速度改为'medium' ， 并将其点数改为10
for alien in aliens[0:3]:
    if alien['color']== 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'mendium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
    
    #显示前5个外星人
    for alien in aliens[:5]:
        print(alien)
    print("...")
#len()函数
#返回对象的长度参数可以是序列
# （字符串str、元组tuple、列表list）或
# 集合（字典dict、集合set或冻结集合frozenset）
#str() 函数将对象转化为适于人阅读的形式。
print("Total number of aliens: " + str(len(aliens)))
