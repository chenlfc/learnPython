class User:
    # first_name: str
    # last_name: str
    # age: int
    # sex: str
    # full_name: str = first_name + ' ' + last_name

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("The name is: " + self.first_name.title() + " " +
              self.last_name.title() + ".")
        print("The age is: " + str(self.age) + ".")
        print("The gender is: " + self.sex.upper() + ".")

    def greet_user(self):
        print("Hello " + self.full_name.title() + ".")


# first_user = User("Jack", "Lee", 32, "M")
# last_user = User("Maleen", "Jiang", 24, "F")

# first_user.describe_user()
# first_user.greet_user()

# last_user.describe_user()
# last_user.greet_user()

# first_user.increment_login_attempts()
# print("%s login attempts is %d." % (first_user.full_name,
#                                     first_user.login_attempts))
# first_user.increment_login_attempts()
# print("%s login attempts is %d." % (first_user.full_name,
#                                     first_user.login_attempts))
# first_user.increment_login_attempts()
# print("%s login attempts is %d." % (first_user.full_name,
#                                     first_user.login_attempts))
# first_user.reset_login_attempts()
# print("%s login attempts is %d." % (first_user.full_name,
#                                     first_user.login_attempts))
