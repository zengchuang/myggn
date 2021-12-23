
# 7-4 比萨配料 ： 编写一个循环， 提示用户输入一系列的比萨配料，
# 并在用户输入'quit' 时结束循环。 每当用户输入一种配料后，
# 都打印一条消息， 说我们会在比萨中添加这种配料。

# pizza = "\n请输入您需要的pizza配料:"
# pizza += "\n配料输入完成后,请输入'quit'结束程序"
#
# active = True
# while active:
#     message = input(pizza)
#
#     if message == 'quit':
#         break
#     else:
#         print("好的,我们会在pizza里添加" + message + "!")
        
# 7-5 电影票 ： 有家电影院根据观众的年龄收取不同的票价：
# 不到3岁的观众免费； 3~12岁的观众为10美元； 超过12岁的观众为15美元。 请编写一个循环，
# 在其中询问用户的年龄， 并指出其票价。
# dian = "请输入年龄获取票价:"
#
# while True:
#
#     try:
#         shuru = int(input(dian))
#     except:
#         print("输入有误，请输入正整数")
#     else:
#
#         shuru = int(shuru)
#         if shuru < 3:
#             print("不到" + str(shuru) + "岁的观众免费" + "!")
#         elif shuru <=12:
#             print(str(shuru) + "岁的观众,票价是10美元" + "!")
#         elif shuru >12:
#             print("超过12岁的观众票价是15美元," + "你的年龄是" + str(shuru))

dian = "请输入年龄获取票价:"

while True:

    try:
        shuru = int(input(dian))
        if shuru >= 0 or shuru < 100:
            shuru = int(shuru)

            if shuru < 3:
                print("不到" + str(shuru) + "岁的观众免费" + "!")
            elif shuru <= 12:
                print(str(shuru) + "岁的观众,票价是10美元" + "!")
            elif shuru > 12:
                print("超过12岁的观众票价是15美元," + "你的年龄是" + str(shuru))
            # elif shuru < 3 or shuru <= 12 or shuru > 12:
            #     pass
        break
    except:

        print("输入有误，请输入1~100的正整数")