
side1 = float(input("Input longest side of triangle"))
side2 = float(input("Input second side of triangle"))
side3 = float(input("Input third side of triangle"))

print(side1, side2, side3)

if (side1>=side2+side3) or (side2>=side1+side3) or (side3>=side2+side1):
    print("This cannot make a triangle")
else:
    print("This can make a triangle")

