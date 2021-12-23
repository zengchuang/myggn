#首先,创建一个待验证用户列表
#和一个用于储存已验证用户的空列表
unconfirmed_user = ['alice','brian','candace']
confirmed_user = []

#验证每个用户,直到没有未验证用户为止
#将每个经过验证的列表都移到已验证用户列表中

while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print("Verifying user:"+current_user.title())
    confirmed_user.append(current_user)
    
#显示所有已验证的用户
print("\nThe following user have been confirmed:")
for confirmed_user in confirmed_user:
    print(confirmed_user.title())
'''
我们首先创建了一个未验证用户列表（见❶） ， 其中包含用户Alice、 Brian和Candace，
还创建了一个空列表， 用于存储已验证的用户。 ❷处的while 循环将不断地运行， 直到列
表unconfirmed_users 变成空的。 在这个循环中，
❸处的函数pop() 以每次一个的方式从列表unconfirmed_users 末尾删除未验证的用户。
 由于Candace位于列表unconfirmed_users 末尾，
 因此其名字将首先被删除、 存储到变量current_user 中并加入到列表confirmed_users 中（见❹） 。 接下来是Brian， 然后是Alice。
'''

# 我们首先创建了一个列表， 其中包含多个值为'cat' 的元素。
# 打印这个列表后， Python进入while 循环， 因为它发现'cat' 在列表中至少出现了一次。
# 进入这个循环后， Python删除第一个'cat' 并返回到while 代码行，
# 然后发现'cat' 还包含在列表中， 因此再次进入循环。 它不断删除'cat' ，
# 直到这个值不再包含在列表中， 然后退出循环并再次打印列表
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat') #函数remove() 来删除列表中的特定值
print(pets)


responses = {}
#设置一个标志,指出调查是否继续
polling_active = True

while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    #将答卷储存在字典中
    responses[name] = response
    
    #看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# 调查结束， 显示结果
print("\n--- Poll Results ---")
for name,responses in responses.items():
    print(name + " would like to climb " + responses + ".")

