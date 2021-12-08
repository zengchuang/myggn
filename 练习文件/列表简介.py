#将列表全部打印出来
test = ['python','airtest','postman','fidder']
print(test)

#访问列表元素的语法,当你请求获取列表元素时,python只返回该元素,而不包括方括号和引号
test = ['python','airtest','postman','fodder','jmeret']
print(test[0])

#使用方法title()让元素'python'的格式更整洁
test = ['python','airtest','postman','fodder','jmeret']
print(test[0].title())

test = ['python','airtest','postman','foddle']
print(test[1])
print(test[3])

#python为访问最后一个列表元素提供一种特殊语法.通过将索引指定为-1,就可以拿到最后的一个元素
test = ['python','airtest','postman','foddle']
print(test[-1])

#-2返回倒数第二个
test = ['python','airtest','postman','foddle']
print(test[-2])

#可以使用拼接根据列表中的值来创建消息
test = ['python','airtest','postman','foddle']
message = "My first test was a " + test[0].title() + "."
print(message)


name = ['liuqinghan','liuxunlin','dujunfeng','songdao','gongjianbo']
fin = "my friend's name ".title() + name[0] + '!!'
print(fin)