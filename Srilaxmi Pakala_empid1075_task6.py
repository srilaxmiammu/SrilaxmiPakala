import random

target_units = int(input("Enter target units: "))
workers_per_shift = int(input("Enter workers per shift: "))
defect_rate = float(input("Enter defect rate (%): "))

total_produced = 0
total_defects = 0

print("\n===== Production Counter Report =====")

for shift in range(1, 4):  

    shift_produced = 0
    shift_defects = 0

    print(f"\nShift {shift}")

    for cycle in range(1, 21):  

        if total_produced >= target_units:
            break

        units = random.randint(1, workers_per_shift)

        for _ in range(units):

            if total_produced >= target_units:
                break

            if random.randint(1, 100) <= defect_rate:
                shift_defects += 1
                total_defects += 1
                continue

            shift_produced += 1
            total_produced += 1

    productivity = (
        shift_produced / workers_per_shift
        if workers_per_shift > 0 else 0
    )

    print("Items Produced :", shift_produced)
    print("Defects        :", shift_defects)
    print("Productivity   :", round(productivity, 2))

    if total_produced >= target_units:
        print("\nTarget achieved. Production stopped.")
        break

print("\n===== Final Summary =====")
print("Target Units      :", target_units)
print("Total Produced    :", total_produced)
print("Total Defects     :", total_defects)
print("Workers per Shift :", workers_per_shift)
