weight= float(input("Enter your weight in kg:"))
height= float(input("Enter your height in m:"))

BMI= weight / height**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight")

elif BMI <= 24.9:
    print("You are healthy")

elif BMI <= 29.9:
    print("You are overweight")

else:
    print("You are obese")