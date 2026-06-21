print("====================")
print(" Area Calculator 📐 ")
print("====================")

print()

print("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")

print()

while True:

    shape = int(input("Which Shape: "))

    if shape == 1:
        
        print()
        
        base = int(input("Base of triangle: "))
        height = int(input("Height of triangle: "))
        
        area = (height * base) / 2
        
        print()
        
        print("The area of triangle is:", area)
        
    elif shape == 2:
        
        print()
        
        length = int(input("Length of rectangle: "))
        width = int(input("Width of rectangle: "))
        
        area = length * width
        
        print()
        
        print("The area of rectangle is:", area)
        
    elif shape == 3:
        
        print()
        
        side = int(input("Side of square: "))
        
        area = side ** 2
        
        print()
        
        print("The area of square is:", area)
        
    elif shape == 4:
        
        print()
        
        radius = int(input("Radius of circle: "))
        
        area = 3.14 * (radius ** 2)
        
        print()
        
        print("The area of circle is:", area)
        
    elif shape == 5:
        print("Thanks for using the calculator!")
        break
    
    else:
        print("Invalid Input")
