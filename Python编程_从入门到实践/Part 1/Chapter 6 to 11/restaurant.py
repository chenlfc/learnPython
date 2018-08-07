class Restaurant():
    """一个表示餐馆的类"""

    def __init__(self, restaurant_name, restaurant_type, number_served=0):
        """餐厅的名字和类型"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = number_served

    def describe_restaurant(self):
        """用于输出餐厅的名字和类型"""
        print("The restaurant's name is " + self.restaurant_name.title() + ".")
        print("Restaurant type is " + self.restaurant_type.title() +
              " restaurant.")

    def open_restaurant(self):
        """用于输出餐厅是否营业"""
        print("The restaurant is OPEN!")

    def describe_served(self):
        print("The %s restaurant have %d peoples served." % (
            self.restaurant_name, self.number_served
        ))

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, number_served):
        if number_served <= 50:
            self.number_served += number_served
        else:
            print("超出餐厅每天能接待人数的上限了！")


# restaurant = Restaurant("O.C. RST", "Chinese")
# restaurant.describe_restaurant()
# restaurant.describe_served()
# restaurant.set_number_served(23)
# restaurant.describe_served()
# restaurant.increment_number_served(24)
# restaurant.describe_served()
# restaurant.increment_number_served(55)


# my_restaurant = Restaurant("A'J RST", "CHINESE")
# print("My restaurant's name is " +
# 	my_restaurant.restaurant_name.title() + ".")
# print("My restaurant type is " +
# 	my_restaurant.restaurant_type + "restaurant.")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# your_restaurant = Restaurant("Jack's RST", "JAPANESE")
# your_restaurant.describe_restaurant()

# hes_restaurant = Restaurant("Stven's RST", "ABC")
# hes_restaurant.describe_restaurant()
