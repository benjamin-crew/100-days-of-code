height = int(input("Please enter your height in cm: "))

if height >= 120:
    print("You can ride the rollcoaster!")
    age = int(input("What is your age?: "))

    if age < 12:
        print("Please pay £5.")
    elif age <= 18:
        print("Please pay £7.")
    else:
        print("Please pay £12.")

else:
    print("Sorry, you can not tall enough to ride the rollercoaster.")