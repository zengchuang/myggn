'''
题目:
检测用户输入得密码强度.要求密码长度6-16位,可以包含数字,英文大小写,标点符号中得1种或几种
自动检测用户输入的密码,显示强度分类:弱,中,强,很强.'''

import getpass

a = getpass.getpass('password')
# a = input('psaaword')
b = len(a)

for i in a:
    if b is None:
        print('请输入最少6位长度密码')
        break
    if b < 6:
        print('请输入最少6位长度密码')
        break
    elif b < 8:
        print("密码弱")
        break
    elif b < 11:
        print("密码中")
        break
    elif b < 13:
        print("密码强")
        break
    elif b < 17:
        print("密码很强")
        break
    else:
        print("你的密码超过长度")
        breal
