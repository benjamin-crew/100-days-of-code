height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"{bmi}: Underweight.")
elif bmi < 25:
    print(f"{bmi}: Normal weight.")
elif bmi < 30:
    print(f"{bmi}: Overweight.")
elif bmi < 35:
    print(f"{bmi}: Obese.")
else:
    print(f"{bmi}: Clinically obese.")