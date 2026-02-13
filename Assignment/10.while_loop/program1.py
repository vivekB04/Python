start=int(input("Enter Starting number:"))
end=int(input("Enter Ending number:"))

while start<=end:
    
    if start%4==0 and start%5==0:
        print(start)
    start+=1

