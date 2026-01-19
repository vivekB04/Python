def areaCircle(radius):
    pi=3.14
    area=pi*radius*radius

    return area
rad=float(input("Enter Radius of the Circle"))

print("Radius=",rad)

retArea=areaCircle(rad)
print("Area=",retArea)


