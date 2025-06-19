# - Write a BMI calculator and classify underweight/normal/overweight
# 	Hint : use int() for type caste, BMI uses formula Weight (Kgs) / (Height (Meters)) 2

weight=int(input("Enter Weight in kg:"))
Height=int(input("Enter Height in meters:"))
bmi= weight / (Height * Height)
print(bmi)

if bmi > 18.5:
   print("You are under weight.")

elif bmi < 25:
     print("You are normal weight.")

else:
    print("You are overweight.")








