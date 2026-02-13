def cube(a):

    i=0
    cu=0
    while i<a:

        cu= a**3
        i=i+1
    return cu

num=int(input("Enter Number="))
ret=cube(num)
print(ret)
