class User:
    "Class used for creating a generic user"
    instances = []
    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.followers = 0
        User.instances.append(self)


def ammount_of_users():
    return len(User.instances)

def print_users():

    user_list = []

    for obj in User.instances:
        user_list += [obj.username]
    
    for i in range(0, len(user_list)):
        print(user_list[i])