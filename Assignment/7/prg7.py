percent = int(input("Enter Your Percentage:"))
marks = int(input("Enter Your Marks:"))

if percent>=90 and marks>=90:
    print("Addmission in Elite Program")

elif percent>=80 and marks>=70:
    print("Addmission in Standard Program")

elif percent>=60 and marks>=50:
    print("Addmission in Basic Program")

else:
    print("Not Eligible")

