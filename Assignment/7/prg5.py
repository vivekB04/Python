temp = int(input("Enter Temperature (C)="))

if temp<0:
    print("Freezing Cold")

elif temp>=0 or temp<=11temp = int(input("Enter Temperature (C)="))

if temp < 0:
    print("Freezing Cold")
elif temp >= 0 and temp <= 10:
    print("Very cold")
elif temp >= 11 and temp <= 20:
    print("cold")
elif temp >= 21 and temp <= 30:
    print("warm")
elif temp >= 31 and temp <= 40:
    print("hot")
else:
    print("extreme heat")

