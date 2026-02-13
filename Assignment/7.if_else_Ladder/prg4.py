income= int(input("Annual Income : "))

if income<=250000:
    print("NO TAX")

elif income<=500000:
    tax=(income-250000)*0.05
    print("Tax to be paid:",tax)

elif income<=1000000:
    tax=(250000*0.05)+(income-500000)*0.20
    print("Tax to be paid:",tax)

else:
    tax=(250000*0.05)+(500000*0.20)+(income-1000000)*0.30
    print("Tax to be paid:",tax)
