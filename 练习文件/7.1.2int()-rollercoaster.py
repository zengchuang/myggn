# 7.1.2 使用int() 来获取数值输入
# # 使用函数input() 时， Python将用户输入解读为字符串。 请看下面让用户输入其年龄的解释器会话

age = input("How old are you? ")
print(age)
age = int(age)#可使用函数int() ， 它让Python将输入视为数值。 函数int() 将数字的字符串表示转换为数值表示
age >= 18
# age >= 18  '>=' not supported between instances of 'str' and 'int'

# 用户输入的是数字21， 但我们请求Python提供变量age 的值时，
# 它返回的是'21' ——用户输入的数值的字符串表示。 我
# 们怎么知道Python将输入解读成了字符串呢？ 因为这个数字用引号括起了。
# 如果我们只想打印输入， 这一点问题都没有； 但如果你试图将输入作为数字使用， 就会引发错误：


# 这个程序中， 为何可以将height 同36 进行比较呢？ 因为在比较前，
# height = int(height) 将输入转换成了数值表示。 如果输入的数字大于或等于36，
# 我们就告诉用户他满足身高条件：
height = input("How tall are you, in inches? ")
height = int(height)
#print(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")