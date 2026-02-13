unit=int(input("Enter Units : "))

if 0<=unit <=100:
    bill=unit*5
    print("Total Bill :",bill)

elif 101<=unit <=200:
    bill=unit*7
    print("Total Bill :",bill)

elif 201<=unit <=300:
    bill=unit*10
    print("Total Bill :",bill)

elif unit >300:
    bill=unit*15
    print("Total Bill :",bill)
