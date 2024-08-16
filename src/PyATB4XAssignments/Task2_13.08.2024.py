# Task 2
#
# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

num1 = int(input("Enter the value of num1:"))
num2 = int(input("Enter the value of num2:"))

Max_Number=max(num1,num2)
print("maximum of 2 numbers", num1, "&", num2, "=", Max_Number)

Power=pow(num1,num2)
print("Result of", f"{num1}", "^", f"{num2}", "=", Power)

Sub=num1-num2
print("Substraction Result",f"{num1}","_",f"{num2}",Sub)

Mul=num1*num2
print("Multiplication Result:",Mul)

Sum=num1+num2
print(f"Addition of", f"{num1}","+",f"{num2}","=", Sum)


division = num2 / num1
print("Result of", f"{num2}", "/", f"{num1}", "=", division)




