cars = 100  # 汽车的数量
space_in_a_car = 4.0  # 汽车的乘坐人数
drivers = 30  # 司机的数量
passengers = 90  # 旅客的数量
cars_not_driven = cars-drivers  # 不能运营的车辆数量
cars_driven = drivers  # 能够运营的车辆数量
carpool_capacity = cars_driven*space_in_a_car  # 能够载客的数量
average_passengers_per_car = passengers//cars_driven  # 每辆车上需要乘坐的乘客的数量

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
