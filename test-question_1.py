valid_grades = []
while True:
    try:
        if len(valid_grades) < 10:
                grade = int(input("Enter a grade: "))
                if grade >= 0 and grade <= 100 or grade==-999:
                    valid_grades.append(grade)
                else:
                    print("Please enter a valid grade - number between 0 and 100")
        else:
            if grade == -999:
                break
            else:
                grade = int(input("Enter a grade: "))
                if grade >= 0 and grade <= 100 or grade==-999:
                    valid_grades.append(grade)
    except ValueError:
        print("Please enter a valid grade - number between 0 and 100")
valid_grades.remove(-999)
print(f"number of valid grades: {len(valid_grades)}")
print(f"class average: {sum(valid_grades)/len(valid_grades)}")
print(f"highest grade: {max(valid_grades)}")
print(valid_grades)
