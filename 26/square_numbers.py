with open("26/file1.txt") as file_one:
    file_one = file_one.readlines()

with open("26/file2.txt") as file_two:
    file_two = file_two.readlines()

result = [int(num.strip("\n")) for num in file_one if num in file_two]
print(result)