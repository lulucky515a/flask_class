import random

class User:
    @property
    def pwd(self):
        return random.randint(1, 99)

    @pwd.setter
    def pwd(self, data):
        self.new_prop = data


if __name__ == '__main__':
    user = User()
    print(user.pwd)
    user.pwd = "hello"
    print(user.new_prop)
    print(user.pwd)

