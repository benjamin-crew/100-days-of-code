### Day 24 - Intermediate - Files, Directories and Paths

# Read files
    file = open("my_file.txt")
    contents = file.read()
    print(contents)
    file.close()

or:

    with open("my_file.txt") as file:
        contents = file.read()
        print(contents)

# Write file

    with open("my_file.txt", mode="w") as file:
        file.write("\nNew text.")

# Append File

    with open("my_file.txt", mode="a") as file:
        file.write("\nNew text.")