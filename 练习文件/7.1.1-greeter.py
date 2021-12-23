

# 函数input() 接受一个参数： 即要向用户显示的提示 或说明，
# 让用户知道该如何做。 在这个示例中， Python运行第1行代码时，
# 用户将看到提示Tell me something, andI will repeat it back to you: 。
# 程序等待用户输入， 并在用户按回车键后继续运行。 输入存储在变量message 中，
# 接下来的print(message) 将输入呈现给用户
name = input("Please enter your name:")
print("Hello," + name + "!")

# 有时候， 提示可能超过一行， 例如， 你可能需要指出获取特定输入的原因。
# 在这种情况下， 可将提示存储在一个变量中， 再将该变量传递给函数input() 。
# 这样， 即便提示超过一行， input() 语句也非常清晰。
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nwhat is your first name? "

name = input(prompt)
print("\nHello,"+name + "!")
# 这个示例演示了一种创建多行字符串的方式。 第1行将消息的前半部分存储在变量prompt 中；
# 在第2行中， 运算符+= 在存储在prompt 中的字符串末尾附加一个字符串。
# 最终的提示横跨两行， 并在问号后面包含一个空格， 这也是出于清晰考虑：
