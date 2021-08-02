# You would normally use len and sum in this example, but these functions were not permitted
# as part of the challenge

student_heights = input("Input a list of student heights: ").split()
total = 0
number_of_people = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total += student_heights[n]
    number_of_people += 1

average = round(total / number_of_people)

print(f"The average is: {average}.")
