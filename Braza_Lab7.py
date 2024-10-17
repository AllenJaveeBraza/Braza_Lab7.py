# Student Name --- Basic Info
Name=input("Insert your Name here: ")
Section=input("Insert your Section here: ")

# Grades --- Semester
Pre=float(input("Insert your Prelim Grade Here: "))
Mid=float(input("Insert your Midterm Grade Here: "))
Final=float(input("Insert your Final Grade Here: "))

# Grades --- validity
if float(Pre)>100 or float(Pre)<40:
    print("Invalid Input, please try again.")
    exit()
    
elif float(Mid)>100 or float(Mid)<40:
    print("Invalid Input, please try again.")
    exit()
    
elif float(Final)>100 or float(Final)<40:
    print("Invalid Input, please try again.")
    exit()
    
# Computation --- Final Grade
Total = float(Pre) + float(Mid) + float(Final)
Grade = float(f"{Total:.2f}")/3
Final_Grade=round(Grade)

# User --- Print Out:
print(f"Good Day {Name} from {Section}!")

# Grades --- Grades Description
if float(Final_Grade)==100 or float(Final_Grade)>=99:
    print(f"You have an Excellent performance. \nYour Grade is {Final_Grade}.")
    
elif float(Final_Grade)==98 or float(Final_Grade)>=96:
    print(f"You have an Outstanding performance. \nYour Grade is {Final_Grade}.")
    
elif float(Final_Grade)==95 or float(Final_Grade)>=93:
    print(f"You have a Superior performance. \nYour Grade is {Final_Grade}.")
    
elif float(Final_Grade)==92 or float(Final_Grade)>=90:
    print(f"You have a Very Good performance. \nYour Grade is {Final_Grade}.")
    
elif float(Final_Grade)==87 or float(Final_Grade)>=89:
    print(f"You have a Good performance. \nYour Grade is {Final_Grade}.")
    
elif float(Final_Grade)==86 or float(Final_Grade)>=84:
    print(f"You have a Satisfactory performance. \nYour Grade is {Final_Grade}.")

elif float(Final_Grade)==83 or float(Final_Grade)>=81:
    print(f"You have a Fairly Satisfactory performance. \nYour Grade is {Final_Grade}.")

elif float(Final_Grade)==80 or float(Final_Grade)>=78:
    print(f"You have a Fair performance. \nYour Grade is {Final_Grade}.")

elif float(Final_Grade)==77 or float(Final_Grade)>=75:
    print(f"You have Passed. \nYour Grade is {Final_Grade}.")

else:
    print(f"You have Failed. \nYour Grade is {Final_Grade}.")
    




