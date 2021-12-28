# Python 定义函数使用 def 关键字，一般格式如下：
#
# def 函数名（参数列表）:
#     函数体
# 默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。

def hello():
    print("Hello World!")
hello()

#更复杂点的应用，函数中带上参数变量:
#比较两个数，并返回较大的数:
def max(a,b):
    if a>b:
        return a
    else:
        return b
a = 4
b = 5
print(max(a,b))

#计算面积函数:
def area(width,height):
    return width * height
def print_welcome(name):
    print("Wlecome",name)
print_welcome("Runoob")
w = 4
h = 5
print("width =",w,"height =",h,"area =",area(w,h))

