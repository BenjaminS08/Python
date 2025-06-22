#Creating Function of Square
def square(side):
    square_area = side * side #Calculating Area of square
    print(f"The area of the square is {square_area:.2f} square units.")


#Creating Function of Circle
def circle(Radius):
    pi = 3.14
    circle_area = pi * Radius * Radius #Calculating Area of circle
    print(f"The area of the circle is {circle_area:.2f} square units.")
square(float(input("Enter a side length of a square: ")))
circle(float(input("Enter the radius of a circle: ")))
