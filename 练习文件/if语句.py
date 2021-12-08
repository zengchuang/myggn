
# 以首字母大写的方式打印其中的汽车名， 但对于汽车名'bmw' ， 以全大写的方式打印

cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
       print(car.upper())
    else:
       print(car.title())
