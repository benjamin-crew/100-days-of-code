import random


class User:
    def __init__(self, name, num):
        self.name = name
        self.favourite = num

num = 10

for i in range(0, num):
    i = str(i)
    user = "user" + i
    favourite_number = random.randint(0, 50)
    user = User(user, favourite_number)
    print(f" {user.name} created. He has a favourite number of {user.favourite}")