start=int(input("START :"))
end=int(input("END :"))

fact=1
i=1

while start<=end:
    fact=fact*i
    print("Factorial of",start,"=",fact)

    start+=1
    i+=1
