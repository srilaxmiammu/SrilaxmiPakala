temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing! Stay indoors and wear heavy clothing")

elif 0 <= temperature <= 15:
    print("Cold. A jacket is recommended")

elif 16 <= temperature <= 25:
    print("Pleasant weather! Great for outdoor activities")

elif 26 <= temperature <= 35:
    print("Hot. Stay hydrated and use sunscreen")

else:
    print("Extreme heat! Avoid going outside")
