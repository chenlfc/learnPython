from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """这是一个模拟冰淇淋小店的类
    
    Arguments:
        Restaurant {class} -- 一个模拟餐厅的基类
            icecreamstand_name {str} -- 冰淇淋小店的名字
            icecreamstand_type {str} -- 冰淇淋小店的类型
            icecreamstand_flavors {list} -- 冰淇淋的种类
        Keyword Arguments:
            number_served {int} -- 服务过的人数 (default: {0})
    """

    def __init__(self,
                 icecreamstand_name,
                 icecreamstand_type,
                 icecreamstand_flavors,
                 number_served=0):
        """用于初始冰淇淋小店的基本信息
        """

        super().__init__(icecreamstand_name, icecreamstand_type, number_served)
        self.flavors = icecreamstand_flavors

    def describe_flavors(self):
        print("%s冰淇淋小店的冰淇淋品种列表:" % self.restaurant_name)
        print("-" * 40)
        for f in self.flavors:
            print(f + "口味冰淇淋")
