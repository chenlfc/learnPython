from user import User


class Admin(User):
    """模拟管理员用于群的类
    
    Arguments:
        User {class} -- 用户信息基类
    """

    def __init__(self, first_name, last_name, age, sex, privileges):
        """用于初始化管理员信息
        
        Arguments:
            first_name {str} -- 姓
            last_name {str} -- 名
            age {int}} -- 年龄
            sex {str} -- 性别
            privileges {str} -- 权限字符串
        """

        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges(privileges)


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """用于显示管理员得权限
        """
        print("The privileges is %s." % self.privileges)
