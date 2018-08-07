class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def dog_info(self):
        """以标准格式输出小狗的信息"""
        print("Dog's name is " + self.name.title() + ".")
        print("Dog is " + str(self.age) + " years old.")
        print("-" * 72)

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('Harry', 14)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.dog_info()

my_dog.sit()
my_dog.roll_over()

print("-" * 72)

small_dog = Dog('willie', 6)
print("Small dog's name is " + small_dog.name.title() + ".")
print("Small dog is " + str(small_dog.age) + " years old.")
my_dog.dog_info()

small_dog.sit()
small_dog.roll_over()
