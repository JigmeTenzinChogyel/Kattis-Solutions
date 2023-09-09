import math
height, angle = input().split(" ")
angle = math.sin(math.radians(int(angle)))
hypotenuse = int(height)/angle
print(math.ceil(hypotenuse))