age = int(input("Enter Your Age = "))
weight = int(input("Enter Your Weight = "))
hb = float(input("Enter Your Hb = "))

if age<=17 or age>65:
    print("Not eligible for blood Donation")

elif weight<50:
    print("Not eligible for blood Donation")

elif hb<12.5:
    print("Not eligible for blood Donation")

else:
    print("you are eligible")
