total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

tip_amount = (tip_percentage / 100) * total_bill

total_with_tip = total_bill + tip_amount

amount_per_person = total_with_tip / people

print("\n===== BILL SUMMARY =====")
print(f"Original Bill Amount : ₹{total_bill}")
print(f"Tip Percentage       : {tip_percentage}%")
print(f"Tip Amount           : ₹{round(tip_amount, 2)}")
print(f"Total With Tip       : ₹{round(total_with_tip, 2)}")
print(f"Amount Per Person    : ₹{round(amount_per_person, 2)}")
print("========================")
