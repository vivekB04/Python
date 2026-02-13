def square(a):
    
    i=0
    sq=0
    while i<a:
        
        sq= a*a
        i=i+1
    return sq

num=int(input("Enter Number="))
ret=square(num)
print(ret)

