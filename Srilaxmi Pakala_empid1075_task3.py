age = int(input("Enter age: "))
salary = int(input("Enter salary: "))
employment = input("Enter employment type (salaried/self-employed): ").lower()

if age < 21 or age > 60:
    print("Rejected: Age should be between 21 and 60")

elif salary < 25000:
    print("Rejected: Salary should be at least 25000")

elif 21 <= age <= 30 and salary < 30000:
    print("Needs guarantor")

elif age > 55 and employment == "self-employed":
    print("High risk, senior review needed")

else:
    print("Approved")
