def main():
    print("Welcome to the Band Name Generator.")
    town_city = input("What is the name of the town or city you grew up in?:\n")
    pet = input("And what is the name of your pet?:\n")

    band_name = (town_city.capitalize() + " " + pet.capitalize())

    print("Your band name is: " + band_name + ".")

if __name__ == "__main__":
    main()