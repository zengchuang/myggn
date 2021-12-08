cars = 100

space_in_a_car = 4.0

drivers = 30

passengers = 90

#这里意思就是 cars_not_driven这个变量等于cars(100)-drivers(30)=70,这个变量就是70
cars_not_driven = cars - drivers 
 
#cars_driven这个变量是30
cars_driven = drivers

#carpool_capacity这个变量是等于30*4 = 120
carpool_capacity = cars_driven * space_in_a_car

#变量数值等于90/30 = 3
average_passengers_per_car = passengers / cars_driven


print ("There are",cars,"cars available.")

print ("There are only", drivers, "drivers available.")

print ("There will be", cars_not_driven, "empty cars today.")

print ("We can transport", carpool_capacity, "people today.")

print ("We need to put about", average_passengers_per_car, "ineach car.")
