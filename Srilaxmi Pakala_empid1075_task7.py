# EMI Calculator

def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return emi

p = float(input("Enter Loan Amount: "))
r = float(input("Enter Annual Interest Rate (%): "))
t = int(input("Enter Loan Tenure (Years): "))

emi = calculate_emi(p, r, t)

print("\n----- EMI DETAILS -----")
print(f"Loan Amount : {p:.2f}")
print(f"Interest Rate : {r}%")
print(f"Tenure : {t} Years")
print(f"Monthly EMI : {emi:.2f}")
