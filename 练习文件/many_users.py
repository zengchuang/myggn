"""
在字典中存储字典
可在字典中嵌套字典， 但这样做时， 代码可能很快复杂起来。 例如， 如果有多个网站用户， 每个都有独特的用户名，
可在字典中将用户名作为键， 然后将每位用户的信息存储在一个字典中，
并将该字典作为与用户名相关联的值。 在下面的程序中，
对于每位用户， 我们都存储了其三项信息： 名、 姓和居住地；
为访问这些信息， 我们遍历所有的用户名，并访问与每个用户名相关联的信息字典：
"""

'''
我们首先定义了一个名为users 的字典， 其中包含两个键： 用户名'aeinstein' 和'mcurie' ；
与每个键相关联的值都是一个字典， 其中包含用户的名、 姓和居住地。
在❶处， 我们遍历字典users ， 让Python依次将每个键存储在变量username 中，
并依次将与当前键相关联的字典存储在变量user_info 中。
在主循环内部的❷处， 我们将用户名打印出来。
在❸处， 我们开始访问内部的字典。 变量user_info 包含用户信息字典，
而该字典包含三个键： 'first' 、 'last' 和'location' ； 对于每位用户， 我们都使用这些键来
生成整洁的姓名和居住地， 然后打印有关用户的简要信息（见❹） ：
'''

users = {
    'aeinstein':{'first':'albert',
                 'last':'einstein',
                 'location':'princeton'},
    'mcurie':{'first':'marie',
              'last':'curie',
              'location':'paris'},
}#❶处
for username,user_info in users.items():#items用于字典, 作用是以列表返回可遍历的(key, value)的元组数组
    print("\nUsername:" + username)#❷处
    full_name = user_info['first'] + " " + user_info['last']#❸处
    location = user_info['location']
    
    print("\tFull name:" + full_name.title())#❹
print("\tLocation:" + location.title())

