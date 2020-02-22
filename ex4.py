#how many cars available
cars=100
#space_in_a_car=4.0
# how many space in one car
space_in_a_car=4
# how many drivers today
drivers=30
# how many passengers today
passengers=90
#how many cars can not be use
cars_not_driven=cars-drivers
#how many car could be driven
cars_driven=drivers
#the capacity of cars today
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven

print("there are",cars,"cars available")
print("there are only",drivers,"divers available")
print("there will be",cars_not_driven,"empty cars today")
print("we can transport",carpool_capacity,"people today.")
print("we have",passengers,"to carpool today.")
print("we need to put about",average_passengers_per_car,"in each car.")
