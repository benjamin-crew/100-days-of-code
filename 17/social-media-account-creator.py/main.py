from classes import User, ammount_of_users, print_users

allow_signup = True
while allow_signup is True:

    users = ammount_of_users()

    print(users)

    if users < 3:

        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        user_id = (users + 1)

        username = User(username, password, user_id)
    else:
        print("We have too many users at this time.")
        allow_signup = False

print_users()