### Day 30 - Intermediate - Errors, Exceptions and JSON Data: Improving the Password

## Error Catching

# try
Try something.

# except
If there is an exception, do this.

# else
if no exception, do this.

# finally
Does this no matter what happens.

    try:
        file = open("a_file.txt")
        a_dictionary = {"key": "value"}
        print(a_dictionary["key"])
    except FileNotFoundError:
        file = open("a_file.txt", "w")
        file.write("Something")
    except KeyError as error_message:
        print(f"The key {error_message} does not exist.")
    else:
        content = file.read()
        print(content)
    finally:
        file.close()
        print("File was closed.")

# raise
Raise allows you to raise your own exception.

    height = float(input("Height: "))
    weight = int(input("Weight: "))

    if height > 3:
        raise ValueError("Human height should not be over 3 meters.")

    bmi = weight / height ** 2
    print(bmi)