temperature = int(input("Enter a temperature (Celsius): "))

if temperature < 15:
    print(f"{temperature} -> Cold")
elif temperature >= 15 and temperature <= 25:
    print(f"{temperature} -> Comfortable")
elif temperature > 25 and temperature < 35:
    print(f"{temperature} -> Hot")
elif temperature >= 35:
    print(f"{temperature} -> Extreme Heat")
else:
    print("Invalid Temperature.")
