def circumference():
    diameter = int(input("Enter the length of the diameter: "))
    radius = diameter / 2    
    circum = 2 * 3.142 * radius
    print("The circumference of the circle is: ", circum)
    
circumference()