print("Welcome to the BMI Calculator")

#
height = input("Please enter your height in metre: \n")
weight = input("Please enter your weight in kilograms: \n")
#

height = float(height)
weight = float(weight)

BMI = weight/(height**2)
print(f"Your Body Mass Index is {round(BMI,2)}")
