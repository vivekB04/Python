def product(x,y):
    n=1
    while n<=y:
        x*=n
        n+=1
    return x

num=int(input("Enter a number: "))
limit=int(input("Enter the limit: "))

ret=product(num,limit)
print(ret)

