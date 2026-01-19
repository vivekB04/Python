amt = int(input("Enter Toatal Purchase Amount: "))

discount_rate = 0.0
discount_amount = 0.0

if amt < 1000:
    print("No Discount")
    final_amount = amt
    discount_rate = 0.0
    
elif amt <= 4999:
    discount_rate = 0.05
    discount_amount = amt * discount_rate
    print("Discount Applied: 5%")

elif amt <= 9999:
    discount_rate = 0.10
    discount_amount = amt * discount_rate
    print("Discount Applied: 10%")

elif amt <= 19999:
    discount_rate = 0.20
    discount_amount = amt * discount_rate
    print("Discount Applied: 20%")

else:
    discount_rate = 0.30
    discount_amount = amt * discount_rate
    print("Discount Applied: 30%")

if amt >= 1000:
    final_amount = amt - discount_amount
    print(f"Discount Amount: ",discount_amount)
    print(f"Final Amount: ",final_amount)
else:
    print(f"Final Amount:",final_amount)
