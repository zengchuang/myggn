
# 7-1 汽车租赁 ： 编写一个程序， 询问用户要租赁什么样的汽车， 并打印一条消息，
# 如“Let me see if I can find you a Subaru”。

car = input("What car are you looking for? ")
print("Let me see if I can find you a " + car + ".")

# 7-2 餐馆订位 ： 编写一个程序， 询问用户有多少人用餐。 如果超过8人， 就打印一条消息， 指出没有空桌； 否则指出有空桌。
Restaurant = input("How many of you are coming to dinner? ")
Restaurant = int(Restaurant)

if Restaurant > 8:
    print("There is no room for more than eight people in our restaurant!")
else:
    print("OK,rhis way,l'll make a reservation for you rughtaway.")
    
# 7-3 10的整数倍 ： 让用户输入一个数字， 并指出这个数字是否是10的整数倍。

shu = input("请输入大于10的数字:")
shu = int(shu)

if shu % 2 == 0 :
    print("这个数是10的整倍数!")
else:
    print("这个数不是10的整倍数..")