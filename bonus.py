


def runCalculation(xsalary, xyearsWorked):
    if xyearsWorked >= 5:
        fivePercentOfSalary = salary * .05
        total = xsalary + fivePercentOfSalary
        print("You qualify for a bonus and your salary total will now be", total)

    if xyearsWorked < 5:
        print("You do not qualify for a bonus, your salary is", xsalary)


salary = int(input("What is your salary"))
yearsWorked = int(input("How many years have you worked at this job"))
runCalculation(salary, yearsWorked)