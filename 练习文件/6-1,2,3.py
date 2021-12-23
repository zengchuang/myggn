#字典用放在花括号{} 中的一系列键—值对表示
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#返回字典alien_0 中与键'color' 相关联的值green
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned "+str(new_points)+' points!')

#首先定义了一个表示外星人alien_0 的字典， 其中只包含这个外星人的颜色。
# 接下来， 我们将与键'color' 相关联的值改为'yellow' 。
# 输出表明， 这个外星人确实从绿色变成了黄色：
alien_1 = {'color':'green'}
print("The alien is "+ alien_1['color'] +'.' )

alien_1['color'] = 'yellow'
print("The alien is now "+ alien_1['color'] + '.')

# 一个更有趣的例子： 对一个能够以不同速度移动的外星人的位置进行跟踪。
# 为此， 我们将存储该外星人的当前速度， 并据此确定该外星人将向右移动多远：

alien_2 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: " + str(alien_2['x_position']))

#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的速度一定很快
    x_increment = 3
#新文职等于老位置加上增量
alien_2['x_position'] = alien_2['x_position']+x_increment
print("new x-position:" + str(alien_2['x_position']))

#删除
shanchu = {'1':1,'2':2}
del shanchu['1']
print(shanchu)

#由类似对象组成的字典
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
#为获悉Sarah 喜欢的语言， 我们使用如下代码favorite_languages['sarah']
print("sarah's favorite language is "+
      favorite_languages['sarah'].title()
      +".")

# 6-1 人 ： 使用一个字典来存储一个熟人的信息， 包括名、 姓、 年龄和居住的城市。
# 该字典应包含键first_name 、 last_name 、 age 和city 。 将存储在该字典中的每项信息都打印出来。
xiaoming = {'first_name':'ming','last_name':'xiao','age':'18','city':'shenzhen'}
print(xiaoming)

# 6-2 喜欢的数字 ： 使用一个字典来存储一些人喜欢的数字。 请想出5个人的名字， 并将这些名字用作字典中的键；
# 想出每个人喜欢的一个数字， 并将这些数字作为值存储在字典中。 打印每个人的名字和喜欢的数字。 为让这个程序更有趣，
# 通过询问朋友确保数据是真实的。
shuzi = {
    'tu':'1',
    'hong':'2',
    'nan':'3',
    'simon':'4',
    'car':'5',
}
print(shuzi)

# 6-3 词汇表 ： Python字典可用于模拟现实生活中的字典， 但为避免混淆， 我们将后者称为词汇表。
# 想出你在前面学过的5个编程词汇， 将它们用作词汇表中的键， 并将它们的含义作为值存储在词汇表中。
# 以整洁的方式打印每个词汇及其含义。 为此， 你可以先打印词汇， 在它后面加上一个冒号， 再打印词汇的含义； 也可在一行打印词汇，
# 再使用换行符（\n ） 插入一个空行， 然后在下一行以缩进的方式打印词汇的含义
python = {
    'title()':'title() 以首字母大写的方式显示每个单词， 即将每个单词的首字母都改为大写',
    'lower()':'lower()把字母全部变成小写',
    'append()':'添加元素到最后',
    'pop()':'方法pop() 可删除列表末尾的元素， 并让你能够接着使用它',
    'str()':'str() 函数将对象转化为适于人阅读的形式。例如sty(python)',
}
print("\ntitle()这个是做啥用的? " + python['title()'] +'.')
print("\nlower()这个有啥作用? "+python['lower()'] +'.')
print("\nappend()这个呢? "+ python['append()'] + '.')
#items() 方法的遍历：items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回。
d = {'one':1,'two':2,'three':3}
print(d.items())

for key,value in d.items():#当两个参数时
    print(key + ":" + str(value))
    
for i in d.items():#当一个参数时
    print(i)
    
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key,value in user_0.items():
    print('\nkey:'+ key)
    print('value:' + value)
    
for name,languages in favorite_languages.items():
    print(name.title()+"'s favorite language is "
          + languages.title() + ".")
#在不需要使用字典中的值时， 方法keys() 很有用。
# 下面来遍历字典favorite_languages ， 并将每个被调查者的名字都打印出来


friends = ['phil','sarah']
for name in favorite_languages.keys():#Python提取字典favorite_languages 中的所有键， 并依次将它们存储到变量name 中。 输出列出了每个被调查者的名字
    print(name.title())
if name in friends:
    print(" Hi " + name.title() +#title就是单词的开头为大写,其余为小写
          ", I see your favorite language is " +
          favorite_languages[name].title() + "!")
    
    

