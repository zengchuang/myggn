'''
有时候， 需要接受任意数量的实参， 但预先不知道传递给函数的会是什么样的信息。
在这种情况下， 可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
一个这样的示例是创建用户简介： 你知道你将收到有关用户的信息， 但不确定会是什么样的信息。
在下面的示例中， 函数build_profile() 接受名和姓， 同时还接受任意数量的关键字实参：
'''
def build_profile(first,last,**user_info):
    """创建一个字典,其中包含我们知道的有关用户的一切"""
    #形参**user_info 中的两个星号让Python创建一个名为user_info 的空字典，
    # 并将收到的所有名称—值对都封装到这个字典中。 在这个函数中，
    # 可以像访问其他字典那样访问user_info 中的名称—值对。
    profile = {}
    
    profile['first_name'] = first #❶
    profile['last_name'] = last
# 在❶处， 我们将名和姓加入到这个字典中， 因为我们总是会从用户那里收到这两项信息。
    for key,value in user_info.items(): #❷
        profile[key] = value
    return profile
# 在❷处， 我们遍历字典user_info 中的键—值对， 并将每个键—值对都加入到字典profile 中。
# 最后， 我们将字典profile 返回给函数调用行。
user_profile = build_profile('albert','einstein',location='princeton',field='physics')
#函数build_profile() 的定义要求提供名和姓， 同时允许用户根据需要提供任意数量的名称—值对。
#在build_profile() 的函数体内， 我们创建了一个名为profile 的空字典， 用于存储用户简介。

print(user_profile)
#我们调用build_profile() ， 向它传递名（'albert' ） 、 姓（'einstein' ）
# 和两个键—值对（location='princeton' 和field='physics' ） ，
# 并将返回的profile 存储在变量user_profile 中， 再打印这个变量：