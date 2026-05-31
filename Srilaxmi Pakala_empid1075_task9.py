# Attendance Calculator

total_classes = int(input("Enter Total Classes Conducted: "))
attended_classes = int(input("Enter Classes Attended: "))

attendance = (attended_classes / total_classes) * 100

print("\n----- ATTENDANCE DETAILS -----")
print(f"Attendance Percentage : {attendance:.2f}%")

required = 75

if attendance >= required:
    print("Eligible for Exams")
else:
    needed = 0

    while ((attended_classes + needed) /
           (total_classes + needed)) * 100 < required:
        needed += 1

    print("Not Eligible for Exams")
    print("Classes needed to reach 75% attendance:", needed)
