"""一组用于表示燃油汽车和电动汽车的类"""


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性
        
        Arguments:
            make {str} -- 汽车的品牌
            model {str} -- 型号
            year {int} -- 生产年份
        """

        self.make = make
        self.model = model
        self.year = year
        self.odomenter_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odomenter(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odomenter_reading) + " miles on it.")

    def update_odomenter(self, mileage):
        """
        将里程表读书设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odomenter_reading:
            self.odomenter_reading = mileage
        else:
            print("You can't roll back an odomenter!")

    def increment_odomenter(self, miles):
        """将里程表读数增加指定的量"""
        self.odomenter_reading += miles

    def fill_gas_tank(self):
        """汽车有邮箱"""
        print("This car have a gas tank!")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """        
        电动汽车的独特之处
        初始化父类的属性, 再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动汽车没有邮箱"""
        print("This car doesn't need a gas tank!")


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            print("This car has been upgraded!")
        else:
            print("This car can't be upgrade.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程
        """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a %s -kWh battery." % str(self.battery_size))