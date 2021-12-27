# 8-3 T恤 ： 编写一个名为make_shirt() 的函数， 它接受一个尺码以及要印到T恤上的字样。
# 这个函数应打印一个句子， 概要地说明T恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件T恤； 再使用关键字实参来调用这个函数。

def make_shirt(size='XL',word='I love python'):
    print("这件T恤的尺码是 "+size+" !")
    print("T恤正面印有 "+word+" 的字样")
make_shirt()


# 8-4 大号T恤 ： 修改函数make_shirt() ， 使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
# 调用这个函数来制作如下T恤： 一件印有默认字样的大号T恤、 一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要） 。

make_shirt(size='大号T恤')
make_shirt(size='中号T恤')
make_shirt(word='china')

# 8-5 城市 ： 编写一个名为describe_city() 的函数， 它接受一座城市的名字以及该城市所属的国家。
# 这个函数应打印一个简单的句子， 如Reykjavik is inIceland 。
# 给用于存储国家的形参指定默认值。 为三座不同的城市调用这个函数， 且其中至少有一座城市不属于默认国家。

def describe_city(city,country='china'):
    print(city+"是属于"+country)

describe_city(city='深圳')
describe_city(city='北京')
describe_city(city='莫斯科不')
