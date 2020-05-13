
"""
Adult Body Mass Index Calculator 
THis code calculates your BMi and tells if you are overweight,normal,underweight or obese.
it writes all the data into a new file that is created by your name.

"""
inputname = input("enter your name :")
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in m): "))

bmi = (weight/height)/height
f = open(inputname+".txt","w")
x = str(bmi)
f.write("weight:")
f.write("\n")
f.write(str(weight))
f.write("\n")
f.write("height:")
f.write("\n")
f.write(str(height))
f.write("\n")
f.write("your BMI is:")
f.write("\n")
f.write(x)
f.write("\n")


print("Your bmi is:",bmi)

if bmi<18.5:
    print("underweight")
    y = "underweight"
elif 18.5<bmi<24.9:
    print("normal weight")
    y ="normal weight"
elif 25<bmi<29.9:
    print("overweight")
    y ="overweight"
elif bmi>30:
    print("obese")
    y = "obese"
f.write("you are:")
f.write("\n")
f.write(y)
f.close()
