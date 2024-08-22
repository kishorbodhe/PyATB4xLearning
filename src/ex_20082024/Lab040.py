# Problem find the max between three numbers

#Logic Building

# USer Inputs - numb1, numb2, numb3 -->integers ask to user what they want
# Output --> Int or string with max number

#LOgic output ? If else -- for 1 condition
#more than one condition --> if elif else

#Syntax:-
# if condition 1:
#     print("do 1")
# elif condition 2:
#     print("do 2")
# elif condition 3:
#     print("do 3")
# else:
#     print("do 4")

num1 = int(input("Enter the num1\n"))   #5,  #10
num2 = int(input("Enter the num2\n"))   #3,  #12
num3= int(input("Enter the num3\n"))    #2,  #11

# 5>3 and 5>2 -> true -->5
# num1>num2 and num1>num3 -->num1
#12>10 and 12>11 --> num2
# num3

if num1>num2 and num1>num3:
    print(f"Max num is:- {num1}")
elif num2>num1 and num2>num3:
    print(f"Max num is:- {num2}")
else:
    print(f"Max num is:-{num3}")

result = max(num1,num2,num3)
print(f"Max numb is:-{result}")










