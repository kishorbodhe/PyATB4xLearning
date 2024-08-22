# Conditions and Loops


#Write a program to take a user age and let him know if he can go to the club
#21

#Logic Building
#1.User input - data type ->int
#output-->String-->user if he can go or not

# 2. Rough Logic

# age >21 -->print can go to the club
#age< 21 -->print can't go to the club

#3. Write the logic
age = input("Enter your age\n")
age = int(age)

if age >= 21:                           # Condition
    print(f"Can go to the Club ->{age}")
else:
    print(f"Can't go to the Club -> {age}")


