''''''
'''
while 循环简介
for 循环用于针对集合中的每个元素都一个代码块， 而while 循环不断地运行， 直到指定的条件不满足为止。
'''
# while 循环从1数到5：

# 在第1行， 我们将current_number 设置为1， 从而指定从1开始数。 接下来的while 循环被设置成这样：
# 只要current_number 小于或等于5， 就接着运行这个循环。
# 循环中的代码打印current_number 的值， 再使用代码current_number += 1
# （代码current_number = current_number + 1 的简写） 将其值加1。
# 只要满足条件current_number <= 5 ， Python就接着运行这个循环。 由于1小于5，
# 因此Python打印1 ， 并将current_number 加1， 使其为2 ； 由于2小于5， 因此Python打印2 ，
# 并将current_number 加1 ， 使其为3 ， 以此类推。 一旦current_number 大于5， 循环将停止， 整个程序也将到此结束：
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
    