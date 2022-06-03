class User:
    def __init__(self, first_name, last_name, age, email, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = login_attempts

    def describe_user(self):
        return f"Ви увійшли як {self.first_name} {self.last_name}"

    def greeting_user(self):
        return f"З поверненням {self.first_name}!"

    def increment_login_attempts(self):
        return self.login_attempts + 1

    def reset_login_attempts(self):
        login_attempts = 0
        return login_attempts

    pass


us1 = User("Андріана", "Руснак", "18", "rusnak.andriana@chnu.edu.ua", 2)
us2 = User("Ліана", "Лисак", "18", "lysak.liana@chnu.edu.ua", 1)

print(us1.describe_user())
print(us1.greeting_user())

print(us2.describe_user())
print(us2.greeting_user())

print(us1.increment_login_attempts())
print(us2.increment_login_attempts())
print(us2.reset_login_attempts())


class Admin(User):
    def __init__(self):
        self.priv = list([["«Allowed to add message»"],
                          ["«Allowed to delete users»"],
                          ["«Allowed to ban users»"]])

    def show_privileges(self):
        return self.priv

    pass


Admin = Admin()
print(Admin.show_privileges())


class Privileges():
    def __init__(self):
        self.privilegies = list([["«Allowed to add message»"],
                                 ["«Allowed to delete users»"],
                                 ["«Allowed to ban users»"]])

    def show_privileges(self):
        return self.privilegies

    pass


admin = Privileges()
print(admin.show_privileges())

print
