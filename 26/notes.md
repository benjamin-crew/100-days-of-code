# Day 26 - Intermediate - List Comprehension and the NATO Alphabet

## List Comprehension

### List + 1
    numbers = [1, 2, 3]
    new_list = []
    for n in list:
        add_1 = n + 1
    new_list.append(add_1)

    new_list = [n + 1 for n in numbers]

### Range * 2
    new_list = [n * 2 for n in range(1,5)]
    print(new_list)

### String to char
    name = "Benjamin"
    new_list = [letter for letter in name]

    print(new_list)

### List of short names
    names = ["Alex", "Beth", "Dave", "Caroline", "Benjamin", "Freddie"]
    short_names = [name for name in names if len(name) < 5]
    print(short_names)

### Uppercase the longer names
    long_names = [name.upper() for name in names if len(name) > 5]
    print(long_names)

### Square Numbers
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [num ** 2 for num in numbers]
    print(squared_numbers)

### Even Numbers
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    result = [num for num in numbers if num % 2 == 0]
    print(result)

### Compare files for unique data
    with open("26/file1.txt") as file_one:
    file_one = file_one.readlines()

    with open("26/file2.txt") as file_two:
        file_two = file_two.readlines()

    result = [int(num.strip("\n")) for num in file_one if num in file_two]
    print(result)

## Dictionary Comprehension

### Example Syntax
    student_scores = {new_key:new_value for item in list if item > 50}

### Random scores
    import random
    names = ["Ben", "Dave", "Laura"]
    student_scores = {student:random.randint(1,100) for student in names}

### Scores over 60
    import random
    names = ["Ben", "Dave", "Laura"]
    student_scores = {student:random.randint(1,100) for student in names}
    passed_students = {student:"pass" for (student, score) in student_scores.items() if score >= 60}
