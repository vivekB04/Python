angle1=int(input("enter angle1 = "))
angle2=int(input("enter angle2 = "))
angle3=int(input("enter angle3 = "))

sum = angle1+angle2+angle3
if (angle1==60 or 30 or 90) and (angle2==30 or 60 or 90) and (angle3 == 90 or 30 or 60) and (sum == 180):
    print("It is a right angle triangle")

else:
    print("not a right angle triangle")
