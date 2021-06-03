weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print(f"Weight in Lbs: { converted }")
else:
    converted = weight * 0.45
    print(f"Weight in Kgs: { converted }")