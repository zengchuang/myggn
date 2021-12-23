# 在下面的示例中， 存储了比萨的两方面信息：
# 外皮类型和配料列表。 其中的配料列表是一个与键'toppings'
# 相关联的值。 要访问该列表， 我们使用字典名和键'toppings'
# ， 就像访问字典中的其他值一样。 这将返回一个配料列表， 而不是单个值

#储存所点比萨的信息
pizza = {
    'crusr':'thick',
    'toppings':['mushrooms','extra cheese'],
}

#概述所点的比萨
print("You ordered a " + pizza['crusr'] + "-crusr pizza"
      + " with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
    