n = int(input("Enter n: "))

print("\n1. Right Triangle of Stars")
for i in range(1, n + 1):
    print("*" * i)

print("\n2. Inverted Triangle of Numbers")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n3. Pascal's Triangle")
for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

print("\n4. Prime Numbers up to", n)
for num in range(2, n + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
