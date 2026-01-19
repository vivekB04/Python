def sumBetNum(start,end):

    sum1=0
    cur=start
    while cur<=end:
        sum1+=cur
        
        cur+=1
    #print(sum1)
    return sum1

num1=int(input("Enter starting num:"))
num2=int(input("enter end num:"))

ret=sumBetNum(num1,num2)
print("Total sum from",num1,"to",num2,'is',ret)







    

