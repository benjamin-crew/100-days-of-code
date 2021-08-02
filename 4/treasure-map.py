import sys

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
maps = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position_string = input("Where do you want to put the treasure? ")
position = int(position_string)

column = int(position_string[0]) - 1
row = int(position_string[1]) - 1

if position <= 33:
    maps[row][column] = 'x'
else:
    print("You should hav entered two integers.")
    sys.exit()

print(f"{row1}\n{row2}\n{row3}")