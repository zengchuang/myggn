#输出前3个元素
players = ['py','java','html','jmeter','airtest']
# print(players[0:3])
#输入2-3个元素,终止索引为指定为3
#这一次,切片始于Java,终于html
# print(players[1:3])
# #没有指定索引的话,python将会自动从列表开头开始提取
# print(players[:3])
# #提取从第3个元素到列表末尾的所有元素， 可将起始索引指定为2 ， 并省略终止索引
# print(players[2:])
# #打印最后三个元素
# print(players[-3:])
# 历遍切片
# 遍历整个队员列表， 而只遍历前三名队员
print("here are the first three palyers on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['baishi','xuebi','senlin','chengzhi']
ni_foods = my_foods[:]
my_foods.append('hongniu')
print("ni foods are:")
print(ni_foods)
print("\nmy ni foods:")
print(my_foods)

my_foods = ni_foods
my_foods.append('laji')
ni_foods.append('laji2')
print("TMD:")
print(my_foods)
print(("NMD:"))
print(ni_foods)