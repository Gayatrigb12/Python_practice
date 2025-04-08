import math
radius = int(input("Enter the radius of the circle: "))

def circle(radius):
#    area = math.pi * radius**2
#area with 2 percision
   area = round(math.pi * radius**2, 2)
   circumference = round( 2 * math.pi * radius , 2)
   return area, circumference

area, circumference = circle(radius)
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")