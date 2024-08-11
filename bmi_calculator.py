# BMI calculator
# input - weight / height 
# output - BMI value 

# Metric System : 
# BMI = weight (in kilograms) / height**2 (in meters)

# Imperial System : 
# BMI = 703 * weight (in pounds) / height**2 (in inches)

weight = float(input("Please, enter your weight in pounds => "))
height = float(input("Please, enter your height in inches => "))

bmi_value = 703 * (weight / height ** 2)
rounded_bmi = round(bmi_value, 2)

print(f"Your BMI is {rounded_bmi}")