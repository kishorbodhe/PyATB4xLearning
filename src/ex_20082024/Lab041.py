# Grade Calculator
# Write a program that calculates and displays theletter grade
# for a given numrical score (e.g.A,B,C,D,E, or F)
# based on the following grading scale
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

#Logic Building Formulae
#User Inout
#1 -->USer input -->score --> int
#2 -->Output -->str -->A,B or....

score = int(input("Enter your Score\n"))

#score>=90 and score <=100 -->"A"
#score>=80 and score <=89 -->"B"

if score>=90 and score<=100:
      print(f"Your grade is:","A")
elif score>= 80 and score<=89:
    print(f"Your grade is:","B")
elif score>=70 and score<=79:
    print(f"Your grade is:","C")
elif score>=60 and score<=69:
    print(f"Your grade is:","D")
elif score>100
    print("You are Superman!")
else:
     print(f"Your gerade is:","F")




