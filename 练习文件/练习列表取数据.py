# 全部打印出来
# friend = ['liuqinghan','xiaolong','xiaoyanlin','duge','songdao']
# print(friend)

# 只打印第一个元素
friend = ['liuqinghan', 'xiaolong', 'xiaoyanlin', 'duge', 'songdao']
print(friend[0])

# 整洁的取第一个元素,第一个字母变大写  upper() 就是全部变成大写
friend = ['liuqinghan', 'xiaolong', 'xiaoyanlin', 'duge', 'songdao']
print(friend[0].title())

# 取最后一个元素
# friend = ['liuqinghan','xiaolong','xiaoyanlin','duge','songdao']
# print(friend[-1])

# 取倒数第三个元素
# friend = ['liuqinghan','xiaolong','xiaoyanlin','duge','songdao']
# print(friend[-3])


# friend = ['liuqinghan','xiaolong','xiaoyanlin','duge','songdao']
# name = "我叫" + friend[0].title() + "大家好!"
# print(name)


friend = ['liuqinghan', 'xiaolong', 'xiaoyanlin', 'duge', 'songdao']
name = "我叫" + friend[0] + "大家好!"
print(name)


kongge = ' python '
kongge = kongge.strip()
print(kongge)

s = ' this is a puppy '
# 删除左边空白
print(s.lstrip())
# 删除右边空白
print(s.rstrip())
# 删除两边的空白
print(s.strip())
# 再次输出s,将会看到s并没有改变
print(s)

# 下面代码示范了删除字符串前后指定宇符的功能

s2 = 'i think it a scarecrow'
# 删除左边的i t o w字符
print(s2.lstrip('itow'))
# 删除右边的itow字符
print(s2.rstrip('itow'))
# 删除两边的itow字符
print(s2.strip('itow'))
